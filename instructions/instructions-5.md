## Create your ontology

1. In the workspace item list, open **ZavaSupplyChain2027_SemanticModel**.
2. In the semantic model toolbar, select **Generate Ontology**. For details, see
   [Microsoft Learn guidance for generating an ontology from a semantic model][fabric-generate-ontology].
3. In the dialog, select the workspace root as the location, enter
   `Ignite2026_Zava_MyTest` as the ontology name, and select **Create**.
4. In the workspace item list, open the new ontology.
5. On the ontology Home canvas, select an entity type in the **Explorer**, then select
   **View Entity Type details** on the top ribbon. In the **Configure** tab, review its
   properties, key, and data bindings. Repeat for Shipment, InventoryPosition,
   CustomerOrder, Disruption, Intervention, and DecisionRecord.
6. To inspect relationships, return to the Home canvas, switch the canvas to
   **Relationship** view, and select each entity type in the **Explorer**. Review the
   connected entity types; do not activate all inactive relationships.
7. In the Ontology agent, ask it to explain the metrics available for these entity
   types. Compare its answer with the starting semantic model; don't change the model.

**Expect:** the ontology has concepts corresponding to the model's 13 business tables.
The starter doesn't include a prebuilt reference ontology.
