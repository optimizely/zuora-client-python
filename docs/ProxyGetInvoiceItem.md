# ProxyGetInvoiceItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the invoice item&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the invoice item was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**accounting_code** | **str** |  The accounting code for the item&#39;s charge. Accounting codes group transactions that contain similar accounting attributes. **Character limit**: 100 **Values**: inherited from &#x60;RatePlanCharge.AccountingCode&#x60;  | [optional] 
**applied_to_invoice_item_id** | **str** |  Associates a discount invoice item to a specific invoice item.  **Character limit**: 32  **Values**: inherited from &#x60;InvoiceItem.Id&#x60; for the invoice item that the discount charge is applied to  | [optional] 
**charge_amount** | **float** |  The amount being charged for the invoice item. This amount doesn&#39;t include taxes regardless if the charge&#39;s tax mode is inclusive or exclusive. **Character limit**: **Values**: automatically calculated from multiple fields in multiple objects  | [optional] 
**charge_date** | **datetime** |  The date when the Invoice Item is created . **Character limit**: 29 **Values**: automatically generated  | [optional] 
**charge_name** | **str** |  The name of the invoice item&#39;s charge. **Character limi**t: 50 **Values: **inherited from &#x60;RatePlanCharge.Name&#x60;  | [optional] 
**created_by_id** | **str** |  The user ID of the person who created the invoice item. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**created_date** | **datetime** |  The date the invoice item was created. **Character limit:** 29 **Values**: automatically generated  | [optional] 
**id** | **str** | Object identifier. | [optional] 
**invoice_id** | **str** |  The ID of the invoice that&#39;s associated with this invoice item. **Character limit**: 32 **Values**: inherited from &#x60;Invoice.Id&#x60;  | [optional] 
**processing_type** | **float** |  Identifies the kind of charge where 0 is a charge, 1 is a discount, 2 is a prepayment, and 3 is a tax. The returned value is text not decimal on data sources. **Character limit**: **Values: **  - 0: charge - 1: discount - 2: prepayment - 3: tax  | [optional] 
**product_description** | **str** |  A description of the product associated with this invoice item.  **Character limit**: 500  **Values**: inherited from &#x60;Product.Description&#x60;  **Note**: This value changes if &#x60;Product.Description&#x60; is updated. The values of &#x60;UpdatedById&#x60; and &#x60;UpdatedDate&#x60; for the &#x60;InvoiceItem&#x60; do not change when &#x60;Product.Description&#x60; is updated.  | [optional] 
**product_name** | **str** |  The name of the product associated with this invoice item.  **Character limit**: 255  **Values**: inherited from &#x60;Product.Name&#x60;  **Note**: This value changes if &#x60;Product.Name&#x60; is updated. The values of &#x60;UpdatedById&#x60; and &#x60;UpdatedDate&#x60; for the &#x60;InvoiceItem&#x60; do not change when &#x60;Product.Name&#x60; is updated.  | [optional] 
**quantity** | **float** |  The number of units for this invoice item. **Values**: inherited from &#x60;RatePlanCharge.Quantity&#x60;  | [optional] 
**rate_plan_charge_id** | **str** |  The ID of the rate plan charge that&#39;s associated with this invoice item. **Character limit**: 32 **Values**: inherited from &#x60;RatePlanCharge.Id&#x60;  | [optional] 
**rev_rec_start_date** | **date** |  The date when revenue recognition is triggered. **Character limit**: 29 **Values**: generated from &#x60;InvoiceItem.RevRecTriggerCondition&#x60;  | [optional] 
**sku** | **str** |  The unique SKU for the product associated with this invoice item. **Character limit**: 255 **Values**: inherited from &#x60;Product.SKU&#x60;  | [optional] 
**service_end_date** | **date** |  The end date of the service period associated with this invoice item. Service ends one second before the date in this value. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**service_start_date** | **date** |  The start date of the service period associated with this invoice item. If the associated charge is a one-time fee, then this date is the date of that charge. **Character limit:** 29 **Values**: automatically generated  | [optional] 
**subscription_id** | **str** |  The ID of the subscription associated with the invoice item. **Character limit**: 32 **Values**: inherited from &#x60;Subscription.Id&#x60;  | [optional] 
**tax_amount** | **float** |  The amount of tax applied to the invoice item&#39;s charge. **Character limit**: **Values**: calculated from multiple fields in the ProductRatePlanCharge object  | [optional] 
**tax_code** | **str** |  Specifies the tax code for taxation rules. **Character limit**: 6 **Values**: inherited from &#x60;ProductRatePlanCharge.TaxCode&#x60;  | [optional] 
**tax_exempt_amount** | **float** |  The amount of the invoice item&#39;s charge that&#39;s tax exempt. **Character limit**: **Values**: calculated from multiple fields in the ProductRatePlanCharge object  | [optional] 
**tax_mode** | **str** |  The tax mode of the invoice item. **Character limit**: 12 **Values**: &#x60;TaxExclusive&#x60;, &#x60;TaxInclusive&#x60;  | [optional] 
**uom** | **str** |  Specifies the units to measure usage. **Character limit**: **Values**: inherited from &#x60;ProductRatePlanCharge.UOM&#x60;  | [optional] 
**unit_price** | **float** |  The per-unit price of the invoice item. **Character limit**: **Values**: calculated from multiple fields in ProductRatePlanCharge and ProductRatePlanChargeTier objets  | [optional] 
**updated_by_id** | **str** |  The ID of the user who last updated the invoice item. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**updated_date** | **datetime** |  The date when the invoice item was last updated. **Character limit**: 29 **Values**: automatically generated  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


