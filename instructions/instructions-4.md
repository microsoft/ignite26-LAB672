## Verify the data and semantic model

1. In the workspace item list, select the SQL analytics endpoint with the same name as
   the Lakehouse. The SQL query editor opens. For details, see [Microsoft Learn guidance
   for accessing a Lakehouse SQL analytics endpoint][fabric-sql-endpoint].
2. In the explorer pane, expand **Tables** > **dbo** and wait for the 19 lowercase
   tables to appear.
3. Paste this query into the editor and select **Run**:

   ```sql
   SELECT TOP (2) ShipmentId, CustomerOrderId, ShipmentQuantity
   FROM dbo.shipment
   WHERE ShipmentId IN ('SHIPMENT-0001', 'SHIPMENT-0002')
   ORDER BY ShipmentId;
   ```

   **Expect:** both shipments appear, each with a quantity of **120**.

4. Return to the `FabricIQWorkspace` item list.
5. Select the semantic model's **...** menu, then select
   **Write DAX queries**. Paste this query into the DAX query editor and select **Run**.
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
6. Return to the `FabricIQWorkspace` item list.
