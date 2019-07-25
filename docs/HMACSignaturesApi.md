# swagger_client.HMACSignaturesApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_osthmac_signatures**](HMACSignaturesApi.md#p_osthmac_signatures) | **POST** /v1/hmac-signatures | Return HMAC signatures

# **p_osthmac_signatures**
> POSTHMACSignatureResponseType p_osthmac_signatures(body, zuora_entity_ids=zuora_entity_ids)

Return HMAC signatures

This REST API reference describes how to return unique signature and token values that used to process a CORS enabled API call. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HMACSignaturesApi()
body = swagger_client.POSTHMACSignatureType() # POSTHMACSignatureType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Return HMAC signatures
    api_response = api_instance.p_osthmac_signatures(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HMACSignaturesApi->p_osthmac_signatures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTHMACSignatureType**](POSTHMACSignatureType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTHMACSignatureResponseType**](POSTHMACSignatureResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

