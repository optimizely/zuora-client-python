# POSTBillingPreviewInvoiceItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_to_item_id** | **str** | The unique ID of the invoice item that the discount charge is applied to.  | [optional] 
**charge_amount** | **str** | The amount of the charge. This amount doesn&#39;t include taxes regardless if the charge&#39;s tax mode is inclusive or exclusive.  | [optional] 
**charge_date** | **datetime** | The date when the invoice item was created.  | [optional] 
**charge_description** | **str** | Description of the charge.  | [optional] 
**charge_id** | **str** | Id of the charge.  | [optional] 
**charge_name** | **str** | Name of the charge.  | [optional] 
**charge_number** | **str** | Number of the charge.  | [optional] 
**charge_type** | **str** | The type of charge.   Possible values are &#x60;OneTime&#x60;, &#x60;Recurring&#x60;, and &#x60;Usage&#x60;.  | [optional] 
**id** | **str** | Invoice item ID.  | [optional] 
**processing_type** | **str** | Identifies the kind of charge.   Possible values: * charge * discount * prepayment * tax | [optional] 
**product_name** | **str** | Name of the product associated with this item.  | [optional] 
**quantity** | **str** | Quantity of this item, in the configured unit of measure for the charge.  | [optional] 
**service_end_date** | **date** | End date of the service period for this item, i.e., the last day of the service period, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**service_start_date** | **date** | Start date of the service period for this item, in &#x60;yyyy-mm-dd&#x60; format. If the charge is a one-time fee, this is the date of that charge.  | [optional] 
**subscription_id** | **str** | ID of the subscription associated with this item.  | [optional] 
**subscription_name** | **str** | Name of the subscription associated with this item.  | [optional] 
**subscription_number** | **str** | Number of the subscription associated with this item.  | [optional] 
**tax_amount** | **str** | Tax applied to the charge. This field returns &#x60;0&#x60; becasue the BillingPreview operation does not calculate taxes for charges in the subscription.  | [optional] 
**unit_of_measure** | **str** | Unit used to measure consumption.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


