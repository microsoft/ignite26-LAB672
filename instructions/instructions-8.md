## Enrich the ontology with observations

1. In the Ontology agent chat, ask:

    `Add shipment delay, handling shock, and route risk, plus inventory availability, days of supply, and stockout risk, from the Zava source Eventhouse. Match the existing objects and use observation time. Show the plan first.`

2. Review the plan against these source mappings:

   | Existing concept | Source table | Matching key | Time column |
   |---|---|---|---|
   | Shipment | ShipmentTelemetry | ShipmentId | ObservationTime |
   | InventoryPosition | InventoryPositionTelemetry | InventoryPositionId | ObservationTime |

3. Confirm that the plan adds six observation properties without replacing existing
   concepts or losing their semantic-model grounding.
4. Use the mode toggle below the chat box to switch to **Act** mode. In the chat, send:

  `Apply only the plan we just reviewed. Keep everything else unchanged.`

5. Use the same mode toggle to switch back to **Plan** mode.
6. Verify that the properties and bindings persisted.
