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
