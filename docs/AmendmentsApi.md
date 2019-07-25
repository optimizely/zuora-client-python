# swagger_client.AmendmentsApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_amendments_by_key**](AmendmentsApi.md#g_et_amendments_by_key) | **GET** /v1/amendments/{amendment-key} | Get amendments by key
[**g_et_amendments_by_subscription_id**](AmendmentsApi.md#g_et_amendments_by_subscription_id) | **GET** /v1/amendments/subscriptions/{subscription-id} | Get amendments by subscription ID
[**object_delete_amendment**](AmendmentsApi.md#object_delete_amendment) | **DELETE** /v1/object/amendment/{id} | CRUD: Delete amendment
[**object_get_amendment**](AmendmentsApi.md#object_get_amendment) | **GET** /v1/object/amendment/{id} | CRUD: Get amendment
[**object_put_amendment**](AmendmentsApi.md#object_put_amendment) | **PUT** /v1/object/amendment/{id} | CRUD: Update amendment

# **g_et_amendments_by_key**
> GETAmendmentType g_et_amendments_by_key(amendment_key, zuora_entity_ids=zuora_entity_ids)

Get amendments by key

Retrieves detailed information about the specified subscription amendment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmendmentsApi()
amendment_key = 'amendment_key_example' # str | Can be the amendment ID or the amendment code.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get amendments by key
    api_response = api_instance.g_et_amendments_by_key(amendment_key, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmendmentsApi->g_et_amendments_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amendment_key** | **str**| Can be the amendment ID or the amendment code. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETAmendmentType**](GETAmendmentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_amendments_by_subscription_id**
> GETAmendmentType g_et_amendments_by_subscription_id(subscription_id, zuora_entity_ids=zuora_entity_ids)

Get amendments by subscription ID

Retrieves detailed information about the amendment with the specified subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmendmentsApi()
subscription_id = 'subscription_id_example' # str | The ID of the subscription whose amendment changes you want to retrieve.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get amendments by subscription ID
    api_response = api_instance.g_et_amendments_by_subscription_id(subscription_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmendmentsApi->g_et_amendments_by_subscription_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The ID of the subscription whose amendment changes you want to retrieve. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETAmendmentType**](GETAmendmentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_delete_amendment**
> ProxyDeleteResponse object_delete_amendment(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Delete amendment

**Note:** This feature is unavailable if you have the Orders feature enabled. See [Orders Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information.  Invoiced amendments cannot usually be deleted. One exception to this rule is auto-renew amendments. You can delete the last auto-renew amendment even if an invoice has been generated. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmendmentsApi()
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Delete amendment
    api_response = api_instance.object_delete_amendment(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmendmentsApi->object_delete_amendment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 

### Return type

[**ProxyDeleteResponse**](ProxyDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_get_amendment**
> ProxyGetAmendment object_get_amendment(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, fields=fields)

CRUD: Get amendment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmendmentsApi()
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
fields = 'fields_example' # str | Object fields to return (optional)

try:
    # CRUD: Get amendment
    api_response = api_instance.object_get_amendment(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmendmentsApi->object_get_amendment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **fields** | **str**| Object fields to return | [optional] 

### Return type

[**ProxyGetAmendment**](ProxyGetAmendment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_put_amendment**
> ProxyCreateOrModifyResponse object_put_amendment(body, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Update amendment

**Note:** This feature is unavailable if you have the Orders feature enabled. See [Orders Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmendmentsApi()
body = swagger_client.Object() # Object | 
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Update amendment
    api_response = api_instance.object_put_amendment(body, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmendmentsApi->object_put_amendment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **id** | **str**| Object id | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 

### Return type

[**ProxyCreateOrModifyResponse**](ProxyCreateOrModifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

