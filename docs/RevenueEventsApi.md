# zuora_client.RevenueEventsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_revenue_event_details**](RevenueEventsApi.md#g_et_revenue_event_details) | **GET** /v1/revenue-events/{event-number} | Get revenue event details
[**g_et_revenue_event_for_revenue_schedule**](RevenueEventsApi.md#g_et_revenue_event_for_revenue_schedule) | **GET** /v1/revenue-events/revenue-schedules/{rs-number} | Get revenue events for a revenue schedule


# **g_et_revenue_event_details**
> GETRevenueEventDetailType g_et_revenue_event_details(event_number, zuora_entity_ids=zuora_entity_ids)

Get revenue event details

 This REST API reference describes how to get revenue event details by specifying the revenue event number. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueEventsApi()
event_number = 'event_number_example' # str | The number associated with the revenue event.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get revenue event details
    api_response = api_instance.g_et_revenue_event_details(event_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueEventsApi->g_et_revenue_event_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_number** | **str**| The number associated with the revenue event. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRevenueEventDetailType**](GETRevenueEventDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_revenue_event_for_revenue_schedule**
> GETRevenueEventDetailsType g_et_revenue_event_for_revenue_schedule(rs_number, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get revenue events for a revenue schedule

 This REST API reference describes how to get all revenue events in a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueEventsApi()
rs_number = 'rs_number_example' # str | Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 8 # int | Number of rows returned per page.  (optional) (default to 8)

try:
    # Get revenue events for a revenue schedule
    api_response = api_instance.g_et_revenue_event_for_revenue_schedule(rs_number, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueEventsApi->g_et_revenue_event_for_revenue_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rs_number** | **str**| Revenue schedule number. The revenue schedule number is always prefixed with \&quot;RS\&quot;, for example, \&quot;RS-00000001\&quot;. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] [default to 8]

### Return type

[**GETRevenueEventDetailsType**](GETRevenueEventDetailsType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

