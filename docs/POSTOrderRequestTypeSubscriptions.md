# POSTOrderRequestTypeSubscriptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | [**SubscriptionObjectCustomFields**](SubscriptionObjectCustomFields.md) |  | [optional] 
**order_actions** | [**list[CreateOrderOrderAction]**](CreateOrderOrderAction.md) | The actions to be applied to the subscription. Order actions will be stored with the sequence when it was provided in the request. | [optional] 
**subscription_number** | **str** | Leave this empty to represent new subscription creation. Specify a subscription number to update an existing subscription.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


