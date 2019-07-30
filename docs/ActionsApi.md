# zuora_client.ActionsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_pos_tamend**](ActionsApi.md#action_pos_tamend) | **POST** /v1/action/amend | Amend
[**action_pos_tcreate**](ActionsApi.md#action_pos_tcreate) | **POST** /v1/action/create | Create
[**action_pos_tdelete**](ActionsApi.md#action_pos_tdelete) | **POST** /v1/action/delete | Delete
[**action_pos_texecute**](ActionsApi.md#action_pos_texecute) | **POST** /v1/action/execute | Execute
[**action_pos_tgenerate**](ActionsApi.md#action_pos_tgenerate) | **POST** /v1/action/generate | Generate
[**action_pos_tquery**](ActionsApi.md#action_pos_tquery) | **POST** /v1/action/query | Query
[**action_pos_tquery_more**](ActionsApi.md#action_pos_tquery_more) | **POST** /v1/action/queryMore | QueryMore
[**action_pos_tsubscribe**](ActionsApi.md#action_pos_tsubscribe) | **POST** /v1/action/subscribe | Subscribe
[**action_pos_tupdate**](ActionsApi.md#action_pos_tupdate) | **POST** /v1/action/update | Update


# **action_pos_tamend**
> ProxyActionamendResponse action_pos_tamend(amend_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)

Amend

Modifies a subscription by creating Amendment objects.  The availability of this operation depends on whether you have the Orders feature enabled:  * If you have the Orders feature enabled, this operation is not available. See [Orders Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information.  * If you do not have the Orders feature enabled, this operation is available. However, Zuora recommends that you use [Update subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription) instead of this operation.  You can use this operation to create up to 10 Amendment objects. You must specify the following fields for each Amendment object:  * `ContractEffectiveDate` * `Name` * `SubscriptionId` * `Type`  Additionally, the value of `SubscriptionId` must be the same for each Amendment object. You cannot use this operation to update multiple subscriptions.  **Note:** When you call this operation, Zuora modifies the subscription in the order that you specify Amendment objects in the request body.  If Zuora is unable to create an Amendment object when you call this operation, the entire call fails. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.ActionsApi()
amend_request = zuora_client.ProxyActionamendRequest() # ProxyActionamendRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
x_zuora_wsdl_version = '79' # str | Zuora WSDL version number.  (optional) (default to 79)

try:
    # Amend
    api_response = api_instance.action_pos_tamend(amend_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->action_pos_tamend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amend_request** | [**ProxyActionamendRequest**](ProxyActionamendRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **x_zuora_wsdl_version** | **str**| Zuora WSDL version number.  | [optional] [default to 79]

### Return type

[**ProxyActionamendResponse**](ProxyActionamendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_pos_tcreate**
> list[SaveResult] action_pos_tcreate(create_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)

Create

Use the create call to create one or more objects of a specific type. You can specify different types in different create calls, but each create call must apply to only one type of object.  ## Limitations   This call has the following limitations:  * A maximum of 50 objects are supported in a single call. * The Invoice Settlement feature is not supported. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. The Orders feature is also not supported. * The default WSDL version for Actions is 79. To create objects according to a different WSDL version, set the `X-Zuora-WSDL-Version` header. To find out in which WSDL version a particular object or field was introduced, see [Zuora SOAP API Version History](https://knowledgecenter.zuora.com/DC_Developers/G_SOAP_API/Zuora_SOAP_API_Version_History).   ## How to Use this Call  You can call create on an array of one or more zObjects. It returns an array of SaveResults, indicating the success or failure of creating each object. The following information applies to this call:  * You cannot pass in null zObjects. * You can pass in a maximum of 50 zObjects at a time. * All objects must be of the same type.  ### Using Create and Subscribe Calls  Both the create and subscribe calls will create a new account. However, there are differences between the calls.  Use the create call to create an account independent of a subscription.  Use the subscribe call to create the account with the subscription and the initial payment information. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.ActionsApi()
create_request = zuora_client.ProxyActioncreateRequest() # ProxyActioncreateRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
x_zuora_wsdl_version = '79' # str | Zuora WSDL version number.  (optional) (default to 79)

try:
    # Create
    api_response = api_instance.action_pos_tcreate(create_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->action_pos_tcreate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request** | [**ProxyActioncreateRequest**](ProxyActioncreateRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **x_zuora_wsdl_version** | **str**| Zuora WSDL version number.  | [optional] [default to 79]

### Return type

[**list[SaveResult]**](SaveResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_pos_tdelete**
> list[DeleteResult] action_pos_tdelete(delete_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)

Delete

Deletes one or more objects of the same type. You can specify different types in different delete calls, but each delete call must apply only to one type of object.  The following information applies to this call:  * You will need to first determine the IDs for the objects you wish to delete. * You cannot pass in any null IDs. * All objects in a specific delete call must be of the same type.   ### Objects per Call 50 objects are supported in a single call. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.ActionsApi()
delete_request = zuora_client.ProxyActiondeleteRequest() # ProxyActiondeleteRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
x_zuora_wsdl_version = '79' # str | Zuora WSDL version number.  (optional) (default to 79)

try:
    # Delete
    api_response = api_instance.action_pos_tdelete(delete_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->action_pos_tdelete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_request** | [**ProxyActiondeleteRequest**](ProxyActiondeleteRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **x_zuora_wsdl_version** | **str**| Zuora WSDL version number.  | [optional] [default to 79]

### Return type

[**list[DeleteResult]**](DeleteResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_pos_texecute**
> list[ExecuteResult] action_pos_texecute(execute_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)

Execute

Use the execute call to execute a process to split an invoice into multiple invoices. The original invoice must be in draft status. The resulting invoices are called split invoices.  **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com).   To split a draft invoice into multiple split invoices:  1. Use the create call to create a separate InvoiceSplitItem object for each split invoice that you want to create from the original draft invoice. 2. Use the create call to create a single InvoiceSplit object to collect all of the InvoiceSplitItem objects. 3. Use the execute call to split the draft invoice into multiple split invoices.  You need to create InvoiceSplitItem objects and an InvoiceSplit object before you can use the execute call.   * Supported objects: InvoiceSplit * Asynchronous process: yes 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.ActionsApi()
execute_request = zuora_client.ProxyActionexecuteRequest() # ProxyActionexecuteRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
x_zuora_wsdl_version = '79' # str | Zuora WSDL version number.  (optional) (default to 79)

try:
    # Execute
    api_response = api_instance.action_pos_texecute(execute_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->action_pos_texecute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execute_request** | [**ProxyActionexecuteRequest**](ProxyActionexecuteRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **x_zuora_wsdl_version** | **str**| Zuora WSDL version number.  | [optional] [default to 79]

### Return type

[**list[ExecuteResult]**](ExecuteResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_pos_tgenerate**
> list[SaveResult] action_pos_tgenerate(generate_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)

Generate

Generates an on-demand invoice for a specific customer. This is similar to creating an ad-hoc bill run for a specific customer account in the Zuora UI.  * Supported objects: Invoice * Asynchronous process: yes  The ID of the generated invoice is returned in the response. If multiple invoices are generated, only the id of the first invoice generated is returned. This occurs when an account has multiple subscriptions with the [invoice subscription separately](https://knowledgecenter.zuora.com/BC_Subscription_Management/Subscriptions/B_Creating_Subscriptions/Invoicing_Subscriptions_Separately) option enabled. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.ActionsApi()
generate_request = zuora_client.ProxyActiongenerateRequest() # ProxyActiongenerateRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
x_zuora_wsdl_version = '79' # str | Zuora WSDL version number.  (optional) (default to 79)

try:
    # Generate
    api_response = api_instance.action_pos_tgenerate(generate_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->action_pos_tgenerate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_request** | [**ProxyActiongenerateRequest**](ProxyActiongenerateRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **x_zuora_wsdl_version** | **str**| Zuora WSDL version number.  | [optional] [default to 79]

### Return type

[**list[SaveResult]**](SaveResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_pos_tquery**
> ProxyActionqueryResponse action_pos_tquery(query_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)

Query

The query call sends a query expression by specifying the object to query, the fields to retrieve from that object, and any filters to determine whether a given object should be queried.   You can use [Zuora Object Query Language](https://knowledgecenter.zuora.com/DC_Developers/K_Zuora_Object_Query_Language) (ZOQL) to construct those queries, passing them through the `queryString`.   Once the call is made, the API executes the query against the specified object and returns a query response object to your application. Your application can then iterate through rows in the query response to retrieve information.  ## Limitations   This call has the following limitations:  * All ZOQL keywords must be in lower case. * The number of records returned is limited to 2000 records * The Invoice Settlement feature is not supported. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. The Orders feature is also not supported. * The default WSDL version for Actions is 79. To query objects or fields according to a different WSDL version, set the `X-Zuora-WSDL-Version` header. To find out in which WSDL version a particular object or field was introduced, see [Zuora SOAP API Version History](https://knowledgecenter.zuora.com/DC_Developers/G_SOAP_API/Zuora_SOAP_API_Version_History). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.ActionsApi()
query_request = zuora_client.ProxyActionqueryRequest() # ProxyActionqueryRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
x_zuora_wsdl_version = '79' # str | Zuora WSDL version number.  (optional) (default to 79)

try:
    # Query
    api_response = api_instance.action_pos_tquery(query_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->action_pos_tquery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**ProxyActionqueryRequest**](ProxyActionqueryRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **x_zuora_wsdl_version** | **str**| Zuora WSDL version number.  | [optional] [default to 79]

### Return type

[**ProxyActionqueryResponse**](ProxyActionqueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_pos_tquery_more**
> ProxyActionqueryMoreResponse action_pos_tquery_more(query_more_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)

QueryMore

Use queryMore to request additional results from a previous query call. If your initial query call returns more than 2000 results, you can use queryMore to query for the additional results.   Any `queryLocator` results greater than 2,000, will only be stored by Zuora for 5 days before it is deleted.    This call sends a request for additional results from an initial query call. If the initial query call returns more than 2000 results, you can use the `queryLocator` returned from query to request the next set of results.   **Note:** Zuora expires queryMore cursors after 15 minutes of activity.   To use queryMore, you first construct a query call. By default, the query call will return up to 2000 results. If there are more than 2000 results, query will return a boolean `done`, which will be marked as `false`, and a `queryLocator`, which is a marker you will pass to queryMore to get the next set of results. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.ActionsApi()
query_more_request = zuora_client.ProxyActionqueryMoreRequest() # ProxyActionqueryMoreRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
x_zuora_wsdl_version = '79' # str | Zuora WSDL version number.  (optional) (default to 79)

try:
    # QueryMore
    api_response = api_instance.action_pos_tquery_more(query_more_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->action_pos_tquery_more: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_more_request** | [**ProxyActionqueryMoreRequest**](ProxyActionqueryMoreRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **x_zuora_wsdl_version** | **str**| Zuora WSDL version number.  | [optional] [default to 79]

### Return type

[**ProxyActionqueryMoreResponse**](ProxyActionqueryMoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_pos_tsubscribe**
> list[SubscribeResult] action_pos_tsubscribe(subscribe_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)

Subscribe

 This call performs many actions.  Use the subscribe call to bundle information required to create at least one new subscription.  **Note:** This feature is unavailable if you have the Orders feature enabled. See [Orders Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information.  The call takes in an array of SubscribeRequests. Because it takes an array, you can submit a batch of subscription requests at once. You can create up to 50 different subscriptions in a single subscribe call.  This is a combined call that you can use to perform all of the following tasks in a single call:  * Create accounts * Create contacts * Create payment methods, including external payment options * Create an invoice for the subscription * Apply the first payment to a subscription  ## Object Limits  50 objects are supported in a single call.    ## Effective Date If the effective date is in the future, the invoices will not be generated, and there will be no invoice number.  ## Subscription Name, Number, and ID  ### Subscription Name and Number  The subscription name is a unique identifier for the subscription. If you do not specify a value for the name, Zuora will create one automatically. The automatically generated value is known as the subscription number, such as `A-S00000080`. You cannot change the subscription name or number after creating the subscription.   * **Subscription name**: The name that you set for the subscription. * **Subscription number**: The value generated by Zuora automatically if you do not specify a subscription name.   Both the subscription name and number must be unique. If they are not, an error will occur.  ### Subscription ID  The subscription ID is a 32-digit ID in the format 4028xxxx. This is also the unique identifier for a subscription. This value is automatically generated by the system and cannot be edited or updated, but it can be queried. One subscription can have only one subscription name or number, but it can have multiple IDs: Each version of a subscription has a different ID.  The Subscription object contains the fields `OriginalId` and `PreviousSubscriptionId`. `OriginalId` is the ID for the first version of a subscription. `PreviousSubscriptionId` is the ID of the version created immediately prior to the current version.  ## Subscription Preview  You can preview invoices that would be generated by the subscribe call.   ## Invoice Subscriptions Separately If you have enabled the invoice subscriptions separately feature, a subscribe call will generate an invoice for each subscription for every subscription where the field `IsInvoiceSeparate` is set to `true`.  If the invoice subscriptions separately feature is disabled, a subscribe call will generate a single invoice for all subscriptions.  See [Invoicing Subscriptions Separately](https://knowledgecenter.zuora.com/BC_Subscription_Management/Subscriptions/B_Creating_Subscriptions/Invoicing_Subscriptions_Separately) for more information.  ## Subscriptions and Draft Invoices  If a draft invoice that includes charges exists in a customer account, using the subscribe call to create a new subscription and generate an invoice will cause the new subscription to be added to the existing draft invoice. Zuora will then post the invoice.   ## When to Use Subscribe and Create Calls  You can use either the subscribe call or the create call to create the objects associated with a subscription (accounts, contacts, and so on). There are differences between these calls, however, and some situations are better for one or the other.  ### Use the Subscribe Call  The subscribe call bundles up all the information you need for a subscription. Use the subscribe call to create new subscriptions when you have all the information you need.  Subscribe calls cannot update BillTo, SoldTo, and Account objects. Payment information objects cannot be updated if there is an existing account ID in the call. These objects are not supported in a subscribe call.  ### Use the Create Call  The create call is more useful when you want to develop in stages. For example, if you want to first create an account, then a contact, and so on. If you do not have all information available, use the create call. To create a subscription, you must activate the account from Draft status to Active by calling the subscribe call. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.ActionsApi()
subscribe_request = zuora_client.ProxyActionsubscribeRequest() # ProxyActionsubscribeRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
x_zuora_wsdl_version = '79' # str | Zuora WSDL version number.  (optional) (default to 79)

try:
    # Subscribe
    api_response = api_instance.action_pos_tsubscribe(subscribe_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->action_pos_tsubscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscribe_request** | [**ProxyActionsubscribeRequest**](ProxyActionsubscribeRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **x_zuora_wsdl_version** | **str**| Zuora WSDL version number.  | [optional] [default to 79]

### Return type

[**list[SubscribeResult]**](SubscribeResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_pos_tupdate**
> list[SaveResult] action_pos_tupdate(update_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)

Update

 Updates the information in one or more objects of the same type. You can specify different types of objects in different update calls, but each specific update call must apply to only one type of object.  You can update an array of one or more zObjects. It returns an array of SaveResults, indicating the success or failure of updating each object. The following information applies to this call:  * You cannot pass in null zObjects. * You can pass in a maximum of 50 zObjects at a time. * All objects must be of the same type. * For each field in each object, you must determine that object's ID. Then populate the fields that you want update with the new information. * Zuora ignores unrecognized fields in update calls. For example, if an optional field is spelled incorrectly or a field that does not exist is specified, Zuora ignores the field and continues to process the call. No error message is returned for unrecognized fields.  ## Limitations   This call has the following limitations:  * A maximum of 50 objects are supported in a single call. * The Invoice Settlement feature is not supported. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. The Orders feature is also not supported. * The default WSDL version for Actions is 79. To update objects or fields according to a different WSDL version, set the `X-Zuora-WSDL-Version` header. To find out in which WSDL version a particular object or field was introduced, see [Zuora SOAP API Version History](https://knowledgecenter.zuora.com/DC_Developers/G_SOAP_API/Zuora_SOAP_API_Version_History). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.ActionsApi()
update_request = zuora_client.ProxyActionupdateRequest() # ProxyActionupdateRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
x_zuora_wsdl_version = '79' # str | Zuora WSDL version number.  (optional) (default to 79)

try:
    # Update
    api_response = api_instance.action_pos_tupdate(update_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, x_zuora_wsdl_version=x_zuora_wsdl_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->action_pos_tupdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_request** | [**ProxyActionupdateRequest**](ProxyActionupdateRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **x_zuora_wsdl_version** | **str**| Zuora WSDL version number.  | [optional] [default to 79]

### Return type

[**list[SaveResult]**](SaveResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

