# zuora_client.PaymentMethodsApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_payment_methods**](PaymentMethodsApi.md#d_elete_payment_methods) | **DELETE** /v1/payment-methods/{payment-method-id} | Delete payment method
[**g_et_payment_methods_credit_card**](PaymentMethodsApi.md#g_et_payment_methods_credit_card) | **GET** /v1/payment-methods/credit-cards/accounts/{account-key} | Get credit card payment methods for account
[**g_et_stored_credential_profiles**](PaymentMethodsApi.md#g_et_stored_credential_profiles) | **GET** /v1/payment-methods/{payment-method-id}/profiles | Get stored credential profiles
[**object_delete_payment_method**](PaymentMethodsApi.md#object_delete_payment_method) | **DELETE** /v1/object/payment-method/{id} | CRUD: Delete payment method
[**object_get_payment_method**](PaymentMethodsApi.md#object_get_payment_method) | **GET** /v1/object/payment-method/{id} | CRUD: Get payment method
[**object_post_payment_method**](PaymentMethodsApi.md#object_post_payment_method) | **POST** /v1/object/payment-method | CRUD: Create payment method
[**object_put_payment_method**](PaymentMethodsApi.md#object_put_payment_method) | **PUT** /v1/object/payment-method/{id} | CRUD: Update payment method
[**p_ost_cancel_authorization**](PaymentMethodsApi.md#p_ost_cancel_authorization) | **POST** /v1/payment-methods/{payment-method-id}/voidAuthorize | Cancel authorization
[**p_ost_cancel_stored_credential_profile**](PaymentMethodsApi.md#p_ost_cancel_stored_credential_profile) | **POST** /v1/payment-methods/{payment-method-id}/profiles/{profile-number}/cancel | Cancel stored credential profile
[**p_ost_create_authorization**](PaymentMethodsApi.md#p_ost_create_authorization) | **POST** /v1/payment-methods/{payment-method-id}/authorize | Create authorization
[**p_ost_create_stored_credential_profile**](PaymentMethodsApi.md#p_ost_create_stored_credential_profile) | **POST** /v1/payment-methods/{payment-method-id}/profiles | Create stored credential profile
[**p_ost_expire_stored_credential_profile**](PaymentMethodsApi.md#p_ost_expire_stored_credential_profile) | **POST** /v1/payment-methods/{payment-method-id}/profiles/{profile-number}/expire | Expire stored credential profile
[**p_ost_payment_methods**](PaymentMethodsApi.md#p_ost_payment_methods) | **POST** /v1/payment-methods | Create payment method
[**p_ost_payment_methods_credit_card**](PaymentMethodsApi.md#p_ost_payment_methods_credit_card) | **POST** /v1/payment-methods/credit-cards | Create credit card payment method
[**p_ost_payment_methods_decryption**](PaymentMethodsApi.md#p_ost_payment_methods_decryption) | **POST** /v1/payment-methods/decryption | Create Apple Pay payment method
[**p_ut_payment_methods_credit_card**](PaymentMethodsApi.md#p_ut_payment_methods_credit_card) | **PUT** /v1/payment-methods/credit-cards/{payment-method-id} | Update credit card payment method
[**p_ut_scrub_payment_methods**](PaymentMethodsApi.md#p_ut_scrub_payment_methods) | **PUT** /v1/payment-methods/{payment-method-id}/scrub | Scrub payment method
[**p_ut_verify_payment_methods**](PaymentMethodsApi.md#p_ut_verify_payment_methods) | **PUT** /v1/payment-methods/{payment-method-id}/verify | Verify payment method

# **d_elete_payment_methods**
> CommonResponseType d_elete_payment_methods(payment_method_id, zuora_entity_ids=zuora_entity_ids)

Delete payment method

Deletes a credit card payment method from the specified customer account.  If the specified payment method is the account's default payment method, the request will fail.  In that case, you must first designate a different payment method for that customer to be the default. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
payment_method_id = 'payment_method_id_example' # str | Unique identifier of a payment method. (Since this ID is unique, and linked to a customer account in the system, no customer identifier is needed.)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete payment method
    api_response = api_instance.d_elete_payment_methods(payment_method_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->d_elete_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| Unique identifier of a payment method. (Since this ID is unique, and linked to a customer account in the system, no customer identifier is needed.) | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_methods_credit_card**
> GETPaymentMethodsType g_et_payment_methods_credit_card(account_key, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get credit card payment methods for account

This REST API reference describes how to retrieve all credit card information for the specified customer account.   ## Notes The response includes details credit or debit cards for the specified customer account. Card numbers are masked, e.g., \"************1234\". Cards are returned in reverse chronological order of last update.  You can send requests for bank transfer payment methods types. The response will not include bank transfer details.  The response only includes payment details on payment methods that are credit or debit cards. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
account_key = 'account_key_example' # str | Account number or account ID.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get credit card payment methods for account
    api_response = api_instance.g_et_payment_methods_credit_card(account_key, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->g_et_payment_methods_credit_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_key** | **str**| Account number or account ID. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GETPaymentMethodsType**](GETPaymentMethodsType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_stored_credential_profiles**
> GetStoredCredentialProfilesResponse g_et_stored_credential_profiles(payment_method_id, zuora_entity_ids=zuora_entity_ids, include_all=include_all)

Get stored credential profiles

Retrieves the stored credential profiles within a payment method.  **Note:** This feature is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
payment_method_id = 'payment_method_id_example' # str | ID of a payment method. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
include_all = true # bool | Specifies whether to retrieve all the stored credential profiles within the payment method.  By default, Zuora returns only the stored credential profiles with `Agreed` or `Active` status. If you set this parameter to `true`, Zuora returns all the stored credential profiles.  (optional)

try:
    # Get stored credential profiles
    api_response = api_instance.g_et_stored_credential_profiles(payment_method_id, zuora_entity_ids=zuora_entity_ids, include_all=include_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->g_et_stored_credential_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| ID of a payment method.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **include_all** | **bool**| Specifies whether to retrieve all the stored credential profiles within the payment method.  By default, Zuora returns only the stored credential profiles with &#x60;Agreed&#x60; or &#x60;Active&#x60; status. If you set this parameter to &#x60;true&#x60;, Zuora returns all the stored credential profiles.  | [optional] 

### Return type

[**GetStoredCredentialProfilesResponse**](GetStoredCredentialProfilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_delete_payment_method**
> ProxyDeleteResponse object_delete_payment_method(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Delete payment method

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Delete payment method
    api_response = api_instance.object_delete_payment_method(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->object_delete_payment_method: %s\n" % e)
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

# **object_get_payment_method**
> ProxyGetPaymentMethod object_get_payment_method(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, fields=fields)

CRUD: Get payment method

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
fields = 'fields_example' # str | Object fields to return (optional)

try:
    # CRUD: Get payment method
    api_response = api_instance.object_get_payment_method(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->object_get_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **fields** | **str**| Object fields to return | [optional] 

### Return type

[**ProxyGetPaymentMethod**](ProxyGetPaymentMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_post_payment_method**
> ProxyCreateOrModifyResponse object_post_payment_method(body, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Create payment method

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
body = zuora_client.Object() # Object | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Create payment method
    api_response = api_instance.object_post_payment_method(body, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->object_post_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
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

# **object_put_payment_method**
> ProxyCreateOrModifyResponse object_put_payment_method(body, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Update payment method

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
body = zuora_client.Object() # Object | 
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Update payment method
    api_response = api_instance.object_put_payment_method(body, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->object_put_payment_method: %s\n" % e)
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

# **p_ost_cancel_authorization**
> POSTVoidAuthorizeResponse p_ost_cancel_authorization(body, payment_method_id, zuora_entity_ids=zuora_entity_ids)

Cancel authorization

**Note:** If you wish to enable this feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Allows you to cancel an authorization. The payment gateways that support this operation include Verifi, CyberSource 1.28, CyberSource 1.97, Chase Paymentech Orbital, and Ingenico ePayments. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
body = zuora_client.POSTVoidAuthorize() # POSTVoidAuthorize | 
payment_method_id = 'payment_method_id_example' # str | The unique ID of the payment method where the authorization is cancelled. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Cancel authorization
    api_response = api_instance.p_ost_cancel_authorization(body, payment_method_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_cancel_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTVoidAuthorize**](POSTVoidAuthorize.md)|  | 
 **payment_method_id** | **str**| The unique ID of the payment method where the authorization is cancelled.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTVoidAuthorizeResponse**](POSTVoidAuthorizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_cancel_stored_credential_profile**
> ModifiedStoredCredentialProfileResponse p_ost_cancel_stored_credential_profile(payment_method_id, profile_number, zuora_entity_ids=zuora_entity_ids)

Cancel stored credential profile

Cancels a stored credential profile within a pyament method.  Cancelling the stored credential profile indicates that the stored credentials are no longer valid, per a customer request. You cannot reactivate the stored credential profile after you have cancelled it.  **Note:** This feature is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
payment_method_id = 'payment_method_id_example' # str | ID of a payment method. 
profile_number = 56 # int | Number that identifies a stored credential profile within the payment method. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Cancel stored credential profile
    api_response = api_instance.p_ost_cancel_stored_credential_profile(payment_method_id, profile_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_cancel_stored_credential_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| ID of a payment method.  | 
 **profile_number** | **int**| Number that identifies a stored credential profile within the payment method.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**ModifiedStoredCredentialProfileResponse**](ModifiedStoredCredentialProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_create_authorization**
> POSTAuthorizeResponse p_ost_create_authorization(body, payment_method_id, zuora_entity_ids=zuora_entity_ids)

Create authorization

**Note:** If you wish to enable this feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Enables you to authorize the availability of funds for a transaction but delay the capture of funds until a later time. Subsequently, use [CRUD: Create payment](https://www.zuora.com/developer/api-reference/#operation/Object_POSTPayment) to capture the authorized funds, or use [Cancel authorization](https://www.zuora.com/developer/api-reference/#operation/POST_CancelAuthorization) to cancel the authorization.   The payment gateways that support this operation include Verifi, CyberSource 1.28, CyberSource 1.97, Chase Paymentech Orbital, and Ingenico ePayments.  **Known limitation:** If you have the Invoice Settlement feature enabled, you cannot use the \"CRUD: Create payment\" operation to capture the funds. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
body = zuora_client.POSTDelayAuthorizeCapture() # POSTDelayAuthorizeCapture | 
payment_method_id = 'payment_method_id_example' # str | The unique ID of the payment method where the authorization is created. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create authorization
    api_response = api_instance.p_ost_create_authorization(body, payment_method_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_create_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTDelayAuthorizeCapture**](POSTDelayAuthorizeCapture.md)|  | 
 **payment_method_id** | **str**| The unique ID of the payment method where the authorization is created.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTAuthorizeResponse**](POSTAuthorizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_create_stored_credential_profile**
> ModifiedStoredCredentialProfileResponse p_ost_create_stored_credential_profile(body, payment_method_id, zuora_entity_ids=zuora_entity_ids)

Create stored credential profile

Creates a stored credential profile within a pyament method.  The stored credential profile represents a consent agreement that you have established with a customer. When you use the payment method in a transaction, Zuora may include information from the stored credential profile to inform the payment processor that the transaction is related to your pre-existing consent agreement with the customer.  **Note:** This feature is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
body = zuora_client.CreateStoredCredentialProfileRequest() # CreateStoredCredentialProfileRequest | 
payment_method_id = 'payment_method_id_example' # str | ID of a payment method. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create stored credential profile
    api_response = api_instance.p_ost_create_stored_credential_profile(body, payment_method_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_create_stored_credential_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateStoredCredentialProfileRequest**](CreateStoredCredentialProfileRequest.md)|  | 
 **payment_method_id** | **str**| ID of a payment method.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**ModifiedStoredCredentialProfileResponse**](ModifiedStoredCredentialProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_expire_stored_credential_profile**
> ModifiedStoredCredentialProfileResponse p_ost_expire_stored_credential_profile(payment_method_id, profile_number, zuora_entity_ids=zuora_entity_ids)

Expire stored credential profile

Expires a stored credential profile within a pyament method.  Expiring the stored credential profile indicates that the stored credentials are no longer valid, per an expiration policy in the stored credential transaction framework. You cannot reactivate the stored credential profile after you have expired it.  **Note:** This feature is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
payment_method_id = 'payment_method_id_example' # str | ID of a payment method. 
profile_number = 56 # int | Number that identifies a stored credential profile within the payment method. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Expire stored credential profile
    api_response = api_instance.p_ost_expire_stored_credential_profile(payment_method_id, profile_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_expire_stored_credential_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| ID of a payment method.  | 
 **profile_number** | **int**| Number that identifies a stored credential profile within the payment method.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**ModifiedStoredCredentialProfileResponse**](ModifiedStoredCredentialProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_payment_methods**
> POSTPaymentMethodResponse p_ost_payment_methods(body, zuora_entity_ids=zuora_entity_ids)

Create payment method

You can use this operation to create a payment method for a customer account. This operation supports the payment methods listed below.  ### PayPal Express Checkout The following request body fields are specific to this payment method: * `BAID` (required) * `email` (required)  ### PayPal Native Express Checkout The following request body fields are specific to this payment method: * `BAID` (required) * `email` (optional)  ### PayPal Adaptive The following request body fields are specific to this payment method: * `preapprovalKey` (required) * `email` (required)  ### Credit Card **Note:** This feature is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.  The following request body fields are specific to this payment method: * `cardHolderInfo` (`cardHolderName` required) * `cardNumber` (required) * `cardType` (required) * `expirationMonth` (required) * `expirationYear` (required) * `mitConsentAgreementRef` * `mitConsentAgreementSrc` * `mitNetworkTransactionId` * `mitProfileAction` * `mitProfileType` * `mitProfileAgreedOn` * `securityCode`   ### ACH The following request body fields are applicable to this payment method: * `bankABACode` (required) * `achBankAccountName` (required) * `achBankAccountNumber` (required) * `achBankAccountType` (required) * `achBankName` (required) * `addressLine1` * `addressLine2` * `phone` * `email` * `city` * `country` * `state` * `zipCode` 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
body = zuora_client.POSTPaymentMethodRequest() # POSTPaymentMethodRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create payment method
    api_response = api_instance.p_ost_payment_methods(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTPaymentMethodRequest**](POSTPaymentMethodRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTPaymentMethodResponse**](POSTPaymentMethodResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_payment_methods_credit_card**
> POSTPaymentMethodResponseType p_ost_payment_methods_credit_card(body, zuora_entity_ids=zuora_entity_ids)

Create credit card payment method

This REST API reference describes how to create a new credit card payment method for a customer account.  This API call is CORS Enabled. Use client-side JavaScript to invoke the call.   **Note**: If you use this operation to create credit card payment methods instead of using the [iFrame of Hosted Payment Pages](https://knowledgecenter.zuora.com/CB_Billing/LA_Hosted_Payment_Pages/C_Hosted_Payment_Pages/B_Implementing_Hosted_Payment_Pages_on_Your_Website/C_Embed_and_Submit_the_iFrame), you are subject to PCI-compliance audit requirements. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
body = zuora_client.Object() # Object | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create credit card payment method
    api_response = api_instance.p_ost_payment_methods_credit_card(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_payment_methods_credit_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTPaymentMethodResponseType**](POSTPaymentMethodResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_payment_methods_decryption**
> POSTPaymentMethodResponseDecryption p_ost_payment_methods_decryption(body, zuora_entity_ids=zuora_entity_ids)

Create Apple Pay payment method

The decryption API endpoint can conditionally perform 3 tasks in one atomic call:   * Decrypt Apple Pay Payment token   * Create Credit Card Payment Method in Zuora with decrypted Apple Pay information   * Process Payment on a specified Invoice (optional) 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
body = zuora_client.POSTPaymentMethodDecryption() # POSTPaymentMethodDecryption | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create Apple Pay payment method
    api_response = api_instance.p_ost_payment_methods_decryption(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ost_payment_methods_decryption: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTPaymentMethodDecryption**](POSTPaymentMethodDecryption.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTPaymentMethodResponseDecryption**](POSTPaymentMethodResponseDecryption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_payment_methods_credit_card**
> PUTPaymentMethodResponseType p_ut_payment_methods_credit_card(body, payment_method_id, zuora_entity_ids=zuora_entity_ids)

Update credit card payment method

Updates an existing credit card payment method for the specified customer account. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
body = zuora_client.Object() # Object | 
payment_method_id = 'payment_method_id_example' # str | Unique ID of the payment method to update.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update credit card payment method
    api_response = api_instance.p_ut_payment_methods_credit_card(body, payment_method_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ut_payment_methods_credit_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **payment_method_id** | **str**| Unique ID of the payment method to update. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**PUTPaymentMethodResponseType**](PUTPaymentMethodResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_scrub_payment_methods**
> CommonResponseType p_ut_scrub_payment_methods(payment_method_id, zuora_entity_ids=zuora_entity_ids)

Scrub payment method

 This operation enables you to replace all sensitive data in a payment method, related payment method snapshot table, and four related log tables with dummy values that will be stored in Zuora databases.   This operation will scrub the sensitive data and soft-delete the specified payment method at the same time.   **Note:** In order to use this operation, you must ensure that the **Scrub Sensitive Data of Specific Payment Method payments** permission is enabled in your user role. Contact your tenant administrator if you want to enable this permission. See [Scrub Payment Methods](https://knowledgecenter.zuora.com/CB_Billing/L_Payment_Methods/Scrub_Payment_Methods) for more information. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
payment_method_id = 'payment_method_id_example' # str | The ID of the payment method where you want to scrub the sensitive data. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Scrub payment method
    api_response = api_instance.p_ut_scrub_payment_methods(payment_method_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ut_scrub_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**| The ID of the payment method where you want to scrub the sensitive data.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_verify_payment_methods**
> PUTVerifyPaymentMethodResponseType p_ut_verify_payment_methods(body, payment_method_id)

Verify payment method

Sends an authorization request to the corresponding payment gateway to verify the payment method, even though no changes are made for the payment method. Supported payment methods are Credit Cards and Paypal.  Zuora now supports performing a standalone zero dollar verification or one dollar authorization for credit cards. It also supports a billing agreement status check on PayPal payment methods.  If a payment method is created by Hosted Payment Pages and is not assigned to any billing account, the payment method cannot be verified through this operation. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentMethodsApi()
body = zuora_client.PUTVerifyPaymentMethodType() # PUTVerifyPaymentMethodType | 
payment_method_id = 'payment_method_id_example' # str | The ID of the payment method to be verified. 

try:
    # Verify payment method
    api_response = api_instance.p_ut_verify_payment_methods(body, payment_method_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentMethodsApi->p_ut_verify_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTVerifyPaymentMethodType**](PUTVerifyPaymentMethodType.md)|  | 
 **payment_method_id** | **str**| The ID of the payment method to be verified.  | 

### Return type

[**PUTVerifyPaymentMethodResponseType**](PUTVerifyPaymentMethodResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

