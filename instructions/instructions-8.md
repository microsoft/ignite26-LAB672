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
6. Return to the ontology Home canvas. In the **Explorer**, select Shipment, then
   select **View Entity Type details** on the top ribbon. In the **Configure** tab,
   confirm that the three shipment observation properties and their bindings to
   **ShipmentTelemetry** are present. Repeat for InventoryPosition and confirm its
   three properties are bound to **InventoryPositionTelemetry**. Check that the
   matching keys and **ObservationTime** column match the table above. Open the
   **Instances** tab for each entity type and confirm that source data appears.
