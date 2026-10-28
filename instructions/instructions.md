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

## Verify the data and semantic model

1. In the workspace item list, select the SQL analytics endpoint with the same name as
   the Lakehouse. The SQL query editor opens. For details, see [Microsoft Learn guidance
   for accessing a Lakehouse SQL analytics endpoint][fabric-sql-endpoint].
2. In the explorer pane, expand **Tables** > **dbo** and wait for the 19 lowercase
   tables to appear.
3. Paste this query into the editor and select **Run**:

   ```sql
   SELECT TOP (2) ShipmentId, CustomerOrderId, ShipmentQuantity
   FROM dbo.shipment
   WHERE ShipmentId IN ('SHIPMENT-0001', 'SHIPMENT-0002')
   ORDER BY ShipmentId;
   ```

   **Expect:** both shipments appear, each with a quantity of **120**.

4. Return to the LAB672 workspace item list.
5. Select the semantic model's **...** menu, then select
   **Write DAX queries**. Paste this query into the DAX query editor and select **Run**.
   For details, see [Microsoft Learn guidance for DAX query view][fabric-dax-query-view].

   ```dax
   EVALUATE
   ROW(
       "Products", [Product Count],
       "OnHandUnits", [On Hand Inventory Units],
       "NetAvailableUnits", [Net Available Inventory Units],
       "AtRiskOrderUnits", [At Risk Customer Order Units]
   )
   ```

   **Expect:** `80`, `100700`, `72100`, and `3534`.
6. Return to the LAB672 workspace item list.

## Create your ontology

1. In the workspace item list, open **ZavaSupplyChain2027_SemanticModel**.
2. In the semantic model toolbar, select **Generate Ontology**. For details, see
   [Microsoft Learn guidance for generating an ontology from a semantic model][fabric-generate-ontology].
3. In the dialog, select the workspace root as the location, enter
   `Ignite2026_Zava_MyTest` as the ontology name, and select **Create**.
4. In the workspace item list, open the new ontology.
5. In the ontology canvas, select each entity type to inspect its details. Review the
   keys, relationships, and metrics for Shipment, InventoryPosition, CustomerOrder,
   Disruption, Intervention, and DecisionRecord. Do not activate all inactive
   relationships.

**Expect:** the ontology has concepts corresponding to the model's 13 business tables.
The starter doesn't include a prebuilt reference ontology.

## Ask a business question

1. In the ontology toolbar, select **Ontology agent**. The chat panel opens in **Plan**
   mode. For details, see [Microsoft Learn guidance for using the Ontology agent][fabric-ontology-agent].
2. Enter this context in the agent chat:

   > We are working on my Zava workshop ontology. Keep the source data and semantic model
   > unchanged. Discover the available snapshot and observation times from the data
   > rather than using today's clock. Show the dates, analysis window, and assumptions
   > behind time-sensitive answers.

3. Ask:

   > Where is our supply chain most vulnerable?

4. Ask:

   > Why is that a risk? Show me what depends on it.

**Expect:** a model-backed answer with a supporting query. This is the starting static
view, not yet evidence that the agent used telemetry.

## Enrich the ontology with dependencies

1. In the Ontology agent chat, ask:

   > Find the supply-chain dependencies in our Zava lakehouse that aren't in this
   > ontology yet. Add the new business objects and connect them to what we already
   > have. Keep the existing model and measures. Show the plan first.

2. When the agent posts a draft preview, select it. Review the proposed entity types,
   properties, data bindings, and relationships. The plan should add **BillOfMaterial**,
   **SupplierSite**, **ComponentSupply**, **SupplyRoute**, **RouteHub**, and **LogisticsHub**
   using the Lakehouse. Check the identifiers and 11 relationships against the
   [dependency contract][dependency-contract].
3. Confirm that the plan reuses Product, Component, Supplier, Facility, and Carrier.
   Facility joins use **ObjectId**. Keep the existing Shipment and InventoryPosition
   backing and semantic metrics. Do not duplicate existing objects or keys.
4. Use the mode toggle below the chat box to switch to **Act** mode. In the chat, send:

   > Apply only the plan we just reviewed. Keep everything else unchanged.

