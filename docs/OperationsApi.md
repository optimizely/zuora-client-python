# swagger_client.OperationsApi

All URIs are relative to *https://rest.zuora.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p_ost_billing_preview**](OperationsApi.md#p_ost_billing_preview) | **POST** /v1/operations/billing-preview | Create billing preview
[**p_ost_transaction_invoice_payment**](OperationsApi.md#p_ost_transaction_invoice_payment) | **POST** /v1/operations/invoice-collect | Invoice and collect

# **p_ost_billing_preview**
> BillingPreviewResult p_ost_billing_preview(body, zuora_entity_ids=zuora_entity_ids)

Create billing preview

**Note:** The Billing Preview feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    Generates a preview of future invoice items for one customer account. Use the BillingPreview call to calculate how much a single customer will be invoiced from the most recent invoice to a specific end of term date in the future.  Additionally, you can use the BillingPreview service to access real-time data on an individual customer's usage consumption.   The BillingPreview call does not calculate taxes for charges in the subscription.  If you have the Invoice Settlement feature enabled, you can also generate a preview of future credit memo items for one customer account. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
body = swagger_client.PostBillingPreviewParam() # PostBillingPreviewParam | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Create billing preview
    api_response = api_instance.p_ost_billing_preview(body, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->p_ost_billing_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostBillingPreviewParam**](PostBillingPreviewParam.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 

### Return type

[**BillingPreviewResult**](BillingPreviewResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_transaction_invoice_payment**
> POSTInvoiceCollectResponseType p_ost_transaction_invoice_payment(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)

Invoice and collect

Generates and posts invoices and credit memos and collects payments for posted invoices. Credit memos are only available if you have the Invoice Settlement feature enabled and negative charges exist. Credit memos will not be applied to invoices. If draft invoices and credit memos exist when you run this operation, this operation will post the invoices and credit memos. Note that draft credit memos created from an invoice or a product rate plan charge will not be posted.  You can use this operation to generate invoices and collect payments on the posted invoices,  or else simply collect payment on a specified existing invoice. The customer's default payment method is used, and the full amount due is collected. The operation depends on the parameters you specify.  - To generate one or more new invoices for that customer and collect payment on the generated and other unpaid invoice(s), leave the **invoiceId** field empty.   - To collect payment on an existing invoice, specify the invoice ID.    The operation is atomic; if any part is unsuccessful, the entire operation is rolled back.  When an error occurs, gateway reason codes and error messages are returned the error response of this operation. The following items are some gateway response code examples.  - Orbital: `05 Do Not Honor`; `14 Invalid Credit Card Number` - Vantiv: `301 Invalid Account Number`; `304 Lost/Stolen Card`   - CyberSource2: `202 Expired card`; `231 Invalid account number`  For more reason code information, see the corresponding payment gateway documentation.    ## Notes  Timeouts may occur when using this method on an account that has an extremely high number of subscriptions. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OperationsApi()
body = swagger_client.POSTInvoiceCollectType() # POSTInvoiceCollectType | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_version = 'zuora_version_example' # str |  The minor version of the Zuora REST API.   You need to set this parameter if you use the following fields: * documentDate * targetDate              If you have the Invoice Settlement feature enabled, you need to specify this parameter. Otherwise, an error is returned.   See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.  (optional)

try:
    # Invoice and collect
    api_response = api_instance.p_ost_transaction_invoice_payment(body, zuora_entity_ids=zuora_entity_ids, zuora_version=zuora_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->p_ost_transaction_invoice_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**POSTInvoiceCollectType**](POSTInvoiceCollectType.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_version** | **str**|  The minor version of the Zuora REST API.   You need to set this parameter if you use the following fields: * documentDate * targetDate              If you have the Invoice Settlement feature enabled, you need to specify this parameter. Otherwise, an error is returned.   See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.  | [optional] 

### Return type

[**POSTInvoiceCollectResponseType**](POSTInvoiceCollectResponseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

