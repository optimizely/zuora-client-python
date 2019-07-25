# swagger_client.EntitiesApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_entities**](EntitiesApi.md#d_elete_entities) | **DELETE** /v1/entities/{id} | Multi-entity: Delete entity
[**g_et_entities**](EntitiesApi.md#g_et_entities) | **GET** /v1/entities | Multi-entity: Get entities
[**g_et_entity_by_id**](EntitiesApi.md#g_et_entity_by_id) | **GET** /v1/entities/{id} | Multi-entity: Get entity by Id
[**p_ost_entities**](EntitiesApi.md#p_ost_entities) | **POST** /v1/entities | Multi-entity: Create entity
[**p_ut_entities**](EntitiesApi.md#p_ut_entities) | **PUT** /v1/entities/{id} | Multi-entity: Update entity
[**p_ut_provision_entity**](EntitiesApi.md#p_ut_provision_entity) | **PUT** /v1/entities/{id}/provision | Multi-entity: Provision entity

# **d_elete_entities**
> DELETEntityResponseType d_elete_entities(id, zuora_entity_ids=zuora_entity_ids)

Multi-entity: Delete entity

**Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Removes an entity and its sub-entities from a multi-entity hierarchy. You can only remove unprovisioned entities. An error occurred when you remove a provisioned entity.  ## User Access Permission You must make the call as a global entity administrator.    

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EntitiesApi()
id = 'id_example' # str | Specify the Id of the entity that you want to delete. You can get the entity Id from the GET Entities call.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Multi-entity: Delete entity
    api_response = api_instance.d_elete_entities(id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitiesApi->d_elete_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify the Id of the entity that you want to delete. You can get the entity Id from the GET Entities call. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**DELETEntityResponseType**](DELETEntityResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_entities**
> GETEntitiesResponseType g_et_entities(zuora_entity_ids=zuora_entity_ids, provisioned=provisioned)

Multi-entity: Get entities

**Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    Retrieves detailed information of certain entities in a multi-entity hierarchy.   You can retrieve:   - Provisioned entities     - Unprovisioned entities     - Both provisioned and unprovisioned entities  ## User Access Permission  You can make the call as any entity user. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EntitiesApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
provisioned = 'provisioned_example' # str | Specify whether to retrieve provisioned or unprovisioned entities:  - `true`: Provisioned entities  - `false`: Unprovisioned entities   If you do not specify this field in the request, both the provisioned and unprovisioned entities are returned.  (optional)

try:
    # Multi-entity: Get entities
    api_response = api_instance.g_et_entities(zuora_entity_ids=zuora_entity_ids, provisioned=provisioned)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitiesApi->g_et_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **provisioned** | **str**| Specify whether to retrieve provisioned or unprovisioned entities:  - &#x60;true&#x60;: Provisioned entities  - &#x60;false&#x60;: Unprovisioned entities   If you do not specify this field in the request, both the provisioned and unprovisioned entities are returned.  | [optional] 

### Return type

[**GETEntitiesResponseType**](GETEntitiesResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_entity_by_id**
> GETEntitiesResponseTypeWithId g_et_entity_by_id(id, zuora_entity_ids=zuora_entity_ids)

Multi-entity: Get entity by Id

**Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves detailed information about a specified entity.  ## User Access Permission You can make the call as any entity user.      

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EntitiesApi()
id = 'id_example' # str | Specify the Id of the entity that you want to retrieve. You can get the entity Id from the GET Entities call.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Multi-entity: Get entity by Id
    api_response = api_instance.g_et_entity_by_id(id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitiesApi->g_et_entity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify the Id of the entity that you want to retrieve. You can get the entity Id from the GET Entities call. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETEntitiesResponseTypeWithId**](GETEntitiesResponseTypeWithId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_entities**
> CreateEntityResponseType p_ost_entities(body, zuora_entity_ids=zuora_entity_ids)

Multi-entity: Create entity

**Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates an entity in a multi-entity hierarchy.  ## User Access Permission You must make the call as a global entity administrator.  ## Notes * We recommend that you assign only one administrator to manage the entity hierarchy, because an administrator of the global entity by default can only access to the entities that are created by themselves. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EntitiesApi()
body = swagger_client.CreateEntityType() # CreateEntityType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Multi-entity: Create entity
    api_response = api_instance.p_ost_entities(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitiesApi->p_ost_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntityType**](CreateEntityType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CreateEntityResponseType**](CreateEntityResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_entities**
> UpdateEntityResponseType p_ut_entities(body, id, zuora_entity_ids=zuora_entity_ids)

Multi-entity: Update entity

**Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Edits the following information about an unprovisioned entity:   - Name    - Display name    - Locale    - Timezone  ## User Access Permission You must make the call as a global entity administrator.  ## Notes * You are not allowed to edit the locale and time zone of the provisioned entities through the REST API. * You are not allowed to edit the display name of the global entity. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EntitiesApi()
body = swagger_client.UpdateEntityType() # UpdateEntityType | 
id = 'id_example' # str | The Id of the entity that you want to edit. You can get the entity Id from the GET Entities call.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Multi-entity: Update entity
    api_response = api_instance.p_ut_entities(body, id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitiesApi->p_ut_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateEntityType**](UpdateEntityType.md)|  | 
 **id** | **str**| The Id of the entity that you want to edit. You can get the entity Id from the GET Entities call. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**UpdateEntityResponseType**](UpdateEntityResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_provision_entity**
> ProvisionEntityResponseType p_ut_provision_entity(id, zuora_entity_ids=zuora_entity_ids)

Multi-entity: Provision entity

**Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Provisions an entity. You can only provision an entity if its parent entity is provisioned.  ## User Access Permission You must make the call as a global entity administrator.   ## Notes * Zuora does not allow you to remove a provisioned entity from the multi-entity hierarchy. So before you provision an entity, make sure that you put the entity in the correct place in the multi-entity hierarchy.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EntitiesApi()
id = 'id_example' # str | Specify the Id of the entity that you want to provision.  You can get the entity Id from the GET Entities call.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Multi-entity: Provision entity
    api_response = api_instance.p_ut_provision_entity(id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitiesApi->p_ut_provision_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specify the Id of the entity that you want to provision.  You can get the entity Id from the GET Entities call. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**ProvisionEntityResponseType**](ProvisionEntityResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