5. Use the same mode toggle to switch back to **Plan** mode.
6. Ask:

   > Where is our supply chain most vulnerable?

7. Ask:

   > Why is that a risk? Show me what depends on it.

8. Ask:

   > Do we have a genuine alternative?

9. Ask:

   > Which customer orders could be affected?

10. Inspect the source queries and confirm that the traversal includes primary-component
    links and bills of material. Make timing assumptions explicit.
11. Check available supply capacity and shared dependencies.

**Expect:** the answer follows multiple hops through new and existing entities, checks
qualification and lead time, and deduplicates orders. It describes dependency exposure,
not predicted lost sales or proof of the cause of earlier delays. A plausible diagram
alone isn't enough.

## Enrich the ontology with observations

1. In the Ontology agent chat, ask:

   > Add shipment delay, handling shock, and route risk, plus inventory availability,
   > days of supply, and stockout risk, from the Zava source Eventhouse. Match the
   > existing objects and use observation time. Show the plan first.

2. Review the plan against these source mappings:

   | Existing concept | Source table | Matching key | Time column |
   |---|---|---|---|
   | Shipment | ShipmentTelemetry | ShipmentId | ObservationTime |
   | InventoryPosition | InventoryPositionTelemetry | InventoryPositionId | ObservationTime |

3. Confirm that the plan adds six observation properties without replacing existing
   concepts or losing their semantic-model grounding.
4. Use the mode toggle below the chat box to switch to **Act** mode. In the chat, send:

   > Apply only the plan we just reviewed. Keep everything else unchanged.

5. Use the same mode toggle to switch back to **Plan** mode.
6. Verify that the properties and bindings persisted.

## Investigate deliveries and compare responses

1. In the Ontology agent chat, ask:

   > Which deliveries need our attention?

2. Ask:

   > What makes these stand out?

3. Ask:

   > Should we respond to all of them the same way?

4. Ask:

   > What have we already decided, and what still needs checking?

5. Ask:

   > Show me the data behind that.

6. Ask:

   > Show the actual queries, sources, and observation times behind that answer.
   > Separate recorded facts from your interpretation.

7. Use the dates discovered in the data. Don't substitute today's date.

**Expect:** the agent discovers the available time range, selects a bounded window
within the data, and shows the latest observations per identity in that window. The
answer distinguishes stock-supported reroute discussion from a proposed quality hold.
It doesn't claim that either action was executed or that on-time delivery was proved.
Shock values are observations, not documented policy thresholds. The example evidence
window in the source data is **17:00-20:00 UTC on 31 December 2027**. A correct-looking
answer without actual source queries isn't a full pass.

## If setup or a query fails

1. Stop and share the step number and exact error with the facilitator. Do not delete
   resources, clear the ownership ledger, or start another setup run.
2. Keep the notebook in its original location after setup so its ownership ledger can be
   used safely if setup needs to resume.

**Finished means:** setup completed, the model query returned the expected values, the
ontology was generated, reviewed enrichments persisted, and the final answer included
verifiable source queries.



[starter-notebook]: https://github.com/microsoft/ignite26-LAB672/blob/main/data/Stage_Zava_Workshop.ipynb
[dependency-contract]: ../data/dependencies/contract.json
[fabric-notebook-import]: https://learn.microsoft.com/fabric/data-engineering/how-to-use-notebook#import-existing-notebooks
[fabric-notebook-run]: https://learn.microsoft.com/fabric/data-engineering/author-execute-notebook#run-all-cells
[fabric-sql-endpoint]: https://learn.microsoft.com/fabric/data-engineering/lakehouse-sql-analytics-endpoint#access-the-sql-analytics-endpoint
[fabric-dax-query-view]: https://learn.microsoft.com/power-bi/transform-model/dax-query-view#open-dax-query-view
[fabric-generate-ontology]: https://learn.microsoft.com/fabric/iq/ontology/how-to-generate-from-semantic-models
[fabric-ontology-agent]: https://learn.microsoft.com/fabric/iq/ontology/how-to-use-ontology-agent
