# swagger_client.OrdersApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_order**](OrdersApi.md#d_elete_order) | **DELETE** /v1/orders/{orderNumber} | Delete order
[**g_et_all_orders**](OrdersApi.md#g_et_all_orders) | **GET** /v1/orders | Get all orders
[**g_et_breakdown_invoice_by_order**](OrdersApi.md#g_et_breakdown_invoice_by_order) | **GET** /v1/invoices/{invoiceNumber}/amountBreakdownByOrder | Get breakdown of invoice by order
[**g_et_job_status_and_response**](OrdersApi.md#g_et_job_status_and_response) | **GET** /async-jobs/{jobId} | Get job status and response
[**g_et_order**](OrdersApi.md#g_et_order) | **GET** /v1/orders/{orderNumber} | Get an order
[**g_et_order_billing_info**](OrdersApi.md#g_et_order_billing_info) | **GET** /v1/orders/{orderNumber}/billingInfo | Get billing information for order
[**g_et_order_metricsfor_evergreen_subscription**](OrdersApi.md#g_et_order_metricsfor_evergreen_subscription) | **GET** /v1/orders/{orderNumber}/evergreenMetrics/{subscriptionNumber} | Get order metrics for evergreen subscription
[**g_et_order_rated_result**](OrdersApi.md#g_et_order_rated_result) | **GET** /v1/orders/{orderNumber}/ratedResults | Get rated result for order
[**g_et_orders_by_invoice_owner**](OrdersApi.md#g_et_orders_by_invoice_owner) | **GET** /v1/orders/invoiceOwner/{accountNumber} | Get orders by invoice owner
[**g_et_orders_by_subscription_number**](OrdersApi.md#g_et_orders_by_subscription_number) | **GET** /v1/orders/subscription/{subscriptionNumber} | Get orders by subscription number
[**g_et_orders_by_subscription_owner**](OrdersApi.md#g_et_orders_by_subscription_owner) | **GET** /v1/orders/subscriptionOwner/{accountNumber} | Get orders by subscription owner
[**g_et_subscription_term_info**](OrdersApi.md#g_et_subscription_term_info) | **GET** /v1/orders/term/{subscriptionNumber} | Get term information for subscription
[**p_ost_create_order_asynchronously**](OrdersApi.md#p_ost_create_order_asynchronously) | **POST** /async/orders | Create order asynchronously
[**p_ost_order**](OrdersApi.md#p_ost_order) | **POST** /v1/orders | Create order
[**p_ost_preview_order**](OrdersApi.md#p_ost_preview_order) | **POST** /v1/orders/preview | Preview order
[**p_ost_preview_order_asynchronously**](OrdersApi.md#p_ost_preview_order_asynchronously) | **POST** /async/orders/preview | Preview order asynchronously
[**p_ost_request_breakdown_invoice_items_by_order**](OrdersApi.md#p_ost_request_breakdown_invoice_items_by_order) | **POST** /v1/invoices/items/amountBreakdownByOrder | Request breakdown of invoice items by order
[**p_ut_order_trigger_dates**](OrdersApi.md#p_ut_order_trigger_dates) | **PUT** /v1/orders/{orderNumber}/triggerDates | Update order action trigger dates
[**p_ut_update_order_custom_fields**](OrdersApi.md#p_ut_update_order_custom_fields) | **PUT** /v1/orders/{orderNumber}/customFields | Update order custom fields
[**p_ut_update_subscription_custom_fields**](OrdersApi.md#p_ut_update_subscription_custom_fields) | **PUT** /v1/subscriptions/{subscriptionNumber}/customFields | Update subscription custom fields

# **d_elete_order**
> CommonResponseType d_elete_order(order_number, zuora_entity_ids=zuora_entity_ids)

Delete order

**Note:** This operation is only available if you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled. The migration to Orders is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.    Deletes a specified order. All the subscriptions changed by this order are deleted. After the deletion, the subscriptions are rolled back to the previous version.   You are not allowed to delete an order if the charges that are affected by this order are invoiced. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
order_number = 'order_number_example' # str | The number of the order to be deleted.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete order
    api_response = api_instance.d_elete_order(order_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->d_elete_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_number** | **str**| The number of the order to be deleted. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_all_orders**
> GetAllOrdersResponseType g_et_all_orders(zuora_entity_ids=zuora_entity_ids, page=page, page_size=page_size, date_filter_option=date_filter_option, start_date=start_date, end_date=end_date)

Get all orders

**Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. The migration to Order Metrics is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. If you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders) feature enabled, you already have the Order Metrics feature enabled.   Retrieves information about all orders in your tenant. By default, it returns the first page of the orders.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page = 56 # int | The page number of the orders retrieved.   (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
date_filter_option = 'date_filter_option_example' # str | The date type to filter on. This field value can be orderDate or updatedDate. Default is orderDate.  (optional)
start_date = '2013-10-20' # date | The result will only contain the orders with the date of dateFilterOption later than or equal to this date.  (optional)
end_date = '2013-10-20' # date | The result will only contains orders with the date of dateFilterOption earlier than or equal to this date.  (optional)

try:
    # Get all orders
    api_response = api_instance.g_et_all_orders(zuora_entity_ids=zuora_entity_ids, page=page, page_size=page_size, date_filter_option=date_filter_option, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->g_et_all_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page** | **int**| The page number of the orders retrieved.   | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **date_filter_option** | **str**| The date type to filter on. This field value can be orderDate or updatedDate. Default is orderDate.  | [optional] 
 **start_date** | **date**| The result will only contain the orders with the date of dateFilterOption later than or equal to this date.  | [optional] 
 **end_date** | **date**| The result will only contains orders with the date of dateFilterOption earlier than or equal to this date.  | [optional] 

### Return type

[**GetAllOrdersResponseType**](GetAllOrdersResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_breakdown_invoice_by_order**
> GetInvoiceAmountBreakdownByOrderResponse g_et_breakdown_invoice_by_order(invoice_number, zuora_entity_ids=zuora_entity_ids)

Get breakdown of invoice by order

**Note:** This feature is in Limited Availability.   Retrieves a specified invoice that is broken down by orders. One invoice item might be broken down into a list of order related items.  ### Phantom Invoice Item  Phantom invoice items are generated via this API operation if an invoice item has a credit back scenario and the action you are making is prior to the end of a previous action.  Phantom invoice items are not real invoice items and have no impact to billing. They are generated in parallel with the real invoice item and are used to properly allocate invoice items to the relevant orders. They share the same invoice item id with the real invoice item but with a prefix of \"Phantom-\". Also, the amount of a phantom invoice item is always zero.  Below is an example phantom invoice item, which reflects in the period of 2017-10-01 to 2017-12-31: * Order 1 creates the initial subscription with an invoice breakdown amount of \"3000\". * Order 2 decreases the product quantity and so reduces the amount by \"1500\". * Order 3 cancels the subscription and so reduces the remaining amount by \"1500\".  ``` {   \"invoiceItemId\": \"Phantom-2c98903063f6d7b1016416df98c721b6\",   \"subscriptionNumber\": \"55073a2fc6eb462aac0422aad7657f3c\",   \"chargeNumber\": \"d-000001\",   \"applyToChargeNumber\": null,   \"startDate\": \"2017-10-01\",   \"endDate\": \"2017-12-31\",   \"amount\": 0,   \"isCredit\": true,   \"breakdownDetails\": [     {       \"orderNumber\": \"980c4a4d414644339c113c7919a49fc2\",       \"amount\": -1500,       \"termNumber\": 1,       \"startDate\": \"2017-10-01\",       \"endDate\": \"2017-12-31\",       \"orderItemId\": \"2c98903063f6d7b1016416df8c512147\",       \"generatedReason\": \"Contraction\",       \"orderActionId\": \"2c98903063f6d7b1016416df9738219b\"     },     {       \"orderNumber\": \"e0a839e8b33d476b9a86ca50e71ccbb4\",       \"amount\": -1500,       \"termNumber\": 1,       \"startDate\": \"2017-10-01\",       \"endDate\": \"2017-12-31\",       \"orderItemId\": \"2c98903063f6d7b1016416df8c512147\",       \"generatedReason\": \"DecreaseQuantity\",       \"orderActionId\": \"2c98903063f6d7b1016416df92242167\"     },     {       \"orderNumber\": \"fd0e377b1bca4cc4805fc4cf1be72e05\",       \"amount\": 3000,       \"termNumber\": 1,       \"startDate\": \"2017-10-01\",       \"endDate\": \"2017-12-31\",       \"orderItemId\": \"2c98903063f6d7b1016416df8c512147\",       \"generatedReason\": \"Extension\",       \"orderActionId\": \"2c98903063f6d7b1016416df8bb12136\"     }   ] } ``` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
invoice_number = 'invoice_number_example' # str | Number of invoice to be broken down.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get breakdown of invoice by order
    api_response = api_instance.g_et_breakdown_invoice_by_order(invoice_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->g_et_breakdown_invoice_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_number** | **str**| Number of invoice to be broken down. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GetInvoiceAmountBreakdownByOrderResponse**](GetInvoiceAmountBreakdownByOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_job_status_and_response**
> object g_et_job_status_and_response(job_id)

Get job status and response

**Note:** This operation is only available if you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled. This operation is in **Limited Availability**.   Get the status and response of an asynchronous job. Currently, an asynchronous job created by \"Create order asynchronously\" or \"Preview order asynchronously\" is supported. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
job_id = 'job_id_example' # str | UUID of the asynchronous job created by an asynchronous API operation.

try:
    # Get job status and response
    api_response = api_instance.g_et_job_status_and_response(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->g_et_job_status_and_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| UUID of the asynchronous job created by an asynchronous API operation. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_order**
> GetOrderResponse g_et_order(order_number, zuora_entity_ids=zuora_entity_ids)

Get an order

**Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. The migration to Order Metrics is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. If you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders) feature enabled, you already have the Order Metrics feature enabled.   Retrieves the detailed information about a specified order. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
order_number = 'order_number_example' # str | The order number to be retrieved.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get an order
    api_response = api_instance.g_et_order(order_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->g_et_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_number** | **str**| The order number to be retrieved. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GetOrderResponse**](GetOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_order_billing_info**
> GetOrderBillingInfoResponseType g_et_order_billing_info(order_number, zuora_entity_ids=zuora_entity_ids, as_of_date=as_of_date)

Get billing information for order

**Note:** This feature is in Limited Availability.  Retrieves the billing information about a specified order. The information includes the billed and unbilled amount of the order. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
order_number = 'order_number_example' # str | The order number.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
as_of_date = '2013-10-20' # date | Billing states of the order will be calculated as of this date. Invoices with the invoice date later than this date will not be counted into the billed amount. The default value is today. (optional)

try:
    # Get billing information for order
    api_response = api_instance.g_et_order_billing_info(order_number, zuora_entity_ids=zuora_entity_ids, as_of_date=as_of_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->g_et_order_billing_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_number** | **str**| The order number. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **as_of_date** | **date**| Billing states of the order will be calculated as of this date. Invoices with the invoice date later than this date will not be counted into the billed amount. The default value is today. | [optional] 

### Return type

[**GetOrderBillingInfoResponseType**](GetOrderBillingInfoResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_order_metricsfor_evergreen_subscription**
> GetOrderResponseForEvergreen g_et_order_metricsfor_evergreen_subscription(order_number, subscription_number, start_date, end_date, zuora_entity_ids=zuora_entity_ids)

Get order metrics for evergreen subscription

**Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. The migration to Order Metrics is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. If you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders) feature enabled, you already have the Order Metrics feature enabled.   Retrieves the metrics of an evergreen subscription in a specified order. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
order_number = 'order_number_example' # str | The order number. 
subscription_number = 'subscription_number_example' # str | The subscription number you want to get the metrics for. 
start_date = '2013-10-20' # date | The start date of the date range for which you want to get the metrics. The date must be in yyyy-mm-dd format. For example, 2017-12-03. 
end_date = '2013-10-20' # date | The end date of the date range for which you want to get the metrics. The date must be in yyyy-mm-dd format. For example, 2017-12-03. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get order metrics for evergreen subscription
    api_response = api_instance.g_et_order_metricsfor_evergreen_subscription(order_number, subscription_number, start_date, end_date, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->g_et_order_metricsfor_evergreen_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_number** | **str**| The order number.  | 
 **subscription_number** | **str**| The subscription number you want to get the metrics for.  | 
 **start_date** | **date**| The start date of the date range for which you want to get the metrics. The date must be in yyyy-mm-dd format. For example, 2017-12-03.  | 
 **end_date** | **date**| The end date of the date range for which you want to get the metrics. The date must be in yyyy-mm-dd format. For example, 2017-12-03.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GetOrderResponseForEvergreen**](GetOrderResponseForEvergreen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_order_rated_result**
> GetOrderRatedResultResponseType g_et_order_rated_result(order_number, zuora_entity_ids=zuora_entity_ids)

Get rated result for order

**Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. The migration to Order Metrics is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. If you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders) feature enabled, you already have the Order Metrics feature enabled.  Retrieves the rated results of all the subscriptions in the specified order. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
order_number = 'order_number_example' # str | The order number.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get rated result for order
    api_response = api_instance.g_et_order_rated_result(order_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->g_et_order_rated_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_number** | **str**| The order number. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GetOrderRatedResultResponseType**](GetOrderRatedResultResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_orders_by_invoice_owner**
> GetOrdersResponse g_et_orders_by_invoice_owner(account_number, zuora_entity_ids=zuora_entity_ids, page=page, page_size=page_size, date_filter_option=date_filter_option, start_date=start_date, end_date=end_date)

Get orders by invoice owner

**Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. The migration to Order Metrics is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. If you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders) feature enabled, you already have the Order Metrics feature enabled.  Retrieves the detailed information about all orders for a specified invoice owner. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
account_number = 'account_number_example' # str | The invoice owner account number.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page = 56 # int | The page number of the orders retrieved. The default is 1.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
date_filter_option = 'date_filter_option_example' # str | The date type to filter on. This field value can be orderDate or updatedDate. Default is orderDate.  (optional)
start_date = '2013-10-20' # date | The result will only contain the orders with the date of dateFilterOption later than or equal to this date.  (optional)
end_date = '2013-10-20' # date | The result will only contain the orders with the date of dateFilterOption earlier than or equal to this date.  (optional)

try:
    # Get orders by invoice owner
    api_response = api_instance.g_et_orders_by_invoice_owner(account_number, zuora_entity_ids=zuora_entity_ids, page=page, page_size=page_size, date_filter_option=date_filter_option, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->g_et_orders_by_invoice_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The invoice owner account number. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page** | **int**| The page number of the orders retrieved. The default is 1.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **date_filter_option** | **str**| The date type to filter on. This field value can be orderDate or updatedDate. Default is orderDate.  | [optional] 
 **start_date** | **date**| The result will only contain the orders with the date of dateFilterOption later than or equal to this date.  | [optional] 
 **end_date** | **date**| The result will only contain the orders with the date of dateFilterOption earlier than or equal to this date.  | [optional] 

### Return type

[**GetOrdersResponse**](GetOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_orders_by_subscription_number**
> GetOrdersResponse g_et_orders_by_subscription_number(subscription_number, zuora_entity_ids=zuora_entity_ids, page=page, page_size=page_size, date_filter_option=date_filter_option, start_date=start_date, end_date=end_date)

Get orders by subscription number

**Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. The migration to Order Metrics is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. If you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders) feature enabled, you already have the Order Metrics feature enabled.  Retrieves the detailed information about all orders for a specified subscription. Any orders containing the changes on the specified subscription are returned. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
subscription_number = 'subscription_number_example' # str | The subscription number.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page = 56 # int | The page number of the orders retrieved. The default is '1'.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
date_filter_option = 'date_filter_option_example' # str | The date type to filter on. This field value can be 'orderDate' or 'updatedDate'. Default is orderDate.  (optional)
start_date = '2013-10-20' # date | The result will only contain the orders with the date of 'dateFilterOption' later than or equal to this date.  (optional)
end_date = '2013-10-20' # date | The result will only contain the orders with the date of 'dateFilterOption' earlier than or equal to this date.  (optional)

try:
    # Get orders by subscription number
    api_response = api_instance.g_et_orders_by_subscription_number(subscription_number, zuora_entity_ids=zuora_entity_ids, page=page, page_size=page_size, date_filter_option=date_filter_option, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->g_et_orders_by_subscription_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_number** | **str**| The subscription number. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page** | **int**| The page number of the orders retrieved. The default is &#x27;1&#x27;.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **date_filter_option** | **str**| The date type to filter on. This field value can be &#x27;orderDate&#x27; or &#x27;updatedDate&#x27;. Default is orderDate.  | [optional] 
 **start_date** | **date**| The result will only contain the orders with the date of &#x27;dateFilterOption&#x27; later than or equal to this date.  | [optional] 
 **end_date** | **date**| The result will only contain the orders with the date of &#x27;dateFilterOption&#x27; earlier than or equal to this date.  | [optional] 

### Return type

[**GetOrdersResponse**](GetOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_orders_by_subscription_owner**
> GetOrdersResponse g_et_orders_by_subscription_owner(account_number, zuora_entity_ids=zuora_entity_ids, page=page, page_size=page_size, date_filter_option=date_filter_option, start_date=start_date, end_date=end_date)

Get orders by subscription owner

**Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. The migration to Order Metrics is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. If you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders) feature enabled, you already have the Order Metrics feature enabled.  Retrieves the detailed information about all orders for a specified subscription owner. Any orders containing the changes on the subscriptions owned by this account are returned. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
account_number = 'account_number_example' # str | The subscription owner account number.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page = 56 # int | The page number of the orders retrieved. The default is 1.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
date_filter_option = 'date_filter_option_example' # str | The date type to filter on. This field value can be 'orderDate' or 'updatedDate'. Default is orderDate.  (optional)
start_date = '2013-10-20' # date | The result will only contain the orders with the date of 'dateFilterOption' later than or equal to this date.  (optional)
end_date = '2013-10-20' # date | The result will only contain the orders with the date of 'dateFilterOption' earlier than or equal to this date.  (optional)

try:
    # Get orders by subscription owner
    api_response = api_instance.g_et_orders_by_subscription_owner(account_number, zuora_entity_ids=zuora_entity_ids, page=page, page_size=page_size, date_filter_option=date_filter_option, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->g_et_orders_by_subscription_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| The subscription owner account number. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page** | **int**| The page number of the orders retrieved. The default is 1.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **date_filter_option** | **str**| The date type to filter on. This field value can be &#x27;orderDate&#x27; or &#x27;updatedDate&#x27;. Default is orderDate.  | [optional] 
 **start_date** | **date**| The result will only contain the orders with the date of &#x27;dateFilterOption&#x27; later than or equal to this date.  | [optional] 
 **end_date** | **date**| The result will only contain the orders with the date of &#x27;dateFilterOption&#x27; earlier than or equal to this date.  | [optional] 

### Return type

[**GetOrdersResponse**](GetOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_subscription_term_info**
> GetSubscriptionTermInfoResponseType g_et_subscription_term_info(subscription_number, zuora_entity_ids=zuora_entity_ids, version=version, page=page, page_size=page_size)

Get term information for subscription

**Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. The migration to Order Metrics is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. If you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders) feature enabled, you already have the Order Metrics feature enabled.  Retrieves the terms of the specified subscription. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
subscription_number = 'subscription_number_example' # str | The number of the subscription to retrieve terms for. For example, A-S00000001. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
version = 56 # int | The version of the subscription to retrieve terms for. If you do not specify this parameter, Zuora returns the terms for the latest version of the subscription.  (optional)
page = 56 # int | The page number of the terms retrieved.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get term information for subscription
    api_response = api_instance.g_et_subscription_term_info(subscription_number, zuora_entity_ids=zuora_entity_ids, version=version, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->g_et_subscription_term_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_number** | **str**| The number of the subscription to retrieve terms for. For example, A-S00000001.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **version** | **int**| The version of the subscription to retrieve terms for. If you do not specify this parameter, Zuora returns the terms for the latest version of the subscription.  | [optional] 
 **page** | **int**| The page number of the terms retrieved.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GetSubscriptionTermInfoResponseType**](GetSubscriptionTermInfoResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_create_order_asynchronously**
> object p_ost_create_order_asynchronously(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Create order asynchronously

**Note:** This operation is only available if you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled. This operation is in **Limited Availability**.   In the case where a normal \"Create order\" operation call will time out, use this operation instead to create an order asynchronously. A job will be creating the order in the back end; the job ID will be returned for tracking the job status and result.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
body = swagger_client.POSTOrderRequestType() # POSTOrderRequestType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str |  The minor version of the Zuora REST API.   You need to set this parameter if you use the following fields: * subscriptions * subscriptionNumbers  (optional)

try:
    # Create order asynchronously
    api_response = api_instance.p_ost_create_order_asynchronously(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->p_ost_create_order_asynchronously: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTOrderRequestType**](POSTOrderRequestType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**|  The minor version of the Zuora REST API.   You need to set this parameter if you use the following fields: * subscriptions * subscriptionNumbers  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_order**
> PostOrderResponseType p_ost_order(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Create order

**Note:** This operation is only available if you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled. The migration to Orders is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.   You can use this operation to create subscriptions and make changes to subscriptions by creating orders. The following tutorials demonstrate how to use this operation:   * [Add a Product to a Subscription](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/A_Add_a_Product_to_a_Subscription)  * [Create a Ramp Deal](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/A_Create_a_Ramp_Deal)  * [Create a Subscription](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/A_Create_a_Subscription)  * [Change the Owner of a Subscription](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/C_Change_the_Owner_of_a_Subscription)  * [Change the Terms and Conditions of a Subscription](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/C_Change_the_Terms_and_Conditions_of_a_Subscription)  * [Renew a Subscription](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/C_Renew_a_Subscription)  * [Renew a Subscription and Upgrade a Product](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/C_Renew_a_Subscription_and_Upgrade_a_Product)  * [Replace a Product in a Subscription](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/C_Replace_a_Product_in_a_Subscription)  * [Update a Product in a Subscription](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/C_Update_a_Product_in_a_Subscription)  * [Cancel a Subscription](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/D_Cancel_a_Subscription)  * [Remove a Product from a Subscription](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/D_Remove_a_Product_from_a_Subscription)  To return the IDs associated with the numbers returned in the Create Order operation, use `?returnIds=true` at the end of the operation's endpoint.  Creating a draft order is currently not supported. See [Known Limitations in Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/C_Known_Limitations_in_Orders) for additional limitations.  **Note:** When you are to suspend a subcription (via the `suspend` order action), if in the same \"Create order\" call you are to perform other subsequent order actions on the supscription to suspend, you must first resume the subscription (via a `resume` order action).   **Note:** When using this operation to create an account, create a subscription, run billing, and collect payment in a single call, if the payment processing fails then all the other steps will be rolled back. This means that the invoice will not be generated, the subscription will not be created, and the account will not be created. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
body = swagger_client.POSTOrderRequestType() # POSTOrderRequestType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str |  The minor version of the Zuora REST API.   You need to set this parameter if you use the following fields: * subscriptions * subscriptionNumbers  (optional)

try:
    # Create order
    api_response = api_instance.p_ost_order(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->p_ost_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTOrderRequestType**](POSTOrderRequestType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**|  The minor version of the Zuora REST API.   You need to set this parameter if you use the following fields: * subscriptions * subscriptionNumbers  | [optional] 

### Return type

[**PostOrderResponseType**](PostOrderResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_preview_order**
> PostOrderPreviewResponseType p_ost_preview_order(body, zuora_entity_ids=zuora_entity_ids)

Preview order

**Note:** This operation is only available if you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled. The migration to Orders is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.    Retrieves the preview of the charge metrics and invoice items of a specified order. This operation is only an order preview and no order is created. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
body = swagger_client.POSTOrderPreviewRequestType() # POSTOrderPreviewRequestType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Preview order
    api_response = api_instance.p_ost_preview_order(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->p_ost_preview_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTOrderPreviewRequestType**](POSTOrderPreviewRequestType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**PostOrderPreviewResponseType**](PostOrderPreviewResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_preview_order_asynchronously**
> object p_ost_preview_order_asynchronously(body, zuora_entity_ids=zuora_entity_ids)

Preview order asynchronously

**Note:** This operation is only available if you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled. This operation is in **Limited Availability**.    In the case where a normal \"Preview order\" operation call will time out, use this operation instead to preview an order asynchronously. A job will be previewing the order in the back end; the job ID will be returned for tracking the job status and result. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
body = swagger_client.POSTOrderPreviewRequestType() # POSTOrderPreviewRequestType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Preview order asynchronously
    api_response = api_instance.p_ost_preview_order_asynchronously(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->p_ost_preview_order_asynchronously: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTOrderPreviewRequestType**](POSTOrderPreviewRequestType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_request_breakdown_invoice_items_by_order**
> GetInvoiceAmountBreakdownByOrderResponse p_ost_request_breakdown_invoice_items_by_order(body, zuora_entity_ids=zuora_entity_ids)

Request breakdown of invoice items by order

**Note:** This feature is in Limited Availability.  Retrieves the specified invoice items which are broken down by orders. One invoice item might be broken down into a list of order related items.  The maximum number of invoice items to retrieve is 1000. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
body = swagger_client.POSTInvoiceItemsForOrderBreakdown() # POSTInvoiceItemsForOrderBreakdown | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Request breakdown of invoice items by order
    api_response = api_instance.p_ost_request_breakdown_invoice_items_by_order(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->p_ost_request_breakdown_invoice_items_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTInvoiceItemsForOrderBreakdown**](POSTInvoiceItemsForOrderBreakdown.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GetInvoiceAmountBreakdownByOrderResponse**](GetInvoiceAmountBreakdownByOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_order_trigger_dates**
> PUTOrderTriggerDatesResponseType p_ut_order_trigger_dates(body, order_number, zuora_entity_ids=zuora_entity_ids)

Update order action trigger dates

**Note:**  This operation is only available if you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled. The migration to Orders is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.  Updates a `CreateSubscription` order action's triggering dates. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
body = swagger_client.PUTOrderActionTriggerDatesRequestType() # PUTOrderActionTriggerDatesRequestType | 
order_number = 'order_number_example' # str | Order number of a pending order in which you are to update a `CreateSubscription` order action's triggering dates.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update order action trigger dates
    api_response = api_instance.p_ut_order_trigger_dates(body, order_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->p_ut_order_trigger_dates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTOrderActionTriggerDatesRequestType**](PUTOrderActionTriggerDatesRequestType.md)|  | 
 **order_number** | **str**| Order number of a pending order in which you are to update a &#x60;CreateSubscription&#x60; order action&#x27;s triggering dates. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**PUTOrderTriggerDatesResponseType**](PUTOrderTriggerDatesResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_update_order_custom_fields**
> CommonResponseType p_ut_update_order_custom_fields(body, order_number, zuora_entity_ids=zuora_entity_ids)

Update order custom fields

**Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. The migration to Order Metrics is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. If you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders) feature enabled, you already have the Order Metrics feature enabled.   Updates the custom fields of a specified order. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
body = swagger_client.PUTOrderPatchRequestType() # PUTOrderPatchRequestType | 
order_number = 'order_number_example' # str | The order number.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update order custom fields
    api_response = api_instance.p_ut_update_order_custom_fields(body, order_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->p_ut_update_order_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTOrderPatchRequestType**](PUTOrderPatchRequestType.md)|  | 
 **order_number** | **str**| The order number. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_update_subscription_custom_fields**
> CommonResponseType p_ut_update_subscription_custom_fields(body, subscription_number, zuora_entity_ids=zuora_entity_ids)

Update subscription custom fields

**Note:**  This operation is only available if you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled. The migration to Orders is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.   Updates the custom fields of a specified subscription. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
body = swagger_client.PUTSubscriptionPatchRequestType() # PUTSubscriptionPatchRequestType | 
subscription_number = 'subscription_number_example' # str | The subscription number to be updated.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update subscription custom fields
    api_response = api_instance.p_ut_update_subscription_custom_fields(body, subscription_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->p_ut_update_subscription_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTSubscriptionPatchRequestType**](PUTSubscriptionPatchRequestType.md)|  | 
 **subscription_number** | **str**| The subscription number to be updated. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

