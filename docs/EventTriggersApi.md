# zuora_client.EventTriggersApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_event_trigger**](EventTriggersApi.md#d_elete_event_trigger) | **DELETE** /events/event-triggers/{id} | Remove an event trigger
[**g_et_event_trigger**](EventTriggersApi.md#g_et_event_trigger) | **GET** /events/event-triggers/{id} | Get an event trigger by ID
[**g_et_event_triggers**](EventTriggersApi.md#g_et_event_triggers) | **GET** /events/event-triggers | Query event triggers
[**p_ost_event_trigger**](EventTriggersApi.md#p_ost_event_trigger) | **POST** /events/event-triggers | Create an event trigger
[**p_ut_event_trigger**](EventTriggersApi.md#p_ut_event_trigger) | **PUT** /events/event-triggers/{id} | Update an event trigger


# **d_elete_event_trigger**
> d_elete_event_trigger(authorization, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Remove an event trigger



### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.EventTriggersApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
id = 'id_example' # str | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Remove an event trigger
    api_instance.d_elete_event_trigger(authorization, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
except ApiException as e:
    print("Exception when calling EventTriggersApi->d_elete_event_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **id** | [**str**](.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_event_trigger**
> EventTrigger g_et_event_trigger(authorization, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Get an event trigger by ID

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.EventTriggersApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
id = 'id_example' # str | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Get an event trigger by ID
    api_response = api_instance.g_et_event_trigger(authorization, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventTriggersApi->g_et_event_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **id** | [**str**](.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**EventTrigger**](EventTrigger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_event_triggers**
> InlineResponse2001 g_et_event_triggers(authorization, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, base_object=base_object, event_type_name=event_type_name, active=active, start=start, limit=limit)

Query event triggers

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.EventTriggersApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
base_object = 'base_object_example' # str | The Zuora object that trigger condition is defined upon. Should be specified in the pattern: ^[A-Z][\\\\w\\\\-]*$ (optional)
event_type_name = 'event_type_name_example' # str | The event type name. Should be specified in the pattern: ^[A-Za-z]{1,}[\\w\\-]*$ (optional)
active = 'active_example' # str | The status of the event trigger. (optional)
start = 0 # int | The first index of the query result. Default to 0 if absent, and the minimum is 0. (optional) (default to 0)
limit = 10 # int | The maximum number of data records to be returned. Default to 10 if absent. (optional) (default to 10)

try:
    # Query event triggers
    api_response = api_instance.g_et_event_triggers(authorization, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, base_object=base_object, event_type_name=event_type_name, active=active, start=start, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventTriggersApi->g_et_event_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **base_object** | **str**| The Zuora object that trigger condition is defined upon. Should be specified in the pattern: ^[A-Z][\\\\w\\\\-]*$ | [optional] 
 **event_type_name** | **str**| The event type name. Should be specified in the pattern: ^[A-Za-z]{1,}[\\w\\-]*$ | [optional] 
 **active** | **str**| The status of the event trigger. | [optional] 
 **start** | **int**| The first index of the query result. Default to 0 if absent, and the minimum is 0. | [optional] [default to 0]
 **limit** | **int**| The maximum number of data records to be returned. Default to 10 if absent. | [optional] [default to 10]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_event_trigger**
> EventTrigger p_ost_event_trigger(authorization, post_event_trigger_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Create an event trigger

You can define an event trigger on any of the following objects:    * Account   * AccountingCode   * AccountingPeriod   * Amendment   * BillingRun   * Contact   * CreditBalanceAdjustment   * CreditMemo   * CreditMemoApplication   * CreditMemoApplicationItem   * CreditMemoItem   * DebitMemo   * DebitMemoItem   * Feature   * Invoice   * InvoiceAdjustment   * InvoiceItem   * InvoiceItemAdjustment   * JournalEntry   * JournalEntryItem   * Order   * OrderAction   * Payment   * PaymentApplication   * PaymentMethod   * PaymentPart   * Product   * ProductFeature   * ProductRatePlan   * ProductRatePlanCharge   * RatePlan   * RatePlanCharge   * Refund   * RefundApplication   * RevenueEvent   * RevenueEventItem   * RevenueSchedule   * RevenueScheduleItem   * Subscription   * SubscriptionProductFeature   * TaxationItem   * Usage  The `baseObject` field specifies which object to define a trigger on. The `condition` field is a [JEXL](http://commons.apache.org/proper/commons-jexl/) expression that specifies when to trigger events. The expression can contain fields from the object that the trigger is defined on.  **Note:** The condition cannot contain fields from [data source](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL) objects that are joined to the object that the trigger is defined on.  For example, the following condition causes an event to be triggered whenever an invoice is posted with an amount greater than 1000:  ```changeType == 'UPDATE' && Invoice.Status == 'Posted' && Invoice.Status_old != 'Posted' && Invoice.Amount > 1000```  Where:    * `changeType` is a keyword that specifies the type of change that occurred to the Invoice object. For all objects, the supported values of `changeType` are `INSERT`, `UPDATE`,  and `DELETE`.   * `Invoice.Status` is the value of the Invoice object's `Status` field after the change occurred.   * `Invoice.Status_old` is the value of the Invoice object's `Status` field before the change occurred.  In the above example, the value of `baseObject` would be `Invoice`.  **Note:** The number of the event triggers that you can create depends on the [edition of Zuora Central Platform](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) you are using. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.EventTriggersApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
post_event_trigger_request = zuora_client.PostEventTriggerRequest() # PostEventTriggerRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Create an event trigger
    api_response = api_instance.p_ost_event_trigger(authorization, post_event_trigger_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventTriggersApi->p_ost_event_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **post_event_trigger_request** | [**PostEventTriggerRequest**](PostEventTriggerRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**EventTrigger**](EventTrigger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_event_trigger**
> EventTrigger p_ut_event_trigger(authorization, id, put_event_trigger_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Update an event trigger



### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.EventTriggersApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
id = 'id_example' # str | 
put_event_trigger_request = zuora_client.PutEventTriggerRequest() # PutEventTriggerRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Update an event trigger
    api_response = api_instance.p_ut_event_trigger(authorization, id, put_event_trigger_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventTriggersApi->p_ut_event_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **id** | [**str**](.md)|  | 
 **put_event_trigger_request** | [**PutEventTriggerRequest**](PutEventTriggerRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**EventTrigger**](EventTrigger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

