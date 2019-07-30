# zuora_client.SequenceSetsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_sequence_set**](SequenceSetsApi.md#d_elete_sequence_set) | **DELETE** /v1/sequence-sets/{id} | Delete sequence set
[**g_et_sequence_set**](SequenceSetsApi.md#g_et_sequence_set) | **GET** /v1/sequence-sets/{id} | Get sequence set
[**g_et_sequence_sets**](SequenceSetsApi.md#g_et_sequence_sets) | **GET** /v1/sequence-sets | Get sequence sets
[**p_ost_sequence_sets**](SequenceSetsApi.md#p_ost_sequence_sets) | **POST** /v1/sequence-sets | Create sequence sets
[**p_ut_sequence_set**](SequenceSetsApi.md#p_ut_sequence_set) | **PUT** /v1/sequence-sets/{id} | Update sequence set


# **d_elete_sequence_set**
> CommonResponseType d_elete_sequence_set(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Delete sequence set

Deletes a specific billing document sequence set. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.SequenceSetsApi()
id = 'id_example' # str | The ID of the sequence set to delete
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Delete sequence set
    api_response = api_instance.d_elete_sequence_set(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceSetsApi->d_elete_sequence_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the sequence set to delete | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_sequence_set**
> GETSequenceSetResponse g_et_sequence_set(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Get sequence set

Retrieves information about a specific billing document sequence set.  **Note**: The Credit and Debit Memos feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.SequenceSetsApi()
id = 'id_example' # str | The ID of the sequence set to return.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Get sequence set
    api_response = api_instance.g_et_sequence_set(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceSetsApi->g_et_sequence_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the sequence set to return. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**GETSequenceSetResponse**](GETSequenceSetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_sequence_sets**
> GETSequenceSetsResponse g_et_sequence_sets(zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, page_size=page_size, page=page, name=name)

Get sequence sets

Retrieves information about all billing document sequence sets.   You can use query parameters to restrict the data returned in the response.  **Note**: The Credit and Debit Memos feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.SequenceSetsApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
page_size = 20 # int | Number of rows returned per page.  (optional) (default to 20)
page = 1 # int | Page number.  (optional) (default to 1)
name = 'name_example' # str | The name of a specific billing document sequence set.  (optional)

try:
    # Get sequence sets
    api_response = api_instance.g_et_sequence_sets(zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, page_size=page_size, page=page, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceSetsApi->g_et_sequence_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] [default to 20]
 **page** | **int**| Page number.  | [optional] [default to 1]
 **name** | **str**| The name of a specific billing document sequence set.  | [optional] 

### Return type

[**GETSequenceSetsResponse**](GETSequenceSetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_sequence_sets**
> POSTSequenceSetsResponse p_ost_sequence_sets(request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Create sequence sets

Creates billing document sequence sets, allowing distinct gapless numbering sequences for invoices, credit memos, and debit memos.   You can create a maximum of 100 billing document sequence sets at a time. A sequence set comprises a set of custom prefixes and starting document numbers that are used for billing documents to generate.  See [Prefix and Numbering Configuration for Billing Documents](https://knowledgecenter.zuora.com/CB_Billing/Billing_Settings/Prefix_and_Numbering_Configuration_for_Billing_Documents) for more information about limitations.  **Note**: The Credit and Debit Memos feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.SequenceSetsApi()
request = zuora_client.POSTSequenceSetsRequest() # POSTSequenceSetsRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Create sequence sets
    api_response = api_instance.p_ost_sequence_sets(request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceSetsApi->p_ost_sequence_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**POSTSequenceSetsRequest**](POSTSequenceSetsRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**POSTSequenceSetsResponse**](POSTSequenceSetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_sequence_set**
> PUTSequenceSetResponse p_ut_sequence_set(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, sequence_set=sequence_set)

Update sequence set

Updates a specific billing document sequence set.  **Note**: The Credit and Debit Memos feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.SequenceSetsApi()
id = 'id_example' # str | The ID of the sequence set to update.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
sequence_set = zuora_client.PUTSequenceSetRequest() # PUTSequenceSetRequest | Sequence set to modify (optional)

try:
    # Update sequence set
    api_response = api_instance.p_ut_sequence_set(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, sequence_set=sequence_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceSetsApi->p_ut_sequence_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the sequence set to update. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **sequence_set** | [**PUTSequenceSetRequest**](PUTSequenceSetRequest.md)| Sequence set to modify | [optional] 

### Return type

[**PUTSequenceSetResponse**](PUTSequenceSetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

