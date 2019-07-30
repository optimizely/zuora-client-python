# InvoiceItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the invoice item&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the invoice item was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**applied_to_item_id** | **str** | The unique ID of the invoice item that the discount charge is applied to. | [optional] 
**available_to_credit_amount** | **float** | The amount of the invoice item that is available to credit.          | [optional] 
**balance** | **str** | The balance of the invoice item. | [optional] 
**charge_amount** | **str** | The amount of the charge. This amount does not include taxes regardless if the charge&#39;s tax mode is inclusive or exclusive. | [optional] 
**charge_description** | **str** | Description of the charge. | [optional] 
**charge_id** | **str** | ID of the charge. | [optional] 
**charge_name** | **str** | Name of the charge. | [optional] 
**id** | **str** | Item ID. | [optional] 
**product_name** | **str** | Name of the product associated with this item. | [optional] 
**quantity** | **str** | Quantity of this item, in the configured unit of measure for the charge. | [optional] 
**service_end_date** | **date** | End date of the service period for this item, i.e., the last day of the service period, as _yyyy-mm-dd_. | [optional] 
**service_start_date** | **date** | Start date of the service period for this item, as _yyyy-mm-dd_. For a one-time fee item, the date of the charge. | [optional] 
**subscription_id** | **str** | ID of the subscription for this item. | [optional] 
**subscription_name** | **str** | Name of the subscription for this item. | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully. | [optional] 
**tax_amount** | **str** | Tax applied to the charge. | [optional] 
**taxation_items** | [**InvoiceItemTaxationItems**](InvoiceItemTaxationItems.md) |  | [optional] 
**unit_of_measure** | **str** | Unit used to measure. consumption. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


