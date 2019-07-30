# POSTSubscriptionPreviewInvoiceItemsType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_amount** | **str** | The amount of the charge. This amount doesn&#39;t include taxes unless the charge&#39;s tax mode is inclusive.  | [optional] 
**charge_description** | **str** | Description of the charge.  | [optional] 
**charge_name** | **str** | Name of the charge.  | [optional] 
**product_name** | **str** | Name of the product associated with this item.  | [optional] 
**product_rate_plan_charge_id** | **str** | ID of the product rate plan charge.  | [optional] 
**quantity** | **str** | Quantity of this item.  | [optional] 
**service_end_date** | **date** | End date of the service period for this item, i.e., the last day of the period, as yyyy-mm-dd.  | [optional] 
**service_start_date** | **date** | Service start date as yyyy-mm-dd. If the charge is a one-time fee, this is the date of that charge.  | [optional] 
**tax_amount** | **float** | The tax amount of the invoice item.  | [optional] 
**unit_of_measure** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


