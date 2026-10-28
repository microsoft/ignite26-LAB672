# LAB672: Ground agents in your business with an ontology in Fabric IQ

Follow this walkthrough to stage the Zava supply-chain data, create an ontology,
enrich it with the Ontology agent, and explore supply-chain risks and delivery
responses.

## Get the lab notebook

1. Open the [LAB672 setup notebook][starter-notebook] and select **Download raw file**.
2. Open a dedicated LAB672 workspace in the Fabric portal. Use a workspace other than
   **My workspace**; the workspace root must be empty before you import the notebook.
3. In the workspace toolbar, select **Import** > **Notebook** > **From this computer** >
   **Upload**.
4. Select the notebook file you downloaded, then select **Upload**.
5. In the workspace item list, select the imported notebook to open it. For details, see
   [Microsoft Learn notebook import guidance][fabric-notebook-import].
6. Do not attach a Lakehouse to the notebook.

## Stage the sources

1. In the notebook toolbar, select **Run all** once. For details, see [Microsoft Learn
   guidance for running notebook cells][fabric-notebook-run].
2. Keep the notebook open and wait for setup and model refresh to finish. Do not start
   another run while setup is in progress.
3. Note the source names printed by the notebook. Use those names in the following steps.
4. Return to the LAB672 workspace item list.

**Expect:** the notebook reports that sources are staged and the semantic model refresh
is complete.

| Item | What it provides |
|---|---|
| ZavaSupplyChain2027_Lakehouse_Source | 19 managed Delta tables, including six dependency tables absent from the model |
| ZavaSupplyChain2027_Eventhouse_Source | Source Eventhouse and KQL database with four telemetry tables |
| ZavaSupplyChain2027_SemanticModel | Starting model with 13 business tables and 12 measures |
