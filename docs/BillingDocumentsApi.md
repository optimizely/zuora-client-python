# zuora_client.BillingDocumentsApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**g_et_billing_documents**](BillingDocumentsApi.md#g_et_billing_documents) | **GET** /v1/billing-documents | Get billing documents

# **g_et_billing_documents**
> BillingDocumentQueryResponseElementType g_et_billing_documents(account_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, document_date=document_date, status=status, sort=sort)

Get billing documents

Retrieves the information about all billing documents associated with a specified account. The billing documents contain invoices, credit memos, and debit memos.   To retrieve information about credit memos and debit memos, you must have the Invoice Settlement feature enabled.  

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.BillingDocumentsApi()
account_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the customer account that the billing documents are associated with.  
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
page_size = 56 # int | Number of rows returned per page.  (optional)
document_date = '2013-10-20' # date | The date of the billing document. It represents the invoice date for invoices, credit memo date for credit memos, and debit memo date for debit memos.  (optional)
status = 'status_example' # str | The status of the billing document.  (optional)
sort = 'sort_example' # str | This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  If you do not specify any sortable field, the response data is sorted by the `documentDate` field in descending order.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.      - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - documentDate   - documentType    Examples: - /billing-documents?accountId=4028905f5e4feb38015e50af9aa002d1   &sort=+documentDate,-documentType - /billing-documents?accountId=4028905f5e4feb38015e50af9aa002d1   &status=Posted&sort=+documentDate&page=2&pageSize=15  (optional)

try:
    # Get billing documents
    api_response = api_instance.g_et_billing_documents(account_id, zuora_entity_ids=zuora_entity_ids, page_size=page_size, document_date=document_date, status=status, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingDocumentsApi->g_et_billing_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)| The ID of the customer account that the billing documents are associated with.   | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **page_size** | **int**| Number of rows returned per page.  | [optional] 
 **document_date** | **date**| The date of the billing document. It represents the invoice date for invoices, credit memo date for credit memos, and debit memo date for debit memos.  | [optional] 
 **status** | **str**| The status of the billing document.  | [optional] 
 **sort** | **str**| This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  If you do not specify any sortable field, the response data is sorted by the &#x60;documentDate&#x60; field in descending order.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.      - The &#x60;-&#x60; operator indicates an ascending order.   - The &#x60;+&#x60; operator indicates a descending order.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - documentDate   - documentType    Examples: - /billing-documents?accountId&#x3D;4028905f5e4feb38015e50af9aa002d1   &amp;sort&#x3D;+documentDate,-documentType - /billing-documents?accountId&#x3D;4028905f5e4feb38015e50af9aa002d1   &amp;status&#x3D;Posted&amp;sort&#x3D;+documentDate&amp;page&#x3D;2&amp;pageSize&#x3D;15  | [optional] 

### Return type

[**BillingDocumentQueryResponseElementType**](BillingDocumentQueryResponseElementType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

