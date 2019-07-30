# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**additional_email_addresses** | **str** | List of additional email addresses to receive emailed invoices. Values should be a comma-separated list of email addresses.  | [optional] 
**allow_invoice_edit** | **bool** | Indicates if associated invoices can be edited. Values are:   * &#x60;true&#x60; * &#x60;false&#x60; (default)  | [optional] 
**auto_pay** | **bool** | Specifies whether future payments are to be automatically billed when they are due. Possible values are &#x60;true&#x60;, &#x60;false&#x60;. | [optional] 
**batch** | **str** |  | [optional] 
**bill_cycle_day** | **int** | Day of the month that the account prefers billing periods to begin on. If set to 0, the bill cycle day will be set as \&quot;AutoSet\&quot;. | 
**bill_to_contact** | [**BillToContactPostOrder**](BillToContactPostOrder.md) |  | 
**communication_profile_id** | **str** |  | [optional] 
**credit_card** | [**CreditCard**](CreditCard.md) |  | [optional] 
**credit_memo_template_id** | **str** | **Note**: This field is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  The unique ID of the credit memo template, configured in **Billing Settings** &gt; **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08a6246fdf101626b1b3fe0144b.  | [optional] 
**crm_id** | **str** |  | [optional] 
**currency** | **str** | 3 uppercase character currency code | 
**custom_fields** | [**AccountObjectCustomFields**](AccountObjectCustomFields.md) |  | [optional] 
**customer_service_rep_name** | **str** | Name of the account&#39;s customer service representative, if applicable.  | [optional] 
**debit_memo_template_id** | **str** | **Note**: This field is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  The unique ID of the debit memo template, configured in **Billing Settings** &gt; **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08d62470a8501626b19d24f19e2.  | [optional] 
**hpm_credit_card_payment_method_id** | **str** |  | [optional] 
**invoice_delivery_prefs_email** | **bool** | Specifies whether to turn on the invoice delivery method &#39;Email&#39; for the new account.  Values are:   * &#x60;true&#x60; (default). Turn on the invoice delivery method &#39;Email&#39; for the new account. * &#x60;false&#x60;. Turn off the invoice delivery method &#39;Email&#39; for the new account.  | [optional] 
**invoice_delivery_prefs_print** | **bool** | Specifies whether to turn on the invoice delivery method &#39;Print&#39; for the new account. Values are:   * &#x60;true&#x60;. Turn on the invoice delivery method &#39;Print&#39; for the new account. * &#x60;false&#x60; (default). Turn off the invoice delivery method &#39;Print&#39; for the new account.  | [optional] 
**invoice_template_id** | **str** |  | [optional] 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**parent_id** | **str** | Identifier of the parent customer account for this Account object. Use this field if you have customer hierarchy enabled. | [optional] 
**payment_gateway** | **str** |  | [optional] 
**payment_term** | **str** |  | [optional] 
**purchase_order_number** | **str** | The number of the purchase order associated with this account. Purchase order information generally comes from customers.  | [optional] 
**sales_rep** | **str** | The name of the sales representative associated with this account, if applicable.  | [optional] 
**sequence_set_id** | **str** | The ID of the billing document sequence set to assign to the customer account.   The billing documents to generate for this account will adopt the prefix and starting document number configured in the sequence set.  | [optional] 
**sold_to_contact** | [**SoldToContactPostOrder**](SoldToContactPostOrder.md) |  | [optional] 
**tax_info** | [**TaxInfo**](TaxInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


