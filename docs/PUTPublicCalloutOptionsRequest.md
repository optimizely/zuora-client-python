# PUTPublicCalloutOptionsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirm_suc_from_res_content** | **bool** | If the value is &#x60;false&#x60;, callout is successful when response code is 200. If value is &#x60;true&#x60;, when the response code is 200, and ONLY when response &#x60;Content-Type&#x60; is &#x60;application/json&#x60; and body payload is &#x60;{success:true}&#x60;, the callout is succesful. | [optional] 
**interval_time** | **int** | The interval, in minutes, between callout retries. | [optional] 
**retry_number** | **int** | The number of retries when the callout fails. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


