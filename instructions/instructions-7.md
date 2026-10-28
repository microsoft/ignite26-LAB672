## Enrich the ontology with dependencies

1. In the Ontology agent chat, use the toggle below the chat box to select **Plan** mode.
2. Ask the agent to propose the changes without applying them:

   `Find the supply-chain dependencies in our Zava lakehouse that aren't in this ontology yet. Propose adding BillOfMaterial, SupplierSite, ComponentSupply, SupplyRoute, RouteHub, and LogisticsHub using the Lakehouse, and connect them to the existing ontology. Reuse Product, Component, Supplier, Facility, and Carrier. Use ObjectId for Facility joins. Keep the existing Shipment and InventoryPosition backing, semantic metrics, and model unchanged. Show the plan first; don't apply it yet.`

3. When the agent posts a draft preview, select it. Review the proposed entity types,
   properties, data bindings, and relationships against the
   [dependency contract][dependency-contract]. For each proposed entity type, check
   its source table, property-to-column bindings, and key. Check all 11 relationships
   and their source and target keys. Confirm the proposal reuses Product, Component,
   Supplier, Facility, and Carrier; Facility joins use **ObjectId**. Preserve existing
   Shipment and InventoryPosition backing, semantic metrics, and the model.
4. After reviewing the proposal, switch to **Act** mode with the toggle below the chat
   box and send:

   `Apply only the plan we just reviewed. Keep everything else unchanged.`

5. After the agent finishes, return to **Plan** mode. On the Home canvas, use the
   **Explorer** and **View Entity Type details** to verify the applied entity bindings
   and keys. Switch to **Relationship** view to confirm the relationships match the
   reviewed proposal.
6. Ask:

   `Where is our supply chain most vulnerable?`

7. Ask:

   `Why is that a risk? Show me what depends on it.`

8. Ask:

   `Do we have a genuine alternative?`

9. Ask:

   `Which customer orders could be affected?`

10. Ask the agent to show the query and source tables behind its answer. Read the
    generated query in the response and confirm that the traversal includes
    primary-component links and bills of material. Ask it to state any timing
    assumptions.
11. Ask:

    `For the alternative you identified, show the available qualified supply capacity,
    lead time, and shared dependencies. Include the source tables and query you used.`

12. Check the returned supply and dependency evidence against the entities and
    relationships in the ontology.

**Expect:** the answer follows multiple hops through new and existing entities, checks
qualification and lead time, and deduplicates orders. It describes dependency exposure,
not predicted lost sales or proof of the cause of earlier delays. A plausible diagram
alone isn't enough.
