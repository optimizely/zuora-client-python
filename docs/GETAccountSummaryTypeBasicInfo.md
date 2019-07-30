# GETAccountSummaryTypeBasicInfo

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
**account_number** | **str** | Account number.  | [optional] 
**additional_email_addresses** | **list[str]** | A list of additional email addresses to receive emailed invoices.  | [optional] 
**balance** | **str** | Current outstanding balance.  | [optional] 
**batch** | **str** | The alias name given to a batch. A string of 50 characters or less.  | [optional] 
**bill_cycle_day** | **str** | Billing cycle day (BCD), the day of the month when a bill run generates invoices for the account.  | [optional] 
**currency** | **str** | A currency as defined in Billing Settings in the Zuora UI.  | [optional] 
**default_payment_method** | [**GETAccountSummaryTypeBasicInfoDefaultPaymentMethod**](GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.md) |  | [optional] 
**id** | **str** | Account ID.  | [optional] 
**invoice_delivery_prefs_email** | **bool** | Whether the customer wants to receive invoices through email.   | [optional] 
**invoice_delivery_prefs_print** | **bool** | Whether the customer wants to receive printed invoices, such as through postal mail.  | [optional] 
**last_invoice_date** | **date** | Date of the most recent invoice for the account; null if no invoice has ever been generated.  | [optional] 
**last_payment_amount** | **str** | Amount of the most recent payment collected for the account; null if no payment has ever been collected.  | [optional] 
**last_payment_date** | **date** | Date of the most recent payment collected for the account. Null if no payment has ever been collected.  | [optional] 
**name** | **str** | Account name.  | [optional] 
**status** | **str** | Account status; possible values are: &#x60;Active&#x60;, &#x60;Draft&#x60;, &#x60;Canceled&#x60;.  | [optional] 
**tags** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


