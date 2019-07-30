# OrderSubscriptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_version** | **int** | The base version of the subscription. | [optional] 
**custom_fields** | [**SubscriptionObjectCustomFields**](SubscriptionObjectCustomFields.md) |  | [optional] 
**new_version** | **int** | The latest version of the subscription. | [optional] 
**order_actions** | [**list[OrderAction]**](OrderAction.md) |  | [optional] 
**sequence** | **int** | The sequence number of a certain subscription processed by the order. | [optional] 
**subscription_number** | **str** | The new subscription number for a new subscription created, or the existing subscription number. Unlike the order request, the subscription number here always has a value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


