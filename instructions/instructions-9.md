## Add a business rule

[Previous: Enrich the ontology with observations](instructions-8.md) | [Contents](../README.md#walkthrough) | [Next: Investigate deliveries and compare responses](instructions-10.md)

1. Ask the agent to propose a new rule without applying them:

   `Add a rule for shipment's and if any latest shock reading is 10 g or higher, it needs a quality
   inspection before we recommend releasing or rerouting it.`

2. Review the reasoning in Ontology Agent and apply
   `Apply the plan reviewed, keep everything else unchanged`

3. After the agent finishes, click on **Rules** on the left sidebar under Overview. Review the created rule applied to Shipment.

**Expect**: the rule is saved in the ontology and linked to Shipment and its shock observation property. Existing data bindings, semantic metrics, and source data are unchanged.

### Investigate deliveries and compare responses 

4. In the Ontology agent chat, use the toggle below the chat box to select **Plan** mode.
   Then ask:

   `Which deliveries need our attention?`

5. Ask:

   `What makes these stand out?`

6. Ask:

   `Should we respond to all of them the same way?`

7. Ask:

   `What have we already decided, and what still needs checking?`

8. Ask:

   `Show me the data behind that.`

9. Ask:

   `Show the actual queries, sources, and observation times behind that answer.
   Separate recorded facts from your interpretation.`

   Read the query shown with the answer. Identify its source table and time column,
   and compare the observation times with the available window the agent discovered.
   If the answer doesn't show a query, ask the agent to display it.

10. Use the dates discovered in the data. Don't substitute today's date. If the answer
   doesn't state the available time range, ask the agent to show the earliest and
   latest observation times before continuing.

**Expect:** the agent discovers the available time range, selects a bounded window
within the data, and shows the latest observations per identity in that window. The
answer distinguishes stock-supported reroute discussion from a proposed quality hold.
It doesn't claim that either action was executed or that on-time delivery was proved.
Shock values are measured against the rules. The example evidence
window in the source data is **17:00-20:00 UTC on 31 December 2027**. A correct-looking
answer without actual source queries isn't a full pass.
