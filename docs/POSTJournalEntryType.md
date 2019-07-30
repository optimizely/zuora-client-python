# POSTJournalEntryType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_period_name** | **str** | Name of the accounting period. The open-ended accounting period is named &#x60;Open-Ended&#x60;.  | 
**currency** | **str** | The type of currency used. Currency must be active.  | 
**journal_entry_date** | **date** | Date of the journal entry.  | 
**journal_entry_items** | [**list[POSTJournalEntryItemType]**](POSTJournalEntryItemType.md) | Key name that represents the list of journal entry items.  | 
**notes** | **str** | The number associated with the revenue event.  Character limit: 2,000  | [optional] 
**segments** | [**list[POSTJournalEntrySegmentType]**](POSTJournalEntrySegmentType.md) | List of segments that apply to the summary journal entry.  | [optional] 
**transferred_to_accounting** | **str** | Status shows whether the journal entry has been transferred to an accounting system.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


