## Create your ontology

[Previous: Verify the data and semantic model](instructions-4.md) | [Contents](../README.md#walkthrough) | [Next: Ask a business question](instructions-6.md)

1. In the workspace's **SupplyChain** folder, open
   **ZavaSupplyChain2027_SemanticModel**.
2. In the semantic model toolbar, select **Generate Ontology**. For details, see
   [Microsoft Learn guidance for generating an ontology from a semantic model](https://learn.microsoft.com/fabric/iq/ontology/how-to-generate-from-semantic-models#create-the-ontology-item).

   ![Semantic model Home ribbon showing Generate Ontology.](../img/screenshots/generate-ontology.png)

3. Wait for **Generate an ontology from this Semantic Model** to open, then select
   **Get started**. The first launch can take time; do not repeatedly select
   **Generate Ontology** while it loads.

   ![Generate an ontology from this Semantic Model introduction with Get started.](../img/screenshots/generate-ontology-start.png)

4. In **New Ontology**, select the workspace root as the location, enter
   `Ignite2026_Zava_MyTest` as the ontology name, and select **Create**. If that
   name already exists, use a unique suffix. The screenshots use
   `Ignite2026_Zava_MyTest_Generated`.
   If a welcome dialog opens in the new ontology, select **Get started**.
   If you need to reopen the item, find it at the workspace root, outside
   **SupplyChain**.

   ![New Ontology dialog with the ontology name and workspace-root location.](../img/screenshots/new-ontology.png)

   ![Generated ontology canvas with the source model's business entity types.](../img/screenshots/ontology-generated.png)

5. On the ontology Home canvas, select an entity type in the **Explorer**, then select
   **View Entity Type details** on the top ribbon. In the **Configure** tab, review its
   properties, key, data bindings, and **Metrics**. Repeat for Shipment,
   InventoryPosition, CustomerOrder, Disruption, Intervention, and DecisionRecord.
   The metrics should still name **ZavaSupplyChain2027_SemanticModel** as their
   source.

   ![Shipment Configure page showing properties, semantic-model data bindings, entity key, and relationships.](../img/screenshots/shipment-configure.png)

6. Open **Instances** for Shipment and confirm that rows appear.

   ![Shipment instance list showing the source rows.](../img/screenshots/shipment-instances.png)

7. To inspect relationships, return to the Home canvas and select a relationship.
   Do not change the relationship in this step.
8. Open **Ontology agent** from the toolbar and select **Plan** mode with the toggle
   below the chat box. Ask it to explain the metrics available for these entity types.
   Compare its answer with the starting semantic model; don't change the model.

**Expect:** the ontology has concepts corresponding to the model's 13 business tables.
The starter doesn't include a prebuilt reference ontology.
