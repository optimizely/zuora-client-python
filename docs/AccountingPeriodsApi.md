# zuora_client.AccountingPeriodsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_accounting_period**](AccountingPeriodsApi.md#d_elete_accounting_period) | **DELETE** /v1/accounting-periods/{ap-id} | Delete accounting period
[**g_et_accounting_period**](AccountingPeriodsApi.md#g_et_accounting_period) | **GET** /v1/accounting-periods/{ap-id} | Get accounting period
[**g_et_all_accounting_periods**](AccountingPeriodsApi.md#g_et_all_accounting_periods) | **GET** /v1/accounting-periods | Get all accounting periods
[**p_ost_accounting_period**](AccountingPeriodsApi.md#p_ost_accounting_period) | **POST** /v1/accounting-periods | Create accounting period
[**p_ut_close_accounting_period**](AccountingPeriodsApi.md#p_ut_close_accounting_period) | **PUT** /v1/accounting-periods/{ap-id}/close | Close accounting period
[**p_ut_pending_close_accounting_period**](AccountingPeriodsApi.md#p_ut_pending_close_accounting_period) | **PUT** /v1/accounting-periods/{ap-id}/pending-close | Set accounting period to pending close
[**p_ut_reopen_accounting_period**](AccountingPeriodsApi.md#p_ut_reopen_accounting_period) | **PUT** /v1/accounting-periods/{ap-id}/reopen | Re-open accounting period
[**p_ut_run_trial_balance**](AccountingPeriodsApi.md#p_ut_run_trial_balance) | **PUT** /v1/accounting-periods/{ap-id}/run-trial-balance | Run trial balance
[**p_ut_update_accounting_period**](AccountingPeriodsApi.md#p_ut_update_accounting_period) | **PUT** /v1/accounting-periods/{ap-id} | Update accounting period


# **d_elete_accounting_period**
> CommonResponseType d_elete_accounting_period(ap_id, zuora_entity_ids=zuora_entity_ids)

Delete accounting period

 Deletes an accounting period.  Prerequisites -------------   * You must have Zuora Finance enabled on your tenant.   * You must have the Delete Accounting Period user permission. See [Finance Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/f_Finance_Roles).   Limitations -----------  The accounting period to be deleted:  * Must be the most recent accounting period  * Must be an open accounting period  * Must have no revenue distributed into it  * Must not have any active journal entries  * Must not be the open-ended accounting period  * Must not be in the process of running a trial balance 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AccountingPeriodsApi()
ap_id = 'ap_id_example' # str | ID of the accounting period you want to delete.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete accounting period
    api_response = api_instance.d_elete_accounting_period(ap_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingPeriodsApi->d_elete_accounting_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ap_id** | **str**| ID of the accounting period you want to delete. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_accounting_period**
> GETAccountingPeriodType g_et_accounting_period(ap_id, zuora_entity_ids=zuora_entity_ids)

Get accounting period

Retrieves an accounting period. Prerequisites -------------  You must have Zuora Finance enabled on your tenant. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AccountingPeriodsApi()
ap_id = 'ap_id_example' # str | ID of the accounting period you want to get.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get accounting period
    api_response = api_instance.g_et_accounting_period(ap_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingPeriodsApi->g_et_accounting_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ap_id** | **str**| ID of the accounting period you want to get. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETAccountingPeriodType**](GETAccountingPeriodType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_all_accounting_periods**
> GETAccountingPeriodsType g_et_all_accounting_periods(zuora_entity_ids=zuora_entity_ids, page_size=page_size)

Get all accounting periods

Retrieves all accounting periods on your tenant.

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AccountingPeriodsApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 300 # int | Number of rows returned per page.  (optional) (default to 300)

try:
    # Get all accounting periods
    api_response = api_instance.g_et_all_accounting_periods(zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingPeriodsApi->g_et_all_accounting_periods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] [default to 300]

### Return type

[**GETAccountingPeriodsType**](GETAccountingPeriodsType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_accounting_period**
> POSTAccountingPeriodResponseType p_ost_accounting_period(request, zuora_entity_ids=zuora_entity_ids)

Create accounting period

Creates an accounting period. Prerequisites ------------- * You must have Zuora Finance enabled on your tenant. * You must have the Create Accounting Period user permission.  Limitations ----------- * When creating the first accounting period on your tenant, the start date must be equal to or earlier than the date of the earliest transaction on the tenant. * Start and end dates of accounting periods must be contiguous. For example, if one accounting period ends on January 31, the next period must start on February 1. * If you have the Revenue Recognition Package and have enabled the \"Monthly recognition over time\" revenue recognition model, the accounting period start date and end date must be on the first day and last day of the month, respectively. Note that the start and end dates do not necessarily have to be in the same month.

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AccountingPeriodsApi()
request = zuora_client.POSTAccountingPeriodType() # POSTAccountingPeriodType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create accounting period
    api_response = api_instance.p_ost_accounting_period(request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingPeriodsApi->p_ost_accounting_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**POSTAccountingPeriodType**](POSTAccountingPeriodType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTAccountingPeriodResponseType**](POSTAccountingPeriodResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_close_accounting_period**
> CommonResponseType p_ut_close_accounting_period(ap_id, zuora_entity_ids=zuora_entity_ids)

Close accounting period

Close an accounting period by accounting period ID.  Prerequisites ------------- You must have Zuora Finance enabled on your tenant. You must have the Manage Close Process and Run Trial Balance user permissions.  Limitations ----------- * The accounting period cannot already be closed. * The accounting period cannot be in the process of running a trial balance. * All earlier accounting periods must be closed. * There must be no required action items for the accounting period. See Reconcile Transactions Before Closing an Accounting Period for more information.  Notes ----- When you close an accounting period in Zuora, a trial balance is automatically run for that period. A successful response means only that the accounting period is now closed, but does not mean that the trial balance has successfully completed.

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AccountingPeriodsApi()
ap_id = 'ap_id_example' # str | ID of the accounting period you want to close.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Close accounting period
    api_response = api_instance.p_ut_close_accounting_period(ap_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingPeriodsApi->p_ut_close_accounting_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ap_id** | **str**| ID of the accounting period you want to close. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_pending_close_accounting_period**
> CommonResponseType p_ut_pending_close_accounting_period(ap_id, zuora_entity_ids=zuora_entity_ids)

Set accounting period to pending close

Sets an accounting period to pending close.   Prerequisites -------------  * You must have Zuora Finance enabled on your tenant. * You must have the Manage Close Process and Run Trial Balance user permissions.               Limitations   -----------    * The accounting period cannot be closed or pending close.    * The accounting period cannot be in the process of running a trial balance.    * All earlier accounting periods must be closed.     Notes ----- When you set an accounting period to pending close in Zuora, a trial balance is automatically run for that period. A response of `{ \"success\": true }`  means only that the accounting period status is now pending close, but does not mean that the trial balance has successfully completed. You can use the Get Accounting Period REST API call to view details about the outcome of the trial balance. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AccountingPeriodsApi()
ap_id = 'ap_id_example' # str | ID of the accounting period you want to set to pending close.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Set accounting period to pending close
    api_response = api_instance.p_ut_pending_close_accounting_period(ap_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingPeriodsApi->p_ut_pending_close_accounting_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ap_id** | **str**| ID of the accounting period you want to set to pending close. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_reopen_accounting_period**
> CommonResponseType p_ut_reopen_accounting_period(ap_id, zuora_entity_ids=zuora_entity_ids)

Re-open accounting period

Re-opens an accounting period. Prerequisites ------------- * You must have Zuora Finance enabled on your tenant. * You must have the Manage Close Process and Run Trial Balance user permissions.  Limitations ----------- * The accounting period must be closed or pending close. * You can only re-open an accounting period that is immediately previous to an open period.

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AccountingPeriodsApi()
ap_id = 'ap_id_example' # str | ID of the accounting period that you want to re-open.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Re-open accounting period
    api_response = api_instance.p_ut_reopen_accounting_period(ap_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingPeriodsApi->p_ut_reopen_accounting_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ap_id** | **str**| ID of the accounting period that you want to re-open. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_run_trial_balance**
> CommonResponseType p_ut_run_trial_balance(ap_id, zuora_entity_ids=zuora_entity_ids)

Run trial balance

Runs the trial balance for an accounting period.   Prerequisites -------------  * You must have Zuora Finance enabled on your tenant.  * You must have the Manage Close Process and Run Trial Balance user permissions. See [Finance Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/f_Finance_Roles).             Limitations  -----------    * The accounting period must be open.    * The accounting period cannot already be in the process of running a trial balance.   Notes ----- The trial balance is run asynchronously. A response of `{ \"success\": true }` means only that the trial balance has started processing, but does not mean that the trial balance has successfully completed. You can use the [Get Accounting Period](https://www.zuora.com/developer/api-reference/#operation/GET_AccountingPeriod) REST API call to view details about the outcome of the trial balance. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AccountingPeriodsApi()
ap_id = 'ap_id_example' # str | ID of the accounting period for which you want to run a trial balance.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Run trial balance
    api_response = api_instance.p_ut_run_trial_balance(ap_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingPeriodsApi->p_ut_run_trial_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ap_id** | **str**| ID of the accounting period for which you want to run a trial balance. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_update_accounting_period**
> CommonResponseType p_ut_update_accounting_period(ap_id, request, zuora_entity_ids=zuora_entity_ids)

Update accounting period

 Updates an accounting period.  Prerequisites -------------  * You must have Zuora Finance enabled on your tenant.  * You must have the Create Accounting Period user permission. See [Finance Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/f_Finance_Roles).  Limitations -----------  * You can update the start date of only the earliest accounting period on your tenant. You cannot update the start date of later periods.  * If you update the earliest accounting period, the start date must be equal to or earlier than the date of the earliest transaction on the tenant.  * Start and end dates of accounting periods must be contiguous. For example, if one accounting period ends on January 31, the next period must start on February 1.  * If you have the Revenue Recognition Package and have enabled the \"Monthly recognition over time\" revenue recognition model, the accounting period start date and end date must be on the first day and last day of the month, respectively. Note that the start and end dates do not necessarily have to be in the same month.  * You cannot update the start date or end date of an accounting period if:   * Any revenue has been distributed into the period.   * The period has any active journal entries. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AccountingPeriodsApi()
ap_id = 'ap_id_example' # str | ID of the accounting period you want to update.
request = zuora_client.PUTAccountingPeriodType() # PUTAccountingPeriodType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Update accounting period
    api_response = api_instance.p_ut_update_accounting_period(ap_id, request, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingPeriodsApi->p_ut_update_accounting_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ap_id** | **str**| ID of the accounting period you want to update. | 
 **request** | [**PUTAccountingPeriodType**](PUTAccountingPeriodType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

