# GETPublicNotificationDefinitionResponseCallout

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the callout. The default is true. | [optional] [default to True]
**callout_auth** | [**CalloutAuth**](CalloutAuth.md) |  | [optional] 
**callout_baseurl** | **str** | The callout URL. It must start with &#39;https://&#39; | [optional] 
**callout_params** | [**CalloutMergeFields**](CalloutMergeFields.md) |  | [optional] 
**callout_retry** | **bool** | Specified whether to retry the callout when the callout fails. The default is true. | [optional] [default to True]
**description** | **str** | Description for the callout. | [optional] 
**event_type_name** | **str** | The name of the event type. | [optional] 
**http_method** | **str** | The HTTP method of the callout. | [optional] 
**id** | **str** | The ID of the callout. If &#x60;calloutActive&#x60; is true, a callout is required. The eventTypeName of the callout MUST be the same as the eventTypeName. | [optional] 
**name** | **str** | The name of the created callout. | [optional] 
**required_auth** | **bool** | Specifies whether the callout requires auth. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


