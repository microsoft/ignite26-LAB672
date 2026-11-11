## Investigate deliveries and compare responses

1. In the Ontology agent chat, use the toggle below the chat box to select **Plan** mode.
   Then ask:

   `Which deliveries need our attention?`

2. Ask:

   `What makes these stand out?`

3. Ask:

   `Should we respond to all of them the same way?`

4. Ask:

   `What have we already decided, and what still needs checking?`

5. Ask:

   `Show me the data behind that.`

6. Ask:

   `Show the actual queries, sources, and observation times behind that answer.
   Separate recorded facts from your interpretation.`

   Read the query shown with the answer. Identify its source table and time column,
   and compare the observation times with the available window the agent discovered.
   If the answer doesn't show a query, ask the agent to display it.

7. Use the dates discovered in the data. Don't substitute today's date. If the answer
   doesn't state the available time range, ask the agent to show the earliest and
   latest observation times before continuing.

8. Start a fresh Ontology agent conversation in **Plan** mode to check that the agent
   can discover the saved rule, rather than repeat a rule pasted into chat. Ask:

   `Using the saved Shipment quality review rule, compare SHIPMENT-0001 and
   SHIPMENT-0002. Identify the rule and its definition. Discover the available
   observation times and use the latest reading per shipment within the analysis
   window. Show the actual source queries and observation times, and explain whether
   either shipment needs a quality inspection. Separate what the rule requires from
   what the recorded interventions and decisions show. Keep the ontology, source data,
   and semantic model unchanged.`

   **Expect:** SHIPMENT-0001 has a latest shock reading of **3 g**, so it doesn't
   trigger this rule. That alone doesn't prove the shipment is safe to release or
   reroute. SHIPMENT-0002 has a latest shock reading of **12 g**, so the rule requires
   a quality inspection. Its **HoldAndInspect** intervention and decision are
   **Proposed**, not evidence that an inspection or release occurred.

   Confirm that the agent identifies the saved rule and shows the queries used to
   retrieve the observations and recorded response states. If it can't retrieve the
   saved rule, the rule-grounding check hasn't passed; don't paste the definition
   into chat and count that as retrieval.

**Expect:** the agent discovers the available time range, selects a bounded window
within the data, and shows the latest observations per identity in that window. The
answer distinguishes stock-supported reroute discussion from a proposed quality hold.
It doesn't claim that either action was executed or that on-time delivery was proved.
Shock values are source observations; the **10 g** quality-review threshold is a
fictional policy added in the preceding step, not a threshold inferred from those
observations. The example evidence window in the source data is
**17:00-20:00 UTC on 31 December 2027**. A correct-looking answer without actual source
queries isn't a full pass.
