# zuora_client.DebitMemosApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_debit_memo**](DebitMemosApi.md#d_elete_debit_memo) | **DELETE** /v1/debitmemos/{debitMemoId} | Delete debit memo
[**g_et_debit_memo**](DebitMemosApi.md#g_et_debit_memo) | **GET** /v1/debitmemos/{debitMemoId} | Get debit memo
[**g_et_debit_memo_application_parts**](DebitMemosApi.md#g_et_debit_memo_application_parts) | **GET** /v1/debitmemos/{debitMemoId}/application-parts | Get debit memo application parts
[**g_et_debit_memo_item**](DebitMemosApi.md#g_et_debit_memo_item) | **GET** /v1/debitmemos/{debitMemoId}/items/{dmitemid} | Get debit memo item
[**g_et_debit_memo_items**](DebitMemosApi.md#g_et_debit_memo_items) | **GET** /v1/debitmemos/{debitMemoId}/items | Get debit memo items
[**g_et_debit_memos**](DebitMemosApi.md#g_et_debit_memos) | **GET** /v1/debitmemos | Get debit memos
[**g_et_taxation_items_of_debit_memo_item**](DebitMemosApi.md#g_et_taxation_items_of_debit_memo_item) | **GET** /v1/debitmemos/{debitMemoId}/items/{dmitemid}/taxation-items | Get taxation items of debit memo item
[**p_ost_debit_memo_from_prpc**](DebitMemosApi.md#p_ost_debit_memo_from_prpc) | **POST** /v1/debitmemos | Create debit memo from charge
[**p_ost_debit_memo_pdf**](DebitMemosApi.md#p_ost_debit_memo_pdf) | **POST** /v1/debitmemos/{debitMemoId}/pdfs | Create debit memo PDF
[**p_ost_email_debit_memo**](DebitMemosApi.md#p_ost_email_debit_memo) | **POST** /v1/debitmemos/{debitMemoId}/emails | Email debit memo
[**p_ost_upload_file_for_debit_memo**](DebitMemosApi.md#p_ost_upload_file_for_debit_memo) | **POST** /v1/debitmemos/{debitMemoId} | Upload file for debit memo
[**p_ostdm_taxation_items**](DebitMemosApi.md#p_ostdm_taxation_items) | **POST** /v1/debitmemos/{debitMemoId}/taxationitems | Create taxation items for debit memo
[**p_ut_batch_update_debit_memos**](DebitMemosApi.md#p_ut_batch_update_debit_memos) | **PUT** /v1/debitmemos | Update debit memos
[**p_ut_cancel_debit_memo**](DebitMemosApi.md#p_ut_cancel_debit_memo) | **PUT** /v1/debitmemos/{debitMemoId}/cancel | Cancel debit memo
[**p_ut_debit_memo**](DebitMemosApi.md#p_ut_debit_memo) | **PUT** /v1/debitmemos/{debitMemoId} | Update debit memo
[**p_ut_post_debit_memo**](DebitMemosApi.md#p_ut_post_debit_memo) | **PUT** /v1/debitmemos/{debitMemoId}/post | Post debit memo
[**p_ut_unpost_debit_memo**](DebitMemosApi.md#p_ut_unpost_debit_memo) | **PUT** /v1/debitmemos/{debitMemoId}/unpost | Unpost debit memo

# **d_elete_debit_memo**
> CommonResponseType d_elete_debit_memo(debit_memo_id, zuora_entity_ids=zuora_entity_ids)

Delete debit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Deletes a debit memo. Only debit memos with the Cancelled status can be deleted.   You can delete a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete debit memo
    api_response = api_instance.d_elete_debit_memo(debit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->d_elete_debit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debit_memo_id** | **str**| The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_debit_memo**
> GETDebitMemoType g_et_debit_memo(debit_memo_id, zuora_entity_ids=zuora_entity_ids)

Get debit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific debit memo. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get debit memo
    api_response = api_instance.g_et_debit_memo(debit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->g_et_debit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debit_memo_id** | **str**| The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETDebitMemoType**](GETDebitMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_debit_memo_application_parts**
> GetDebitMemoApplicationPartCollectionType g_et_debit_memo_application_parts(debit_memo_id, zuora_entity_ids=zuora_entity_ids)

Get debit memo application parts

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves information about the payments or credit memos that are applied to a specified debit memo. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get debit memo application parts
    api_response = api_instance.g_et_debit_memo_application_parts(debit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->g_et_debit_memo_application_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debit_memo_id** | **str**| The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GetDebitMemoApplicationPartCollectionType**](GetDebitMemoApplicationPartCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_debit_memo_item**
> GETDebitMemoItemType g_et_debit_memo_item(dmitemid, debit_memo_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Get debit memo item

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves information about a specific item of a debit memo. A debit memo item is a single line item in a debit memo. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
dmitemid = 'dmitemid_example' # str | The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems). 
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str |  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * taxItems * taxationItems  (optional)

try:
    # Get debit memo item
    api_response = api_instance.g_et_debit_memo_item(dmitemid, debit_memo_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->g_et_debit_memo_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dmitemid** | **str**| The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  | 
 **debit_memo_id** | **str**| The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**|  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * taxItems * taxationItems  | [optional] 

### Return type

[**GETDebitMemoItemType**](GETDebitMemoItemType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_debit_memo_items**
> GETDebitMemoItemCollectionType g_et_debit_memo_items(debit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, zuora_version=zuora_version, amount=amount, be_applied_amount=be_applied_amount, created_by_id=created_by_id, created_date=created_date, id=id, service_end_date=service_end_date, service_start_date=service_start_date, sku=sku, sku_name=sku_name, source_item_id=source_item_id, subscription_id=subscription_id, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)

Get debit memo items

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all items of a debit memo. A debit memo item is a single line item in a debit memo.   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100&sort=createdDate 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
zuora_version = 'zuora_version_example' # str |  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * taxItems * taxationItems  (optional)
amount = 1.2 # float | This parameter filters the response based on the `amount` field.  (optional)
be_applied_amount = 1.2 # float | This parameter filters the response based on the `beAppliedAmount` field.  (optional)
created_by_id = 'created_by_id_example' # str | This parameter filters the response based on the `createdById` field.  (optional)
created_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `createdDate` field.  (optional)
id = 'id_example' # str | This parameter filters the response based on the `id` field.  (optional)
service_end_date = '2013-10-20' # date | This parameter filters the response based on the `serviceEndDate` field.  (optional)
service_start_date = '2013-10-20' # date | This parameter filters the response based on the `serviceStartDate` field.  (optional)
sku = 'sku_example' # str | This parameter filters the response based on the `sku` field.  (optional)
sku_name = 'sku_name_example' # str | This parameter filters the response based on the `skuName` field.  (optional)
source_item_id = 'source_item_id_example' # str | This parameter filters the response based on the `sourceItemId` field.  (optional)
subscription_id = 'subscription_id_example' # str | This parameter filters the response based on the `subscriptionId` field.  (optional)
updated_by_id = 'updated_by_id_example' # str | This parameter filters the response based on the `updatedById` field.  (optional)
updated_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `updatedDate` field.  (optional)
sort = 'sort_example' # str | This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by updated date.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - id   - amount   - beAppliedAmount   - sku   - skuName   - serviceStartDate   - serviceEndDate   - sourceItemId   - createdDate   - createdById   - updatedDate   - updatedById   - subscriptionId    Examples:  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?sort=createdDate  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100&sort=createdDate  (optional)

try:
    # Get debit memo items
    api_response = api_instance.g_et_debit_memo_items(debit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, zuora_version=zuora_version, amount=amount, be_applied_amount=be_applied_amount, created_by_id=created_by_id, created_date=created_date, id=id, service_end_date=service_end_date, service_start_date=service_start_date, sku=sku, sku_name=sku_name, source_item_id=source_item_id, subscription_id=subscription_id, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->g_et_debit_memo_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debit_memo_id** | **str**| The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **zuora_version** | **str**|  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * taxItems * taxationItems  | [optional] 
 **amount** | **float**| This parameter filters the response based on the &#x60;amount&#x60; field.  | [optional] 
 **be_applied_amount** | **float**| This parameter filters the response based on the &#x60;beAppliedAmount&#x60; field.  | [optional] 
 **created_by_id** | **str**| This parameter filters the response based on the &#x60;createdById&#x60; field.  | [optional] 
 **created_date** | **datetime**| This parameter filters the response based on the &#x60;createdDate&#x60; field.  | [optional] 
 **id** | **str**| This parameter filters the response based on the &#x60;id&#x60; field.  | [optional] 
 **service_end_date** | **date**| This parameter filters the response based on the &#x60;serviceEndDate&#x60; field.  | [optional] 
 **service_start_date** | **date**| This parameter filters the response based on the &#x60;serviceStartDate&#x60; field.  | [optional] 
 **sku** | **str**| This parameter filters the response based on the &#x60;sku&#x60; field.  | [optional] 
 **sku_name** | **str**| This parameter filters the response based on the &#x60;skuName&#x60; field.  | [optional] 
 **source_item_id** | **str**| This parameter filters the response based on the &#x60;sourceItemId&#x60; field.  | [optional] 
 **subscription_id** | **str**| This parameter filters the response based on the &#x60;subscriptionId&#x60; field.  | [optional] 
 **updated_by_id** | **str**| This parameter filters the response based on the &#x60;updatedById&#x60; field.  | [optional] 
 **updated_date** | **datetime**| This parameter filters the response based on the &#x60;updatedDate&#x60; field.  | [optional] 
 **sort** | **str**| This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The &#x60;-&#x60; operator indicates an ascending order.   - The &#x60;+&#x60; operator indicates a descending order.  By default, the response data is displayed in descending order by updated date.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - id   - amount   - beAppliedAmount   - sku   - skuName   - serviceStartDate   - serviceEndDate   - sourceItemId   - createdDate   - createdById   - updatedDate   - updatedById   - subscriptionId    Examples:  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?sort&#x3D;createdDate  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount&#x3D;100&amp;sort&#x3D;createdDate  | [optional] 

### Return type

[**GETDebitMemoItemCollectionType**](GETDebitMemoItemCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_debit_memos**
> GETDebitMemoCollectionType g_et_debit_memos(zuora_entity_ids=zuora_entity_ids, page_size=page_size, account_id=account_id, amount=amount, balance=balance, be_applied_amount=be_applied_amount, created_by_id=created_by_id, created_date=created_date, currency=currency, debit_memo_date=debit_memo_date, due_date=due_date, number=number, referred_invoice_id=referred_invoice_id, status=status, target_date=target_date, tax_amount=tax_amount, total_tax_exempt_amount=total_tax_exempt_amount, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)

Get debit memos

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the information about all debit memos associated with all customer accounts.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/debitmemos?status=Processed  - /v1/debitmemos?referredInvoiceId=null&status=Draft  - /v1/debitmemos?status=Processed&type=External&sort=+number 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
account_id = 'account_id_example' # str | This parameter filters the response based on the `accountId` field.  (optional)
amount = 1.2 # float | This parameter filters the response based on the `amount` field.  (optional)
balance = 1.2 # float | This parameter filters the response based on the `balance` field.  (optional)
be_applied_amount = 1.2 # float | This parameter filters the response based on the `beAppliedAmount` field.  (optional)
created_by_id = 'created_by_id_example' # str | This parameter filters the response based on the `createdById` field.  (optional)
created_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `createdDate` field.  (optional)
currency = 'currency_example' # str | This parameter filters the response based on the `currency` field.  (optional)
debit_memo_date = '2013-10-20' # date | This parameter filters the response based on the `debitMemoDate` field.  (optional)
due_date = '2013-10-20' # date | This parameter filters the response based on the `dueDate` field.  (optional)
number = 'number_example' # str | This parameter filters the response based on the `number` field.  (optional)
referred_invoice_id = 'referred_invoice_id_example' # str | This parameter filters the response based on the `referredInvoiceId` field.  (optional)
status = 'status_example' # str | This parameter filters the response based on the `status` field.  (optional)
target_date = '2013-10-20' # date | This parameter filters the response based on the `targetDate` field.  (optional)
tax_amount = 1.2 # float | This parameter filters the response based on the `taxAmount` field.  (optional)
total_tax_exempt_amount = 1.2 # float | This parameter filters the response based on the `totalTaxExemptAmount` field.  (optional)
updated_by_id = 'updated_by_id_example' # str | This parameter filters the response based on the `updatedById` field.  (optional)
updated_date = '2013-10-20T19:20:30+01:00' # datetime | This parameter filters the response based on the `updatedDate` field.  (optional)
sort = 'sort_example' # str | This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by debit memo number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - number   - accountId   - debitMemoDate   - targetDate   - dueDate   - amount   - taxAmount   - totalTaxExemptAmount   - balance   - beAppliedAmount   - referredInvoiceId   - createdDate   - createdById   - updatedDate   - updatedById    Examples:  - /v1/debitmemos?sort=+number  - /v1/debitmemos?status=Processed&sort=-number,+amount  (optional)

try:
    # Get debit memos
    api_response = api_instance.g_et_debit_memos(zuora_entity_ids=zuora_entity_ids, page_size=page_size, account_id=account_id, amount=amount, balance=balance, be_applied_amount=be_applied_amount, created_by_id=created_by_id, created_date=created_date, currency=currency, debit_memo_date=debit_memo_date, due_date=due_date, number=number, referred_invoice_id=referred_invoice_id, status=status, target_date=target_date, tax_amount=tax_amount, total_tax_exempt_amount=total_tax_exempt_amount, updated_by_id=updated_by_id, updated_date=updated_date, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->g_et_debit_memos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **account_id** | **str**| This parameter filters the response based on the &#x60;accountId&#x60; field.  | [optional] 
 **amount** | **float**| This parameter filters the response based on the &#x60;amount&#x60; field.  | [optional] 
 **balance** | **float**| This parameter filters the response based on the &#x60;balance&#x60; field.  | [optional] 
 **be_applied_amount** | **float**| This parameter filters the response based on the &#x60;beAppliedAmount&#x60; field.  | [optional] 
 **created_by_id** | **str**| This parameter filters the response based on the &#x60;createdById&#x60; field.  | [optional] 
 **created_date** | **datetime**| This parameter filters the response based on the &#x60;createdDate&#x60; field.  | [optional] 
 **currency** | **str**| This parameter filters the response based on the &#x60;currency&#x60; field.  | [optional] 
 **debit_memo_date** | **date**| This parameter filters the response based on the &#x60;debitMemoDate&#x60; field.  | [optional] 
 **due_date** | **date**| This parameter filters the response based on the &#x60;dueDate&#x60; field.  | [optional] 
 **number** | **str**| This parameter filters the response based on the &#x60;number&#x60; field.  | [optional] 
 **referred_invoice_id** | **str**| This parameter filters the response based on the &#x60;referredInvoiceId&#x60; field.  | [optional] 
 **status** | **str**| This parameter filters the response based on the &#x60;status&#x60; field.  | [optional] 
 **target_date** | **date**| This parameter filters the response based on the &#x60;targetDate&#x60; field.  | [optional] 
 **tax_amount** | **float**| This parameter filters the response based on the &#x60;taxAmount&#x60; field.  | [optional] 
 **total_tax_exempt_amount** | **float**| This parameter filters the response based on the &#x60;totalTaxExemptAmount&#x60; field.  | [optional] 
 **updated_by_id** | **str**| This parameter filters the response based on the &#x60;updatedById&#x60; field.  | [optional] 
 **updated_date** | **datetime**| This parameter filters the response based on the &#x60;updatedDate&#x60; field.  | [optional] 
 **sort** | **str**| This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The &#x60;-&#x60; operator indicates an ascending order.   - The &#x60;+&#x60; operator indicates a descending order.  By default, the response data is displayed in descending order by debit memo number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - number   - accountId   - debitMemoDate   - targetDate   - dueDate   - amount   - taxAmount   - totalTaxExemptAmount   - balance   - beAppliedAmount   - referredInvoiceId   - createdDate   - createdById   - updatedDate   - updatedById    Examples:  - /v1/debitmemos?sort&#x3D;+number  - /v1/debitmemos?status&#x3D;Processed&amp;sort&#x3D;-number,+amount  | [optional] 

### Return type

[**GETDebitMemoCollectionType**](GETDebitMemoCollectionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_taxation_items_of_debit_memo_item**
> GETTaxationItemsOfDebitMemoItemType g_et_taxation_items_of_debit_memo_item(dmitemid, debit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, page=page)

Get taxation items of debit memo item

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves information about the taxation items of a specific debit memo item. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
dmitemid = 'dmitemid_example' # str | The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems). 
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
page = 56 # int | Page number.  (optional)

try:
    # Get taxation items of debit memo item
    api_response = api_instance.g_et_taxation_items_of_debit_memo_item(dmitemid, debit_memo_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->g_et_taxation_items_of_debit_memo_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dmitemid** | **str**| The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  | 
 **debit_memo_id** | **str**| The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **page** | **int**| Page number.  | [optional] 

### Return type

[**GETTaxationItemsOfDebitMemoItemType**](GETTaxationItemsOfDebitMemoItemType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_debit_memo_from_prpc**
> GETDebitMemoType p_ost_debit_memo_from_prpc(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Create debit memo from charge

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates an ad-hoc debit memo from a product rate plan charge. Zuora supports the creation of debit memos from any type of product rate plan charge. The charges can also have any amount and any charge model, except for discout charge models.   You can create a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
body = zuora_client.DebitMemoFromChargeType() # DebitMemoFromChargeType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str |  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * amount * memoItemAmount  (optional)

try:
    # Create debit memo from charge
    api_response = api_instance.p_ost_debit_memo_from_prpc(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->p_ost_debit_memo_from_prpc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DebitMemoFromChargeType**](DebitMemoFromChargeType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**|  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * amount * memoItemAmount  | [optional] 

### Return type

[**GETDebitMemoType**](GETDebitMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_debit_memo_pdf**
> POSTMemoPdfResponse p_ost_debit_memo_pdf(debit_memo_id, zuora_entity_ids=zuora_entity_ids)

Create debit memo PDF

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a PDF file for a specified debit memo. To access the generated PDF file, you can download it by clicking **View PDF** on the detailed debit memo page through the Zuora UI.  This REST API operation can be used only if you have the Billing user permission \"Regenerate PDF\" enabled. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of the debit memo that you want to create a PDF file for. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create debit memo PDF
    api_response = api_instance.p_ost_debit_memo_pdf(debit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->p_ost_debit_memo_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debit_memo_id** | **str**| The unique ID of the debit memo that you want to create a PDF file for. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTMemoPdfResponse**](POSTMemoPdfResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_email_debit_memo**
> CommonResponseType p_ost_email_debit_memo(body, debit_memo_id, zuora_entity_ids=zuora_entity_ids)

Email debit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Sends a posted debit memo to the specified email addresses manually.    ## Notes   - You must activate the **Email Debit Memo | Manually email Debit Memo** notification before emailing debit memos. To include the debit memo PDF in the email, select the **Include Debit Memo PDF** check box in the **Edit notification** dialog from the Zuora UI. See [Create and Edit Notifications](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/C_Create_Notifications#section_2) for more information.     - Zuora sends the email messages based on the email template you set. You can set the email template to use in the **Delivery Options** panel of the **Edit notification** dialog from the Zuora UI. By default, the **Manual Email for Debit Memo Default Template** template is used. See [Create and Edit Email Templates](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/Create_Email_Templates) for more information.     - The debit memos are sent only to the work email addresses or personal email addresses of the Bill To contact if the following conditions are all met:      * The `useEmailTemplateSetting` field is set to `false`.     * The email addresses are not specified in the `emailAddresses` field. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
body = zuora_client.PostDebitMemoEmailType() # PostDebitMemoEmailType | 
debit_memo_id = 'debit_memo_id_example' # str | The ID of a posted debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Email debit memo
    api_response = api_instance.p_ost_email_debit_memo(body, debit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->p_ost_email_debit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDebitMemoEmailType**](PostDebitMemoEmailType.md)|  | 
 **debit_memo_id** | **str**| The ID of a posted debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_upload_file_for_debit_memo**
> POSTUploadFileResponse p_ost_upload_file_for_debit_memo(debit_memo_id, file=file, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Upload file for debit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Uploads an externally generated PDF file for a debit memo that is in Draft or Posted status.  This operation has the following restrictions: - Only the PDF file format is supported. - The maximum size of the PDF file to upload is 4 MB. - A maximum of 50 PDF files can be uploaded for one debit memo. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
debit_memo_id = 'debit_memo_id_example' # str | The ID of the debit memo that you want to upload a PDF file for. For example, 402890555a87d7f5015a8919e4fe002e. 
file = 'file_example' # file |  (optional)
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Upload file for debit memo
    api_response = api_instance.p_ost_upload_file_for_debit_memo(debit_memo_id, file=file, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->p_ost_upload_file_for_debit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debit_memo_id** | **str**| The ID of the debit memo that you want to upload a PDF file for. For example, 402890555a87d7f5015a8919e4fe002e.  | 
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

# **p_ostdm_taxation_items**
> GETTaxationItemListType p_ostdm_taxation_items(body, debit_memo_id, zuora_entity_ids=zuora_entity_ids)

Create taxation items for debit memo

**Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates taxation items for a debit memo. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
body = zuora_client.POSTTaxationItemListForDMType() # POSTTaxationItemListForDMType | 
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create taxation items for debit memo
    api_response = api_instance.p_ostdm_taxation_items(body, debit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->p_ostdm_taxation_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTTaxationItemListForDMType**](POSTTaxationItemListForDMType.md)|  | 
 **debit_memo_id** | **str**| The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETTaxationItemListType**](GETTaxationItemListType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_batch_update_debit_memos**
> CommonResponseType p_ut_batch_update_debit_memos(body, zuora_entity_ids=zuora_entity_ids)

Update debit memos

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Updates the due date for multiple debit memos in batches with one call.  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
body = zuora_client.PUTBatchDebitMemosRequest() # PUTBatchDebitMemosRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update debit memos
    api_response = api_instance.p_ut_batch_update_debit_memos(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->p_ut_batch_update_debit_memos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTBatchDebitMemosRequest**](PUTBatchDebitMemosRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_cancel_debit_memo**
> GETDebitMemoType p_ut_cancel_debit_memo(debit_memo_id, zuora_entity_ids=zuora_entity_ids)

Cancel debit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Cancels a debit memo. Only debit memos with the Draft status can be cancelled.   You can cancel a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Cancel debit memo
    api_response = api_instance.p_ut_cancel_debit_memo(debit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->p_ut_cancel_debit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debit_memo_id** | **str**| The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETDebitMemoType**](GETDebitMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_debit_memo**
> GETDebitMemoType p_ut_debit_memo(body, debit_memo_id, zuora_entity_ids=zuora_entity_ids)

Update debit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Updates the basic and finance information about a debit memo. Currently, Zuora supports updating tax-exclusive memo items, but does not support updating tax-inclusive memo items.   If the amount of a memo item is updated, the tax will be recalculated in the following conditions:   - The memo is created from a product rate plan charge and you use Avalara to calculate the tax.   - The memo is created from an invoice and you use Avalara or Zuora Tax to calculate the tax.  You can update a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
body = zuora_client.PUTDebitMemoType() # PUTDebitMemoType | 
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update debit memo
    api_response = api_instance.p_ut_debit_memo(body, debit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->p_ut_debit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PUTDebitMemoType**](PUTDebitMemoType.md)|  | 
 **debit_memo_id** | **str**| The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETDebitMemoType**](GETDebitMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_post_debit_memo**
> GETDebitMemoType p_ut_post_debit_memo(debit_memo_id, zuora_entity_ids=zuora_entity_ids)

Post debit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Posts a debit memo to activate it. You can post debit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Post debit memo
    api_response = api_instance.p_ut_post_debit_memo(debit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->p_ut_post_debit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debit_memo_id** | **str**| The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETDebitMemoType**](GETDebitMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_unpost_debit_memo**
> GETDebitMemoType p_ut_unpost_debit_memo(debit_memo_id, zuora_entity_ids=zuora_entity_ids)

Unpost debit memo

**Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Unposts a debit memo that is in Posted status. If any credit memo or payment has been applied to a debit memo, you are not allowed to unpost the debit memo. After a debit memo is unposted, its status becomes Draft.  You can unpost debit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions). 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.DebitMemosApi()
debit_memo_id = 'debit_memo_id_example' # str | The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Unpost debit memo
    api_response = api_instance.p_ut_unpost_debit_memo(debit_memo_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebitMemosApi->p_ut_unpost_debit_memo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debit_memo_id** | **str**| The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETDebitMemoType**](GETDebitMemoType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

