# PUTDebitMemoType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the debit memo&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the debit memo was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**auto_pay** | **bool** | Whether debit memos are automatically picked up for processing in the corresponding payment run.   By default, debit memos are automatically picked up for processing in the corresponding payment run.  | [optional] 
**comment** | **str** | Comments about the debit memo.  | [optional] 
**due_date** | **date** | The date by which the payment for the debit memo is due, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**effective_date** | **date** | The date when the debit memo takes effect.  | [optional] 
**items** | [**list[PUTDebitMemoItemType]**](PUTDebitMemoItemType.md) | Container for debit memo items.  | [optional] 
**reason_code** | **str** | A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code  | [optional] 
**transferred_to_accounting** | **str** | Whether the debit memo is transferred to an external accounting system. Use this field for integration with accounting systems, such as NetSuite.   | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


