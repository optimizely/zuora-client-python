# PUTOrderTriggerDatesResponseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_id** | **str** | The Id of the process that handle the operation.  | [optional] 
**reasons** | [**list[CommonResponseTypeReasons]**](CommonResponseTypeReasons.md) |  | [optional] 
**success** | **bool** | Indicates whether the call succeeded.  | [optional] 
**account_number** | **str** | The account number for the order. | [optional] 
**order_number** | **str** | The order number of the order updated. | [optional] 
**status** | **str** | Status of the order. &#x60;Pending&#x60; is only applicable for an order that contains a &#x60;CreateSubscription&#x60; order action. | [optional] 
**subscriptions** | [**list[PUTOrderTriggerDatesResponseTypeSubscriptions]**](PUTOrderTriggerDatesResponseTypeSubscriptions.md) | The subscriptions updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


