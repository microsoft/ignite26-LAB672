## Add a business rule

[Previous: Enrich the ontology with observations](instructions-8.md) | [Contents](../README.md#walkthrough) | [Next: Investigate deliveries and compare responses](instructions-10.md)

1. Ask the agent to propose a new rule without applying them:

   `Add a rule for shipment's and if any latest shock reading is 10 g or higher, it needs a quality
   inspection before we recommend releasing or rerouting it.`

2. Review output and apply
   `Apply the plan reviewed, keep everything else unchanged`

3. After the agent finishes, click on **Rules** on the left sidebar under Overview. Review the created rule applied to Shipment.

**Expect**: the rule is saved in the ontology and linked to Shipment and its shock observation property. Existing data bindings, semantic metrics, and source data are unchanged.

