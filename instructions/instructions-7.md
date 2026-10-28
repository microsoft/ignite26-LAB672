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
