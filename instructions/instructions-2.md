
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

   **Expect:** 80, 100700, 72100, and 3534.
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

   `We are working on my Zava workshop ontology. Keep the source data and semantic model unchanged. Discover the available snapshot and observation times from the data rather than using today's clock. Show the dates, analysis window, and assumptions behind time-sensitive answers. `

3. Ask:

   `Where is our supply chain most vulnerable?`

4. Ask:

   `Why is that a risk? Show me what depends on it.`

**Expect:** a model-backed answer with a supporting query. This is the starting static
view, not yet evidence that the agent used telemetry.

## Enrich the ontology with dependencies

1. In the Ontology agent chat, ask:

   `Find the supply-chain dependencies in our Zava lakehouse that aren't in this ontology yet. Add the new business objects and connect them to what we already have. Keep the existing model and measures. Show the plan first.`

2. When the agent posts a draft preview, select it. Review the proposed entity types,
   properties, data bindings, and relationships. The plan should add **BillOfMaterial**,
   **SupplierSite**, **ComponentSupply**, **SupplyRoute**, **RouteHub**, and **LogisticsHub**
   using the Lakehouse. Check the identifiers and 11 relationships against the
   [dependency contract][dependency-contract].
3. Confirm that the plan reuses Product, Component, Supplier, Facility, and Carrier.
   Facility joins use **ObjectId**. Keep the existing Shipment and InventoryPosition
   backing and semantic metrics. Do not duplicate existing objects or keys.
4. Use the mode toggle below the chat box to switch to **Act** mode. In the chat, send:

  `Apply only the plan we just reviewed. Keep everything else unchanged.`

5. Use the same mode toggle to switch back to **Plan** mode.
6. Ask:

   `Where is our supply chain most vulnerable?`

7. Ask:

   `Why is that a risk? Show me what depends on it.`

8. Ask:

   `Do we have a genuine alternative?`

9. Ask:

   Which customer orders could be affected?`

10. Inspect the source queries and confirm that the traversal includes primary-component
    links and bills of material. Make timing assumptions explicit.
11. Check available supply capacity and shared dependencies.

**Expect:** the answer follows multiple hops through new and existing entities, checks
qualification and lead time, and deduplicates orders. It describes dependency exposure,
not predicted lost sales or proof of the cause of earlier delays. A plausible diagram
alone isn't enough.
