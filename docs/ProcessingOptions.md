# ProcessingOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_credit_balance** | **bool** | Indicates if any credit balance on a customer&#39;s account is automatically applied to invoices. If no value is specified then this field defaults to false. This feature is not available if you have enabled the Invoice Settlement feature. | [optional] 
**billing_options** | [**BillingOptions**](BillingOptions.md) |  | [optional] 
**collect_payment** | **bool** | Indicates if the current request needs to collect payments. This value can not be &#39;true&#39; when &#39;runBilling&#39; flag is &#39;false&#39;. | [optional] 
**electronic_payment_options** | [**ProcessingOptionsElectronicPaymentOptions**](ProcessingOptionsElectronicPaymentOptions.md) |  | [optional] 
**run_billing** | **bool** | Indicates if the current request needs to generate an invoice. The invoice will be generated against all subscriptions included in this order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


