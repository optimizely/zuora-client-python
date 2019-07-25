# EventTrigger

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the trigger. | [optional] 
**base_object** | **str** | The base object that the trigger rule is defined upon. Should be specified in the pattern: ^[A-Z][\\\\w\\\\-]*$ | [optional] 
**condition** | **str** | The JEXL expression to be evaluated against object changes. See above for more information and an example. | [optional] 
**description** | **str** | The description of the trigger. | [optional] 
**event_type** | [**EventType**](EventType.md) |  | [optional] 
**id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

