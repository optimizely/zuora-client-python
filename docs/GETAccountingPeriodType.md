# GETAccountingPeriodType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | ID of the user who created the accounting period.  | [optional] 
**created_on** | **datetime** | Date and time when the accounting period was created.  | [optional] 
**end_date** | **date** | The end date of the accounting period.  | [optional] 
**file_ids** | [**GETAccountingPeriodTypeFileIds**](GETAccountingPeriodTypeFileIds.md) |  | [optional] 
**fiscal_year** | **str** | Fiscal year of the accounting period.  | [optional] 
**fiscal_quarter** | **int** |  | [optional] 
**id** | **str** | ID of the accounting period.  | [optional] 
**name** | **str** | Name of the accounting period.  | [optional] 
**notes** | **str** | Any optional notes about the accounting period.  | [optional] 
**run_trial_balance_end** | **datetime** | Date and time that the trial balance was completed. If the trial balance status is &#x60;Pending&#x60;, &#x60;Processing&#x60;, or &#x60;Error&#x60;, this field is &#x60;null&#x60;.  | [optional] 
**run_trial_balance_error_message** | **str** | If trial balance status is Error, an error message is returned in this field.  | [optional] 
**run_trial_balance_start** | **datetime** | Date and time that the trial balance was run. If the trial balance status is Pending, this field is null.  | [optional] 
**run_trial_balance_status** | **str** | Status of the trial balance for the accounting period. Possible values:  * &#x60;Pending&#x60; * &#x60;Processing&#x60; * &#x60;Completed&#x60; * &#x60;Error&#x60;  | [optional] 
**start_date** | **date** | The start date of the accounting period.  | [optional] 
**status** | **str** | Status of the accounting period. Possible values: * &#x60;Open&#x60; * &#x60;PendingClose&#x60; * &#x60;Closed&#x60;  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**updated_by** | **str** | ID of the user who last updated the accounting period.  | [optional] 
**updated_on** | **datetime** | Date and time when the accounting period was last updated.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


