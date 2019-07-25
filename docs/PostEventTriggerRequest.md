# PostEventTriggerRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the event trigger. | 
**base_object** | **str** | The base object that the trigger rule is defined upon. Should be specified in the pattern: ^[A-Z][\\\\w\\\\-]*$ | 
**condition** | **str** | The JEXL expression to be evaluated against object changes. See above for more information and an example. | 
**description** | **str** | The description of the event trigger. | [optional] 
**event_type** | [**EventType**](EventType.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

