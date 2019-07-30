# PUTOrderActionTriggerDatesRequestTypeOrderActions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charges** | [**list[PUTOrderActionTriggerDatesRequestTypeCharges]**](PUTOrderActionTriggerDatesRequestTypeCharges.md) |  | [optional] 
**sequence** | **int** | Identifies which order action will have its triggering dates updated. Currently, you can only update the triggering dates of &#x60;CreateSubscription&#x60; order actions. This means that you must set &#x60;sequence&#x60; to 0, as there is only one &#x60;CreateSubscription&#x60; order action that affects each subscription.  | 
**trigger_dates** | [**list[PUTOrderActionTriggerDatesRequestTypeTriggerDates]**](PUTOrderActionTriggerDatesRequestTypeTriggerDates.md) | Container for the service activation and customer acceptance dates of the order action. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


