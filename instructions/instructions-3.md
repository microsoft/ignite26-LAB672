## Stage the sources

1. In the notebook toolbar, select **Run all** once. For details, see [Microsoft Learn
   guidance for running notebook cells][fabric-notebook-run].
2. Keep the notebook open and wait for the SQL analytics endpoint metadata sync and
   semantic model refresh to finish. Do not start another run while setup is in progress.
3. Note the source names printed by the notebook. Use those names in the following steps.
4. Return to the `FabricIQWorkspace` item list.

**Expect:** the notebook reports that sources are staged and the semantic model refresh
is complete.

SQL endpoint metadata can take time to become available after the tables are
created. Setup checks completed metadata refreshes again every 30 seconds when
table results are missing or marked `NotRun`, within a 10-minute readiness window.
It does not repeat ingestion or recreate tables. If this window expires, select
**Run all** in the same notebook to resume after the run has stopped. Do not delete
the existing resources or import another copy. If setup reports a table `Failure`,
inspect its error details and resolve the problem before resuming.

| Item | What it provides |
|---|---|
| ZavaSupplyChain2027_Lakehouse_Source | 19 managed Delta tables, including six dependency tables absent from the model |
| ZavaSupplyChain2027_Eventhouse_Source | Source Eventhouse and KQL database with four telemetry tables |
| ZavaSupplyChain2027_SemanticModel | Starting model with 13 business tables and 12 measures |
