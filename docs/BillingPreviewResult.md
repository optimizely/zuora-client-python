# BillingPreviewResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the customer account to which the billing preview applies.  | [optional] 
**credit_memo_items** | [**list[POSTBillingPreviewCreditMemoItem]**](POSTBillingPreviewCreditMemoItem.md) | An array of credit memo items returned as the result of the billing preivew request.  **Note:** The credit memo items are only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  | [optional] 
**invoice_items** | [**list[POSTBillingPreviewInvoiceItem]**](POSTBillingPreviewInvoiceItem.md) | An array of invoice items returned as the result of the billing preview request.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


