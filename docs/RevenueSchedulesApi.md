# zuora_client.RevenueSchedulesApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_eleters**](RevenueSchedulesApi.md#d_eleters) | **DELETE** /v1/revenue-schedules/{rs-number} | Delete revenue schedule
[**g_etr_sby_credit_memo_item**](RevenueSchedulesApi.md#g_etr_sby_credit_memo_item) | **GET** /v1/revenue-schedules/credit-memo-items/{cmi-id} | Get revenue schedule by credit memo item ID 
[**g_etr_sby_debit_memo_item**](RevenueSchedulesApi.md#g_etr_sby_debit_memo_item) | **GET** /v1/revenue-schedules/debit-memo-items/{dmi-id} | Get revenue schedule by debit memo item ID 
[**g_etr_sby_invoice_item**](RevenueSchedulesApi.md#g_etr_sby_invoice_item) | **GET** /v1/revenue-schedules/invoice-items/{invoice-item-id} | Get revenue schedule by invoice item ID
[**g_etr_sby_invoice_item_adjustment**](RevenueSchedulesApi.md#g_etr_sby_invoice_item_adjustment) | **GET** /v1/revenue-schedules/invoice-item-adjustments/{invoice-item-adj-key} | Get revenue schedule by invoice item adjustment
[**g_etr_sby_product_charge_and_billing_account**](RevenueSchedulesApi.md#g_etr_sby_product_charge_and_billing_account) | **GET** /v1/revenue-schedules/product-charges/{charge-key}/{account-key} | Get all revenue schedules of product charge by charge ID and billing account ID 
[**g_etr_sfor_subsc_charge**](RevenueSchedulesApi.md#g_etr_sfor_subsc_charge) | **GET** /v1/revenue-schedules/subscription-charges/{charge-key} | Get revenue schedule by subscription charge
[**g_etrs**](RevenueSchedulesApi.md#g_etrs) | **GET** /v1/revenue-schedules/{rs-number} | Get revenue schedule details
[**p_ostr_sfor_credit_memo_item_distribute_by_date_range**](RevenueSchedulesApi.md#p_ostr_sfor_credit_memo_item_distribute_by_date_range) | **POST** /v1/revenue-schedules/credit-memo-items/{cmi-id}/distribute-revenue-with-date-range | Create revenue schedule for credit memo item (distribute by date range) 
[**p_ostr_sfor_credit_memo_item_manual_distribution**](RevenueSchedulesApi.md#p_ostr_sfor_credit_memo_item_manual_distribution) | **POST** /v1/revenue-schedules/credit-memo-items/{cmi-id} | Create revenue schedule for credit memo item (manual distribution) 
[**p_ostr_sfor_debit_memo_item_distribute_by_date_range**](RevenueSchedulesApi.md#p_ostr_sfor_debit_memo_item_distribute_by_date_range) | **POST** /v1/revenue-schedules/debit-memo-items/{dmi-id}/distribute-revenue-with-date-range | Create revenue schedule for debit memo item (distribute by date range) 
[**p_ostr_sfor_debit_memo_item_manual_distribution**](RevenueSchedulesApi.md#p_ostr_sfor_debit_memo_item_manual_distribution) | **POST** /v1/revenue-schedules/debit-memo-items/{dmi-id} | Create revenue schedule for debit memo item (manual distribution) 
[**p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range**](RevenueSchedulesApi.md#p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range) | **POST** /v1/revenue-schedules/invoice-item-adjustments/{invoice-item-adj-key}/distribute-revenue-with-date-range | Create revenue schedule for Invoice Item Adjustment (distribute by date range)
[**p_ostr_sfor_invoice_item_adjustment_manual_distribution**](RevenueSchedulesApi.md#p_ostr_sfor_invoice_item_adjustment_manual_distribution) | **POST** /v1/revenue-schedules/invoice-item-adjustments/{invoice-item-adj-key} | Create revenue schedule for Invoice Item Adjustment (manual distribution)
[**p_ostr_sfor_invoice_item_distribute_by_date_range**](RevenueSchedulesApi.md#p_ostr_sfor_invoice_item_distribute_by_date_range) | **POST** /v1/revenue-schedules/invoice-items/{invoice-item-id}/distribute-revenue-with-date-range | Create revenue schedule for Invoice Item (distribute by date range)
[**p_ostr_sfor_invoice_item_manual_distribution**](RevenueSchedulesApi.md#p_ostr_sfor_invoice_item_manual_distribution) | **POST** /v1/revenue-schedules/invoice-items/{invoice-item-id} | Create revenue schedule for Invoice Item (manual distribution)
[**p_ostr_sfor_subsc_charge**](RevenueSchedulesApi.md#p_ostr_sfor_subsc_charge) | **POST** /v1/revenue-schedules/subscription-charges/{charge-key} | Create revenue schedule on subscription charge
[**p_ut_revenue_across_ap**](RevenueSchedulesApi.md#p_ut_revenue_across_ap) | **PUT** /v1/revenue-schedules/{rs-number}/distribute-revenue-across-accounting-periods | Distribute revenue across accounting periods
[**p_ut_revenue_by_recognition_startand_end_dates**](RevenueSchedulesApi.md#p_ut_revenue_by_recognition_startand_end_dates) | **PUT** /v1/revenue-schedules/{rs-number}/distribute-revenue-with-date-range | Distribute revenue by recognition start and end dates
[**p_ut_revenue_specific_date**](RevenueSchedulesApi.md#p_ut_revenue_specific_date) | **PUT** /v1/revenue-schedules/{rs-number}/distribute-revenue-on-specific-date | Distribute revenue on specific date
[**p_utrs_basic_info**](RevenueSchedulesApi.md#p_utrs_basic_info) | **PUT** /v1/revenue-schedules/{rs-number}/basic-information | Update revenue schedule basic information

# **d_eleters**
> CommonResponseType d_eleters(rs_number, zuora_entity_ids=zuora_entity_ids)

Delete revenue schedule

Deletes a revenue schedule by specifying its revenue schedule number ## Prerequisites You must have the Delete Custom Revenue Schedule permissions in Zuora Finance. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
rs_number = 'rs_number_example' # str |  Revenue schedule number of the revenue schedule you want to delete, for example, RS-00000256. To be deleted, the revenue schedule: * Must be using a custom unlimited recognition rule. * Cannot have any revenue in a closed accounting period. * Cannot be included in a summary journal entry. * Cannot have a revenue schedule date in a closed accounting period. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete revenue schedule
    api_response = api_instance.d_eleters(rs_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->d_eleters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rs_number** | **str**|  Revenue schedule number of the revenue schedule you want to delete, for example, RS-00000256. To be deleted, the revenue schedule: * Must be using a custom unlimited recognition rule. * Cannot have any revenue in a closed accounting period. * Cannot be included in a summary journal entry. * Cannot have a revenue schedule date in a closed accounting period.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_etr_sby_credit_memo_item**
> GETRSDetailType g_etr_sby_credit_memo_item(cmi_id)

Get revenue schedule by credit memo item ID 

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the details about a revenue schedule by specifying a valid credit memo item ID. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
cmi_id = 'cmi_id_example' # str | The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems). 

try:
    # Get revenue schedule by credit memo item ID 
    api_response = api_instance.g_etr_sby_credit_memo_item(cmi_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->g_etr_sby_credit_memo_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmi_id** | **str**| The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  | 

### Return type

[**GETRSDetailType**](GETRSDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_etr_sby_debit_memo_item**
> GETRSDetailType g_etr_sby_debit_memo_item(dmi_id)

Get revenue schedule by debit memo item ID 

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the details about a revenue schedule by specifying a valid debit memo item ID. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
dmi_id = 'dmi_id_example' # str | The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems). 

try:
    # Get revenue schedule by debit memo item ID 
    api_response = api_instance.g_etr_sby_debit_memo_item(dmi_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->g_etr_sby_debit_memo_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dmi_id** | **str**| The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  | 

### Return type

[**GETRSDetailType**](GETRSDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_etr_sby_invoice_item**
> GETRSDetailType g_etr_sby_invoice_item(invoice_item_id, zuora_entity_ids=zuora_entity_ids)

Get revenue schedule by invoice item ID

Retrieves the details of a revenue schedule by specifying the invoice item ID. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
invoice_item_id = 'invoice_item_id_example' # str | A valid Invoice Item ID.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get revenue schedule by invoice item ID
    api_response = api_instance.g_etr_sby_invoice_item(invoice_item_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->g_etr_sby_invoice_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_item_id** | **str**| A valid Invoice Item ID. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRSDetailType**](GETRSDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_etr_sby_invoice_item_adjustment**
> GETRSDetailType g_etr_sby_invoice_item_adjustment(invoice_item_adj_key, zuora_entity_ids=zuora_entity_ids)

Get revenue schedule by invoice item adjustment

Retrieves the details of a revenue schedule by specifying a valid invoice item adjustment identifier. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
invoice_item_adj_key = 'invoice_item_adj_key_example' # str | ID of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get revenue schedule by invoice item adjustment
    api_response = api_instance.g_etr_sby_invoice_item_adjustment(invoice_item_adj_key, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->g_etr_sby_invoice_item_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_item_adj_key** | **str**| ID of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRSDetailType**](GETRSDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_etr_sby_product_charge_and_billing_account**
> GETRSDetailsByProductChargeType g_etr_sby_product_charge_and_billing_account(account_key, charge_key, page_size=page_size)

Get all revenue schedules of product charge by charge ID and billing account ID 

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the details about all revenue schedules of a product rate plan charge by specifying the charge ID and billing account ID. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
account_key = 'account_key_example' # str | The account number or account ID. 
charge_key = 'charge_key_example' # str | The unique ID of a product rate plan charge. For example, 8a8082e65ba86084015bb323d3c61d82. 
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get all revenue schedules of product charge by charge ID and billing account ID 
    api_response = api_instance.g_etr_sby_product_charge_and_billing_account(account_key, charge_key, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->g_etr_sby_product_charge_and_billing_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_key** | **str**| The account number or account ID.  | 
 **charge_key** | **str**| The unique ID of a product rate plan charge. For example, 8a8082e65ba86084015bb323d3c61d82.  | 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GETRSDetailsByProductChargeType**](GETRSDetailsByProductChargeType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_etr_sfor_subsc_charge**
> GETRSDetailsByChargeType g_etr_sfor_subsc_charge(charge_key, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get revenue schedule by subscription charge

Retrieves the revenue schedule details by specifying subscription charge ID. Request and response field descriptions and sample code are provided 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
charge_key = 'charge_key_example' # str | ID of the subscription rate plan charge; for example, 402892793e173340013e173b81000012.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get revenue schedule by subscription charge
    api_response = api_instance.g_etr_sfor_subsc_charge(charge_key, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->g_etr_sfor_subsc_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_key** | **str**| ID of the subscription rate plan charge; for example, 402892793e173340013e173b81000012. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GETRSDetailsByChargeType**](GETRSDetailsByChargeType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_etrs**
> GETRSDetailType g_etrs(rs_number, zuora_entity_ids=zuora_entity_ids)

Get revenue schedule details

Retrieves the details of a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
rs_number = 'rs_number_example' # str | Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\". 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get revenue schedule details
    api_response = api_instance.g_etrs(rs_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->g_etrs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rs_number** | **str**| Revenue schedule number. The revenue schedule number is always prefixed with \&quot;RS\&quot;, for example, \&quot;RS-00000001\&quot;.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRSDetailType**](GETRSDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ostr_sfor_credit_memo_item_distribute_by_date_range**
> POSTRevenueScheduleByTransactionResponseType p_ostr_sfor_credit_memo_item_distribute_by_date_range(body, cmi_id)

Create revenue schedule for credit memo item (distribute by date range) 

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a credit memo item, and automatically distribute the revenue by specifying the recognition start and end dates. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
cmi_id = 'cmi_id_example' # str | The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems). 

try:
    # Create revenue schedule for credit memo item (distribute by date range) 
    api_response = api_instance.p_ostr_sfor_credit_memo_item_distribute_by_date_range(body, cmi_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ostr_sfor_credit_memo_item_distribute_by_date_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **cmi_id** | **str**| The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  | 

### Return type

[**POSTRevenueScheduleByTransactionResponseType**](POSTRevenueScheduleByTransactionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ostr_sfor_credit_memo_item_manual_distribution**
> POSTRevenueScheduleByTransactionResponseType p_ostr_sfor_credit_memo_item_manual_distribution(body, cmi_id)

Create revenue schedule for credit memo item (manual distribution) 

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a credit memo item, and manually distribute the revenue. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
cmi_id = 'cmi_id_example' # str | The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems). 

try:
    # Create revenue schedule for credit memo item (manual distribution) 
    api_response = api_instance.p_ostr_sfor_credit_memo_item_manual_distribution(body, cmi_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ostr_sfor_credit_memo_item_manual_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **cmi_id** | **str**| The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  | 

### Return type

[**POSTRevenueScheduleByTransactionResponseType**](POSTRevenueScheduleByTransactionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ostr_sfor_debit_memo_item_distribute_by_date_range**
> POSTRevenueScheduleByTransactionResponseType p_ostr_sfor_debit_memo_item_distribute_by_date_range(body, dmi_id)

Create revenue schedule for debit memo item (distribute by date range) 

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a debit memo item, and automatically distribute the revenue by specifying the recognition start and end dates. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
dmi_id = 'dmi_id_example' # str | The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems). 

try:
    # Create revenue schedule for debit memo item (distribute by date range) 
    api_response = api_instance.p_ostr_sfor_debit_memo_item_distribute_by_date_range(body, dmi_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ostr_sfor_debit_memo_item_distribute_by_date_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **dmi_id** | **str**| The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  | 

### Return type

[**POSTRevenueScheduleByTransactionResponseType**](POSTRevenueScheduleByTransactionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ostr_sfor_debit_memo_item_manual_distribution**
> POSTRevenueScheduleByTransactionResponseType p_ostr_sfor_debit_memo_item_manual_distribution(body, dmi_id)

Create revenue schedule for debit memo item (manual distribution) 

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a revenue schedule for a debit memo item, and manually distribute the revenue. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
dmi_id = 'dmi_id_example' # str | The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems). 

try:
    # Create revenue schedule for debit memo item (manual distribution) 
    api_response = api_instance.p_ostr_sfor_debit_memo_item_manual_distribution(body, dmi_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ostr_sfor_debit_memo_item_manual_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **dmi_id** | **str**| The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  | 

### Return type

[**POSTRevenueScheduleByTransactionResponseType**](POSTRevenueScheduleByTransactionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range**
> POSTRevenueScheduleByTransactionResponseType p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range(body, invoice_item_adj_key, zuora_entity_ids=zuora_entity_ids)

Create revenue schedule for Invoice Item Adjustment (distribute by date range)

Creates a revenue schedule for an Invoice Item Adjustment and distribute the revenue by specifying the recognition start and end dates. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
invoice_item_adj_key = 'invoice_item_adj_key_example' # str | ID or number of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72. If the specified Invoice Item Adjustment is already associated with a revenue schedule, the call will fail. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create revenue schedule for Invoice Item Adjustment (distribute by date range)
    api_response = api_instance.p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range(body, invoice_item_adj_key, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **invoice_item_adj_key** | **str**| ID or number of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72. If the specified Invoice Item Adjustment is already associated with a revenue schedule, the call will fail.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTRevenueScheduleByTransactionResponseType**](POSTRevenueScheduleByTransactionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ostr_sfor_invoice_item_adjustment_manual_distribution**
> POSTRevenueScheduleByTransactionResponseType p_ostr_sfor_invoice_item_adjustment_manual_distribution(body, invoice_item_adj_key, zuora_entity_ids=zuora_entity_ids)

Create revenue schedule for Invoice Item Adjustment (manual distribution)

Creates a revenue schedule for an Invoice Item Adjustment and manually distribute the revenue. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
invoice_item_adj_key = 'invoice_item_adj_key_example' # str | ID or number of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72. If the specified Invoice Item Adjustment is already associated with a revenue schedule, the call will fail. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create revenue schedule for Invoice Item Adjustment (manual distribution)
    api_response = api_instance.p_ostr_sfor_invoice_item_adjustment_manual_distribution(body, invoice_item_adj_key, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ostr_sfor_invoice_item_adjustment_manual_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **invoice_item_adj_key** | **str**| ID or number of the Invoice Item Adjustment, for example, e20b07fd416dcfcf0141c81164fd0a72. If the specified Invoice Item Adjustment is already associated with a revenue schedule, the call will fail.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTRevenueScheduleByTransactionResponseType**](POSTRevenueScheduleByTransactionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ostr_sfor_invoice_item_distribute_by_date_range**
> POSTRevenueScheduleByTransactionResponseType p_ostr_sfor_invoice_item_distribute_by_date_range(body, invoice_item_id, zuora_entity_ids=zuora_entity_ids)

Create revenue schedule for Invoice Item (distribute by date range)

Creates a revenue schedule for an Invoice Item and distribute the revenue by specifying the recognition start and end dates. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
invoice_item_id = 'invoice_item_id_example' # str | ID of the Invoice Item, for example, e20b07fd416dcfcf0141c81164fd0a75. If the specified Invoice Item is already associated with a revenue schedule, the call will fail. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create revenue schedule for Invoice Item (distribute by date range)
    api_response = api_instance.p_ostr_sfor_invoice_item_distribute_by_date_range(body, invoice_item_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ostr_sfor_invoice_item_distribute_by_date_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **invoice_item_id** | **str**| ID of the Invoice Item, for example, e20b07fd416dcfcf0141c81164fd0a75. If the specified Invoice Item is already associated with a revenue schedule, the call will fail.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTRevenueScheduleByTransactionResponseType**](POSTRevenueScheduleByTransactionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ostr_sfor_invoice_item_manual_distribution**
> POSTRevenueScheduleByTransactionResponseType p_ostr_sfor_invoice_item_manual_distribution(body, invoice_item_id, zuora_entity_ids=zuora_entity_ids)

Create revenue schedule for Invoice Item (manual distribution)

Creates a revenue schedule for an Invoice Item and manually distribute the revenue. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
invoice_item_id = 'invoice_item_id_example' # str | ID of the Invoice Item, for example, e20b07fd416dcfcf0141c81164fd0a75. If the specified Invoice Item is already associated with a revenue schedule, the call will fail. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create revenue schedule for Invoice Item (manual distribution)
    api_response = api_instance.p_ostr_sfor_invoice_item_manual_distribution(body, invoice_item_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ostr_sfor_invoice_item_manual_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **invoice_item_id** | **str**| ID of the Invoice Item, for example, e20b07fd416dcfcf0141c81164fd0a75. If the specified Invoice Item is already associated with a revenue schedule, the call will fail.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTRevenueScheduleByTransactionResponseType**](POSTRevenueScheduleByTransactionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ostr_sfor_subsc_charge**
> POSTRevenueScheduleByChargeResponseType p_ostr_sfor_subsc_charge(body, charge_key, zuora_entity_ids=zuora_entity_ids)

Create revenue schedule on subscription charge

Creates a revenue schedule by specifying the subscription charge. This method is for custom unlimited revenue recognition only. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
charge_key = 'charge_key_example' # str | ID of the subscription rate plan charge; for example, 402892793e173340013e173b81000012.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create revenue schedule on subscription charge
    api_response = api_instance.p_ostr_sfor_subsc_charge(body, charge_key, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ostr_sfor_subsc_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **charge_key** | **str**| ID of the subscription rate plan charge; for example, 402892793e173340013e173b81000012. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTRevenueScheduleByChargeResponseType**](POSTRevenueScheduleByChargeResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_revenue_across_ap**
> PUTRevenueScheduleResponseType p_ut_revenue_across_ap(body, rs_number, zuora_entity_ids=zuora_entity_ids)

Distribute revenue across accounting periods

Distributes revenue by specifying the revenue schedule number. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
rs_number = 'rs_number_example' # str | Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\". 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Distribute revenue across accounting periods
    api_response = api_instance.p_ut_revenue_across_ap(body, rs_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ut_revenue_across_ap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **rs_number** | **str**| Revenue schedule number. The revenue schedule number is always prefixed with \&quot;RS\&quot;, for example, \&quot;RS-00000001\&quot;.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**PUTRevenueScheduleResponseType**](PUTRevenueScheduleResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_revenue_by_recognition_startand_end_dates**
> PUTRevenueScheduleResponseType p_ut_revenue_by_recognition_startand_end_dates(body, rs_number, zuora_entity_ids=zuora_entity_ids)

Distribute revenue by recognition start and end dates

Distributes revenue by specifying the recognition start and end dates. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
rs_number = 'rs_number_example' # str | Revenue schedule number. Specify the revenue schedule whose revenue you want to distribute.    The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\". 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Distribute revenue by recognition start and end dates
    api_response = api_instance.p_ut_revenue_by_recognition_startand_end_dates(body, rs_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ut_revenue_by_recognition_startand_end_dates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **rs_number** | **str**| Revenue schedule number. Specify the revenue schedule whose revenue you want to distribute.    The revenue schedule number is always prefixed with \&quot;RS\&quot;, for example, \&quot;RS-00000001\&quot;.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**PUTRevenueScheduleResponseType**](PUTRevenueScheduleResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_revenue_specific_date**
> PUTRevenueScheduleResponseType p_ut_revenue_specific_date(body, rs_number, zuora_entity_ids=zuora_entity_ids)

Distribute revenue on specific date

Distributes revenue on a specific recognition date. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
rs_number = 'rs_number_example' # str | Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\". 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Distribute revenue on specific date
    api_response = api_instance.p_ut_revenue_specific_date(body, rs_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_ut_revenue_specific_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **rs_number** | **str**| Revenue schedule number. The revenue schedule number is always prefixed with \&quot;RS\&quot;, for example, \&quot;RS-00000001\&quot;.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**PUTRevenueScheduleResponseType**](PUTRevenueScheduleResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_utrs_basic_info**
> CommonResponseType p_utrs_basic_info(body, rs_number, zuora_entity_ids=zuora_entity_ids)

Update revenue schedule basic information

Retrieves basic information of a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RevenueSchedulesApi()
body = zuora_client.Object() # Object | 
rs_number = 'rs_number_example' # str | Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\". 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update revenue schedule basic information
    api_response = api_instance.p_utrs_basic_info(body, rs_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevenueSchedulesApi->p_utrs_basic_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **rs_number** | **str**| Revenue schedule number. The revenue schedule number is always prefixed with \&quot;RS\&quot;, for example, \&quot;RS-00000001\&quot;.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

