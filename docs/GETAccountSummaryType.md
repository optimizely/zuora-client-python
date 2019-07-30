# GETAccountSummaryType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_info** | [**GETAccountSummaryTypeBasicInfo**](GETAccountSummaryTypeBasicInfo.md) |  | [optional] 
**bill_to_contact** | [**GETAccountSummaryTypeBillToContact**](GETAccountSummaryTypeBillToContact.md) |  | [optional] 
**invoices** | [**list[GETAccountSummaryInvoiceType]**](GETAccountSummaryInvoiceType.md) | Container for invoices. Only returns the last 6 invoices.  | [optional] 
**payments** | [**list[GETAccountSummaryPaymentType]**](GETAccountSummaryPaymentType.md) | Container for payments. Only returns the last 6 payments.  | [optional] 
**sold_to_contact** | [**GETAccountSummaryTypeSoldToContact**](GETAccountSummaryTypeSoldToContact.md) |  | [optional] 
**subscriptions** | [**list[GETAccountSummarySubscriptionType]**](GETAccountSummarySubscriptionType.md) | Container for subscriptions.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**tax_info** | [**GETAccountSummaryTypeTaxInfo**](GETAccountSummaryTypeTaxInfo.md) |  | [optional] 
**usage** | [**list[GETAccountSummaryUsageType]**](GETAccountSummaryUsageType.md) | Container for usage data. Only returns the last 6 months of usage.  **Note:** If the [Active Rating](https://knowledgecenter.zuora.com/CB_Billing/J_Billing_Operations/H_Active_Rating) feature is enabled, no usage data is returned in the response body field. To retrive usage data information, you can use the [Usage (with Active Rating)](https://www.zuora.com/developer/active-rating-api/#tag/Usage-(with-Active-Rating)) operations.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


