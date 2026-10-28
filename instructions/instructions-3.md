## Stage the sources

1. In the notebook toolbar, select **Run all** once. For details, see [Microsoft Learn
   guidance for running notebook cells][fabric-notebook-run].
2. Keep the notebook open and wait for setup and model refresh to finish. Do not start
   another run while setup is in progress.
3. Note the source names printed by the notebook. Use those names in the following steps.
4. Return to the `FabricIQWorkspace` item list.

**Expect:** the notebook reports that sources are staged and the semantic model refresh
is complete.

| Item | What it provides |
|---|---|
| ZavaSupplyChain2027_Lakehouse_Source | 19 managed Delta tables, including six dependency tables absent from the model |
| ZavaSupplyChain2027_Eventhouse_Source | Source Eventhouse and KQL database with four telemetry tables |
| ZavaSupplyChain2027_SemanticModel | Starting model with 13 business tables and 12 measures |
