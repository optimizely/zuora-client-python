# PUTPublicNotificationDefinitionRequestCallout

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the callout. The default is true. | [optional] [default to True]
**callout_auth** | [**CalloutAuth**](CalloutAuth.md) |  | [optional] 
**callout_baseurl** | **str** | The callout URL. It must start with &#39;https://&#39; | 
**callout_params** | [**CalloutMergeFields**](CalloutMergeFields.md) |  | [optional] 
**callout_retry** | **bool** | Specified whether to retry the callout when the callout fails. The default is true. | [optional] [default to True]
**description** | **str** | Description for the callout. | [optional] 
**http_method** | **str** | The HTTP method of the callout. | 
**name** | **str** | The name of the created callout. | 
**required_auth** | **bool** | Specifies whether the callout requires auth. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


