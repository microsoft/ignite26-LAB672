## Add a business rule

Give the ontology a business rule that an agent can use when interpreting shipment
observations. For details, see [Microsoft Learn guidance for ontology business
rules](https://learn.microsoft.com/fabric/iq/ontology/how-to-use-rules).

1. In the ontology **Explorer**, expand **Overview** and select **Rules**.
2. Select **+ Create rule**, or **New rule** if rules already exist.
3. Enter **Shipment quality review** as the rule name.
4. Enter this rule definition:

   `If a shipment's latest shock reading is 10 g or higher, it needs a quality
   inspection before we recommend releasing or rerouting it.`

5. Under **Linked ontology concepts**, select **Add concept**. Select the **Shipment**
   entity type and its **ShockG** observation property added in the preceding step.
   If the property has a different display name, use the property bound to
   **ShipmentTelemetry.ShockG**. Save the concept selection.
6. Select **Save** on the rule details page.
7. Return to the **Business rules** page and reopen **Shipment quality review**.
   Verify that its definition and both linked concepts were saved.

**Expect:** the rule is saved in the ontology and linked to Shipment and its shock
observation property. Existing data bindings, semantic metrics, and source data are
unchanged.

The **10 g** threshold is a fictional policy for this lab, not a threshold inferred
from the source observations. Saving a rule gives agents business context; it
doesn't automatically inspect, hold, release, or reroute shipments.

Continue to [Investigate deliveries and compare responses](instructions-10.md) to
check how the saved rule affects the agent's interpretation of the evidence.
