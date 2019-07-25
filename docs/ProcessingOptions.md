# ProcessingOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_credit_balance** | **bool** | Indicates if any credit balance on a customer&#x27;s account is automatically applied to invoices. If no value is specified then this field defaults to false. This feature is not available if you have enabled the Invoice Settlement feature. | [optional] 
**billing_options** | [**BillingOptions**](BillingOptions.md) |  | [optional] 
**collect_payment** | **bool** | Indicates if the current request needs to collect payments. This value can not be &#x27;true&#x27; when &#x27;runBilling&#x27; flag is &#x27;false&#x27;. | [optional] 
**electronic_payment_options** | **object** | Container for the electronic payment options. | [optional] 
**run_billing** | **bool** | Indicates if the current request needs to generate an invoice. The invoice will be generated against all subscriptions included in this order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

