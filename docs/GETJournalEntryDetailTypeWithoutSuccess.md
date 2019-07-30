# GETJournalEntryDetailTypeWithoutSuccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_period_name** | **str** | Name of the accounting period that the journal entry belongs to.  | [optional] 
**aggregate_currency** | **bool** | Returns true if the journal entry is aggregating currencies. That is, if the journal entry was created when the &#x60;Aggregate transactions with different currencies during a JournalRun&#x60; setting was configured to \&quot;Yes\&quot;. Otherwise, returns &#x60;false&#x60;.  | [optional] 
**currency** | **str** | Currency used.  | [optional] 
**home_currency** | **str** | Home currency used.  | [optional] 
**journal_entry_date** | **date** | Date of the journal entry.  | [optional] 
**journal_entry_items** | [**list[GETJournalEntryItemType]**](GETJournalEntryItemType.md) | Key name that represents the list of journal entry items.  | [optional] 
**notes** | **str** | Additional information about this record. Character limit: 2,000  | [optional] 
**number** | **str** | Journal entry number in the format JE-00000001.  | [optional] 
**segments** | [**list[GETJournalEntrySegmentType]**](GETJournalEntrySegmentType.md) | List of segments that apply to the summary journal entry.  | [optional] 
**status** | **str** | Status of journal entry.  | [optional] 
**time_period_end** | **date** | End date of time period included in the journal entry.  | [optional] 
**time_period_start** | **date** | Start date of time period included in the journal entry.  | [optional] 
**transaction_type** | **str** | Transaction type of the transactions included in the summary journal entry.  | [optional] 
**transfer_date_time** | **datetime** | Date and time that transferredToAccounting was changed to &#x60;Yes&#x60;. This field is returned only when transferredToAccounting is &#x60;Yes&#x60;. Otherwise, this field is &#x60;null&#x60;.  | [optional] 
**transferred_by** | **str** | User ID of the person who changed transferredToAccounting to &#x60;Yes&#x60;. This field is returned only when transferredToAccounting is &#x60;Yes&#x60;. Otherwise, this field is &#x60;null&#x60;.  | [optional] 
**transferred_to_accounting** | **str** | Status shows whether the journal entry has been transferred to an accounting system.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


