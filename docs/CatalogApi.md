# zuora_client.CatalogApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_catalog**](CatalogApi.md#g_et_catalog) | **GET** /v1/catalog/products | Get product catalog
[**g_et_product**](CatalogApi.md#g_et_product) | **GET** /v1/catalog/product/{product-id} | Get product
[**p_ost_catalog**](CatalogApi.md#p_ost_catalog) | **POST** /v1/catalog/products/{product-id}/share | Multi-entity: Share a product with an Entity

# **g_et_catalog**
> GETCatalogType g_et_catalog(zuora_entity_ids=zuora_entity_ids, page_size=page_size, zuora_version=zuora_version)

Get product catalog

Retrieves the entire product catalog, including all products, features, and their corresponding product rate plans, charges. Products are returned in reverse chronological order on the `UpdatedDate` field.   With product rate plans and rate plan charges, the REST API has a maximum array size.  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CatalogApi()
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
zuora_version = 'zuora_version_example' # str | The minor version of the Zuora REST API.   You only need to set this parameter if you use the `productRatePlans` field.  (optional)

try:
    # Get product catalog
    api_response = api_instance.g_et_catalog(zuora_entity_ids=zuora_entity_ids, page_size=page_size, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->g_et_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **zuora_version** | **str**| The minor version of the Zuora REST API.   You only need to set this parameter if you use the &#x60;productRatePlans&#x60; field.  | [optional] 

### Return type

[**GETCatalogType**](GETCatalogType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_product**
> GETProductType g_et_product(product_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Get product

Retrieves detailed information about a specific product, including information about its product rate plans and charges.  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CatalogApi()
product_id = 'product_id_example' # str | The unique ID of the product you want to retrieve. For example, 8a808255575bdae4015774e9602e16fe.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str | The minor version of the Zuora REST API.   You only need to set this parameter if you use the `productRatePlans` field.  (optional)

try:
    # Get product
    api_response = api_instance.g_et_product(product_id, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->g_et_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The unique ID of the product you want to retrieve. For example, 8a808255575bdae4015774e9602e16fe. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**| The minor version of the Zuora REST API.   You only need to set this parameter if you use the &#x60;productRatePlans&#x60; field.  | [optional] 

### Return type

[**GETProductType**](GETProductType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_catalog**
> CommonResponseType p_ost_catalog(body, product_id, zuora_entity_ids=zuora_entity_ids)

Multi-entity: Share a product with an Entity

**Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Shares a product with a target entity. Zuora synchronizes the shared products to the target entity after sharing. For more information about product sharing, see [Products Sharing Across Entities](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/C_Business_Objects_Sharing_Across_Entities/B_Products_Sharing_Across_Entities).  Note that:  - You must finish all the [prerequisites](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/C_Business_Objects_Sharing_Across_Entities/B_Products_Sharing_Across_Entities/Share_Products) before sharing products with other entities.   - Only source entity administrators have permission to share products with other entities. You must make the call as a source entity administrator.  - Currently, you can only share a product with one entity at a time. An error occurs if you try to share a product to more than one entity. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.CatalogApi()
body = zuora_client.POSTCatalogType() # POSTCatalogType | 
product_id = 'product_id_example' # str | The unique ID of the product you want to share. For example, 8a808255575bdae4015774e9602e16fe.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Multi-entity: Share a product with an Entity
    api_response = api_instance.p_ost_catalog(body, product_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->p_ost_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTCatalogType**](POSTCatalogType.md)|  | 
 **product_id** | **str**| The unique ID of the product you want to share. For example, 8a808255575bdae4015774e9602e16fe. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

