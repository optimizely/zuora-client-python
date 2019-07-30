# OrderAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_product** | [**RatePlanOverride**](RatePlanOverride.md) |  | [optional] 
**cancel_subscription** | [**CancelSubscription**](CancelSubscription.md) |  | [optional] 
**create_subscription** | [**CreateSubscription**](CreateSubscription.md) |  | [optional] 
**custom_fields** | [**OrderActionObjectCustomFields**](OrderActionObjectCustomFields.md) |  | [optional] 
**order_items** | [**list[OrderItem]**](OrderItem.md) |  | [optional] 
**order_metrics** | [**list[OrderMetric]**](OrderMetric.md) |  | [optional] 
**owner_transfer** | [**OwnerTransfer**](OwnerTransfer.md) |  | [optional] 
**remove_product** | [**RemoveProduct**](RemoveProduct.md) |  | [optional] 
**resume** | [**GetOrderResume**](GetOrderResume.md) |  | [optional] 
**sequence** | **int** | The sequence of the order actions processed in the order. | [optional] 
**suspend** | [**GetOrderSuspend**](GetOrderSuspend.md) |  | [optional] 
**terms_and_conditions** | [**TermsAndConditions**](TermsAndConditions.md) |  | [optional] 
**trigger_dates** | [**list[TriggerDate]**](TriggerDate.md) |  | [optional] 
**type** | **str** | Type of the order action. | [optional] 
**update_product** | [**RatePlanUpdate**](RatePlanUpdate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


