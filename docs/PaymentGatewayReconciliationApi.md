# zuora_client.PaymentGatewayReconciliationApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_ost_reject_payment**](PaymentGatewayReconciliationApi.md#p_ost_reject_payment) | **POST** /v1/gateway-settlement/payments/{payment-id}/reject | Reject Payment
[**p_ost_reverse_payment**](PaymentGatewayReconciliationApi.md#p_ost_reverse_payment) | **POST** /v1/gateway-settlement/payments/{payment-id}/chargeback | Reverse Payment
[**p_ost_settle_payment**](PaymentGatewayReconciliationApi.md#p_ost_settle_payment) | **POST** /v1/gateway-settlement/payments/{payment-id}/settle | Settle Payment


# **p_ost_reject_payment**
> POSTRejectPaymentResponse p_ost_reject_payment(payment_id, request, zuora_entity_ids=zuora_entity_ids)

Reject Payment

Sets the Payment status to \"Rejected\", creates a refund for the payment amount, and returns the Refund object as response. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentGatewayReconciliationApi()
payment_id = 'payment_id_example' # str | Unique ID of the payment.
request = zuora_client.POSTRejectPaymentRequest() # POSTRejectPaymentRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Reject Payment
    api_response = api_instance.p_ost_reject_payment(payment_id, request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayReconciliationApi->p_ost_reject_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Unique ID of the payment. | 
 **request** | [**POSTRejectPaymentRequest**](POSTRejectPaymentRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTRejectPaymentResponse**](POSTRejectPaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_reverse_payment**
> POSTReversePaymentResponse p_ost_reverse_payment(payment_id, request, zuora_entity_ids=zuora_entity_ids)

Reverse Payment

Sets the Payment status to \"Reversed\", creates a refund for the amount specified in the request, and returns the Refund object as response. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentGatewayReconciliationApi()
payment_id = 'payment_id_example' # str | Unique ID of the payment.
request = zuora_client.POSTReversePaymentRequest() # POSTReversePaymentRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Reverse Payment
    api_response = api_instance.p_ost_reverse_payment(payment_id, request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayReconciliationApi->p_ost_reverse_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Unique ID of the payment. | 
 **request** | [**POSTReversePaymentRequest**](POSTReversePaymentRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTReversePaymentResponse**](POSTReversePaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_settle_payment**
> POSTSettlePaymentResponse p_ost_settle_payment(payment_id, request, zuora_entity_ids=zuora_entity_ids)

Settle Payment

Sets the Payment status to \"Settled\" and returns the Payment object as response. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentGatewayReconciliationApi()
payment_id = 'payment_id_example' # str | Unique ID of the payment.
request = zuora_client.POSTSettlePaymentRequest() # POSTSettlePaymentRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Settle Payment
    api_response = api_instance.p_ost_settle_payment(payment_id, request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayReconciliationApi->p_ost_settle_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Unique ID of the payment. | 
 **request** | [**POSTSettlePaymentRequest**](POSTSettlePaymentRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTSettlePaymentResponse**](POSTSettlePaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

