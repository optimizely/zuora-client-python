# OrderItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **date** | The order item&#x27;s effective end date, aligned with the end date of an increased quantity order metrics. | [optional] 
**id** | **str** | The ID of the order item. | [optional] 
**order_action_id** | **str** | Specify the order action that creates this order item. | [optional] 
**quantity** | [**BigDecimal**](BigDecimal.md) | The order item quantity. For the usage charge type, the value of this field is always zero. Also, the Owner Transfer order action always creates an order item whose Quantity field is zero. | [optional] 
**sc_id** | **str** | The ID of the charge segment that gets newly generated when the order item is created. | [optional] 
**start_date** | **date** | The order item&#x27;s effective start date, aligned with the start date of an increased quantity order metrics. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

