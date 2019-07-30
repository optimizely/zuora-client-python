# PUTBasicSummaryJournalEntryType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journal_entry_items** | [**list[PUTJournalEntryItemType]**](PUTJournalEntryItemType.md) | Key name that represents the list of journal entry items.  | [optional] 
**notes** | **str** | Additional information about this record.  ***Character limit:*** 2,000  | [optional] 
**transferred_to_accounting** | **str** | Status shows whether the journal entry has been transferred to an accounting system.   This field cannot be changed after the summary journal entry has been canceled.  **Note:** The Zuora Finance ***Override Transferred to Accounting*** permission is required to change &#x60;transferredToAccounting&#x60; from &#x60;Yes&#x60; to any other value.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


