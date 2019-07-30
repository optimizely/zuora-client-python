# POSTBillingPreviewCreditMemoItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the credit memo item. For tax-inclusive credit memo items, the amount indicates the credit memo item amount including tax. For tax-exclusive credit memo items, the amount indicates the credit memo item amount excluding tax  | [optional] 
**amount_without_tax** | **float** | The credit memo item amount excluding tax.  | [optional] 
**applied_to_item_id** | **str** | The unique ID of the credit memo item that the discount charge is applied to.  | [optional] 
**charge_date** | **datetime** | The date when the credit memo item is created.  | [optional] 
**charge_number** | **str** | Number of the charge.  | [optional] 
**charge_type** | **str** | The type of charge.   Possible values are &#x60;OneTime&#x60;, &#x60;Recurring&#x60;, and &#x60;Usage&#x60;.  | [optional] 
**comment** | **str** | Comment of the credit memo item.  | [optional] 
**id** | **str** | Credit memo item id.  | [optional] 
**processing_type** | **str** | Identifies the kind of charge.   Possible values: * charge * discount * prepayment * tax  | [optional] 
**quantity** | **str** | Quantity of this item, in the configured unit of measure for the charge.  | [optional] 
**rate_plan_charge_id** | **str** | Id of the rate plan charge associated with this item.  | [optional] 
**service_end_date** | **date** | End date of the service period for this item, i.e., the last day of the service period, in yyyy-mm-dd format.  | [optional] 
**service_start_date** | **date** | Start date of the service period for this item, in yyyy-mm-dd format. If the charge is a one-time fee, this is the date of that charge.  | [optional] 
**sku** | **str** | Unique SKU for the product associated with this item.  | [optional] 
**sku_name** | **str** | Name of the unique SKU for the product associated with this item.  | [optional] 
**subscription_id** | **str** | ID of the subscription associated with this item.  | [optional] 
**subscription_number** | **str** | Name of the subscription associated with this item.  | [optional] 
**unit_of_measure** | **str** | Unit used to measure consumption.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


