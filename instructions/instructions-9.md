## Investigate deliveries and compare responses

1. In the Ontology agent chat, ask:

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

7. Use the dates discovered in the data. Don't substitute today's date.

**Expect:** the agent discovers the available time range, selects a bounded window
within the data, and shows the latest observations per identity in that window. The
answer distinguishes stock-supported reroute discussion from a proposed quality hold.
It doesn't claim that either action was executed or that on-time delivery was proved.
Shock values are observations, not documented policy thresholds. The example evidence
window in the source data is **17:00-20:00 UTC on 31 December 2027**. A correct-looking
answer without actual source queries isn't a full pass.
