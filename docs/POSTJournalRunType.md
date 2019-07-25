# POSTJournalRunType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_period_name** | **str** | Name of the accounting period.  This field determines the target start and end dates of the journal run.  Required if you do not include &#x60;targetStartDate&#x60; and &#x60;targetEndDate&#x60;.  | [optional] 
**journal_entry_date** | **date** | Date of the journal entry.  | 
**target_end_date** | **date** | The target end date of the journal run.  If you include &#x60;accountingPeriodName&#x60;, the &#x60;targetEndDate&#x60; must be empty or the same as the end date of the accounting period specified in &#x60;accountingPeriodName&#x60;.  | [optional] 
**target_start_date** | **date** | The target start date of the journal run.  Required if you include targetEndDate.  If you include &#x60;accountingPeriodName&#x60;, the &#x60;targetStartDate&#x60; must be empty or the same as the start date of the accounting period specified in &#x60;accountingPeriodName&#x60;.  | [optional] 
**transaction_types** | [**list[POSTJournalRunTransactionType]**](POSTJournalRunTransactionType.md) | Transaction types included in the journal run.  You can include one or more transaction types.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

