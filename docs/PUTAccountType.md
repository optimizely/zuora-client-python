# PUTAccountType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class__ns** | **str** | Value of the Class field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**customer_type__ns** | **str** | Value of the Customer Type field for the corresponding customer account in NetSuite. The Customer Type field is used when the customer account is created in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**department__ns** | **str** | Value of the Department field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the account&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**location__ns** | **str** | Value of the Location field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**subsidiary__ns** | **str** | Value of the Subsidiary field for the corresponding customer account in NetSuite. The Subsidiary field is required if you use NetSuite OneWorld. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the account was sychronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**syncto_net_suite__ns** | **str** | Specifies whether the account should be synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**additional_email_addresses** | **list[str]** | A list of additional email addresses to receive emailed invoices. Use a comma to separate each email address.  **Note:** Invoices are emailed to the email addresses specified in this field only when the &#x60;invoiceDeliveryPrefsEmail&#x60; field is &#x60;true&#x60;.  | [optional] 
**auto_pay** | **bool** | Whether future payments are to be automatically billed when they are due.   | [optional] 
**batch** | **str** | The alias name given to a batch. A string of 50 characters or less.  | [optional] 
**bill_to_contact** | [**PUTAccountTypeBillToContact**](PUTAccountTypeBillToContact.md) |  | [optional] 
**communication_profile_id** | **str** | The ID of a communication profile.  | [optional] 
**credit_memo_template_id** | **str** | **Note**: This field is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  The unique ID of the credit memo template, configured in **Billing Settings** &gt; **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08a6246fdf101626b1b3fe0144b.  | [optional] 
**crm_id** | **str** | CRM account ID for the account, up to 100 characters.  | [optional] 
**debit_memo_template_id** | **str** | **Note**: This field is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  The unique ID of the debit memo template, configured in **Billing Settings** &gt; **Manage Billing Document Configuration** through the Zuora UI. For example, 2c92c08d62470a8501626b19d24f19e2.  | [optional] 
**invoice_delivery_prefs_email** | **bool** | Whether the customer wants to receive invoices through email.   The default value is &#x60;false&#x60;.  | [optional] 
**invoice_delivery_prefs_print** | **bool** | Whether the customer wants to receive printed invoices, such as through postal mail.  The default value is &#x60;false&#x60;.  | [optional] 
**invoice_template_id** | **str** | Invoice template ID, configured in Billing Settings in the Zuora UI.  | [optional] 
**name** | **str** | Account name, up to 255 characters.  | [optional] 
**notes** | **str** | A string of up to 65,535 characters.  | [optional] 
**parent_id** | **str** | Identifier of the parent customer account for this Account object. The length is 32 characters. Use this field if you have customer hierarchy enabled. | [optional] 
**payment_gateway** | **str** | The name of the payment gateway instance. If null or left unassigned, the Account will use the Default Gateway.  | [optional] 
**sales_rep** | **str** | The name of the sales representative associated with this account, if applicable. Maximum of 50 characters. | [optional] 
**sequence_set_id** | **str** | The ID of the billing document sequence set to assign to the customer account.   The billing documents to generate for this account will adopt the prefix and starting document number configured in the sequence set.  If a customer account has no assigned billing document sequence set, billing documents generated for this account adopt the prefix and starting document number from the default sequence set.  | [optional] 
**sold_to_contact** | [**PUTAccountTypeSoldToContact**](PUTAccountTypeSoldToContact.md) |  | [optional] 
**tagging** | **str** |  | [optional] 
**tax_info** | [**POSTAccountTypeTaxInfo**](POSTAccountTypeTaxInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


