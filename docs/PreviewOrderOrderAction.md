# PreviewOrderOrderAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_product** | [**PreviewOrderRatePlanOverride**](PreviewOrderRatePlanOverride.md) |  | [optional] 
**cancel_subscription** | [**CancelSubscription**](CancelSubscription.md) |  | [optional] 
**create_subscription** | [**PreviewOrderCreateSubscription**](PreviewOrderCreateSubscription.md) |  | [optional] 
**custom_fields** | [**OrderActionObjectCustomFields**](OrderActionObjectCustomFields.md) |  | [optional] 
**owner_transfer** | [**OwnerTransfer**](OwnerTransfer.md) |  | [optional] 
**remove_product** | [**RemoveProduct**](RemoveProduct.md) |  | [optional] 
**resume** | [**CreateOrderResume**](CreateOrderResume.md) |  | [optional] 
**suspend** | [**CreateOrderSuspend**](CreateOrderSuspend.md) |  | [optional] 
**terms_and_conditions** | [**TermsAndConditions**](TermsAndConditions.md) |  | [optional] 
**trigger_dates** | [**list[TriggerDate]**](TriggerDate.md) | Container for the contract effective, service activation, and customer acceptance dates of the order action.   If the service activation date is set as a required field in Default Subscription Settings, skipping this field in a &#x60;CreateSubscription&#x60; order action of your JSON request will result in a &#x60;Pending&#x60; order and a &#x60;Pending Activation&#x60; subscription.  If the customer acceptance date is set as a required field in Default Subscription Settings, skipping this field in a &#x60;CreateSubscription&#x60; order action of your JSON request will result in a &#x60;Pending&#x60; order and a &#x60;Pending Acceptance&#x60; subscription. If the service activation date field is at the same time required and skipped (or set as null), it will be a &#x60;Pending Activation&#x60; subscription.  | [optional] 
**type** | **str** | Type of order action.  Unless the type of order action is &#x60;RenewSubscription&#x60;, you must use the corresponding field to provide information about the order action. For example, if the type of order action is &#x60;AddProduct&#x60;, you must set the &#x60;addProduct&#x60; field.  Zuora returns an error if you set a field that corresponds to a different type of order action. For example, if the type of order action is &#x60;AddProduct&#x60;, Zuora returns an error if you set the &#x60;updateProduct&#x60; field.  | 
**update_product** | [**PreviewOrderRatePlanUpdate**](PreviewOrderRatePlanUpdate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

