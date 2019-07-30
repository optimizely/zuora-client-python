# GETDebitMemoTypewithSuccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the debit memo&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**account_id** | **str** | The ID of the customer account associated with the debit memo.  | [optional] 
**amount** | **float** | The total amount of the debit memo.  | [optional] 
**auto_pay** | **bool** | Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.        | [optional] 
**balance** | **float** | The balance of the debit memo.  | [optional] 
**be_applied_amount** | **float** | The applied amount of the debit memo.  | [optional] 
**cancelled_by_id** | **str** | The ID of the Zuora user who cancelled the debit memo.  | [optional] 
**cancelled_on** | **datetime** | The date and time when the debit memo was cancelled, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**comment** | **str** | Comments about the debit memo.  | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the debit memo.  | [optional] 
**created_date** | **datetime** | The date and time when the debit memo was created, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-01 15:31:10.  | [optional] 
**debit_memo_date** | **date** | The date when the debit memo takes effect, in &#x60;yyyy-mm-dd&#x60; format. For example, 2017-05-20.  | [optional] 
**due_date** | **date** | The date by which the payment for the debit memo is due, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**id** | **str** | The unique ID of the debit memo.  | [optional] 
**latest_pdf_file_id** | **str** | The ID of the latest PDF file generated for the debit memo.  | [optional] 
**number** | **str** | The unique identification number of the debit memo.  | [optional] 
**posted_by_id** | **str** | The ID of the Zuora user who posted the debit memo.  | [optional] 
**posted_on** | **datetime** | The date and time when the debit memo was posted, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**reason_code** | **str** | A code identifying the reason for the transaction. The value must be an existing reason code or empty.  | [optional] 
**referred_invoice_id** | **str** | The ID of a referred invoice.  | [optional] 
**status** | **str** | The status of the debit memo.   | [optional] 
**target_date** | **date** | The target date for the debit memo, in &#x60;yyyy-mm-dd&#x60; format. For example, 2017-07-20.  | [optional] 
**tax_amount** | **float** | The amount of taxation.  | [optional] 
**total_tax_exempt_amount** | **float** | The total amount of taxes or VAT for which the customer has an exemption.  | [optional] 
**transferred_to_accounting** | **str** | Whether the debit memo was transferred to an external accounting system. Use this field for integration with accounting systems, such as NetSuite.   | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the debit memo.  | [optional] 
**updated_date** | **datetime** | The date and time when the debit memo was last updated, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-02 15:31:10.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


