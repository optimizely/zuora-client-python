# swagger_client.AccountingCodesApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_accounting_code**](AccountingCodesApi.md#d_elete_accounting_code) | **DELETE** /v1/accounting-codes/{ac-id} | Delete accounting code
[**g_et_accounting_code**](AccountingCodesApi.md#g_et_accounting_code) | **GET** /v1/accounting-codes/{ac-id} | Query an accounting code
[**g_et_all_accounting_codes**](AccountingCodesApi.md#g_et_all_accounting_codes) | **GET** /v1/accounting-codes | Get all accounting codes
[**p_ost_accounting_code**](AccountingCodesApi.md#p_ost_accounting_code) | **POST** /v1/accounting-codes | Create accounting code
[**p_ut_accounting_code**](AccountingCodesApi.md#p_ut_accounting_code) | **PUT** /v1/accounting-codes/{ac-id} | Update an accounting code
[**p_ut_activate_accounting_code**](AccountingCodesApi.md#p_ut_activate_accounting_code) | **PUT** /v1/accounting-codes/{ac-id}/activate | Activate accounting code
[**p_ut_deactivate_accounting_code**](AccountingCodesApi.md#p_ut_deactivate_accounting_code) | **PUT** /v1/accounting-codes/{ac-id}/deactivate | Deactivate accounting code

# **d_elete_accounting_code**
> CommonResponseType d_elete_accounting_code(ac_id, zuora_entity_ids=zuora_entity_ids)

Delete accounting code

This reference describes how to delete an accounting code through the REST API. ## Prerequisites If you have Zuora Finance enabled on your tenant, then you must have the Delete Unused Accounting Code permission. ## Limitations You can only delete accounting codes that have never been associated with any transactions. An accounting code must be deactivated before you can delete it. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingCodesApi()
ac_id = 'ac_id_example' # str | ID of the accounting code you want to delete.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete accounting code
    api_response = api_instance.d_elete_accounting_code(ac_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->d_elete_accounting_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ac_id** | **str**| ID of the accounting code you want to delete. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_accounting_code**
> GETAccountingCodeItemType g_et_accounting_code(ac_id, zuora_entity_ids=zuora_entity_ids)

Query an accounting code

This reference describes how to query an accounting code through the REST API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingCodesApi()
ac_id = 'ac_id_example' # str | ID of the accounting code you want to query.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Query an accounting code
    api_response = api_instance.g_et_accounting_code(ac_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->g_et_accounting_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ac_id** | **str**| ID of the accounting code you want to query. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETAccountingCodeItemType**](GETAccountingCodeItemType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_all_accounting_codes**
> GETAccountingCodesType g_et_all_accounting_codes(zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get all accounting codes

This reference describes how to query all accounting codes in your chart of accounts through the REST API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingCodesApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)

try:
    # Get all accounting codes
    api_response = api_instance.g_et_all_accounting_codes(zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->g_et_all_accounting_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 

### Return type

[**GETAccountingCodesType**](GETAccountingCodesType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_accounting_code**
> POSTAccountingCodeResponseType p_ost_accounting_code(body, zuora_entity_ids=zuora_entity_ids)

Create accounting code

This reference describes how to create a new accounting code through the REST API.  The accounting code will be active as soon as it has been created.  ## Prerequisites   If you have Zuora Finance enabled on your tenant, you must have the  Configure Accounting Codes permission.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingCodesApi()
body = swagger_client.Object() # Object | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create accounting code
    api_response = api_instance.p_ost_accounting_code(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->p_ost_accounting_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTAccountingCodeResponseType**](POSTAccountingCodeResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_accounting_code**
> CommonResponseType p_ut_accounting_code(body, ac_id, zuora_entity_ids=zuora_entity_ids)

Update an accounting code

This reference describes how to update an existing accounting code through the REST API. ## Prerequisites   If you have Zuora Finance enabled on your tenant, you must have the  Manage Accounting Code permission.  ## Limitations You can only update accounting codes that are not already associated with any transactions. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingCodesApi()
body = swagger_client.Object() # Object | 
ac_id = 'ac_id_example' # str | ID of the accounting code you want to update.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update an accounting code
    api_response = api_instance.p_ut_accounting_code(body, ac_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->p_ut_accounting_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)|  | 
 **ac_id** | **str**| ID of the accounting code you want to update. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_activate_accounting_code**
> CommonResponseType p_ut_activate_accounting_code(ac_id, zuora_entity_ids=zuora_entity_ids)

Activate accounting code

This reference describes how to activate an accounting code through the REST API.  Prerequisites ------------- If you have Zuora Finance enabled on your tenant, you must have the Manage Accounting Code permission.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingCodesApi()
ac_id = 'ac_id_example' # str | ID of the accounting code you want to activate.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Activate accounting code
    api_response = api_instance.p_ut_activate_accounting_code(ac_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->p_ut_activate_accounting_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ac_id** | **str**| ID of the accounting code you want to activate. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_deactivate_accounting_code**
> CommonResponseType p_ut_deactivate_accounting_code(ac_id, zuora_entity_ids=zuora_entity_ids)

Deactivate accounting code

This reference describes how to deactivate an accounting code through the REST API.  ## Prerequisites If you have Zuora Finance enabled on your tenant, you must have the Manage Accounting Code permission. ## Limitations You can only deactivate accounting codes that are not associated with any transactions.  You cannot disable accounting codes of type AccountsReceivable. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingCodesApi()
ac_id = 'ac_id_example' # str | ID of the accounting code you want to deactivate.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Deactivate accounting code
    api_response = api_instance.p_ut_deactivate_accounting_code(ac_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->p_ut_deactivate_accounting_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ac_id** | **str**| ID of the accounting code you want to deactivate. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

