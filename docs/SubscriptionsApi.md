# swagger_client.SubscriptionsApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_subscriptions_by_account**](SubscriptionsApi.md#g_et_subscriptions_by_account) | **GET** /v1/subscriptions/accounts/{account-key} | Get subscriptions by account
[**g_et_subscriptions_by_key**](SubscriptionsApi.md#g_et_subscriptions_by_key) | **GET** /v1/subscriptions/{subscription-key} | Get subscriptions by key
[**g_et_subscriptions_by_key_and_version**](SubscriptionsApi.md#g_et_subscriptions_by_key_and_version) | **GET** /v1/subscriptions/{subscription-key}/versions/{version} | Get subscriptions by key and version
[**object_delete_subscription**](SubscriptionsApi.md#object_delete_subscription) | **DELETE** /v1/object/subscription/{id} | CRUD: Delete Subscription
[**object_get_subscription**](SubscriptionsApi.md#object_get_subscription) | **GET** /v1/object/subscription/{id} | CRUD: Retrieve Subscription
[**object_put_subscription**](SubscriptionsApi.md#object_put_subscription) | **PUT** /v1/object/subscription/{id} | CRUD: Update Subscription
[**p_ost_preview_subscription**](SubscriptionsApi.md#p_ost_preview_subscription) | **POST** /v1/subscriptions/preview | Preview subscription
[**p_ost_subscription**](SubscriptionsApi.md#p_ost_subscription) | **POST** /v1/subscriptions | Create subscription
[**p_ut_cancel_subscription**](SubscriptionsApi.md#p_ut_cancel_subscription) | **PUT** /v1/subscriptions/{subscription-key}/cancel | Cancel subscription
[**p_ut_renew_subscription**](SubscriptionsApi.md#p_ut_renew_subscription) | **PUT** /v1/subscriptions/{subscription-key}/renew | Renew subscription
[**p_ut_resume_subscription**](SubscriptionsApi.md#p_ut_resume_subscription) | **PUT** /v1/subscriptions/{subscription-key}/resume | Resume subscription
[**p_ut_subscription**](SubscriptionsApi.md#p_ut_subscription) | **PUT** /v1/subscriptions/{subscription-key} | Update subscription
[**p_ut_suspend_subscription**](SubscriptionsApi.md#p_ut_suspend_subscription) | **PUT** /v1/subscriptions/{subscription-key}/suspend | Suspend subscription

# **g_et_subscriptions_by_account**
> GETSubscriptionWrapper g_et_subscriptions_by_account(account_key, zuora_entity_ids=zuora_entity_ids, page_size=page_size, charge_detail=charge_detail)

Get subscriptions by account

Retrieves all subscriptions associated with the specified account. Zuora only returns the latest version of the subscriptions.  Subscription data is returned in reverse chronological order based on `updatedDate`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
account_key = 'account_key_example' # str |  Possible values are: * an account number * an account ID 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
charge_detail = 'charge_detail_example' # str | The segmented rate plan charges.  When an amendment results in a change to a charge, Zuora creates a segmented rate plan charge. Use this field to track segment charges.  Possible values are:  * __last-segment__: (Default) The last rate plan charge on the subscription. The last rate plan charge is the last one in the order of time on the subscription rather than the most recent changed charge on the subscription.  * __current-segment__: The segmented charge that is active on today’s date (effectiveStartDate <= today’s date < effectiveEndDate).    * __all-segments__: All the segmented charges. The `chargeSegments` field is returned in the response. The `chargeSegments` field contains an array of the charge information for all the charge segments.   * __specific-segment&as-of-date=date__: The segmented charge that is active on a date you specified (effectiveStartDate <= specific date < effectiveEndDate). The format of the date is yyyy-mm-dd.  (optional)

try:
    # Get subscriptions by account
    api_response = api_instance.g_et_subscriptions_by_account(account_key, zuora_entity_ids=zuora_entity_ids, page_size=page_size, charge_detail=charge_detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->g_et_subscriptions_by_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_key** | **str**|  Possible values are: * an account number * an account ID  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **charge_detail** | **str**| The segmented rate plan charges.  When an amendment results in a change to a charge, Zuora creates a segmented rate plan charge. Use this field to track segment charges.  Possible values are:  * __last-segment__: (Default) The last rate plan charge on the subscription. The last rate plan charge is the last one in the order of time on the subscription rather than the most recent changed charge on the subscription.  * __current-segment__: The segmented charge that is active on today’s date (effectiveStartDate &lt;&#x3D; today’s date &lt; effectiveEndDate).    * __all-segments__: All the segmented charges. The &#x60;chargeSegments&#x60; field is returned in the response. The &#x60;chargeSegments&#x60; field contains an array of the charge information for all the charge segments.   * __specific-segment&amp;as-of-date&#x3D;date__: The segmented charge that is active on a date you specified (effectiveStartDate &lt;&#x3D; specific date &lt; effectiveEndDate). The format of the date is yyyy-mm-dd.  | [optional] 

### Return type

[**GETSubscriptionWrapper**](GETSubscriptionWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_subscriptions_by_key**
> GETSubscriptionTypeWithSuccess g_et_subscriptions_by_key(subscription_key, zuora_entity_ids=zuora_entity_ids, charge_detail=charge_detail)

Get subscriptions by key

This REST API reference describes how to retrieve detailed information about a specified subscription in the latest version. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_key = 'subscription_key_example' # str | Possible values are:   * a subscription number   * a subscription ID 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
charge_detail = 'charge_detail_example' # str |  The segmented rate plan charges. When an amendment results in a change to a charge, Zuora creates a segmented rate plan charge. Use this field to track segment charges.  Possible values are:   * __last-segment__: (Default) The last rate plan charge on the subscription. The last rate plan charge is the last one in the order of time on the subscription rather than the most recent changed charge on the subscription.  * __current-segment__: The segmented charge that is active on today’s date (effectiveStartDate <= today’s date < effectiveEndDate).    * __all-segments__: All the segmented charges. The `chargeSegments` field is returned in the response. The `chargeSegments` field contains an array of the charge information for all the charge segments.   * __specific-segment&as-of-date=date__: The segmented charge that is active on a date you specified ((specific date = effectiveStartDate) OR (effectiveStartDate < specific date < effectiveEndDate)). The format of the date is yyyy-mm-dd.  (optional)

try:
    # Get subscriptions by key
    api_response = api_instance.g_et_subscriptions_by_key(subscription_key, zuora_entity_ids=zuora_entity_ids, charge_detail=charge_detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->g_et_subscriptions_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_key** | **str**| Possible values are:   * a subscription number   * a subscription ID  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **charge_detail** | **str**|  The segmented rate plan charges. When an amendment results in a change to a charge, Zuora creates a segmented rate plan charge. Use this field to track segment charges.  Possible values are:   * __last-segment__: (Default) The last rate plan charge on the subscription. The last rate plan charge is the last one in the order of time on the subscription rather than the most recent changed charge on the subscription.  * __current-segment__: The segmented charge that is active on today’s date (effectiveStartDate &lt;&#x3D; today’s date &lt; effectiveEndDate).    * __all-segments__: All the segmented charges. The &#x60;chargeSegments&#x60; field is returned in the response. The &#x60;chargeSegments&#x60; field contains an array of the charge information for all the charge segments.   * __specific-segment&amp;as-of-date&#x3D;date__: The segmented charge that is active on a date you specified ((specific date &#x3D; effectiveStartDate) OR (effectiveStartDate &lt; specific date &lt; effectiveEndDate)). The format of the date is yyyy-mm-dd.  | [optional] 

### Return type

[**GETSubscriptionTypeWithSuccess**](GETSubscriptionTypeWithSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_subscriptions_by_key_and_version**
> GETSubscriptionTypeWithSuccess g_et_subscriptions_by_key_and_version(subscription_key, version, zuora_entity_ids=zuora_entity_ids, charge_detail=charge_detail)

Get subscriptions by key and version

This REST API reference describes how to retrieve detailed information about a specified subscription in a specified version. When you create a subscription amendment, you create a new version of the subscription. You can use this method to retrieve information about a subscription in any version. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription_key = 'subscription_key_example' # str | Subscription number. For example, A-S00000135. 
version = 'version_example' # str | Subscription version. For example, 1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
charge_detail = 'charge_detail_example' # str |  The segmented rate plan charges. When an amendment results in a change to a charge, Zuora creates a segmented rate plan charge. Use this field to track segment charges.  Possible values are:   * __last-segment__: (Default) The last rate plan charge on the subscription. The last rate plan charge is the last one in the order of time on the subscription rather than the most recent changed charge on the subscription.  * __current-segment__: The segmented charge that is active on today’s date (effectiveStartDate <= today’s date < effectiveEndDate).    * __all-segments__: All the segmented charges. The `chargeSegments` field is returned in the response. The `chargeSegments` field contains an array of the charge information for all the charge segments.   * __specific-segment&as-of-date=date__: The segmented charge that is active on a date you specified (effectiveStartDate <= specific date < effectiveEndDate). The format of the date is yyyy-mm-dd.  (optional)

try:
    # Get subscriptions by key and version
    api_response = api_instance.g_et_subscriptions_by_key_and_version(subscription_key, version, zuora_entity_ids=zuora_entity_ids, charge_detail=charge_detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->g_et_subscriptions_by_key_and_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_key** | **str**| Subscription number. For example, A-S00000135.  | 
 **version** | **str**| Subscription version. For example, 1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **charge_detail** | **str**|  The segmented rate plan charges. When an amendment results in a change to a charge, Zuora creates a segmented rate plan charge. Use this field to track segment charges.  Possible values are:   * __last-segment__: (Default) The last rate plan charge on the subscription. The last rate plan charge is the last one in the order of time on the subscription rather than the most recent changed charge on the subscription.  * __current-segment__: The segmented charge that is active on today’s date (effectiveStartDate &lt;&#x3D; today’s date &lt; effectiveEndDate).    * __all-segments__: All the segmented charges. The &#x60;chargeSegments&#x60; field is returned in the response. The &#x60;chargeSegments&#x60; field contains an array of the charge information for all the charge segments.   * __specific-segment&amp;as-of-date&#x3D;date__: The segmented charge that is active on a date you specified (effectiveStartDate &lt;&#x3D; specific date &lt; effectiveEndDate). The format of the date is yyyy-mm-dd.  | [optional] 

### Return type

[**GETSubscriptionTypeWithSuccess**](GETSubscriptionTypeWithSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_delete_subscription**
> ProxyDeleteResponse object_delete_subscription(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Delete Subscription

**Note:** This feature is unavailable if you have the Orders feature enabled. See [Orders Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Delete Subscription
    api_response = api_instance.object_delete_subscription(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->object_delete_subscription: %s\n" % e)
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

# **object_get_subscription**
> ProxyGetSubscription object_get_subscription(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, fields=fields)

CRUD: Retrieve Subscription

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
fields = 'fields_example' # str | Object fields to return (optional)

try:
    # CRUD: Retrieve Subscription
    api_response = api_instance.object_get_subscription(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->object_get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **fields** | **str**| Object fields to return | [optional] 

### Return type

[**ProxyGetSubscription**](ProxyGetSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_put_subscription**
> ProxyCreateOrModifyResponse object_put_subscription(body, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Update Subscription

**Note:** This feature is unavailable if you have the Orders feature enabled. See [Orders Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
body = swagger_client.ProxyModifySubscription() # ProxyModifySubscription | 
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Update Subscription
    api_response = api_instance.object_put_subscription(body, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->object_put_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProxyModifySubscription**](ProxyModifySubscription.md)|  | 
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

# **p_ost_preview_subscription**
> POSTSubscriptionPreviewResponseType p_ost_preview_subscription(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Preview subscription

The REST API reference describes how to create a new subscription in preview mode. This call does not require a valid customer account. It can be used to show potential new customers a preview of a subscription with complete details and charges before creating an account, or to let existing customers preview a subscription with all charges before committing.  ## Notes - This feature is unavailable if you have the Orders feature enabled. See [Orders Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information. - The response of the Preview Subscription call is based on the REST API minor version you set in the request header. The response structure might be different if you use different minor version numbers.   - If you have the Invoice Settlement feature enabled, we recommend that you set the `zuora-version` parameter to `207.0` or later. Otherwise, an error is returned.   - Default values for **customerAcceptanceDate** and **serviceActivationDate** are set as follows.  |        | serviceActivationDate (SA) specified          | serviceActivationDate (SA) NOT specified  | | ------------- |:-------------:| -----:| | customerAcceptanceDate (CA) specified      | SA uses value in the request call; CA uses value in the request call| CA uses value in the request call;SA uses CE as default | | customerAcceptanceDate (CA) NOT specified      | SA uses value in the request call; CA uses SA as default |   SA and CA use CE as default | 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
body = swagger_client.Object() # Object | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str |  The minor version of the Zuora REST API.   You need to set this parameter if you use the following fields: * targetDate * includeExistingDraftDocItems * previewType   If you have the Invoice Settlement feature enabled, you need to specify this parameter. Otherwise, an error is returned.   See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.   (optional)

try:
    # Preview subscription
    api_response = api_instance.p_ost_preview_subscription(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->p_ost_preview_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**|  The minor version of the Zuora REST API.   You need to set this parameter if you use the following fields: * targetDate * includeExistingDraftDocItems * previewType   If you have the Invoice Settlement feature enabled, you need to specify this parameter. Otherwise, an error is returned.   See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.   | [optional] 

### Return type

[**POSTSubscriptionPreviewResponseType**](POSTSubscriptionPreviewResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_subscription**
> POSTSubscriptionResponseType p_ost_subscription(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Create subscription

This REST API reference describes how to create a new subscription for an existing customer account.  ## Notes This feature is unavailable if you have the Orders feature enabled. See [Orders Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information.  If invoiceCollect is `true`, the call will not return success = `true` unless the subscription, invoice, and payment are all successful.  Default values for **customerAcceptanceDate** and **serviceActivationDate** are set as follows.  |        | serviceActivationDate(SA) specified          | serviceActivationDate (SA) NOT specified  | | ------------- |:-------------:| -----:| | customerAcceptanceDate (CA) specified| SA uses value in the request call; CA uses value in the request call| CA uses value in the request call;SA uses CE as default | | customerAcceptanceDate (CA) NOT specified      | SA uses value in the request call; CA uses SA as default |   SA and CA use CE as default | 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
body = swagger_client.POSTSubscriptionType() # POSTSubscriptionType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str | The minor version of the Zuora REST API.   You only need to set this parameter if you use the following fields: * invoice * collect * runBilling * targetDate  (optional)

try:
    # Create subscription
    api_response = api_instance.p_ost_subscription(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->p_ost_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTSubscriptionType**](POSTSubscriptionType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**| The minor version of the Zuora REST API.   You only need to set this parameter if you use the following fields: * invoice * collect * runBilling * targetDate  | [optional] 

### Return type

[**POSTSubscriptionResponseType**](POSTSubscriptionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_cancel_subscription**
> POSTSubscriptionCancellationResponseType p_ut_cancel_subscription(body, subscription_key, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Cancel subscription

This REST API reference describes how to cancel an active subscription.  **Note:** This feature is unavailable if you have the Orders feature enabled. See [Orders Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
body = swagger_client.POSTSubscriptionCancellationType() # POSTSubscriptionCancellationType | 
subscription_key = 'subscription_key_example' # str | Subscription number or ID. Subscription status must be `Active`.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str | The minor version of the Zuora REST API.   You only need to set this parameter if you use the following fields: * invoice * collect * runBilling * targetDate   (optional)

try:
    # Cancel subscription
    api_response = api_instance.p_ut_cancel_subscription(body, subscription_key, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->p_ut_cancel_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTSubscriptionCancellationType**](POSTSubscriptionCancellationType.md)|  | 
 **subscription_key** | **str**| Subscription number or ID. Subscription status must be &#x60;Active&#x60;. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**| The minor version of the Zuora REST API.   You only need to set this parameter if you use the following fields: * invoice * collect * runBilling * targetDate   | [optional] 

### Return type

[**POSTSubscriptionCancellationResponseType**](POSTSubscriptionCancellationResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_renew_subscription**
> PUTRenewSubscriptionResponseType p_ut_renew_subscription(body, subscription_key, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Renew subscription

Renews a termed subscription using existing renewal terms.   **Note:** This feature is unavailable if you have the Orders feature enabled. See [Orders Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
body = swagger_client.PUTRenewSubscriptionType() # PUTRenewSubscriptionType | 
subscription_key = 'subscription_key_example' # str | Subscription number or ID
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str | The minor version of the Zuora REST API.   You only need to set this parameter if you use the following fields: * invoice * collect * runBilling * targetDate   (optional)

try:
    # Renew subscription
    api_response = api_instance.p_ut_renew_subscription(body, subscription_key, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->p_ut_renew_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTRenewSubscriptionType**](PUTRenewSubscriptionType.md)|  | 
 **subscription_key** | **str**| Subscription number or ID | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**| The minor version of the Zuora REST API.   You only need to set this parameter if you use the following fields: * invoice * collect * runBilling * targetDate   | [optional] 

### Return type

[**PUTRenewSubscriptionResponseType**](PUTRenewSubscriptionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_resume_subscription**
> PUTSubscriptionResumeResponseType p_ut_resume_subscription(body, subscription_key, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Resume subscription

This REST API reference describes how to resume a suspended subscription.   This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://suport.zuora.com).   **Note:** This feature is unavailable if you have the Orders feature enabled. See [Orders API Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
body = swagger_client.PUTSubscriptionResumeType() # PUTSubscriptionResumeType | 
subscription_key = 'subscription_key_example' # str | Subscription number or ID. Subscription status must be Active.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str | The minor version of the Zuora REST API.   You only need to set this parameter if you use the following fields: * invoice * collect * runBilling * targetDate  (optional)

try:
    # Resume subscription
    api_response = api_instance.p_ut_resume_subscription(body, subscription_key, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->p_ut_resume_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTSubscriptionResumeType**](PUTSubscriptionResumeType.md)|  | 
 **subscription_key** | **str**| Subscription number or ID. Subscription status must be Active. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**| The minor version of the Zuora REST API.   You only need to set this parameter if you use the following fields: * invoice * collect * runBilling * targetDate  | [optional] 

### Return type

[**PUTSubscriptionResumeResponseType**](PUTSubscriptionResumeResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_subscription**
> PUTSubscriptionResponseType p_ut_subscription(body, subscription_key, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Update subscription

Use this call to make the following kinds of changes to a subscription:   * Add a note   * Change the renewal term or auto-renewal flag   * Change the term length or change between evergreen and termed   * Add a new product rate plan   * Remove an existing subscription rate plan   * Change the quantity or price of an existing subscription rate plan  ## Notes * This feature is unavailable if you have the Orders feature enabled. See [Orders Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information. * The Update Subscription call creates a new subscription, which has the old subscription number but a new subscription ID.  The old subscription is canceled but remains in the system. * In one request, this call can make:   * Up to 9 combined add, update, and remove changes   * No more than 1 change to terms & conditions * Updates are performed in the following sequence:   1. First change the notes on the existing subscription, if requested.   2. Then change the terms and conditions, if requested.   3. Then perform the remaining amendments based upon the effective dates specified. If multiple amendments have the same contract-effective dates, then execute adds before updates, and updates before removes. * The update operation is atomic. If any of the updates fails, the entire operation is rolled back. * The response of the Update Subscription call is based on the REST API minor version you set in the request header. The response structure might be different if you use different minor version numbers.  * If you have the Invoice Settlement feature enabled, we recommend that you set the `zuora-version` parameter to `207.0` or later. Otherwise, an error is returned.  ## Override a Tiered Price There are two ways you override a tiered price:  * Override a specific tier number For example: `tiers[{tier:1,price:8},{tier:2,price:6}]`  * Override the entire tier structure For example:  `tiers[{tier:1,price:8,startingUnit:1,endingUnit:100,priceFormat:\"FlatFee\"}, {tier:2,price:6,startingUnit:101,priceFormat:\"FlatFee\"}]`  If you just override a specific tier, do not include the `startingUnit` field in the request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
body = swagger_client.PUTSubscriptionType() # PUTSubscriptionType | 
subscription_key = 'subscription_key_example' # str | Subscription number or ID.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str |  The minor version of the Zuora REST API.   You need to set this parameter if you use the following fields: * collect * invoice * includeExistingDraftDocItems * previewType * runBilling * targetDate   If you have the Invoice Settlement feature enabled, you need to specify this parameter. Otherwise, an error is returned.   See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.  (optional)

try:
    # Update subscription
    api_response = api_instance.p_ut_subscription(body, subscription_key, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->p_ut_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTSubscriptionType**](PUTSubscriptionType.md)|  | 
 **subscription_key** | **str**| Subscription number or ID. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**|  The minor version of the Zuora REST API.   You need to set this parameter if you use the following fields: * collect * invoice * includeExistingDraftDocItems * previewType * runBilling * targetDate   If you have the Invoice Settlement feature enabled, you need to specify this parameter. Otherwise, an error is returned.   See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.  | [optional] 

### Return type

[**PUTSubscriptionResponseType**](PUTSubscriptionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_suspend_subscription**
> PUTSubscriptionSuspendResponseType p_ut_suspend_subscription(body, subscription_key, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Suspend subscription

This REST API reference describes how to suspend an active subscription.   This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://suport.zuora.com).  **Note:** This feature is unavailable if you have the Orders feature enabled. See [Orders API Migration Guidance](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AB_Orders_Migration_Guidance) for more information. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
body = swagger_client.PUTSubscriptionSuspendType() # PUTSubscriptionSuspendType | 
subscription_key = 'subscription_key_example' # str | Subscription number or ID. Subscription status must be Active.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str | The minor version of the Zuora REST API.   You only need to set this parameter if you use the following fields: * invoice * collect * runBilling * targetDate  (optional)

try:
    # Suspend subscription
    api_response = api_instance.p_ut_suspend_subscription(body, subscription_key, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->p_ut_suspend_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTSubscriptionSuspendType**](PUTSubscriptionSuspendType.md)|  | 
 **subscription_key** | **str**| Subscription number or ID. Subscription status must be Active. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**| The minor version of the Zuora REST API.   You only need to set this parameter if you use the following fields: * invoice * collect * runBilling * targetDate  | [optional] 

### Return type

[**PUTSubscriptionSuspendResponseType**](PUTSubscriptionSuspendResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

