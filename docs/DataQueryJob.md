# DataQueryJob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_file** | **str** | The URL of the query results. Only applicable if the value of the &#x60;queryStatus&#x60; field is &#x60;completed&#x60;.  | [optional] 
**output_rows** | **int** | The number of rows the query results. Only applicable if the value of the &#x60;queryStatus&#x60; field is &#x60;completed&#x60;.  | [optional] 
**processing_time** | **int** | Processing time of the query job, in milliseconds. Only applicable if the value of the &#x60;queryStatus&#x60; field is &#x60;completed&#x60;.  | [optional] 
**query_status** | **str** | Status of the query job.  If the value of this field is &#x60;completed&#x60;, the &#x60;dataFile&#x60; field contains the location of the query results.  If the value of this field is &#x60;accepted&#x60; or &#x60;in_progress&#x60;, you can use [Cancel data query job](#operation/DELETE_DataQueryJob) to prevent Zuora from performing the query. Zuora then sets the status of the query job to &#x60;cancelled&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

