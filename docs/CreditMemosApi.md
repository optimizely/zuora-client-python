# zuora_client.CreditMemosApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_credit_memo**](CreditMemosApi.md#d_elete_credit_memo) | **DELETE** /v1/creditmemos/{creditMemoId} | Delete credit memo
[**g_et_breakdown_credit_memo_by_order**](CreditMemosApi.md#g_et_breakdown_credit_memo_by_order) | **GET** /v1/creditmemos/{creditMemoNumber}/amountBreakdownByOrder | Get breakdown of credit memo by order
[**g_et_credit_memo**](CreditMemosApi.md#g_et_credit_memo) | **GET** /v1/creditmemos/{creditMemoId} | Get credit memo
[**g_et_credit_memo_item**](CreditMemosApi.md#g_et_credit_memo_item) | **GET** /v1/creditmemos/{creditMemoId}/items/{cmitemid} | Get credit memo item
[**g_et_credit_memo_item_part**](CreditMemosApi.md#g_et_credit_memo_item_part) | **GET** /v1/creditmemos/{creditMemoId}/parts/{partid}/itemparts/{itempartid} | Get credit memo part item
[**g_et_credit_memo_item_parts**](CreditMemosApi.md#g_et_credit_memo_item_parts) | **GET** /v1/creditmemos/{creditMemoId}/parts/{partid}/itemparts | Get credit memo part items
[**g_et_credit_memo_items**](CreditMemosApi.md#g_et_credit_memo_items) | **GET** /v1/creditmemos/{creditMemoId}/items | Get credit memo items
[**g_et_credit_memo_part**](CreditMemosApi.md#g_et_credit_memo_part) | **GET** /v1/creditmemos/{creditMemoId}/parts/{partid} | Get credit memo part
[**g_et_credit_memo_parts**](CreditMemosApi.md#g_et_credit_memo_parts) | **GET** /v1/creditmemos/{creditMemoId}/parts | Get credit memo parts
[**g_et_credit_memos**](CreditMemosApi.md#g_et_credit_memos) | **GET** /v1/creditmemos | Get credit memos
[**g_et_taxation_items_of_credit_memo_item**](CreditMemosApi.md#g_et_taxation_items_of_credit_memo_item) | **GET** /v1/creditmemos/{creditMemoId}/items/{cmitemid}/taxation-items | Get taxation items of credit memo item
[**p_ost_credit_memo_from_prpc**](CreditMemosApi.md#p_ost_credit_memo_from_prpc) | **POST** /v1/creditmemos | Create credit memo from charge
[**p_ost_credit_memo_pdf**](CreditMemosApi.md#p_ost_credit_memo_pdf) | **POST** /v1/creditmemos/{creditMemoId}/pdfs | Create credit memo PDF
[**p_ost_email_credit_memo**](CreditMemosApi.md#p_ost_email_credit_memo) | **POST** /v1/creditmemos/{creditMemoId}/emails | Email credit memo
[**p_ost_refund_credit_memo**](CreditMemosApi.md#p_ost_refund_credit_memo) | **POST** /v1/creditmemos/{creditmemoId}/refunds | Refund credit memo
[**p_ost_request_breakdown_credit_memo_items_by_order**](CreditMemosApi.md#p_ost_request_breakdown_credit_memo_items_by_order) | **POST** /v1/creditmemos/items/amountBreakdownByOrder | Request breakdown of credit memo items by order
[**p_ost_upload_file_for_credit_memo**](CreditMemosApi.md#p_ost_upload_file_for_credit_memo) | **POST** /v1/creditmemos/{creditMemoId}/files | Upload file for credit memo
[**p_ostcm_taxation_items**](CreditMemosApi.md#p_ostcm_taxation_items) | **POST** /v1/creditmemos/{creditMemoId}/taxationitems | Create taxation items for credit memo
[**p_ut_apply_credit_memo**](CreditMemosApi.md#p_ut_apply_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId}/apply | Apply credit memo
[**p_ut_cancel_credit_memo**](CreditMemosApi.md#p_ut_cancel_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId}/cancel | Cancel credit memo
[**p_ut_post_credit_memo**](CreditMemosApi.md#p_ut_post_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId}/post | Post credit memo
[**p_ut_unapply_credit_memo**](CreditMemosApi.md#p_ut_unapply_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId}/unapply | Unapply credit memo
[**p_ut_unpost_credit_memo**](CreditMemosApi.md#p_ut_unpost_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId}/unpost | Unpost credit memo
[**p_ut_update_credit_memo**](CreditMemosApi.md#p_ut_update_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId} | Update credit memo

# **d_elete_credit_memo**
> CommonResponseType d_elete_credit_memo(credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Delete credit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Deletes a credit memo. Only credit memos with the Cancelled status can be deleted.   You can delete a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete credit memo
    api_response = api_instance.d_elete_credit_memo(credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->d_elete_credit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_breakdown_credit_memo_by_order**
> GetCreditMemoAmountBreakdownByOrderResponse g_et_breakdown_credit_memo_by_order(credit_memo_number, zuora_entity_ids=zuora_entity_ids)

Get breakdown of credit memo by order

**Note:** This feature is in Limited Availability.   Retrieves a specified credit memo that is broken down by orders. One credit memo item might be broken down into a list of order related items.  You can only use this operation to retrieve breakdowns of credit memos whose source value is `BillRun` or `API`. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
credit_memo_number = 'credit_memo_number_example' # str | Number of credit memo to be broken down.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get breakdown of credit memo by order
    api_response = api_instance.g_et_breakdown_credit_memo_by_order(credit_memo_number, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->g_et_breakdown_credit_memo_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_memo_number** | **str**| Number of credit memo to be broken down. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GetCreditMemoAmountBreakdownByOrderResponse**](GetCreditMemoAmountBreakdownByOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_credit_memo**
> GETCreditMemoType g_et_credit_memo(credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Get credit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific credit memo. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get credit memo
    api_response = api_instance.g_et_credit_memo(credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->g_et_credit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETCreditMemoType**](GETCreditMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_credit_memo_item**
> GETCreditMemoItemType g_et_credit_memo_item(cmitemid, credit_memo_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Get credit memo item

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the information about a specific item of a credit memo. A credit memo item is a single line item in a credit memo. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
cmitemid = 'cmitemid_example' # str | The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems). 
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str |  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * creditTaxItems * taxationItems  (optional)

try:
    # Get credit memo item
    api_response = api_instance.g_et_credit_memo_item(cmitemid, credit_memo_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->g_et_credit_memo_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmitemid** | **str**| The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  | 
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**|  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * creditTaxItems * taxationItems  | [optional] 

### Return type

[**GETCreditMemoItemType**](GETCreditMemoItemType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_credit_memo_item_part**
> GETCreditMemoItemPartType g_et_credit_memo_item_part(partid, itempartid, credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Get credit memo part item

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the information about a specific credit memo part item.  A credit memo part item is a single line item in a credit memo part. A credit memo part can consist of several different types of items. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
partid = 'partid_example' # str | The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts). 
itempartid = 'itempartid_example' # str | The unique ID of a specific credit memo part item. You can get the credit memo part item ID from the response of [Get credit memo part items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItemParts). 
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get credit memo part item
    api_response = api_instance.g_et_credit_memo_item_part(partid, itempartid, credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->g_et_credit_memo_item_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partid** | **str**| The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts).  | 
 **itempartid** | **str**| The unique ID of a specific credit memo part item. You can get the credit memo part item ID from the response of [Get credit memo part items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItemParts).  | 
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETCreditMemoItemPartType**](GETCreditMemoItemPartType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_credit_memo_item_parts**
> GETCreditMemoItemPartsCollectionType g_et_credit_memo_item_parts(partid, credit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get credit memo part items

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all items of a credit memo part. A credit memo part item is a single line item in a credit memo part. A credit memo part can consist of several different types of items. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
partid = 'partid_example' # str | The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts). . 
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get credit memo part items
    api_response = api_instance.g_et_credit_memo_item_parts(partid, credit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->g_et_credit_memo_item_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partid** | **str**| The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts). .  | 
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GETCreditMemoItemPartsCollectionType**](GETCreditMemoItemPartsCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_credit_memo_items**
> GETCreditMemoItemsListType g_et_credit_memo_items(credit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, zuora_version=zuora_version, amount=amount, applied_amount=applied_amount, created_by_id=created_by_id, created_date=created_date, id=id, refund_amount=refund_amount, service_end_date=service_end_date, service_start_date=service_start_date, sku=sku, sku_name=sku_name, source_item_id=source_item_id, subscription_id=subscription_id, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)

Get credit memo items

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all items of a credit memo. A credit memo item is a single line item in a credit memo.   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:        - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100      - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100&sort=createdDate      

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
zuora_version = 'zuora_version_example' # str |  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * creditTaxItems * taxationItems  (optional)
amount = 1.2 # float | This parameter filters the response based on the `amount` field.   (optional)
applied_amount = 1.2 # float | This parameter filters the response based on the `appliedAmount` field.   (optional)
created_by_id = 'created_by_id_example' # str | This parameter filters the response based on the `createdById` field.   (optional)
created_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `createdDate` field.   (optional)
id = 'id_example' # str | This parameter filters the response based on the `id` field.   (optional)
refund_amount = 1.2 # float | This parameter filters the response based on the `refundAmount` field.   (optional)
service_end_date = '2013-10-20' # date | This parameter filters the response based on the `serviceEndDate` field.   (optional)
service_start_date = '2013-10-20' # date | This parameter filters the response based on the `serviceStartDate` field.   (optional)
sku = 'sku_example' # str | This parameter filters the response based on the `sku` field.   (optional)
sku_name = 'sku_name_example' # str | This parameter filters the response based on the `skuName` field.   (optional)
source_item_id = 'source_item_id_example' # str | This parameter filters the response based on the `sourceItemId` field.   (optional)
subscription_id = 'subscription_id_example' # str | This parameter filters the response based on the `subscriptionId` field.  (optional)
updated_by_id = 'updated_by_id_example' # str | This parameter filters the response based on the `updatedById` field.   (optional)
updated_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `updatedDate` field.  (optional)
sort = 'sort_example' # str | This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by updated date.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - amount   - appliedAmount   - createdById   - createdDate   - id   - refundAmount   - serviceEndDate   - serviceStartDate   - sku   - skuName   - sourceItemId   - subscriptionId   - updatedById   - updatedDate    Examples:  - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?sort=createdDate  - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100&sort=createdDate  (optional)

try:
    # Get credit memo items
    api_response = api_instance.g_et_credit_memo_items(credit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, zuora_version=zuora_version, amount=amount, applied_amount=applied_amount, created_by_id=created_by_id, created_date=created_date, id=id, refund_amount=refund_amount, service_end_date=service_end_date, service_start_date=service_start_date, sku=sku, sku_name=sku_name, source_item_id=source_item_id, subscription_id=subscription_id, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->g_et_credit_memo_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **zuora_version** | **str**|  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * creditTaxItems * taxationItems  | [optional] 
 **amount** | **float**| This parameter filters the response based on the &#x60;amount&#x60; field.   | [optional] 
 **applied_amount** | **float**| This parameter filters the response based on the &#x60;appliedAmount&#x60; field.   | [optional] 
 **created_by_id** | **str**| This parameter filters the response based on the &#x60;createdById&#x60; field.   | [optional] 
 **created_date** | **datetime**| This parameter filters the response based on the &#x60;createdDate&#x60; field.   | [optional] 
 **id** | **str**| This parameter filters the response based on the &#x60;id&#x60; field.   | [optional] 
 **refund_amount** | **float**| This parameter filters the response based on the &#x60;refundAmount&#x60; field.   | [optional] 
 **service_end_date** | **date**| This parameter filters the response based on the &#x60;serviceEndDate&#x60; field.   | [optional] 
 **service_start_date** | **date**| This parameter filters the response based on the &#x60;serviceStartDate&#x60; field.   | [optional] 
 **sku** | **str**| This parameter filters the response based on the &#x60;sku&#x60; field.   | [optional] 
 **sku_name** | **str**| This parameter filters the response based on the &#x60;skuName&#x60; field.   | [optional] 
 **source_item_id** | **str**| This parameter filters the response based on the &#x60;sourceItemId&#x60; field.   | [optional] 
 **subscription_id** | **str**| This parameter filters the response based on the &#x60;subscriptionId&#x60; field.  | [optional] 
 **updated_by_id** | **str**| This parameter filters the response based on the &#x60;updatedById&#x60; field.   | [optional] 
 **updated_date** | **datetime**| This parameter filters the response based on the &#x60;updatedDate&#x60; field.  | [optional] 
 **sort** | **str**| This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The &#x60;-&#x60; operator indicates an ascending order.   - The &#x60;+&#x60; operator indicates a descending order.  By default, the response data is displayed in descending order by updated date.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - amount   - appliedAmount   - createdById   - createdDate   - id   - refundAmount   - serviceEndDate   - serviceStartDate   - sku   - skuName   - sourceItemId   - subscriptionId   - updatedById   - updatedDate    Examples:  - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?sort&#x3D;createdDate  - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount&#x3D;100&amp;sort&#x3D;createdDate  | [optional] 

### Return type

[**GETCreditMemoItemsListType**](GETCreditMemoItemsListType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_credit_memo_part**
> GETCreditMemoPartType g_et_credit_memo_part(partid, credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Get credit memo part

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific credit memo part. A credit memo can consist of an unapplied part, and several parts applied to invoices and debit memos. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
partid = 'partid_example' # str | The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts). 
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get credit memo part
    api_response = api_instance.g_et_credit_memo_part(partid, credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->g_et_credit_memo_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partid** | **str**| The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts).  | 
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETCreditMemoPartType**](GETCreditMemoPartType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_credit_memo_parts**
> GETCreditMemoPartsCollectionType g_et_credit_memo_parts(credit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get credit memo parts

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all parts of a credit memo. A credit memo can consist of an unapplied part, and several parts applied to invoices and debit memos. You can use this operation to get all the applied and unapplied portions of a credit memo. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get credit memo parts
    api_response = api_instance.g_et_credit_memo_parts(credit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->g_et_credit_memo_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GETCreditMemoPartsCollectionType**](GETCreditMemoPartsCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_credit_memos**
> GETCreditMemoCollectionType g_et_credit_memos(zuora_entity_ids=zuora_entity_ids, page_size=page_size, account_id=account_id, amount=amount, applied_amount=applied_amount, auto_apply_upon_posting=auto_apply_upon_posting, created_by_id=created_by_id, created_date=created_date, credit_memo_date=credit_memo_date, currency=currency, exclude_from_auto_apply_rules=exclude_from_auto_apply_rules, number=number, referred_invoice_id=referred_invoice_id, refund_amount=refund_amount, status=status, target_date=target_date, tax_amount=tax_amount, total_tax_exempt_amount=total_tax_exempt_amount, transferred_to_accounting=transferred_to_accounting, unapplied_amount=unapplied_amount, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)

Get credit memos

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all credit memos.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.     Examples:  - /v1/creditmemos?status=Processed  - /v1/creditmemos?referredInvoiceId=null&status=Draft  - /v1/creditmemos?status=Processed&type=External&sort=+number 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
account_id = 'account_id_example' # str | This parameter filters the response based on the `accountId` field.   (optional)
amount = 1.2 # float | This parameter filters the response based on the `amount` field.   (optional)
applied_amount = 1.2 # float | This parameter filters the response based on the `appliedAmount` field.   (optional)
auto_apply_upon_posting = true # bool | This parameter filters the response based on the `autoApplyUponPosting` field.   (optional)
created_by_id = 'created_by_id_example' # str | This parameter filters the response based on the `createdById` field.   (optional)
created_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `createdDate` field.   (optional)
credit_memo_date = '2013-10-20' # date | This parameter filters the response based on the `creditMemoDate` field.   (optional)
currency = 'currency_example' # str | This parameter filters the response based on the `currency` field.   (optional)
exclude_from_auto_apply_rules = true # bool | This parameter filters the response based on the `excludeFromAutoApplyRules` field.   (optional)
number = 'number_example' # str | This parameter filters the response based on the `number` field.   (optional)
referred_invoice_id = 'referred_invoice_id_example' # str | This parameter filters the response based on the `referredInvoiceId` field.   (optional)
refund_amount = 1.2 # float | This parameter filters the response based on the `refundAmount` field.   (optional)
status = 'status_example' # str | This parameter filters the response based on the `status` field.   (optional)
target_date = '2013-10-20' # date | This parameter filters the response based on the `targetDate` field.   (optional)
tax_amount = 1.2 # float | This parameter filters the response based on the `taxAmount` field.   (optional)
total_tax_exempt_amount = 1.2 # float | This parameter filters the response based on the `totalTaxExemptAmount` field.  (optional)
transferred_to_accounting = 'transferred_to_accounting_example' # str | This parameter filters the response based on the `transferredToAccounting` field.   (optional)
unapplied_amount = 1.2 # float | This parameter filters the response based on the `unappliedAmount` field.   (optional)
updated_by_id = 'updated_by_id_example' # str | This parameter filters the response based on the `updatedById` field.   (optional)
updated_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `updatedDate` field.  (optional)
sort = 'sort_example' # str | This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by credit memo number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - accountId   - amount   - appliedAmount   - createdById   - createdDate   - creditMemoDate   - number   - referredInvoiceId   - refundAmount   - status   - targetDate   - taxAmount   - totalTaxExemptAmount   - transferredToAccounting   - unappliedAmount   - updatedDate     Examples:  - /v1/creditmemos?sort=+number  - /v1/creditmemos?status=Processed&sort=-number,+amount  (optional)

try:
    # Get credit memos
    api_response = api_instance.g_et_credit_memos(zuora_entity_ids=zuora_entity_ids, page_size=page_size, account_id=account_id, amount=amount, applied_amount=applied_amount, auto_apply_upon_posting=auto_apply_upon_posting, created_by_id=created_by_id, created_date=created_date, credit_memo_date=credit_memo_date, currency=currency, exclude_from_auto_apply_rules=exclude_from_auto_apply_rules, number=number, referred_invoice_id=referred_invoice_id, refund_amount=refund_amount, status=status, target_date=target_date, tax_amount=tax_amount, total_tax_exempt_amount=total_tax_exempt_amount, transferred_to_accounting=transferred_to_accounting, unapplied_amount=unapplied_amount, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->g_et_credit_memos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **account_id** | **str**| This parameter filters the response based on the &#x60;accountId&#x60; field.   | [optional] 
 **amount** | **float**| This parameter filters the response based on the &#x60;amount&#x60; field.   | [optional] 
 **applied_amount** | **float**| This parameter filters the response based on the &#x60;appliedAmount&#x60; field.   | [optional] 
 **auto_apply_upon_posting** | **bool**| This parameter filters the response based on the &#x60;autoApplyUponPosting&#x60; field.   | [optional] 
 **created_by_id** | **str**| This parameter filters the response based on the &#x60;createdById&#x60; field.   | [optional] 
 **created_date** | **datetime**| This parameter filters the response based on the &#x60;createdDate&#x60; field.   | [optional] 
 **credit_memo_date** | **date**| This parameter filters the response based on the &#x60;creditMemoDate&#x60; field.   | [optional] 
 **currency** | **str**| This parameter filters the response based on the &#x60;currency&#x60; field.   | [optional] 
 **exclude_from_auto_apply_rules** | **bool**| This parameter filters the response based on the &#x60;excludeFromAutoApplyRules&#x60; field.   | [optional] 
 **number** | **str**| This parameter filters the response based on the &#x60;number&#x60; field.   | [optional] 
 **referred_invoice_id** | **str**| This parameter filters the response based on the &#x60;referredInvoiceId&#x60; field.   | [optional] 
 **refund_amount** | **float**| This parameter filters the response based on the &#x60;refundAmount&#x60; field.   | [optional] 
 **status** | **str**| This parameter filters the response based on the &#x60;status&#x60; field.   | [optional] 
 **target_date** | **date**| This parameter filters the response based on the &#x60;targetDate&#x60; field.   | [optional] 
 **tax_amount** | **float**| This parameter filters the response based on the &#x60;taxAmount&#x60; field.   | [optional] 
 **total_tax_exempt_amount** | **float**| This parameter filters the response based on the &#x60;totalTaxExemptAmount&#x60; field.  | [optional] 
 **transferred_to_accounting** | **str**| This parameter filters the response based on the &#x60;transferredToAccounting&#x60; field.   | [optional] 
 **unapplied_amount** | **float**| This parameter filters the response based on the &#x60;unappliedAmount&#x60; field.   | [optional] 
 **updated_by_id** | **str**| This parameter filters the response based on the &#x60;updatedById&#x60; field.   | [optional] 
 **updated_date** | **datetime**| This parameter filters the response based on the &#x60;updatedDate&#x60; field.  | [optional] 
 **sort** | **str**| This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The &#x60;-&#x60; operator indicates an ascending order.   - The &#x60;+&#x60; operator indicates a descending order.  By default, the response data is displayed in descending order by credit memo number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - accountId   - amount   - appliedAmount   - createdById   - createdDate   - creditMemoDate   - number   - referredInvoiceId   - refundAmount   - status   - targetDate   - taxAmount   - totalTaxExemptAmount   - transferredToAccounting   - unappliedAmount   - updatedDate     Examples:  - /v1/creditmemos?sort&#x3D;+number  - /v1/creditmemos?status&#x3D;Processed&amp;sort&#x3D;-number,+amount  | [optional] 

### Return type

[**GETCreditMemoCollectionType**](GETCreditMemoCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_taxation_items_of_credit_memo_item**
> GETTaxationItemsOfCreditMemoItemType g_et_taxation_items_of_credit_memo_item(cmitemid, credit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, page=page)

Get taxation items of credit memo item

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves information about the taxation items of a specific credit memo item.  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
cmitemid = 'cmitemid_example' # str | The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems). 
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
page = 56 # int | Page number.  (optional)

try:
    # Get taxation items of credit memo item
    api_response = api_instance.g_et_taxation_items_of_credit_memo_item(cmitemid, credit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->g_et_taxation_items_of_credit_memo_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmitemid** | **str**| The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  | 
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **page** | **int**| Page number.  | [optional] 

### Return type

[**GETTaxationItemsOfCreditMemoItemType**](GETTaxationItemsOfCreditMemoItemType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_credit_memo_from_prpc**
> GETCreditMemoType p_ost_credit_memo_from_prpc(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Create credit memo from charge

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates an ad-hoc credit memo from a product rate plan charge. Zuora supports the creation of credit memos from any type of product rate plan charge. The charges can also have any amount and any charge model, except for discout charge models.   You can create a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
body = zuora_client.CreditMemoFromChargeType() # CreditMemoFromChargeType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str |  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * amount * memoItemAmount  (optional)

try:
    # Create credit memo from charge
    api_response = api_instance.p_ost_credit_memo_from_prpc(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ost_credit_memo_from_prpc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreditMemoFromChargeType**](CreditMemoFromChargeType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**|  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * amount * memoItemAmount  | [optional] 

### Return type

[**GETCreditMemoType**](GETCreditMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_credit_memo_pdf**
> POSTMemoPdfResponse p_ost_credit_memo_pdf(credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Create credit memo PDF

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates a PDF file for a specified credit memo. To access the generated PDF file, you can download it by clicking **View PDF** on the detailed credit memo page through the Zuora UI.  This REST API operation can be used only if you have the Billing user permission \"Regenerate PDF\" enabled. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of the credit memo that you want to create a PDF file for. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create credit memo PDF
    api_response = api_instance.p_ost_credit_memo_pdf(credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ost_credit_memo_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_memo_id** | **str**| The unique ID of the credit memo that you want to create a PDF file for. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTMemoPdfResponse**](POSTMemoPdfResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_email_credit_memo**
> CommonResponseType p_ost_email_credit_memo(body, credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Email credit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Sends a posted credit memo to the specified email addresses manually.    ## Notes   - You must activate the **Email Credit Memo | Manually email Credit Memo** notification before emailing credit memos. To include the credit memo PDF in the email, select the **Include Credit Memo PDF** check box in the **Edit notification** dialog from the Zuora UI. See [Create and Edit Notifications](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/C_Create_Notifications#section_2) for more information.     - Zuora sends the email messages based on the email template you set. You can set the email template to use in the **Delivery Options** panel of the **Edit notification** dialog from the Zuora UI. By default, the **Manual Email for Credit Memo Default Template** template is used. See [Create and Edit Email Templates](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/Create_Email_Templates) for more information.     - The credit memos are sent only to the work email addresses or personal email addresses of the Bill To contact if the following conditions are all met:      * The `useEmailTemplateSetting` field is set to `false`.     * The email addresses are not specified in the `emailAddresses` field. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
body = zuora_client.PostCreditMemoEmailRequestType() # PostCreditMemoEmailRequestType | 
credit_memo_id = 'credit_memo_id_example' # str | The ID of a posted credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Email credit memo
    api_response = api_instance.p_ost_email_credit_memo(body, credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ost_email_credit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCreditMemoEmailRequestType**](PostCreditMemoEmailRequestType.md)|  | 
 **credit_memo_id** | **str**| The ID of a posted credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_refund_credit_memo**
> GETRefundCreditMemoType p_ost_refund_credit_memo(body, creditmemo_id, zuora_entity_ids=zuora_entity_ids)

Refund credit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Refunds a full or partial posted credit memo to your customers. Only the amount of unapplied part could be refunded.   You can refund a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
body = zuora_client.PostNonRefRefundType() # PostNonRefRefundType | 
creditmemo_id = 'creditmemo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Refund credit memo
    api_response = api_instance.p_ost_refund_credit_memo(body, creditmemo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ost_refund_credit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostNonRefRefundType**](PostNonRefRefundType.md)|  | 
 **creditmemo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRefundCreditMemoType**](GETRefundCreditMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_request_breakdown_credit_memo_items_by_order**
> GetCreditMemoAmountBreakdownByOrderResponse p_ost_request_breakdown_credit_memo_items_by_order(body, zuora_entity_ids=zuora_entity_ids)

Request breakdown of credit memo items by order

**Note:** This feature is in Limited Availability.   Retrieve specified credit memo items which are broken down by orders. One credit memo item might be broken down into a list of order related items.  You can only use this operation to retrieve breakdowns of credit memos whose source value is `BillRun` or `API`.  The maximum number of credit memo items to retrieve is 1000. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
body = zuora_client.POSTCreditMemoItemsForOrderBreakdown() # POSTCreditMemoItemsForOrderBreakdown | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Request breakdown of credit memo items by order
    api_response = api_instance.p_ost_request_breakdown_credit_memo_items_by_order(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ost_request_breakdown_credit_memo_items_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTCreditMemoItemsForOrderBreakdown**](POSTCreditMemoItemsForOrderBreakdown.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GetCreditMemoAmountBreakdownByOrderResponse**](GetCreditMemoAmountBreakdownByOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_upload_file_for_credit_memo**
> POSTUploadFileResponse p_ost_upload_file_for_credit_memo(credit_memo_id, file=file, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Upload file for credit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Uploads an externally generated PDF file for a credit memo that is in Draft or Posted status.  This operation has the following restrictions: - Only the PDF file format is supported. - The maximum size of the PDF file to upload is 4 MB. - A maximum of 50 PDF files can be uploaded for one credit memo. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
credit_memo_id = 'credit_memo_id_example' # str | The ID of the credit memo that you want to upload a PDF file for. For example, 402890555a7e9791015a879f064a0054. 
file = 'file_example' # file |  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Upload file for credit memo
    api_response = api_instance.p_ost_upload_file_for_credit_memo(credit_memo_id, file=file, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ost_upload_file_for_credit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_memo_id** | **str**| The ID of the credit memo that you want to upload a PDF file for. For example, 402890555a7e9791015a879f064a0054.  | 
 **file** | **file**|  | [optional] 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#x27;&#x60;).  | [optional] 

### Return type

[**POSTUploadFileResponse**](POSTUploadFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ostcm_taxation_items**
> GETTaxationItemListType p_ostcm_taxation_items(body, credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Create taxation items for credit memo

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates taxation items for a credit memo. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
body = zuora_client.POSTTaxationItemListForCMType() # POSTTaxationItemListForCMType | 
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create taxation items for credit memo
    api_response = api_instance.p_ostcm_taxation_items(body, credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ostcm_taxation_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTTaxationItemListForCMType**](POSTTaxationItemListForCMType.md)|  | 
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETTaxationItemListType**](GETTaxationItemListType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_apply_credit_memo**
> GETCreditMemoType p_ut_apply_credit_memo(body, credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Apply credit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Applies a posted credit memo to one or more invoices and debit memos.   You can apply a credit memo to an invoice or a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.  When applying a credit memo, the total number of invoices and debit memos that the credit memo will apply to must be less than or equal to 1,000.  If the Proration application rule is used, when applying credit memos, the following quantity must be less than or equal to 10,000:   (number of invoice items + number of debit memo items) * number of credit memo items  Otherwise, the First In First Out rule will be used instead of the Proration rule. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
body = zuora_client.ApplyCreditMemoType() # ApplyCreditMemoType | 
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Apply credit memo
    api_response = api_instance.p_ut_apply_credit_memo(body, credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ut_apply_credit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplyCreditMemoType**](ApplyCreditMemoType.md)|  | 
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETCreditMemoType**](GETCreditMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_cancel_credit_memo**
> GETCreditMemoType p_ut_cancel_credit_memo(credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Cancel credit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Cancels a credit memo. Only credit memos with the Draft status can be cancelled.   You can cancel a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Cancel credit memo
    api_response = api_instance.p_ut_cancel_credit_memo(credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ut_cancel_credit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETCreditMemoType**](GETCreditMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_post_credit_memo**
> GETCreditMemoType p_ut_post_credit_memo(credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Post credit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Posts a credit memo to activate it. You can post credit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Post credit memo
    api_response = api_instance.p_ut_post_credit_memo(credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ut_post_credit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETCreditMemoType**](GETCreditMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_unapply_credit_memo**
> GETCreditMemoType p_ut_unapply_credit_memo(body, credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Unapply credit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Unapplies an applied credit memo from one or more invoices and debit memos. The full applied amount from invoices and debit memos is transferred into the unapplied amount of the credit memo.   You can unapply a credit memo from an invoice or a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.  When unapplying a credit memo, the total number of invoices and debit memos that the credit memo will be unapplied from must be less than or equal to 1,000.  If the Proration application rule is used, when unapplying credit memos, the following quantity must be less than or equal to 10,000:   (number of invoice items + number of debit memo items) * number of credit memo items  Otherwise, the First In First Out rule will be used instead of the Proration rule. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
body = zuora_client.UnapplyCreditMemoType() # UnapplyCreditMemoType | 
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Unapply credit memo
    api_response = api_instance.p_ut_unapply_credit_memo(body, credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ut_unapply_credit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnapplyCreditMemoType**](UnapplyCreditMemoType.md)|  | 
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETCreditMemoType**](GETCreditMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_unpost_credit_memo**
> GETCreditMemoType p_ut_unpost_credit_memo(credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Unpost credit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Unposts a credit memo that is in Posted status. If a credit memo has been applied or refunded, you are not allowed to unpost it. After a credit memo is unposted, its status becomes Draft.   You can unpost credit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Unpost credit memo
    api_response = api_instance.p_ut_unpost_credit_memo(credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ut_unpost_credit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETCreditMemoType**](GETCreditMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_update_credit_memo**
> GETCreditMemoType p_ut_update_credit_memo(body, credit_memo_id, zuora_entity_ids=zuora_entity_ids)

Update credit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Updates the basic and finance information about a credit memo. Currently, Zuora supports updating tax-exclusive memo items, but does not support updating tax-inclusive memo items.   If the amount of a memo item is updated, the tax will be recalculated in the following conditions:   - The memo is created from a product rate plan charge and you use Avalara to calculate the tax.   - The memo is created from an invoice and you use Avalara or Zuora Tax to calculate the tax.  You can update a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CreditMemosApi()
body = zuora_client.PUTCreditMemoType() # PUTCreditMemoType | 
credit_memo_id = 'credit_memo_id_example' # str | The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update credit memo
    api_response = api_instance.p_ut_update_credit_memo(body, credit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditMemosApi->p_ut_update_credit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTCreditMemoType**](PUTCreditMemoType.md)|  | 
 **credit_memo_id** | **str**| The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.   | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETCreditMemoType**](GETCreditMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

