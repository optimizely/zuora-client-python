# ProxyCreateCreditBalanceAdjustment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the credit balance adjustment&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the credit balance adjustment was sychronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**accounting_code** | **str** | An active accounting code in your Zuora [Chart of Accounts](https://knowledgecenter.zuora.com/CB_Billing/W_Billing_and_Payments_Settings/V_Configure_Accounting_Codes/D_Set_Up_Chart_of_Accounts).  The [accounting code](https://knowledgecenter.zuora.com/BC_Subscription_Management/Product_Catalog/A_Product_Catalog_Concepts/Accounting_Codes) for the credit balance adjustment. Typically, an accounting code for a credit balance adjustment maps to a bank account in your accounting system.  | [optional] 
**amount** | **float** | The amount of the adjustment.  | 
**comment** | **str** | Your comments about the credit balance adjustment.  | [optional] 
**reason_code** | **str** | A code identifying the reason for the transaction. Must be an existing [reason code](https://knowledgecenter.zuora.com/CB_Billing/K_Payment_Operations/Reason_Codes_for_Payment_Operations) or empty. If you do not specify a value, Zuora uses the default reason code.  | [optional] 
**reference_id** | **str** | The ID of the payment that the credit balance adjustment is for.  | [optional] 
**source_transaction_id** | **str** | The ID of the object that the credit balance adjustment is applied to. You must specify a value for either the &#x60;SourceTransactionId&#x60; field or the &#x60;SourceTransactionNumber&#x60; field.  The value of this field must be one of the following:  * An invoice ID  * A payment ID  * A refund ID  | [optional] 
**source_transaction_number** | **str** | The number of the object that the credit balance adjustment is applied to. You must specify a value for either the &#x60;SourceTransactionId&#x60; field or the &#x60;SourceTransactionNumber&#x60; field.  The value of this field must be one of the following:  * An invoice number  * A payment number  * A refund number  | [optional] 
**type** | **str** | Whether the credit balance adjustment increases or decrease the amount of the credit balance.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


