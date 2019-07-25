# TriggerParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specific_trigger_date** | **date** | Date in YYYY-MM-DD format. Only applicable if the value of the &#x60;triggerEvent&#x60; field is &#x60;SpecificDate&#x60;.   While this field is applicable, if this field is skipped or its value is left as null, your &#x60;CreateSubscription&#x60; order action will create a &#x60;Pending&#x60; order and a &#x60;Pending Acceptance&#x60; subscription. If at the same time the service activation date is set as required and its value is null, a &#x60;Pending Activation&#x60; subscription will be created.  | [optional] 
**trigger_event** | **str** | Condition for the charge to become active.  If the value of this field is &#x60;SpecificDate&#x60;, use the &#x60;specificTriggerDate&#x60; field to specify the date when the charge becomes active.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

