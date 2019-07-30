# zuora_client.MassUpdaterApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_mass_updater**](MassUpdaterApi.md#g_et_mass_updater) | **GET** /v1/bulk/{bulk-key} | Get mass action result
[**p_ost_mass_updater**](MassUpdaterApi.md#p_ost_mass_updater) | **POST** /v1/bulk | Perform mass action
[**p_ut_mass_updater**](MassUpdaterApi.md#p_ut_mass_updater) | **PUT** /v1/bulk/{bulk-key}/stop | Stop mass action


# **g_et_mass_updater**
> GETMassUpdateType g_et_mass_updater(bulk_key, zuora_entity_ids=zuora_entity_ids)

Get mass action result

This reference describes how to get information about the result of a mass action through the REST API.  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.MassUpdaterApi()
bulk_key = 'bulk_key_example' # str | String of 32 characters that identifies a mass action. You get the bulk-key after performing a mass action through the REST API. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Get mass action result
    api_response = api_instance.g_et_mass_updater(bulk_key, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MassUpdaterApi->g_et_mass_updater: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_key** | **str**| String of 32 characters that identifies a mass action. You get the bulk-key after performing a mass action through the REST API.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETMassUpdateType**](GETMassUpdateType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_mass_updater**
> POSTMassUpdateResponseType p_ost_mass_updater(file, params, zuora_entity_ids=zuora_entity_ids)

Perform mass action

This reference describes how to perform a mass action through the REST API.   Using this API method, you send a multipart/form-data request containing a `.csv` file with data about the mass action you want to perform. Zuora returns a key and then asynchronously processes the mass action. You can use the key to get details about the result of the mass action. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.MassUpdaterApi()
file = '/path/to/file.txt' # file | File containing data about the mass action you want to perform. The file requirements are the same as when uploading a file through the Mass Updater in the Zuora UI. The file must be a .csv file or a zipped .csv file.  The maximum file size is 4 MB.  The data in the file must be formatted according to the mass action type you want to perform. 
params = 'params_example' # str | Container for the following fields. You must format this parameter as a JSON object.  * `actionType` (string, **Required**) - Type of mass action you want to perform. The following mass actions are supported: `UpdateAccountingCode`, `CreateRevenueSchedule`, `UpdateRevenueSchedule`, `DeleteRevenueSchedule`, `ImportFXRate`, and `MPU`.  * `checksum` (string) - An MD5 checksum that is used to validate the integrity of   the uploaded file. The checksum is a 32-character string. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Perform mass action
    api_response = api_instance.p_ost_mass_updater(file, params, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MassUpdaterApi->p_ost_mass_updater: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File containing data about the mass action you want to perform. The file requirements are the same as when uploading a file through the Mass Updater in the Zuora UI. The file must be a .csv file or a zipped .csv file.  The maximum file size is 4 MB.  The data in the file must be formatted according to the mass action type you want to perform.  | 
 **params** | **str**| Container for the following fields. You must format this parameter as a JSON object.  * &#x60;actionType&#x60; (string, **Required**) - Type of mass action you want to perform. The following mass actions are supported: &#x60;UpdateAccountingCode&#x60;, &#x60;CreateRevenueSchedule&#x60;, &#x60;UpdateRevenueSchedule&#x60;, &#x60;DeleteRevenueSchedule&#x60;, &#x60;ImportFXRate&#x60;, and &#x60;MPU&#x60;.  * &#x60;checksum&#x60; (string) - An MD5 checksum that is used to validate the integrity of   the uploaded file. The checksum is a 32-character string.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**POSTMassUpdateResponseType**](POSTMassUpdateResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_mass_updater**
> CommonResponseType p_ut_mass_updater(bulk_key, zuora_entity_ids=zuora_entity_ids)

Stop mass action

This reference describes how to stop a mass action through the REST API. You can stop a mass action when its status is Pending or Processing. After you have stopped a mass action, you can get the mass action result to see details of the mass action.  - If you stop a mass action when its status is Pending, no response file is generated because no records have been processed.  - If you stop a mass action when its status is Processing, a response file is generated. You can check the response file to see which records have been processed and which have not. In the response file, the **Success** column has the value `Y` (successful) or `N` (failed) for processed records, and a blank value for unprocessed records.  Records that have already been processed when a mass action is stopped are not rolled back. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.MassUpdaterApi()
bulk_key = 'bulk_key_example' # str | String of 32 characters that identifies a mass action. You get the bulk-key after performing a mass action through the REST API. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Stop mass action
    api_response = api_instance.p_ut_mass_updater(bulk_key, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MassUpdaterApi->p_ut_mass_updater: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_key** | **str**| String of 32 characters that identifies a mass action. You get the bulk-key after performing a mass action through the REST API.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

