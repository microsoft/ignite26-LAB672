## Verify the data and semantic model

1. In the workspace item list, select the SQL analytics endpoint with the same name as
   the Lakehouse. The SQL query editor opens. For details, see [Microsoft Learn guidance
   for accessing a Lakehouse SQL analytics endpoint](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-sql-analytics-endpoint).
2. In the explorer pane, expand **Schemas** > **dbo** > **Tables** and ensure that the 19 lowercase tables are there.
3. Select **New SQL query**.
4. Paste this query into the editor and select **Run**:

   ```sql
   SELECT TOP (2) ShipmentId, CustomerOrderId, ShipmentQuantity
   FROM dbo.shipment
   WHERE ShipmentId IN ('SHIPMENT-0001', 'SHIPMENT-0002')
   ORDER BY ShipmentId;
   ```

   **Expect:** both shipments appear, each with a quantity of **120**.

5. Return to the `FabricIQWorkspace` item list.
6. Select the semantic model's **...** menu, then select
   **Open in DAX query view**. Paste this query into the DAX query editor and select **Run**.
   For details, see [Microsoft Learn guidance for DAX query view][fabric-dax-query-view].

   ```dax
   EVALUATE
   ROW(
       "Products", [Product Count],
       "OnHandUnits", [On Hand Inventory Units],
       "NetAvailableUnits", [Net Available Inventory Units],
       "AtRiskOrderUnits", [At Risk Customer Order Units]
   )
   ```

   **Expect:** 80, 100700, 72100, and 3534.
7. Return to the `FabricIQWorkspace` item list.
