"""Isolated tests for the runtime embedded in the distributed notebook.

Run: python -m unittest discover -s data/tests -v
No Fabric connection or Spark session is required.
"""

import ast
import contextlib
import io
import json
from pathlib import Path
from types import MethodType, SimpleNamespace
import unittest
from unittest.mock import Mock


NOTEBOOK = Path(__file__).resolve().parents[1] / "Stage_Zava_Workshop.ipynb"
CELLS = json.loads(NOTEBOOK.read_text(encoding="utf-8"))["cells"]
RUNTIME = next("".join(cell["source"]) for cell in CELLS
               if "class Stager:" in "".join(cell["source"]))
TREE = ast.parse(RUNTIME)
STAGER = next(node for node in TREE.body
              if isinstance(node, ast.ClassDef) and node.name == "Stager")
METHOD = next(node for node in STAGER.body
              if isinstance(node, ast.FunctionDef)
              and node.name == "refresh_sql_endpoint_metadata")
ENDPOINT = "11111111-1111-1111-1111-111111111111"
TABLES = [f"table{i:02}" for i in range(19)]


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


class SqlMetadataReadinessTests(unittest.TestCase):
    def setUp(self):
        self.now = 0
        self.sleeps = []
        namespace = {
            "time": SimpleNamespace(monotonic=lambda: self.now, sleep=self.sleep),
            "check": check,
            "uuid_text": lambda value: value,
            "fabric_operation_url": lambda location, identifier: location or identifier,
        }
        exec(compile(ast.Module(body=[METHOD], type_ignores=[]), "<notebook>", "exec"),
             namespace)
        self.client = Mock()
        self.client.get.return_value = {"properties": {
            "sqlEndpointProperties": {"provisioningStatus": "Success", "id": ENDPOINT}}}
        self.stager = SimpleNamespace(
            client=self.client, owned_item=Mock(),
            state={"items": {"lakehouse": "lakehouse-id"}},
            base="https://api.fabric.microsoft.com/v1/workspaces/workspace-id",
            tables={name: {"physical": name} for name in TABLES},
        )
        self.run_check = MethodType(namespace[METHOD.name], self.stager)
        self.output = io.StringIO()
        redirect = contextlib.redirect_stdout(self.output)
        redirect.__enter__()
        self.addCleanup(redirect.__exit__, None, None, None)

    def sleep(self, seconds):
        self.sleeps.append(seconds)
        self.now += seconds

    def result(self, status="Success", names=TABLES):
        return {"value": [{"tableName": f"[dbo].[{name.upper()}]", "status": status}
                          for name in names]}

    def test_immediate_success_verifies_all_19_tables(self):
        self.client.call.return_value = (200, {}, self.result())
        self.run_check()
        self.assertIn("19 Lakehouse tables", self.output.getvalue())
        self.assertEqual(self.sleeps, [])
        args = self.client.call.call_args.args
        self.assertEqual(args[0], "POST")
        self.assertTrue(args[1].endswith(f"/sqlEndpoints/{ENDPOINT}/refreshMetadata"))
        self.assertEqual(args[2], {"tables": [{"schema": "dbo", "tableNames": TABLES}]})

    def test_not_run_and_missing_results_recover(self):
        self.client.call.side_effect = [
            (200, {}, self.result("NotRun")),
            (200, {}, self.result(names=TABLES[:18])),
            (200, {}, self.result()),
        ]
        self.run_check()
        self.assertEqual(self.sleeps, [30, 30])
        self.assertEqual(self.client.call.call_count, 3)
        self.assertIn("missing or NotRun", self.output.getvalue())

    def test_endless_not_run_stops_at_deadline_with_resume_instructions(self):
        self.client.call.return_value = (200, {}, self.result("NotRun"))
        with self.assertRaisesRegex(RuntimeError, "10 minutes.*table18.*same notebook"):
            self.run_check()
        self.assertEqual(self.now, 600)
        self.assertEqual(self.client.call.call_count, 20)
        self.assertNotIn("metadata verified", self.output.getvalue())

    def test_missing_results_also_time_out(self):
        self.client.call.return_value = (200, {}, {"value": []})
        with self.assertRaisesRegex(RuntimeError, "Do not delete"):
            self.run_check()
        self.assertEqual(self.now, 600)

    def test_failure_is_not_retried_and_preserves_error_details(self):
        result = self.result("NotRun")
        result["value"][0].update(
            status="Failure", error={"errorCode": "DeltaTableNotFound", "message": "Missing source"})
        self.client.call.return_value = (200, {}, result)
        with self.assertRaisesRegex(RuntimeError, "table00.*DeltaTableNotFound.*Missing source"):
            self.run_check()
        self.assertEqual(self.client.call.call_count, 1)
        self.assertEqual(self.sleeps, [])

    def test_null_error_and_unknown_status_fail_explicitly(self):
        for status in ("Failure", "Unexpected", None):
            with self.subTest(status=status):
                result = self.result()
                result["value"][0].update(status=status, error=None)
                self.client.call.return_value = (200, {}, result)
                with self.assertRaisesRegex(RuntimeError, "no error details"):
                    self.run_check()
        self.assertEqual(self.sleeps, [])

    def test_async_refresh_finishes_before_another_is_submitted(self):
        self.client.call.side_effect = [
            (202, {"location": "https://api.fabric.microsoft.com/v1/operations/operation"}, {}),
            (200, {}, self.result()),
        ]
        self.client.finish_operation.return_value = self.result("NotRun")
        self.run_check()
        self.client.finish_operation.assert_called_once_with(
            "https://api.fabric.microsoft.com/v1/operations/operation",
            timeout=600, operation_id=None)
        self.assertEqual(self.sleeps, [30])

    def test_pending_async_operation_is_not_resubmitted(self):
        self.client.call.return_value = (202, {"x-ms-operation-id": "operation"}, {})
        self.client.finish_operation.side_effect = TimeoutError("Operation still pending")
        with self.assertRaisesRegex(TimeoutError, "still pending"):
            self.run_check()
        self.assertEqual(self.client.call.call_count, 1)
        self.assertEqual(self.sleeps, [])

    def test_network_and_authentication_failures_are_not_retried(self):
        self.client.call.side_effect = RuntimeError("HTTP 401")
        with self.assertRaisesRegex(RuntimeError, "HTTP 401"):
            self.run_check()
        self.assertEqual(self.client.call.call_count, 1)

    def test_invalid_or_duplicate_response_is_not_retried(self):
        for result in (None, {}, {"value": [None]},
                       {"value": [{"tableName": "dbo.table00", "status": "Success"}] * 2}):
            with self.subTest(result=result):
                self.client.call.reset_mock()
                self.client.call.return_value = (200, {}, result)
                with self.assertRaises(RuntimeError):
                    self.run_check()
                self.assertEqual(self.client.call.call_count, 1)
        self.assertEqual(self.sleeps, [])

    def test_request_duration_counts_toward_readiness_window(self):
        def delayed(*args):
            self.now += 590
            return 200, {}, self.result("NotRun")
        self.client.call.side_effect = delayed
        with self.assertRaisesRegex(RuntimeError, "10 minutes"):
            self.run_check()
        self.assertEqual(self.sleeps, [10])
        self.assertEqual(self.client.call.call_count, 1)

    def test_all_notebook_code_cells_compile(self):
        for cell in CELLS:
            if cell["cell_type"] == "code":
                compile("".join(cell["source"]), str(NOTEBOOK), "exec")


if __name__ == "__main__":
    unittest.main()
