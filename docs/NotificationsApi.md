# swagger_client.NotificationsApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_delete_email_template**](NotificationsApi.md#d_elete_delete_email_template) | **DELETE** /notifications/email-templates/{id} | Delete an email template
[**d_elete_delete_notification_definition**](NotificationsApi.md#d_elete_delete_notification_definition) | **DELETE** /notifications/notification-definitions/{id} | Delete a notification definition
[**g_et_callout_history**](NotificationsApi.md#g_et_callout_history) | **GET** /v1/notification-history/callout | Get callout notification histories
[**g_et_email_history**](NotificationsApi.md#g_et_email_history) | **GET** /v1/notification-history/email | Get email notification histories
[**g_et_get_email_template**](NotificationsApi.md#g_et_get_email_template) | **GET** /notifications/email-templates/{id} | Get an email template
[**g_et_get_notification_definition**](NotificationsApi.md#g_et_get_notification_definition) | **GET** /notifications/notification-definitions/{id} | Get a notification definition
[**g_et_query_email_templates**](NotificationsApi.md#g_et_query_email_templates) | **GET** /notifications/email-templates | Query email templates
[**g_et_query_notification_definitions**](NotificationsApi.md#g_et_query_notification_definitions) | **GET** /notifications/notification-definitions | Query notification definitions
[**p_ost_create_email_template**](NotificationsApi.md#p_ost_create_email_template) | **POST** /notifications/email-templates | Create an email template
[**p_ost_create_notification_definition**](NotificationsApi.md#p_ost_create_notification_definition) | **POST** /notifications/notification-definitions | Create a notification definition
[**p_ut_update_email_template**](NotificationsApi.md#p_ut_update_email_template) | **PUT** /notifications/email-templates/{id} | Update an email template
[**p_ut_update_notification_definition**](NotificationsApi.md#p_ut_update_notification_definition) | **PUT** /notifications/notification-definitions/{id} | Update a notification definition

# **d_elete_delete_email_template**
> d_elete_delete_email_template(authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Delete an email template

Deletes an email template.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the email template to be deleted.
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete an email template
    api_instance.d_elete_delete_email_template(authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
except ApiException as e:
    print("Exception when calling NotificationsApi->d_elete_delete_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **id** | [**str**](.md)| The ID of the email template to be deleted. | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **d_elete_delete_notification_definition**
> d_elete_delete_notification_definition(authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Delete a notification definition

Deletes a notification definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the notification definition to be deleted.
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete a notification definition
    api_instance.d_elete_delete_notification_definition(authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
except ApiException as e:
    print("Exception when calling NotificationsApi->d_elete_delete_notification_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **id** | [**str**](.md)| The ID of the notification definition to be deleted. | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_callout_history**
> GETCalloutHistoryVOsType g_et_callout_history(zuora_entity_ids=zuora_entity_ids, page_size=page_size, end_time=end_time, start_time=start_time, object_id=object_id, failed_only=failed_only, event_category=event_category, include_response_content=include_response_content)

Get callout notification histories

This REST API reference describes how to get a notification history for callouts. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
end_time = '2013-10-20T19:20:30+01:00' # datetime | The final date and time of records to be returned. Defaults to now. Use format yyyy-MM-ddTHH:mm:ss. (optional)
start_time = '2013-10-20T19:20:30+01:00' # datetime | The initial date and time of records to be returned. Defaults to (end time - 1 day). Use format yyyy-MM-ddTHH:mm:ss. (optional)
object_id = 'object_id_example' # str | The ID of an object that triggered a callout notification. (optional)
failed_only = true # bool | If `true`, only return failed records. If `false`, return all records in the given date range. The default value is `true`. (optional)
event_category = 'event_category_example' # str | Category of records to be returned by event category. (optional)
include_response_content = true # bool |  (optional)

try:
    # Get callout notification histories
    api_response = api_instance.g_et_callout_history(zuora_entity_ids=zuora_entity_ids, page_size=page_size, end_time=end_time, start_time=start_time, object_id=object_id, failed_only=failed_only, event_category=event_category, include_response_content=include_response_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->g_et_callout_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **end_time** | **datetime**| The final date and time of records to be returned. Defaults to now. Use format yyyy-MM-ddTHH:mm:ss. | [optional] 
 **start_time** | **datetime**| The initial date and time of records to be returned. Defaults to (end time - 1 day). Use format yyyy-MM-ddTHH:mm:ss. | [optional] 
 **object_id** | **str**| The ID of an object that triggered a callout notification. | [optional] 
 **failed_only** | **bool**| If &#x60;true&#x60;, only return failed records. If &#x60;false&#x60;, return all records in the given date range. The default value is &#x60;true&#x60;. | [optional] 
 **event_category** | **str**| Category of records to be returned by event category. | [optional] 
 **include_response_content** | **bool**|  | [optional] 

### Return type

[**GETCalloutHistoryVOsType**](GETCalloutHistoryVOsType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_email_history**
> GETEmailHistoryVOsType g_et_email_history(zuora_entity_ids=zuora_entity_ids, page_size=page_size, end_time=end_time, start_time=start_time, object_id=object_id, failed_only=failed_only, event_category=event_category)

Get email notification histories

This REST API reference describes how to get a notification history for notification emails.   ## Notes Request parameters and their values may be appended with a \"?\" following the HTTPS GET request.  Additional request parameter are separated by \"&\".   For example:  `GET https://rest.zuora.com/v1/notification-history/email?startTime=2015-01-12T00:00:00&endTime=2015-01-15T00:00:00&failedOnly=false&eventCategory=1000&pageSize=1` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
end_time = '2013-10-20T19:20:30+01:00' # datetime | The end date and time of records to be returned. Defaults to now. Use format yyyy-MM-ddTHH:mm:ss. The maximum date range (endTime - startTime) is three days. (optional)
start_time = '2013-10-20T19:20:30+01:00' # datetime | The initial date and time of records to be returned. Defaults to (end time - 1 day). Use format yyyy-MM-ddTHH:mm:ss. The maximum date range (endTime - startTime) is three days. (optional)
object_id = 'object_id_example' # str | The Id of an object that triggered an email notification. (optional)
failed_only = true # bool | If `true`, only returns failed records. When `false`, returns all records in the given date range. Defaults to `true` when not specified. (optional)
event_category = 'event_category_example' # str | Category of records to be returned by event category. (optional)

try:
    # Get email notification histories
    api_response = api_instance.g_et_email_history(zuora_entity_ids=zuora_entity_ids, page_size=page_size, end_time=end_time, start_time=start_time, object_id=object_id, failed_only=failed_only, event_category=event_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->g_et_email_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **end_time** | **datetime**| The end date and time of records to be returned. Defaults to now. Use format yyyy-MM-ddTHH:mm:ss. The maximum date range (endTime - startTime) is three days. | [optional] 
 **start_time** | **datetime**| The initial date and time of records to be returned. Defaults to (end time - 1 day). Use format yyyy-MM-ddTHH:mm:ss. The maximum date range (endTime - startTime) is three days. | [optional] 
 **object_id** | **str**| The Id of an object that triggered an email notification. | [optional] 
 **failed_only** | **bool**| If &#x60;true&#x60;, only returns failed records. When &#x60;false&#x60;, returns all records in the given date range. Defaults to &#x60;true&#x60; when not specified. | [optional] 
 **event_category** | **str**| Category of records to be returned by event category. | [optional] 

### Return type

[**GETEmailHistoryVOsType**](GETEmailHistoryVOsType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_get_email_template**
> GETPublicEmailTemplateResponse g_et_get_email_template(authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Get an email template

Queries the email template of the specified ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the email template.
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get an email template
    api_response = api_instance.g_et_get_email_template(authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->g_et_get_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **id** | [**str**](.md)| The ID of the email template. | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPublicEmailTemplateResponse**](GETPublicEmailTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_get_notification_definition**
> GETPublicNotificationDefinitionResponse g_et_get_notification_definition(authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Get a notification definition

Queries the notification definition of the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the notification definition.
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get a notification definition
    api_response = api_instance.g_et_get_notification_definition(authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->g_et_get_notification_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **id** | [**str**](.md)| The ID of the notification definition. | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPublicNotificationDefinitionResponse**](GETPublicNotificationDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_query_email_templates**
> object g_et_query_email_templates(authorization, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, start=start, limit=limit, event_type_name=event_type_name, name=name)

Query email templates

Queries email templates. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
start = 56 # int | The first index of the query result. (optional)
limit = 56 # int | The maximum number of results the query should return. (optional)
event_type_name = 'event_type_name_example' # str | The name of the event. (optional)
name = 'name_example' # str | The name of the email template. (optional)

try:
    # Query email templates
    api_response = api_instance.g_et_query_email_templates(authorization, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, start=start, limit=limit, event_type_name=event_type_name, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->g_et_query_email_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **start** | **int**| The first index of the query result. | [optional] 
 **limit** | **int**| The maximum number of results the query should return. | [optional] 
 **event_type_name** | **str**| The name of the event. | [optional] 
 **name** | **str**| The name of the email template. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_query_notification_definitions**
> object g_et_query_notification_definitions(authorization, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, start=start, limit=limit, profile_id=profile_id, event_type_name=event_type_name, email_template_id=email_template_id)

Query notification definitions

Queries notification definitions with the specified filters. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
start = 56 # int | The first index of the query result. (optional)
limit = 56 # int | The maximum number of results the query should return. (optional)
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of the profile. (optional)
event_type_name = 'event_type_name_example' # str | The name of the event. (optional)
email_template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the email template. (optional)

try:
    # Query notification definitions
    api_response = api_instance.g_et_query_notification_definitions(authorization, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids, start=start, limit=limit, profile_id=profile_id, event_type_name=event_type_name, email_template_id=email_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->g_et_query_notification_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **start** | **int**| The first index of the query result. | [optional] 
 **limit** | **int**| The maximum number of results the query should return. | [optional] 
 **profile_id** | [**str**](.md)| Id of the profile. | [optional] 
 **event_type_name** | **str**| The name of the event. | [optional] 
 **email_template_id** | [**str**](.md)| The ID of the email template. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_create_email_template**
> GETPublicEmailTemplateResponse p_ost_create_email_template(body, authorization, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Create an email template

Creates an email template. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
body = swagger_client.POSTPublicEmailTemplateRequest() # POSTPublicEmailTemplateRequest | The request body to create an email template.
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create an email template
    api_response = api_instance.p_ost_create_email_template(body, authorization, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->p_ost_create_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTPublicEmailTemplateRequest**](POSTPublicEmailTemplateRequest.md)| The request body to create an email template. | 
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPublicEmailTemplateResponse**](GETPublicEmailTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_create_notification_definition**
> GETPublicNotificationDefinitionResponse p_ost_create_notification_definition(body, authorization, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Create a notification definition

Creates a notification definition. If a filter rule is specified, it will be evaluated to see if the notification definition is qualified to handle the incoming events  during runtime. If the notification is qualified, it will send the email and invoke the callout if it has an email template or a callout. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
body = swagger_client.POSTPublicNotificationDefinitionRequest() # POSTPublicNotificationDefinitionRequest | The request body used to create the notification definition.
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create a notification definition
    api_response = api_instance.p_ost_create_notification_definition(body, authorization, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->p_ost_create_notification_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTPublicNotificationDefinitionRequest**](POSTPublicNotificationDefinitionRequest.md)| The request body used to create the notification definition. | 
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPublicNotificationDefinitionResponse**](GETPublicNotificationDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_update_email_template**
> GETPublicEmailTemplateResponse p_ut_update_email_template(body, authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Update an email template

Updates an email template. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
body = swagger_client.PUTPublicEmailTemplateRequest() # PUTPublicEmailTemplateRequest | The request body to update an email template.
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the email template to be updated.
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update an email template
    api_response = api_instance.p_ut_update_email_template(body, authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->p_ut_update_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTPublicEmailTemplateRequest**](PUTPublicEmailTemplateRequest.md)| The request body to update an email template. | 
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **id** | [**str**](.md)| The ID of the email template to be updated. | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPublicEmailTemplateResponse**](GETPublicEmailTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_update_notification_definition**
> GETPublicNotificationDefinitionResponse p_ut_update_notification_definition(body, authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)

Update a notification definition

Updates a notification definition. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
body = swagger_client.PUTPublicNotificationDefinitionRequest() # PUTPublicNotificationDefinitionRequest | The request body of the notification definition to be updated.
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the notification definition to be updated.
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update a notification definition
    api_response = api_instance.p_ut_update_notification_definition(body, authorization, id, zuora_track_id=zuora_track_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->p_ut_update_notification_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTPublicNotificationDefinitionRequest**](PUTPublicNotificationDefinitionRequest.md)| The request body of the notification definition to be updated. | 
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **id** | [**str**](.md)| The ID of the notification definition to be updated. | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPublicNotificationDefinitionResponse**](GETPublicNotificationDefinitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

