# GETMassUpdateType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | Type of mass action.  | [optional] 
**ended_on** | **datetime** | Date and time that the mass action was completed. The format is &#x60;yyyy-MM-dd hh:mm:ss&#x60;.  | [optional] 
**error_count** | **str** | Total number of failed records.  This field is updated in real time. When the mass action **status** is Processing, this field returns the number of records that have failed so far. When the mass action **status** is Pending, this field is null.  | [optional] 
**input_size** | **int** | Size of the input file in bytes.  | [optional] 
**output_size** | **int** | Size of the response file in bytes.  | [optional] 
**output_type** | **str** | Type of output for the response file. The following table describes the output type.  | Output Type    | Description                         | |----------------|-------------------------------------| | (url:.csv.zip) | URL pointing to a zipped .csv file. |  | [optional] 
**output_url** | **str** | URL to download the response file. The response file is a zipped .csv file.  The response file is identical to the file you uploaded to perform the mass action, with additional columns providing information about the outcome of each record.  This field only returns a value when the mass action **status** is Completed or Stopped. Otherwise, this field is null.  | [optional] 
**processed_count** | **str** | Total number of processed records. This field is equal to the sum of &#x60;errorCount&#x60; and &#x60;successCount&#x60;.  This field is updated in real time. When the mass action **status** is Processing, this field returns the number of records that have been processed so far. When the mass action **status** is Pending, this field is null.  | [optional] 
**started_on** | **datetime** | Date and time that Zuora started processing the mass action. The format is &#x60;yyyy-MM-dd hh:mm:ss&#x60;.  | [optional] 
**status** | **str** | Status of the mass action. The following table describes the mass action statuses.  | Status     | Description                                                                | |------------|----------------------------------------------------------------------------| | Pending    | Mass action has not yet started being processed.                           | | Processing | Mass action is in progress.                                                | | Stopping   | Mass action is in the process of stopping, but has not yet stopped.        | | Stopped    | Mass action has stopped.                                                   | | Completed  | Mass action was successfully completed. There may still be failed records. | | Failed     | Mass action failed. No records are processed. No response file is created. |  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**success_count** | **str** | Total number of successful records. This field is updated in real time. When the mass action **status** is Processing, this field returns the number of records that have succeeded so far. When the mass action **status** is Pending, this field is null.  | [optional] 
**total_count** | **str** | Total number of records in the uploaded mass action file. When the mass action **status** is Pending, this field is null.  | [optional] 
**uploaded_by** | **str** | Email of the person who uploaded the mass action file.  | [optional] 
**uploaded_on** | **datetime** | Date and time that the mass action file was uploaded. The format is &#x60;yyyy-MM-dd hh:mm:ss&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

