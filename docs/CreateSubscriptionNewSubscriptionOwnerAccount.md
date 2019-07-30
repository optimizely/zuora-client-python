# CreateSubscriptionNewSubscriptionOwnerAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | Account number. For example, A00000001.  | [optional] 
**auto_pay** | **bool** | Specifies whether future payments are automatically billed when they are due.  | [optional] 
**batch** | **str** | Name of the billing batch that the account belongs to. For example, Batch1.  | [optional] 
**bill_cycle_day** | **int** | Day of the month that the account prefers billing periods to begin on. If set to 0, the bill cycle day will be set as \&quot;AutoSet\&quot;.  | 
**bill_to_contact** | [**BillToContact**](BillToContact.md) |  | 
**communication_profile_id** | **str** | Internal identifier of the communication profile that Zuora uses when sending notifications to the account&#39;s contacts.  | [optional] 
**credit_card** | [**CreditCard**](CreditCard.md) |  | [optional] 
**crm_id** | **str** | External identifier of the account in a CRM system.  | [optional] 
**currency** | **str** | ISO 3-letter currency code (uppercase). For example, USD.  | 
**custom_fields** | [**AccountObjectCustomFields**](AccountObjectCustomFields.md) |  | [optional] 
**hpm_credit_card_payment_method_id** | **str** | Internal identifier of the hosted payment method (HPM) credit card payment method associated with the account.  | [optional] 
**invoice_delivery_prefs_email** | **bool** | Specifies whether to turn on the invoice delivery method &#39;Email&#39; for the new account.  Values are:   * &#x60;true&#x60; (default). Turn on the invoice delivery method &#39;Email&#39; for the new account. * &#x60;false&#x60;. Turn off the invoice delivery method &#39;Email&#39; for the new account.           | [optional] 
**invoice_delivery_prefs_print** | **bool** | Specifies whether to turn on the invoice delivery method &#39;Print&#39; for the new account. Values are:   * &#x60;true&#x60;. Turn on the invoice delivery method &#39;Print&#39; for the new account. * &#x60;false&#x60; (default). Turn off the invoice delivery method &#39;Print&#39; for the new account.  | [optional] 
**invoice_template_id** | **str** | Internal identifier of the invoice template that Zuora uses when generating invoices for the account.  | [optional] 
**name** | **str** | Account name.  | 
**notes** | **str** | Notes about the account. These notes are only visible to Zuora users.  | [optional] 
**parent_id** | **str** | Identifier of the parent customer account for this Account object. Use this field if you have customer hierarchy enabled. | [optional] 
**payment_gateway** | **str** | The payment gateway that Zuora uses when processing electronic payments and refunds for the account. If you do not specify this field or if the value of this field is null, Zuora uses your default payment gateway.  | [optional] 
**payment_term** | **str** | Name of the payment term associated with the account. For example, \&quot;Net 30\&quot;. The payment term determines the due dates of invoices.  | [optional] 
**sold_to_contact** | [**SoldToContact**](SoldToContact.md) |  | [optional] 
**tax_info** | [**TaxInfo**](TaxInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


