# zuora_client.RefundsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_refund**](RefundsApi.md#d_elete_refund) | **DELETE** /v1/refunds/{refundId} | Delete refund
[**g_et_refund**](RefundsApi.md#g_et_refund) | **GET** /v1/refunds/{refundId} | Get refund
[**g_et_refund_item_part**](RefundsApi.md#g_et_refund_item_part) | **GET** /v1/refunds/{refundId}/parts/{refundpartid}/itemparts/{itempartid} | Get refund part item
[**g_et_refund_item_parts**](RefundsApi.md#g_et_refund_item_parts) | **GET** /v1/refunds/{refundId}/parts/{refundpartid}/itemparts | Get refund part items
[**g_et_refund_part**](RefundsApi.md#g_et_refund_part) | **GET** /v1/refunds/{refundId}/parts/{refundpartid} | Get refund part
[**g_et_refund_parts**](RefundsApi.md#g_et_refund_parts) | **GET** /v1/refunds/{refundId}/parts | Get refund parts
[**g_et_refunds**](RefundsApi.md#g_et_refunds) | **GET** /v1/refunds | Get all refunds
[**object_delete_refund**](RefundsApi.md#object_delete_refund) | **DELETE** /v1/object/refund/{id} | CRUD: Delete refund
[**object_get_refund**](RefundsApi.md#object_get_refund) | **GET** /v1/object/refund/{id} | CRUD: Get refund
[**object_post_refund**](RefundsApi.md#object_post_refund) | **POST** /v1/object/refund | CRUD: Create refund
[**object_put_refund**](RefundsApi.md#object_put_refund) | **PUT** /v1/object/refund/{id} | CRUD: Update refund
[**p_ut_cancel_refund**](RefundsApi.md#p_ut_cancel_refund) | **PUT** /v1/refunds/{refundId}/cancel | Cancel refund
[**p_ut_update_refund**](RefundsApi.md#p_ut_update_refund) | **PUT** /v1/refunds/{refundId} | Update refund


# **d_elete_refund**
> CommonResponseType d_elete_refund(refund_id, zuora_entity_ids=zuora_entity_ids)

Delete refund

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Deletes a refund. You can delete a refund with the Canceled or Error status.   If you have the Invoice Settlement feature enabled, refunds applied to credit balance cannot be deleted. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
refund_id = 'refund_id_example' # str | The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete refund
    api_response = api_instance.d_elete_refund(refund_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->d_elete_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_refund**
> GETRefundType g_et_refund(refund_id, zuora_entity_ids=zuora_entity_ids)

Get refund

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific refund. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
refund_id = 'refund_id_example' # str | The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get refund
    api_response = api_instance.g_et_refund(refund_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->g_et_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRefundType**](GETRefundType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_refund_item_part**
> GETRefundItemPartType g_et_refund_item_part(itempartid, refundpartid, refund_id, zuora_entity_ids=zuora_entity_ids)

Get refund part item

**Note:** The Invoice Item Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at  [Zuora Global Support](http://support.zuora.com/).    Retrieves the information about a specific refund part item. A refund part item is a single line item in a refund part. A refund part can consist of several different types of items. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
itempartid = 'itempartid_example' # str | The unique ID of a specific refund part item. You can get the refund part item ID from the response of [Get refund part items](https://www.zuora.com/developer/api-reference/#operation/GET_RefundItemParts). 
refundpartid = 'refundpartid_example' # str | The unique ID of a specific refund part. You can get the refund part ID from the response of [Get refund parts](https://www.zuora.com/developer/api-reference/#operation/GET_RefundParts). 
refund_id = 'refund_id_example' # str | The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get refund part item
    api_response = api_instance.g_et_refund_item_part(itempartid, refundpartid, refund_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->g_et_refund_item_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itempartid** | **str**| The unique ID of a specific refund part item. You can get the refund part item ID from the response of [Get refund part items](https://www.zuora.com/developer/api-reference/#operation/GET_RefundItemParts).  | 
 **refundpartid** | **str**| The unique ID of a specific refund part. You can get the refund part ID from the response of [Get refund parts](https://www.zuora.com/developer/api-reference/#operation/GET_RefundParts).  | 
 **refund_id** | **str**| The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRefundItemPartType**](GETRefundItemPartType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_refund_item_parts**
> GETRefundItemPartCollectionType g_et_refund_item_parts(refundpartid, refund_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get refund part items

**Note:** The Invoice Item Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at  [Zuora Global Support](http://support.zuora.com/).  Retrieves the information about all items of a refund part. A refund part item is a single line item in a refund part. A refund part can consist of several different types of items. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
refundpartid = 'refundpartid_example' # str | The unique ID of a specific refund part. You can get the refund part ID from the response of [Get refund parts](https://www.zuora.com/developer/api-reference/#operation/GET_RefundParts). 
refund_id = 'refund_id_example' # str | The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 20 # int | Number of rows returned per page.  (optional) (default to 20)

try:
    # Get refund part items
    api_response = api_instance.g_et_refund_item_parts(refundpartid, refund_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->g_et_refund_item_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refundpartid** | **str**| The unique ID of a specific refund part. You can get the refund part ID from the response of [Get refund parts](https://www.zuora.com/developer/api-reference/#operation/GET_RefundParts).  | 
 **refund_id** | **str**| The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] [default to 20]

### Return type

[**GETRefundItemPartCollectionType**](GETRefundItemPartCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_refund_part**
> RefundPartResponseType g_et_refund_part(refundpartid, refund_id, zuora_entity_ids=zuora_entity_ids)

Get refund part

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific refund part. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
refundpartid = 'refundpartid_example' # str | The unique ID of a specific refund part. You can get the refund part ID from the response of [Get refund parts](https://www.zuora.com/developer/api-reference/#operation/GET_RefundParts). 
refund_id = 'refund_id_example' # str | The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get refund part
    api_response = api_instance.g_et_refund_part(refundpartid, refund_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->g_et_refund_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refundpartid** | **str**| The unique ID of a specific refund part. You can get the refund part ID from the response of [Get refund parts](https://www.zuora.com/developer/api-reference/#operation/GET_RefundParts).  | 
 **refund_id** | **str**| The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**RefundPartResponseType**](RefundPartResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_refund_parts**
> GETRefundPartCollectionType g_et_refund_parts(refund_id, zuora_entity_ids=zuora_entity_ids)

Get refund parts

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all parts of a refund. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
refund_id = 'refund_id_example' # str | The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get refund parts
    api_response = api_instance.g_et_refund_parts(refund_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->g_et_refund_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRefundPartCollectionType**](GETRefundPartCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_refunds**
> GETRefundCollectionType g_et_refunds(zuora_entity_ids=zuora_entity_ids, page_size=page_size, account_id=account_id, amount=amount, created_by_id=created_by_id, created_date=created_date, method_type=method_type, number=number, payment_id=payment_id, refund_date=refund_date, status=status, type=type, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)

Get all refunds

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all refunds. Two types of refunds are available, electronic refunds and external refunds.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.  Examples:  - /v1/refunds?status=Processed  - /v1/refunds?amount=4&status=Processed  - /v1/refunds?status=Processed&type=External&sort=+number 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 20 # int | Number of rows returned per page.  (optional) (default to 20)
account_id = 'account_id_example' # str | This parameter filters the response based on the `accountId` field.  (optional)
amount = 1.2 # float | This parameter filters the response based on the `amount` field.  (optional)
created_by_id = 'created_by_id_example' # str | This parameter filters the response based on the `createdById` field.  (optional)
created_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `createdDate` field.  (optional)
method_type = 'method_type_example' # str | This parameter filters the response based on the `methodType` field.  (optional)
number = 'number_example' # str | This parameter filters the response based on the `number` field.  (optional)
payment_id = 'payment_id_example' # str | This parameter filters the response based on the `paymentId` field.  (optional)
refund_date = '2013-10-20' # date | This parameter filters the response based on the `refundDate` field.  (optional)
status = 'status_example' # str | This parameter filters the response based on the `status` field.  (optional)
type = 'type_example' # str | This parameter filters the response based on the `type` field.  (optional)
updated_by_id = 'updated_by_id_example' # str | This parameter filters the response based on the `updatedById` field.  (optional)
updated_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `updatedDate` field.  (optional)
sort = 'sort_example' # str | This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by refund number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - number   - accountId   - amount   - refundDate   - paymentId   - createdDate   - createdById   - updatedDate   - updatedById    Examples:  - /v1/refunds?sort=+number  - /v1/refunds?status=Processed&sort=-number,+amount  (optional)

try:
    # Get all refunds
    api_response = api_instance.g_et_refunds(zuora_entity_ids=zuora_entity_ids, page_size=page_size, account_id=account_id, amount=amount, created_by_id=created_by_id, created_date=created_date, method_type=method_type, number=number, payment_id=payment_id, refund_date=refund_date, status=status, type=type, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->g_et_refunds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] [default to 20]
 **account_id** | **str**| This parameter filters the response based on the &#x60;accountId&#x60; field.  | [optional] 
 **amount** | **float**| This parameter filters the response based on the &#x60;amount&#x60; field.  | [optional] 
 **created_by_id** | **str**| This parameter filters the response based on the &#x60;createdById&#x60; field.  | [optional] 
 **created_date** | **datetime**| This parameter filters the response based on the &#x60;createdDate&#x60; field.  | [optional] 
 **method_type** | **str**| This parameter filters the response based on the &#x60;methodType&#x60; field.  | [optional] 
 **number** | **str**| This parameter filters the response based on the &#x60;number&#x60; field.  | [optional] 
 **payment_id** | **str**| This parameter filters the response based on the &#x60;paymentId&#x60; field.  | [optional] 
 **refund_date** | **date**| This parameter filters the response based on the &#x60;refundDate&#x60; field.  | [optional] 
 **status** | **str**| This parameter filters the response based on the &#x60;status&#x60; field.  | [optional] 
 **type** | **str**| This parameter filters the response based on the &#x60;type&#x60; field.  | [optional] 
 **updated_by_id** | **str**| This parameter filters the response based on the &#x60;updatedById&#x60; field.  | [optional] 
 **updated_date** | **datetime**| This parameter filters the response based on the &#x60;updatedDate&#x60; field.  | [optional] 
 **sort** | **str**| This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The &#x60;-&#x60; operator indicates an ascending order.   - The &#x60;+&#x60; operator indicates a descending order.  By default, the response data is displayed in descending order by refund number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - number   - accountId   - amount   - refundDate   - paymentId   - createdDate   - createdById   - updatedDate   - updatedById    Examples:  - /v1/refunds?sort&#x3D;+number  - /v1/refunds?status&#x3D;Processed&amp;sort&#x3D;-number,+amount  | [optional] 

### Return type

[**GETRefundCollectionType**](GETRefundCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_delete_refund**
> ProxyDeleteResponse object_delete_refund(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Delete refund



### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Delete refund
    api_response = api_instance.object_delete_refund(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->object_delete_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**ProxyDeleteResponse**](ProxyDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_get_refund**
> ProxyGetRefund object_get_refund(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, fields=fields)

CRUD: Get refund



### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
id = 'id_example' # str | Object id
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
fields = 'fields_example' # str | Object fields to return (optional)

try:
    # CRUD: Get refund
    api_response = api_instance.object_get_refund(id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->object_get_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **fields** | **str**| Object fields to return | [optional] 

### Return type

[**ProxyGetRefund**](ProxyGetRefund.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_post_refund**
> ProxyCreateOrModifyResponse object_post_refund(create_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Create refund



### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
create_request = zuora_client.ProxyCreateRefund() # ProxyCreateRefund | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Create refund
    api_response = api_instance.object_post_refund(create_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->object_post_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request** | [**ProxyCreateRefund**](ProxyCreateRefund.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**ProxyCreateOrModifyResponse**](ProxyCreateOrModifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_put_refund**
> ProxyCreateOrModifyResponse object_put_refund(id, modify_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

CRUD: Update refund



### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
id = 'id_example' # str | Object id
modify_request = zuora_client.ProxyModifyRefund() # ProxyModifyRefund | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # CRUD: Update refund
    api_response = api_instance.object_put_refund(id, modify_request, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->object_put_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Object id | 
 **modify_request** | [**ProxyModifyRefund**](ProxyModifyRefund.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**ProxyCreateOrModifyResponse**](ProxyCreateOrModifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_cancel_refund**
> GETRefundType p_ut_cancel_refund(refund_id, zuora_entity_ids=zuora_entity_ids)

Cancel refund

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Cancels a refund.  If you have the Invoice Settlement feature enabled, refunds applied to credit balance cannot be cancelled. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
refund_id = 'refund_id_example' # str | The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9.       
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Cancel refund
    api_response = api_instance.p_ut_cancel_refund(refund_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->p_ut_cancel_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9.        | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRefundType**](GETRefundType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_update_refund**
> GETRefundType p_ut_update_refund(body, refund_id, zuora_entity_ids=zuora_entity_ids)

Update refund

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Updates the basic and finance information about a refund. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.RefundsApi()
body = zuora_client.PUTRefundType() # PUTRefundType | 
refund_id = 'refund_id_example' # str | The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update refund
    api_response = api_instance.p_ut_update_refund(body, refund_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->p_ut_update_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTRefundType**](PUTRefundType.md)|  | 
 **refund_id** | **str**| The unique ID of a refund. For example, 4028905f5a87c0ff015a889e590e00c9.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETRefundType**](GETRefundType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

