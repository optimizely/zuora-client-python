# GETAccountTypeBillingAndPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_email_addresses** | **list[str]** | A list of additional email addresses to receive emailed invoices.  | [optional] 
**bill_cycle_day** | **str** | Billing cycle day (BCD), the day of the month when a bill run generates invoices for the account.  | [optional] 
**currency** | **str** | A currency defined in the web-based UI administrative settings.  | [optional] 
**invoice_delivery_prefs_email** | **bool** | Whether the customer wants to receive invoices through email.   | [optional] 
**invoice_delivery_prefs_print** | **bool** | Whether the customer wants to receive printed invoices, such as through postal mail.  | [optional] 
**payment_gateway** | **str** | The name of the payment gateway instance. If null or left unassigned, the Account will use the Default Gateway.  | [optional] 
**payment_term** | **str** | A payment-terms indicator defined in the web-based UI administrative settings, e.g., \&quot;Net 30\&quot;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


