## Enrich the ontology with dependencies

1. In the Ontology agent chat, ask:

   `Find the supply-chain dependencies in our Zava lakehouse that aren't in this ontology yet. Add the new business objects and connect them to what we already have. Keep the existing model and measures. Show the plan first.`

2. When the agent posts a draft preview, select it. Review the proposed entity types,
   properties, data bindings, and relationships. The plan should add **BillOfMaterial**,
   **SupplierSite**, **ComponentSupply**, **SupplyRoute**, **RouteHub**, and **LogisticsHub**
   using the Lakehouse. Check the identifiers and 11 relationships against the
   [dependency contract][dependency-contract]. For each proposed entity type, check
   that its binding uses the intended source table, each property maps to the expected
   source column, and its key matches the contract. For each relationship, compare the
   source and target keys with the contract.
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

   `Which customer orders could be affected?`

10. Ask the agent to show the query and source tables behind its answer. Read the
    generated query in the response and confirm that the traversal includes
    primary-component links and bills of material. Ask it to state any timing
    assumptions.
11. Ask:

    `For the alternative you identified, show the available qualified supply capacity,
    lead time, and shared dependencies. Include the source tables and query you used.`

    Check the returned supply and dependency evidence against the entities and
    relationships in the ontology.

**Expect:** the answer follows multiple hops through new and existing entities, checks
qualification and lead time, and deduplicates orders. It describes dependency exposure,
not predicted lost sales or proof of the cause of earlier delays. A plausible diagram
alone isn't enough.
