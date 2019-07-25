# swagger_client.RevenueItemsApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_revenue_items_by_charge_revenue_event_number**](RevenueItemsApi.md#g_et_revenue_items_by_charge_revenue_event_number) | **GET** /v1/revenue-items/revenue-events/{event-number} | Get revenue items by revenue event number
[**g_et_revenue_items_by_charge_revenue_summary_number**](RevenueItemsApi.md#g_et_revenue_items_by_charge_revenue_summary_number) | **GET** /v1/revenue-items/charge-revenue-summaries/{crs-number} | Get revenue items by charge revenue summary number
[**g_et_revenue_items_by_revenue_schedule**](RevenueItemsApi.md#g_et_revenue_items_by_revenue_schedule) | **GET** /v1/revenue-items/revenue-schedules/{rs-number} | Get revenue items by revenue schedule
[**p_ut_custom_fieldson_revenue_items_by_revenue_event**](RevenueItemsApi.md#p_ut_custom_fieldson_revenue_items_by_revenue_event) | **PUT** /v1/revenue-items/revenue-events/{event-number} | Update custom fields on revenue items by revenue event number
[**p_ut_custom_fieldson_revenue_items_by_revenue_schedule**](RevenueItemsApi.md#p_ut_custom_fieldson_revenue_items_by_revenue_schedule) | **PUT** /v1/revenue-items/revenue-schedules/{rs-number} | Update custom fields on revenue items by revenue schedule number

# **g_et_revenue_items_by_charge_revenue_event_number**
> GETRevenueItemsType g_et_revenue_items_by_charge_revenue_event_number(event_number, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get revenue items by revenue event number

This REST API reference describes how to get the details of each revenue item in a revenue event by specifying the revenue event number. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevenueItemsApi()
event_number = 'event_number_example' # str | The number associated with the revenue event.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get revenue items by revenue event number
    api_response = api_instance.g_et_revenue_items_by_charge_revenue_event_number(event_number, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueItemsApi->g_et_revenue_items_by_charge_revenue_event_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_number** | **str**| The number associated with the revenue event. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GETRevenueItemsType**](GETRevenueItemsType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_revenue_items_by_charge_revenue_summary_number**
> GETRevenueItemsType g_et_revenue_items_by_charge_revenue_summary_number(crs_number, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get revenue items by charge revenue summary number

This REST API reference describes how to get the details for each revenue item in a charge revenue summary by specifying the charge revenue summary number. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevenueItemsApi()
crs_number = 'crs_number_example' # str | The charge revenue summary number.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get revenue items by charge revenue summary number
    api_response = api_instance.g_et_revenue_items_by_charge_revenue_summary_number(crs_number, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueItemsApi->g_et_revenue_items_by_charge_revenue_summary_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crs_number** | **str**| The charge revenue summary number. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GETRevenueItemsType**](GETRevenueItemsType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_revenue_items_by_revenue_schedule**
> GETRsRevenueItemsType g_et_revenue_items_by_revenue_schedule(rs_number, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get revenue items by revenue schedule

This REST API reference describes how to get the details for each revenue items in a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevenueItemsApi()
rs_number = 'rs_number_example' # str | Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get revenue items by revenue schedule
    api_response = api_instance.g_et_revenue_items_by_revenue_schedule(rs_number, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueItemsApi->g_et_revenue_items_by_revenue_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rs_number** | **str**| Revenue schedule number. The revenue schedule number is always prefixed with \&quot;RS\&quot;, for example, \&quot;RS-00000001\&quot;. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GETRsRevenueItemsType**](GETRsRevenueItemsType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_custom_fieldson_revenue_items_by_revenue_event**
> CommonResponseType p_ut_custom_fieldson_revenue_items_by_revenue_event(body, event_number, zuora_entity_ids=zuora_entity_ids)

Update custom fields on revenue items by revenue event number

This REST API reference describes how to update custom fields on revenue items by specifying the revenue event number. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevenueItemsApi()
body = swagger_client.PUTEventRIDetailType() # PUTEventRIDetailType | 
event_number = 'event_number_example' # str | The number associated with the revenue event.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update custom fields on revenue items by revenue event number
    api_response = api_instance.p_ut_custom_fieldson_revenue_items_by_revenue_event(body, event_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueItemsApi->p_ut_custom_fieldson_revenue_items_by_revenue_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTEventRIDetailType**](PUTEventRIDetailType.md)|  | 
 **event_number** | **str**| The number associated with the revenue event. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_custom_fieldson_revenue_items_by_revenue_schedule**
> CommonResponseType p_ut_custom_fieldson_revenue_items_by_revenue_schedule(body, rs_number, zuora_entity_ids=zuora_entity_ids)

Update custom fields on revenue items by revenue schedule number

This REST API reference describes how to update custom fields on revenue Items by specifying the revenue schedule number. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevenueItemsApi()
body = swagger_client.PUTScheduleRIDetailType() # PUTScheduleRIDetailType | 
rs_number = 'rs_number_example' # str | Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update custom fields on revenue items by revenue schedule number
    api_response = api_instance.p_ut_custom_fieldson_revenue_items_by_revenue_schedule(body, rs_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueItemsApi->p_ut_custom_fieldson_revenue_items_by_revenue_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTScheduleRIDetailType**](PUTScheduleRIDetailType.md)|  | 
 **rs_number** | **str**| Revenue schedule number. The revenue schedule number is always prefixed with \&quot;RS\&quot;, for example, \&quot;RS-00000001\&quot;. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

