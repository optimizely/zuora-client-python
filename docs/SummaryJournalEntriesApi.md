# zuora_client.SummaryJournalEntriesApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_summary_journal_entry**](SummaryJournalEntriesApi.md#d_elete_summary_journal_entry) | **DELETE** /v1/journal-entries/{je-number} | Delete summary journal entry
[**g_et_all_summary_journal_entries**](SummaryJournalEntriesApi.md#g_et_all_summary_journal_entries) | **GET** /v1/journal-entries/journal-runs/{jr-number} | Get all summary journal entries in a journal run
[**g_et_summary_journal_entry**](SummaryJournalEntriesApi.md#g_et_summary_journal_entry) | **GET** /v1/journal-entries/{je-number} | Get summary journal entry
[**p_ost_summary_journal_entry**](SummaryJournalEntriesApi.md#p_ost_summary_journal_entry) | **POST** /v1/journal-entries | Create summary journal entry
[**p_ut_basic_summary_journal_entry**](SummaryJournalEntriesApi.md#p_ut_basic_summary_journal_entry) | **PUT** /v1/journal-entries/{je-number}/basic-information | Update basic information of a summary journal entry
[**p_ut_summary_journal_entry**](SummaryJournalEntriesApi.md#p_ut_summary_journal_entry) | **PUT** /v1/journal-entries/{je-number}/cancel | Cancel summary journal entry


# **d_elete_summary_journal_entry**
> CommonResponseType d_elete_summary_journal_entry(je_number, zuora_entity_ids=zuora_entity_ids)

Delete summary journal entry

This reference describes how to delete a summary journal entry using the REST API.  You must have the \"Delete Cancelled Journal Entry\" user permission enabled to delete summary journal entries.  A summary journal entry must be canceled before it can be deleted. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.SummaryJournalEntriesApi()
je_number = 'je_number_example' # str | Journal entry number in the format JE-00000001.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete summary journal entry
    api_response = api_instance.d_elete_summary_journal_entry(je_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryJournalEntriesApi->d_elete_summary_journal_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **je_number** | **str**| Journal entry number in the format JE-00000001. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_all_summary_journal_entries**
> GETJournalEntriesInJournalRunType g_et_all_summary_journal_entries(jr_number, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get all summary journal entries in a journal run

 This REST API reference describes how to retrieve information about all summary journal entries in a journal run. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.SummaryJournalEntriesApi()
jr_number = 'jr_number_example' # str | Journal run number.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 8 # int | Number of rows returned per page.  (optional) (default to 8)

try:
    # Get all summary journal entries in a journal run
    api_response = api_instance.g_et_all_summary_journal_entries(jr_number, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryJournalEntriesApi->g_et_all_summary_journal_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jr_number** | **str**| Journal run number. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] [default to 8]

### Return type

[**GETJournalEntriesInJournalRunType**](GETJournalEntriesInJournalRunType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_summary_journal_entry**
> GETJournalEntryDetailType g_et_summary_journal_entry(je_number, zuora_entity_ids=zuora_entity_ids)

Get summary journal entry

This REST API reference describes how to get information about a summary journal entry by its journal entry number. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.SummaryJournalEntriesApi()
je_number = 'je_number_example' # str | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get summary journal entry
    api_response = api_instance.g_et_summary_journal_entry(je_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryJournalEntriesApi->g_et_summary_journal_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **je_number** | **str**|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETJournalEntryDetailType**](GETJournalEntryDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_summary_journal_entry**
> POSTJournalEntryResponseType p_ost_summary_journal_entry(request, zuora_entity_ids=zuora_entity_ids)

Create summary journal entry

This REST API reference describes how to manually create a summary journal entry. Request and response field descriptions and sample code are provided. ## Requirements 1.The sum of debits must equal the sum of credits in the summary journal entry.  2.The following applies only if you use foreign currency conversion:   * If you have configured Aggregate transactions with different currencies during a Journal Run to \"Yes\", the value of the **currency** field must be the same as your tenant's home currency. That is, you must create journal entries using your home currency.   * All journal entries in an accounting period must either all be aggregated or all be unaggregated. You cannot have a mix of aggregated and unaggregated journal entries in the same accounting period. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.SummaryJournalEntriesApi()
request = zuora_client.POSTJournalEntryType() # POSTJournalEntryType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create summary journal entry
    api_response = api_instance.p_ost_summary_journal_entry(request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryJournalEntriesApi->p_ost_summary_journal_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**POSTJournalEntryType**](POSTJournalEntryType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTJournalEntryResponseType**](POSTJournalEntryResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_basic_summary_journal_entry**
> CommonResponseType p_ut_basic_summary_journal_entry(je_number, request, zuora_entity_ids=zuora_entity_ids)

Update basic information of a summary journal entry

 This REST API reference describes how to update the basic information of a summary journal entry. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.SummaryJournalEntriesApi()
je_number = 'je_number_example' # str | Journal entry number in the format JE-00000001.
request = zuora_client.PUTBasicSummaryJournalEntryType() # PUTBasicSummaryJournalEntryType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update basic information of a summary journal entry
    api_response = api_instance.p_ut_basic_summary_journal_entry(je_number, request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryJournalEntriesApi->p_ut_basic_summary_journal_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **je_number** | **str**| Journal entry number in the format JE-00000001. | 
 **request** | [**PUTBasicSummaryJournalEntryType**](PUTBasicSummaryJournalEntryType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_summary_journal_entry**
> CommonResponseType p_ut_summary_journal_entry(je_number, zuora_entity_ids=zuora_entity_ids)

Cancel summary journal entry

 This reference describes how to cancel a summary journal entry using the REST API.  You must have the \"Cancel Journal Entry\" user permission enabled to cancel summary journal entries.  A summary journal entry cannot be canceled if its Transferred to Accounting status is \"Yes\" or \"Processing\". 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.SummaryJournalEntriesApi()
je_number = 'je_number_example' # str | Journal entry number in the format JE-00000001.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Cancel summary journal entry
    api_response = api_instance.p_ut_summary_journal_entry(je_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryJournalEntriesApi->p_ut_summary_journal_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **je_number** | **str**| Journal entry number in the format JE-00000001. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

