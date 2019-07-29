# zuora_client.PaymentsApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_payment**](PaymentsApi.md#d_elete_payment) | **DELETE** /v1/payments/{paymentId} | Delete payment
[**g_et_payment**](PaymentsApi.md#g_et_payment) | **GET** /v1/payments/{paymentId} | Get payment
[**g_et_payment_item_part**](PaymentsApi.md#g_et_payment_item_part) | **GET** /v1/payments/{paymentId}/parts/{partid}/itemparts/{itempartid} | Get payment part item
[**g_et_payment_item_parts**](PaymentsApi.md#g_et_payment_item_parts) | **GET** /v1/payments/{paymentId}/parts/{partid}/itemparts | Get payment part items
[**g_et_payment_part**](PaymentsApi.md#g_et_payment_part) | **GET** /v1/payments/{paymentId}/parts/{partid} | Get payment part
[**g_et_payment_parts**](PaymentsApi.md#g_et_payment_parts) | **GET** /v1/payments/{paymentId}/parts | Get payment parts
[**g_et_retrieve_all_payments**](PaymentsApi.md#g_et_retrieve_all_payments) | **GET** /v1/payments | Get all payments
[**object_delete_payment**](PaymentsApi.md#object_delete_payment) | **DELETE** /v1/object/payment/{id} | CRUD: Delete payment
[**object_get_payment**](PaymentsApi.md#object_get_payment) | **GET** /v1/object/payment/{id} | CRUD: Get payment
[**object_post_payment**](PaymentsApi.md#object_post_payment) | **POST** /v1/object/payment | CRUD: Create payment
[**object_put_payment**](PaymentsApi.md#object_put_payment) | **PUT** /v1/object/payment/{id} | CRUD: Update payment
[**p_ost_create_payment**](PaymentsApi.md#p_ost_create_payment) | **POST** /v1/payments | Create payment
[**p_ost_refund_payment**](PaymentsApi.md#p_ost_refund_payment) | **POST** /v1/payments/{paymentId}/refunds | Refund payment
[**p_ut_apply_payment**](PaymentsApi.md#p_ut_apply_payment) | **PUT** /v1/payments/{paymentId}/apply | Apply payment
[**p_ut_cancel_payment**](PaymentsApi.md#p_ut_cancel_payment) | **PUT** /v1/payments/{paymentId}/cancel | Cancel payment
[**p_ut_transfer_payment**](PaymentsApi.md#p_ut_transfer_payment) | **PUT** /v1/payments/{paymentId}/transfer | Transfer payment
[**p_ut_unapply_payment**](PaymentsApi.md#p_ut_unapply_payment) | **PUT** /v1/payments/{paymentId}/unapply | Unapply payment
[**p_ut_update_payment**](PaymentsApi.md#p_ut_update_payment) | **PUT** /v1/payments/{paymentId} | Update payment

# **d_elete_payment**
> CommonResponseType d_elete_payment(payment_id, zuora_entity_ids=zuora_entity_ids)

Delete payment

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Deletes a payment. Only payments with the Cancelled status can be deleted.   If you have the Invoice Settlement feature enabled, overpayments applied to credit balance cannot be deleted. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
payment_id = 'payment_id_example' # str | The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete payment
    api_response = api_instance.d_elete_payment(payment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->d_elete_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment**
> GETARPaymentType g_et_payment(payment_id, zuora_entity_ids=zuora_entity_ids)

Get payment

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about one specific payment. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
payment_id = 'payment_id_example' # str | The unique ID of a payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get payment
    api_response = api_instance.g_et_payment(payment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->g_et_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| The unique ID of a payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETARPaymentType**](GETARPaymentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_item_part**
> GETPaymentItemPartType g_et_payment_item_part(partid, itempartid, payment_id, zuora_entity_ids=zuora_entity_ids)

Get payment part item

**Note:** The Invoice Item Settlement feature is in **Limited Availability**, and it must be used together with other Invoice Settlement features (Unapplied Payments, and Credit and Debit memos). If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the information about a specific payment part item. A payment part item is a single line item in a payment part. A payment part can consist of several different types of items. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
partid = 'partid_example' # str | The unique ID of a specific payment part. You can get the payment part ID from the response of [Get payment parts](https://www.zuora.com/developer/api-reference/#operation/GET_PaymentParts). 
itempartid = 'itempartid_example' # str | The unique ID of a specific payment part item. You can get the payment part item ID from the response of [Get payment part items](https://www.zuora.com/developer/api-reference/#operation/GET_PaymentItemParts). 
payment_id = 'payment_id_example' # str | The unique ID of a payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get payment part item
    api_response = api_instance.g_et_payment_item_part(partid, itempartid, payment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->g_et_payment_item_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partid** | **str**| The unique ID of a specific payment part. You can get the payment part ID from the response of [Get payment parts](https://www.zuora.com/developer/api-reference/#operation/GET_PaymentParts).  | 
 **itempartid** | **str**| The unique ID of a specific payment part item. You can get the payment part item ID from the response of [Get payment part items](https://www.zuora.com/developer/api-reference/#operation/GET_PaymentItemParts).  | 
 **payment_id** | **str**| The unique ID of a payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPaymentItemPartType**](GETPaymentItemPartType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_item_parts**
> GETPaymentItemPartCollectionType g_et_payment_item_parts(partid, payment_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get payment part items

**Note:** The Invoice Item Settlement feature is in **Limited Availability**, and it must be used together with other Invoice Settlement features (Unapplied Payments, and Credit and Debit memos). If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all items of a payment part. A payment part item is a single line item in a payment part. A payment part can consist of several different types of items. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
partid = 'partid_example' # str | The unique ID of a specific payment part. You can get the payment part ID from the response of [Get payment parts](https://www.zuora.com/developer/api-reference/#operation/GET_PaymentParts). 
payment_id = 'payment_id_example' # str | The unique ID of a payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get payment part items
    api_response = api_instance.g_et_payment_item_parts(partid, payment_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->g_et_payment_item_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partid** | **str**| The unique ID of a specific payment part. You can get the payment part ID from the response of [Get payment parts](https://www.zuora.com/developer/api-reference/#operation/GET_PaymentParts).  | 
 **payment_id** | **str**| The unique ID of a payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GETPaymentItemPartCollectionType**](GETPaymentItemPartCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_part**
> GETPaymentPartType g_et_payment_part(partid, payment_id, zuora_entity_ids=zuora_entity_ids)

Get payment part

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific payment part. A payment can consist of an unapplied part, and several parts applied to invoices and debit memos. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
partid = 'partid_example' # str | The unique ID of a specific payment part. You can get the payment part ID from the response of [Get payment parts](https://www.zuora.com/developer/api-reference/#operation/GET_PaymentParts). 
payment_id = 'payment_id_example' # str | The unique ID of a payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get payment part
    api_response = api_instance.g_et_payment_part(partid, payment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->g_et_payment_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partid** | **str**| The unique ID of a specific payment part. You can get the payment part ID from the response of [Get payment parts](https://www.zuora.com/developer/api-reference/#operation/GET_PaymentParts).  | 
 **payment_id** | **str**| The unique ID of a payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETPaymentPartType**](GETPaymentPartType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_payment_parts**
> GETPaymentPartsCollectionType g_et_payment_parts(payment_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get payment parts

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all parts of a payment. A payment can consist of an unapplied part, and several parts applied to invoices and debit memos. You can use this operation to get all the applied and unapplied portions of a payment. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
payment_id = 'payment_id_example' # str | The unique ID of a payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get payment parts
    api_response = api_instance.g_et_payment_parts(payment_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->g_et_payment_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| The unique ID of a payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GETPaymentPartsCollectionType**](GETPaymentPartsCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_retrieve_all_payments**
> PaymentCollectionResponseType g_et_retrieve_all_payments(zuora_entity_ids=zuora_entity_ids, page_size=page_size, account_id=account_id, amount=amount, applied_amount=applied_amount, created_by_id=created_by_id, created_date=created_date, credit_balance_amount=credit_balance_amount, currency=currency, effective_date=effective_date, number=number, refund_amount=refund_amount, status=status, type=type, unapplied_amount=unapplied_amount, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)

Get all payments

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all payments from all your customer accounts.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.  Examples:  - /v1/payments?status=Processed  - /v1/payments?currency=USD&status=Processed  - /v1/payments?status=Processed&type=External&sort=+number 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
account_id = 'account_id_example' # str | This parameter filters the response based on the `accountId` field.  (optional)
amount = 1.2 # float | This parameter filters the response based on the `amount` field.  (optional)
applied_amount = 1.2 # float | This parameter filters the response based on the `appliedAmount` field.  (optional)
created_by_id = 'created_by_id_example' # str | This parameter filters the response based on the `createdById` field.  (optional)
created_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `createdDate` field.  (optional)
credit_balance_amount = 1.2 # float | This parameter filters the response based on the `creditBalanceAmount` field.  (optional)
currency = 'currency_example' # str | This parameter filters the response based on the `currency` field.  (optional)
effective_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `effectiveDate` field.  (optional)
number = 'number_example' # str | This parameter filters the response based on the `number` field.  (optional)
refund_amount = 1.2 # float | This parameter filters the response based on the `refundAmount` field.  (optional)
status = 'status_example' # str | This parameter filters the response based on the `status` field.  (optional)
type = 'type_example' # str | This parameter filters the response based on the `type` field.  (optional)
unapplied_amount = 1.2 # float | This parameter filters the response based on the `unappliedAmount` field.  (optional)
updated_by_id = 'updated_by_id_example' # str | This parameter filters the response based on the `updatedById` field.  (optional)
updated_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `updatedDate` field.  (optional)
sort = 'sort_example' # str | This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by payment number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - number   - accountId   - amount   - appliedAmount   - unappliedAmount   - refundAmount   - creditBalanceAmount   - effectiveDate   - createdDate   - createdById   - updatedDate   - updatedById    Examples:  - /v1/payments?sort=+number  - /v1/payments?status=Processed&sort=-number,+amount  (optional)

try:
    # Get all payments
    api_response = api_instance.g_et_retrieve_all_payments(zuora_entity_ids=zuora_entity_ids, page_size=page_size, account_id=account_id, amount=amount, applied_amount=applied_amount, created_by_id=created_by_id, created_date=created_date, credit_balance_amount=credit_balance_amount, currency=currency, effective_date=effective_date, number=number, refund_amount=refund_amount, status=status, type=type, unapplied_amount=unapplied_amount, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->g_et_retrieve_all_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **account_id** | **str**| This parameter filters the response based on the &#x60;accountId&#x60; field.  | [optional] 
 **amount** | **float**| This parameter filters the response based on the &#x60;amount&#x60; field.  | [optional] 
 **applied_amount** | **float**| This parameter filters the response based on the &#x60;appliedAmount&#x60; field.  | [optional] 
 **created_by_id** | **str**| This parameter filters the response based on the &#x60;createdById&#x60; field.  | [optional] 
 **created_date** | **datetime**| This parameter filters the response based on the &#x60;createdDate&#x60; field.  | [optional] 
 **credit_balance_amount** | **float**| This parameter filters the response based on the &#x60;creditBalanceAmount&#x60; field.  | [optional] 
 **currency** | **str**| This parameter filters the response based on the &#x60;currency&#x60; field.  | [optional] 
 **effective_date** | **datetime**| This parameter filters the response based on the &#x60;effectiveDate&#x60; field.  | [optional] 
 **number** | **str**| This parameter filters the response based on the &#x60;number&#x60; field.  | [optional] 
 **refund_amount** | **float**| This parameter filters the response based on the &#x60;refundAmount&#x60; field.  | [optional] 
 **status** | **str**| This parameter filters the response based on the &#x60;status&#x60; field.  | [optional] 
 **type** | **str**| This parameter filters the response based on the &#x60;type&#x60; field.  | [optional] 
 **unapplied_amount** | **float**| This parameter filters the response based on the &#x60;unappliedAmount&#x60; field.  | [optional] 
 **updated_by_id** | **str**| This parameter filters the response based on the &#x60;updatedById&#x60; field.  | [optional] 
 **updated_date** | **datetime**| This parameter filters the response based on the &#x60;updatedDate&#x60; field.  | [optional] 
 **sort** | **str**| This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The &#x60;-&#x60; operator indicates an ascending order.   - The &#x60;+&#x60; operator indicates a descending order.  By default, the response data is displayed in descending order by payment number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - number   - accountId   - amount   - appliedAmount   - unappliedAmount   - refundAmount   - creditBalanceAmount   - effectiveDate   - createdDate   - createdById   - updatedDate   - updatedById    Examples:  - /v1/payments?sort&#x3D;+number  - /v1/payments?status&#x3D;Processed&amp;sort&#x3D;-number,+amount  | [optional] 

### Return type

[**PaymentCollectionResponseType**](PaymentCollectionResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_delete_payment**
> ProxyDeleteResponse object_delete_payment(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Delete payment

Deletes a payment. Only payments with the Cancelled status can be deleted.  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
id = 'id_example' # str | The unique ID of the payment to be deleted. For example, 2c92c0f85d4e95ae015d4f7e5d690622. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Delete payment
    api_response = api_instance.object_delete_payment(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->object_delete_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the payment to be deleted. For example, 2c92c0f85d4e95ae015d4f7e5d690622.  | 
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

# **object_get_payment**
> ProxyGetPayment object_get_payment(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Get payment

Retrieves the information about one specific payment.  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
id = 'id_example' # str | The unique ID of a payment. For example, 2c92c095592623ea01596621ada84352. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Get payment
    api_response = api_instance.object_get_payment(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->object_get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of a payment. For example, 2c92c095592623ea01596621ada84352.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 

### Return type

[**ProxyGetPayment**](ProxyGetPayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_post_payment**
> ProxyCreateOrModifyResponse object_post_payment(body, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Create payment

Creates a payment.  **Note:** If you have the Invoice Settlement feature enabled, you cannot use this operation to create a payment. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
body = zuora_client.ProxyCreatePayment() # ProxyCreatePayment | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Create payment
    api_response = api_instance.object_post_payment(body, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->object_post_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProxyCreatePayment**](ProxyCreatePayment.md)|  | 
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

# **object_put_payment**
> ProxyCreateOrModifyResponse object_put_payment(body, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Update payment

Updates a payment.  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
body = zuora_client.ProxyModifyPayment() # ProxyModifyPayment | 
id = 'id_example' # str | The unique ID of a payment. For example, 2c92c095592623ea01596621ada84352. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Update payment
    api_response = api_instance.object_put_payment(body, id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->object_put_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProxyModifyPayment**](ProxyModifyPayment.md)|  | 
 **id** | **str**| The unique ID of a payment. For example, 2c92c095592623ea01596621ada84352.  | 
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

# **p_ost_create_payment**
> GETARPaymentType p_ost_create_payment(body, zuora_entity_ids=zuora_entity_ids)

Create payment

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates a payment for the following scenarios:  - A full payment on an invoice or debit memo - A partial payment - A payment for several invoices and debit memos - An unapplied payment   If you do not know to which customer account the payment belongs, you can create a payment without specifying a customer account.  When creating a payment, the total number of invoices and debit memos that the payment will apply to should be less than or equal to 1,000.  If the Proration application rule is used, when creating a payment, the following quantity must be less than or equal to 10,000:   (number of invoice items + number of debit memo items) * number of payment items  Otherwise, the First In First Out rule will be used instead of the Proration rule.  For more information, see [Create Payments](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/A_Unapplied_Payments/Management_of_Unapplied_Payments/AA_Create_Payments) and [Create Payments Without Specifying Customer Accounts](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/A_Unapplied_Payments/Management_of_Unapplied_Payments/AA_Create_Payments_Without_Specifying_Customer_Accounts).      

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
body = zuora_client.CreatePaymentType() # CreatePaymentType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create payment
    api_response = api_instance.p_ost_create_payment(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->p_ost_create_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePaymentType**](CreatePaymentType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETARPaymentType**](GETARPaymentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_refund_payment**
> GETRefundPaymentType p_ost_refund_payment(body, payment_id, zuora_entity_ids=zuora_entity_ids)

Refund payment

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Refunds a full or partial unapplied payment to your customers. To refund applied payments, you must unapply the applied payments from the invoices or debit memos, and then refund the unapplied payments to customers.  For more information, see [Refund Payments](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/A_Unapplied_Payments/Management_of_Unapplied_Payments/Z_Refund_Payments). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
body = zuora_client.PostRefundType() # PostRefundType | 
payment_id = 'payment_id_example' # str | The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Refund payment
    api_response = api_instance.p_ost_refund_payment(body, payment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->p_ost_refund_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRefundType**](PostRefundType.md)|  | 
 **payment_id** | **str**| The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRefundPaymentType**](GETRefundPaymentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_apply_payment**
> GETARPaymentType p_ut_apply_payment(body, payment_id, zuora_entity_ids=zuora_entity_ids)

Apply payment

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Applies an unapplied payment to invoices and debit memos.  When applying a payment, the total number of invoices and debit memos that the payment will apply to must be less than or equal to 1,000.  If the Proration application rule is used, when applying a payment, the following quantity must be less than or equal to 10,000:   (number of invoice items + number of debit memo items) * number of payment items  Otherwise, the First In First Out rule will be used instead of the Proration rule.   For more information, see [Apply Unapplied Payments to Invoices and Debit Memos](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/A_Unapplied_Payments/Management_of_Unapplied_Payments/Apply_Unapplied_Payments_to_Invoices_and_Debit_Memos). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
body = zuora_client.ApplyPaymentType() # ApplyPaymentType | 
payment_id = 'payment_id_example' # str | The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Apply payment
    api_response = api_instance.p_ut_apply_payment(body, payment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->p_ut_apply_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyPaymentType**](ApplyPaymentType.md)|  | 
 **payment_id** | **str**| The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETARPaymentType**](GETARPaymentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_cancel_payment**
> GETARPaymentType p_ut_cancel_payment(payment_id, zuora_entity_ids=zuora_entity_ids)

Cancel payment

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Cancels a payment.   If you have the Invoice Settlement feature enabled, overpayments applied to credit balance cannot be cancelled. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
payment_id = 'payment_id_example' # str | The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Cancel payment
    api_response = api_instance.p_ut_cancel_payment(payment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->p_ut_cancel_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETARPaymentType**](GETARPaymentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_transfer_payment**
> GETARPaymentType p_ut_transfer_payment(body, payment_id, zuora_entity_ids=zuora_entity_ids)

Transfer payment

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Transfers an unapplied payment.  For more information, see [Transfer Unapplied Payments](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/A_Unapplied_Payments/Management_of_Unapplied_Payments/Transfer_Unapplied_Payments). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
body = zuora_client.TransferPaymentType() # TransferPaymentType | 
payment_id = 'payment_id_example' # str | The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Transfer payment
    api_response = api_instance.p_ut_transfer_payment(body, payment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->p_ut_transfer_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransferPaymentType**](TransferPaymentType.md)|  | 
 **payment_id** | **str**| The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETARPaymentType**](GETARPaymentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_unapply_payment**
> GETARPaymentType p_ut_unapply_payment(body, payment_id, zuora_entity_ids=zuora_entity_ids)

Unapply payment

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Unapplies an applied payment from invoices and debit memos.  For more information, see [Unapply Payments from Invoices and Debit Memos](https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/A_Unapplied_Payments/Management_of_Unapplied_Payments/Unapply_Payments_from_Invoices_and_Debit_Memos). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
body = zuora_client.UnapplyPaymentType() # UnapplyPaymentType | 
payment_id = 'payment_id_example' # str | The unique ID of an applied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Unapply payment
    api_response = api_instance.p_ut_unapply_payment(body, payment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->p_ut_unapply_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnapplyPaymentType**](UnapplyPaymentType.md)|  | 
 **payment_id** | **str**| The unique ID of an applied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETARPaymentType**](GETARPaymentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_update_payment**
> GETARPaymentType p_ut_update_payment(body, payment_id, zuora_entity_ids=zuora_entity_ids)

Update payment

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Updates a payment. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.PaymentsApi()
body = zuora_client.UpdatePaymentType() # UpdatePaymentType | 
payment_id = 'payment_id_example' # str | The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update payment
    api_response = api_instance.p_ut_update_payment(body, payment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->p_ut_update_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePaymentType**](UpdatePaymentType.md)|  | 
 **payment_id** | **str**| The unique ID of an unapplied payment. For example, 8a8082e65b27f6c3015b89e4344c16b1.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETARPaymentType**](GETARPaymentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

