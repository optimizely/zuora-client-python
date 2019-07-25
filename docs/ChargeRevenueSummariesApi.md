# swagger_client.ChargeRevenueSummariesApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_etcrs_by_charge_id**](ChargeRevenueSummariesApi.md#g_etcrs_by_charge_id) | **GET** /v1/charge-revenue-summaries/subscription-charges/{charge-key} | Get charge summary details by charge ID
[**g_etcrs_by_crs_number**](ChargeRevenueSummariesApi.md#g_etcrs_by_crs_number) | **GET** /v1/charge-revenue-summaries/{crs-number} | Get charge summary details by CRS number

# **g_etcrs_by_charge_id**
> GETChargeRSDetailType g_etcrs_by_charge_id(charge_key, zuora_entity_ids=zuora_entity_ids)

Get charge summary details by charge ID

This REST API reference describes how to retrieve the details of a charge revenue summary by specifying the subscription charge ID. This response retrieves all revenue items associated with a charge revenue summary. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChargeRevenueSummariesApi()
charge_key = 'charge_key_example' # str | ID of the subscription rate plan charge; for example, 402892793e173340013e173b81000012. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get charge summary details by charge ID
    api_response = api_instance.g_etcrs_by_charge_id(charge_key, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargeRevenueSummariesApi->g_etcrs_by_charge_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_key** | **str**| ID of the subscription rate plan charge; for example, 402892793e173340013e173b81000012.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETChargeRSDetailType**](GETChargeRSDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_etcrs_by_crs_number**
> GETChargeRSDetailType g_etcrs_by_crs_number(crs_number, zuora_entity_ids=zuora_entity_ids)

Get charge summary details by CRS number

This REST API reference describes how to retrieve the details of a charge revenue summary by specifying the charge revenue summary number. The response includes all revenue items associated with the charge revenue summary. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChargeRevenueSummariesApi()
crs_number = 'crs_number_example' # str | The charge revenue summary number. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get charge summary details by CRS number
    api_response = api_instance.g_etcrs_by_crs_number(crs_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargeRevenueSummariesApi->g_etcrs_by_crs_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crs_number** | **str**| The charge revenue summary number.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETChargeRSDetailType**](GETChargeRSDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

