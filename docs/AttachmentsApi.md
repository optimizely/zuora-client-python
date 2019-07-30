# zuora_client.AttachmentsApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_attachments**](AttachmentsApi.md#d_elete_attachments) | **DELETE** /v1/attachments/{attachment-id} | Delete attachments
[**g_et_attachments**](AttachmentsApi.md#g_et_attachments) | **GET** /v1/attachments/{attachment-id} | View attachments
[**g_et_attachments_list**](AttachmentsApi.md#g_et_attachments_list) | **GET** /v1/attachments/{object-type}/{object-key} | View attachments list
[**p_ost_attachments**](AttachmentsApi.md#p_ost_attachments) | **POST** /v1/attachments | Add attachments
[**p_ut_attachments**](AttachmentsApi.md#p_ut_attachments) | **PUT** /v1/attachments/{attachment-id} | Edit attachments


# **d_elete_attachments**
> CommonResponseType d_elete_attachments(attachment_id, zuora_entity_ids=zuora_entity_ids)

Delete attachments

Use the Delete Attachment REST request to delete an attachment from a Zuora object.

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AttachmentsApi()
attachment_id = 'attachment_id_example' # str | Id of the attachment to be deleted.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete attachments
    api_response = api_instance.d_elete_attachments(attachment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->d_elete_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Id of the attachment to be deleted. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_attachments**
> GETAttachmentResponseType g_et_attachments(attachment_id, zuora_entity_ids=zuora_entity_ids)

View attachments

Use the View Attachment REST request to retrieve information about an attachment document.

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AttachmentsApi()
attachment_id = 'attachment_id_example' # str | Id of the attachment you want to view.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # View attachments
    api_response = api_instance.g_et_attachments(attachment_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->g_et_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Id of the attachment you want to view. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**GETAttachmentResponseType**](GETAttachmentResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_attachments_list**
> GETAttachmentsResponseType g_et_attachments_list(object_type, object_key, zuora_entity_ids=zuora_entity_ids, page_size=page_size)

View attachments list

Use the View Attachment REST request to get a list of attachments on an account, an invoice, or a subscription.

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AttachmentsApi()
object_type = 'object_type_example' # str | The type of object to list attachements for. 
object_key = 'object_key_example' # str | ID of the object to list attachements for.  - If `object-type` is `account`, specify an account ID.  - If `object-type` is `invoice`, specify an invoice ID.  - If `object-type` is `subscription`, specify a subscription number. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 20 # int | Number of rows returned per page.  (optional) (default to 20)

try:
    # View attachments list
    api_response = api_instance.g_et_attachments_list(object_type, object_key, zuora_entity_ids=zuora_entity_ids, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->g_et_attachments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**| The type of object to list attachements for.  | 
 **object_key** | **str**| ID of the object to list attachements for.  - If &#x60;object-type&#x60; is &#x60;account&#x60;, specify an account ID.  - If &#x60;object-type&#x60; is &#x60;invoice&#x60;, specify an invoice ID.  - If &#x60;object-type&#x60; is &#x60;subscription&#x60;, specify a subscription number.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] [default to 20]

### Return type

[**GETAttachmentsResponseType**](GETAttachmentsResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_attachments**
> POSTAttachmentResponseType p_ost_attachments(associated_object_type, associated_object_key, file, zuora_entity_ids=zuora_entity_ids, description=description)

Add attachments

Use the Add Attachment REST request with a multipart/form-data to attach a document file to an Account, a Subscription, or an Invoice.

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AttachmentsApi()
associated_object_type = 'associated_object_type_example' # str | Specify one of the following values: Account, Subscription, or Invoice. 
associated_object_key = 'associated_object_key_example' # str | For the Subscription type, specify the Subscription Number. An attachment is tied to the Subscription Number and thus viewable with every subscription version.  For Account and Invoice, specify the id. 
file = '/path/to/file.txt' # file | The file to be attached. Files with the following extensions are supported: .pdf, .csv, .png, .xlsx, .xls, .doc, .docx, .msg, .jpg, .txt, .htm, .html, .eml, .pptx, .gif, .rtf, .xml, .jpeg, .log, .cls  The maximum file size is 4 MB. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
description = 'description_example' # str | Description of the attachment document.  (optional)

try:
    # Add attachments
    api_response = api_instance.p_ost_attachments(associated_object_type, associated_object_key, file, zuora_entity_ids=zuora_entity_ids, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->p_ost_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **associated_object_type** | **str**| Specify one of the following values: Account, Subscription, or Invoice.  | 
 **associated_object_key** | **str**| For the Subscription type, specify the Subscription Number. An attachment is tied to the Subscription Number and thus viewable with every subscription version.  For Account and Invoice, specify the id.  | 
 **file** | **file**| The file to be attached. Files with the following extensions are supported: .pdf, .csv, .png, .xlsx, .xls, .doc, .docx, .msg, .jpg, .txt, .htm, .html, .eml, .pptx, .gif, .rtf, .xml, .jpeg, .log, .cls  The maximum file size is 4 MB.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **description** | **str**| Description of the attachment document.  | [optional] 

### Return type

[**POSTAttachmentResponseType**](POSTAttachmentResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_attachments**
> CommonResponseType p_ut_attachments(attachment_id, zuora_entity_ids=zuora_entity_ids, request=request)

Edit attachments

Use the Edit Attachment REST request to make changes to the descriptive fields of an attachment, such as the description and the file name. You cannot change the actual content of the attached file in Zuora. If you need to change the actual content, you need to delete the attachment and add the updated file as a new attachment.

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AttachmentsApi()
attachment_id = 'attachment_id_example' # str | Id of the attachment to be updated.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
request = zuora_client.PUTAttachmentType() # PUTAttachmentType |  (optional)

try:
    # Edit attachments
    api_response = api_instance.p_ut_attachments(attachment_id, zuora_entity_ids=zuora_entity_ids, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->p_ut_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Id of the attachment to be updated. | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **request** | [**PUTAttachmentType**](PUTAttachmentType.md)|  | [optional] 

### Return type

[**CommonResponseType**](CommonResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

