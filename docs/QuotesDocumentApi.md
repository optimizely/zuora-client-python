# swagger_client.QuotesDocumentApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_ost_quotes_document**](QuotesDocumentApi.md#p_ost_quotes_document) | **POST** /v1/quotes/document | Generate quotes document

# **p_ost_quotes_document**
> POSTQuoteDocResponseType p_ost_quotes_document(body, zuora_entity_ids=zuora_entity_ids)

Generate quotes document

The `document` call generates a quote document and returns the generated document URL. You can directly access the generated quote file through the returned URL.  The `document` call should be only used from Zuora Quotes.   ## File Size Limitation  The maximum export file size is 2047MB. If you have large data requests that go over this limit, you will get the following 403 HTTP response code from Zuora: `security:max-object-size>2047MB</security:max-object-size>`  Submit a request at [Zuora Global Support](http://support.zuora.com/) if you require additional assistance.  We can work with you to determine if large file optimization is an option for you. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotesDocumentApi()
body = swagger_client.POSTQuoteDocType() # POSTQuoteDocType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Generate quotes document
    api_response = api_instance.p_ost_quotes_document(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesDocumentApi->p_ost_quotes_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTQuoteDocType**](POSTQuoteDocType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTQuoteDocResponseType**](POSTQuoteDocResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

