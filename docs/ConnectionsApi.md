# swagger_client.ConnectionsApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_ost_connections**](ConnectionsApi.md#p_ost_connections) | **POST** /v1/connections | Establish connection to Zuora REST API service

# **p_ost_connections**
> CommonResponseType p_ost_connections(api_access_key_id, api_secret_access_key, content_type, zuora_entity_ids=zuora_entity_ids)

Establish connection to Zuora REST API service

Establishes a connection to the Zuora REST API service based on a valid user credentials.   **Note:**This is a legacy REST API. Zuora recommends you to use [OAuth](https://www.zuora.com/developer/api-reference/#section/Authentication/OAuth-v2.0) for authentication instead.   This call authenticates the user and returns an API session cookie that's used to authorize subsequent calls to the REST API. The credentials must belong to a user account that has permission to access the API service.  As noted elsewhere, it's strongly recommended that an account used for Zuora API activity is never used to log into the Zuora UI.  Once an account is used to log into the UI, it may be subject to periodic forced password changes, which may eventually lead to authentication failures when using the API. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionsApi()
api_access_key_id = 'api_access_key_id_example' # str | Account username 
api_secret_access_key = 'api_secret_access_key_example' # str | Account password 
content_type = 'content_type_example' # str | Must be set to \"application/json\" 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Establish connection to Zuora REST API service
    api_response = api_instance.p_ost_connections(api_access_key_id, api_secret_access_key, content_type, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionsApi->p_ost_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_access_key_id** | **str**| Account username  | 
 **api_secret_access_key** | **str**| Account password  | 
 **content_type** | **str**| Must be set to \&quot;application/json\&quot;  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

