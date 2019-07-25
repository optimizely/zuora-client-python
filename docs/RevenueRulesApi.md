# swagger_client.RevenueRulesApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_revenue_rec_ruleby_product_rate_plan_charge**](RevenueRulesApi.md#g_et_revenue_rec_ruleby_product_rate_plan_charge) | **GET** /v1/revenue-recognition-rules/product-charges/{charge-key} | Get revenue recognition rule by product rate plan charge
[**g_et_revenue_rec_rules**](RevenueRulesApi.md#g_et_revenue_rec_rules) | **GET** /v1/revenue-recognition-rules/subscription-charges/{charge-key} | Get revenue recognition rule by subscription charge

# **g_et_revenue_rec_ruleby_product_rate_plan_charge**
> GETRevenueRecognitionRuleAssociationType g_et_revenue_rec_ruleby_product_rate_plan_charge(charge_key)

Get revenue recognition rule by product rate plan charge

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the revenue recognition rule associated with a production rate plan charge by specifying the charge ID. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevenueRulesApi()
charge_key = 'charge_key_example' # str | The unique ID of a product rate plan charge. For example, 8a8082e65ba86084015bb323d3c61d82. 

try:
    # Get revenue recognition rule by product rate plan charge
    api_response = api_instance.g_et_revenue_rec_ruleby_product_rate_plan_charge(charge_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueRulesApi->g_et_revenue_rec_ruleby_product_rate_plan_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_key** | **str**| The unique ID of a product rate plan charge. For example, 8a8082e65ba86084015bb323d3c61d82.  | 

### Return type

[**GETRevenueRecognitionRuleAssociationType**](GETRevenueRecognitionRuleAssociationType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_revenue_rec_rules**
> GETRevenueRecognitionRuleAssociationType g_et_revenue_rec_rules(charge_key, zuora_entity_ids=zuora_entity_ids)

Get revenue recognition rule by subscription charge

Retrieves the revenue recognition rule associated with a subscription charge by specifying the charge ID. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevenueRulesApi()
charge_key = 'charge_key_example' # str | The unique ID of the subscription rate plan charge. For example, 402892793e173340013e173b81000012. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get revenue recognition rule by subscription charge
    api_response = api_instance.g_et_revenue_rec_rules(charge_key, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueRulesApi->g_et_revenue_rec_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_key** | **str**| The unique ID of the subscription rate plan charge. For example, 402892793e173340013e173b81000012.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRevenueRecognitionRuleAssociationType**](GETRevenueRecognitionRuleAssociationType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

