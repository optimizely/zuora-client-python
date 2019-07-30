# ProxyGetCreditBalanceAdjustment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the credit balance adjustment&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the credit balance adjustment was sychronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**account_id** | **str** |  The account ID of the credit balance&#39;s account. Zuora generates this value from the source transaction. **Character limit**: 32 **Values**: automatically generated from:  - CreditBalanceAdjustment.SourceTransactionId or - CreditBalanceAdjustment.SourceTransactionNumber  | [optional] 
**accounting_code** | **str** |  The Chart of Accounts  | [optional] 
**adjustment_date** | **date** |  The date when the credit balance adjustment is applied. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**amount** | **float** |  The amount of the adjustment. **Character limit**: 16 **Values**: a valid currency amount  | [optional] 
**cancelled_on** | **datetime** |  The date when the credit balance adjustment was canceled. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**comment** | **str** |  Use this field to record comments about the credit balance adjustment. **Character limit**: 255 **Values**: a string of 255 characters or fewer  | [optional] 
**created_by_id** | **str** |  The user ID of the person who created the credit balance adjustment. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**created_date** | **datetime** |  The date when the credit balance adjustmentwas generated. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**id** | **str** | Object identifier. | [optional] 
**number** | **str** |  A unique identifier for the credit balance adjustment. Zuora generates this number in the format, &lt;em&gt;CBA-xxxxxxxx&lt;/em&gt;, such as CBA-00375919. **Character limit**: 255 **Values**: automatically generated  | [optional] 
**reason_code** | **str** |  A code identifying the reason for the transaction. Must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code. **Character limit**: 32 **Values**: a valid reason code  | [optional] 
**reference_id** | **str** |  The ID of the payment that the credit balance adjustment is for. **Character limit**: 32 **Values**: a string of 60 characters or fewer  | [optional] 
**source_transaction_id** | **str** |  The ID of the object that the credit balance adjustment is applied to. You must specify a value for either the &#x60;SourceTransactionId&#x60; field or the &#x60;SourceTransactionNumber&#x60; field. **Character limit**: 32 **Values**: one of the following:  - InvoiceId - PaymentId - RefundId  | [optional] 
**source_transaction_number** | **str** |  The number of the object that the credit balance adjustment is applied to. You must specify a value for either the &#x60;SourceTransactionId&#x60; field or the &#x60;SourceTransactionNumber&#x60; field. **Character limit**: 50 **Values**: one of the following:  - InvoiceNumber - PaymentNumber - RefundNumber  | [optional] 
**source_transaction_type** | **str** |  The source of the credit balance adjustment. **Character limit**: **Values**: automatically generated; one of the following:  - Invoice - Payment - Refund  | [optional] 
**status** | **str** |  The status of the credit balance adjustment. **Character limit**: 9 **Values**: automatically generated; one of the following:  - Processed - Canceled  | [optional] 
**transferred_to_accounting** | **str** | Status of the credit balance adjustment&#39;s transfer to an external accounting system, such as NetSuite.  | [optional] 
**type** | **str** | Create Query Filter | [optional] 
**updated_by_id** | **str** |  The ID of the user who last updated the credit balance adjustment. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**updated_date** | **datetime** |  The date when the credit balance adjustment was last updated. **Character limit**: 29 **Values**: automatically generated  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


