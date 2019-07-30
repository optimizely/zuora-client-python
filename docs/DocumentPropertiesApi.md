# zuora_client.DocumentPropertiesApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_document_properties**](DocumentPropertiesApi.md#d_elete_document_properties) | **DELETE** /v1/document-properties/{documentPropertiesId} | Delete document properties
[**g_et_document_properies**](DocumentPropertiesApi.md#g_et_document_properies) | **GET** /v1/document-properties/{documentType}/{documentId} | Get document properties
[**p_ost_document_properties**](DocumentPropertiesApi.md#p_ost_document_properties) | **POST** /v1/document-properties | Create document properties
[**p_ut_document_properties**](DocumentPropertiesApi.md#p_ut_document_properties) | **PUT** /v1/document-properties/{documentPropertiesId} | Update document properties


# **d_elete_document_properties**
> CommonResponseType d_elete_document_properties(document_properties_id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Delete document properties

**Note:** This feature is available only if you have the Billing Document Properties Setup feature enabled. The Billing Document Properties Setup feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Deletes document properties with a specific ID for a billing document. Billing documents include invoices, credit memos, and debit memos.  **Note:** You can delete document properties for credit and debit memos only if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DocumentPropertiesApi()
document_properties_id = 'document_properties_id_example' # str | The unique ID of document properties. For example, 402892c74c9193cd014c96bbe7c101f9. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Delete document properties
    api_response = api_instance.d_elete_document_properties(document_properties_id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentPropertiesApi->d_elete_document_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_properties_id** | **str**| The unique ID of document properties. For example, 402892c74c9193cd014c96bbe7c101f9.  | 
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

# **g_et_document_properies**
> GETDocumentPropertiesResponseType g_et_document_properies(document_type, document_id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Get document properties

**Note:** This feature is available only if you have the Billing Document Properties Setup feature enabled. The Billing Document Properties Setup feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieve information about document properties of a billing document. Billing documents include invoices, credit memos, and debit memos.    **Note:** You can retrieve information about document properties of credit and debit memos only if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DocumentPropertiesApi()
document_type = 'document_type_example' # str | The type of the billing document.  
document_id = 'document_id_example' # str | The unique ID of document properties to be retrieved. For example, 402892c74c9193cd014c96bbe7c101f9. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Get document properties
    api_response = api_instance.g_et_document_properies(document_type, document_id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentPropertiesApi->g_et_document_properies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_type** | **str**| The type of the billing document.   | 
 **document_id** | **str**| The unique ID of document properties to be retrieved. For example, 402892c74c9193cd014c96bbe7c101f9.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**GETDocumentPropertiesResponseType**](GETDocumentPropertiesResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_document_properties**
> GETDocumentPropertiesResponseType p_ost_document_properties(request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Create document properties

**Note:** This feature is available only if you have the Billing Document Properties Setup feature enabled. The Billing Document Properties Setup feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates custom document properties for a billing document. For example, a document property can be a custom name used for files generated for billing documents. Billing documents include invoices, credit memos, and debit memos.  If you want to configure custom file names for billing documents created through API operations, you have to call this operation before posting the billing documents.   **Note:** You can create document properties for credit and debit memos only if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DocumentPropertiesApi()
request = zuora_client.POSTDocumentPropertiesType() # POSTDocumentPropertiesType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Create document properties
    api_response = api_instance.p_ost_document_properties(request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentPropertiesApi->p_ost_document_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**POSTDocumentPropertiesType**](POSTDocumentPropertiesType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**GETDocumentPropertiesResponseType**](GETDocumentPropertiesResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_document_properties**
> GETDocumentPropertiesResponseType p_ut_document_properties(request, document_properties_id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Update document properties

**Note:** This feature is available only if you have the Billing Document Properties Setup feature enabled. The Billing Document Properties Setup feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Updates document properties with a specific ID for a billing document. Billing documents include invoices, credit memos, and debit memos.  **Note:** You can update document properties for credit and debit memos only if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DocumentPropertiesApi()
request = zuora_client.PUTDocumentPropertiesType() # PUTDocumentPropertiesType | 
document_properties_id = 'document_properties_id_example' # str | The unique ID of document properties to be updated. For example, 402892c74c9193cd014c96bbe7c101f9. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Update document properties
    api_response = api_instance.p_ut_document_properties(request, document_properties_id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentPropertiesApi->p_ut_document_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PUTDocumentPropertiesType**](PUTDocumentPropertiesType.md)|  | 
 **document_properties_id** | **str**| The unique ID of document properties to be updated. For example, 402892c74c9193cd014c96bbe7c101f9.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**GETDocumentPropertiesResponseType**](GETDocumentPropertiesResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

