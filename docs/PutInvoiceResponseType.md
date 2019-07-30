# PutInvoiceResponseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the invoice&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the invoice was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**account_id** | **str** | The ID of the customer account associated with the invoice.  | [optional] 
**amount** | **float** | The total amount of the invoice.  | [optional] 
**auto_pay** | **bool** | Whether invoices are automatically picked up for processing in the corresponding payment run.   | [optional] 
**balance** | **float** | The balance of the invoice.  | [optional] 
**cancelled_by_id** | **str** | The ID of the Zuora user who cancelled the invoice.  | [optional] 
**cancelled_on** | **datetime** | The date and time when the invoice was cancelled, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**comment** | **str** | Comments about the invoice.   | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the invoice.  | [optional] 
**created_date** | **datetime** | The date and time when the invoice was created, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-01 15:31:10.  | [optional] 
**credit_balance_adjustment_amount** | **float** | **Note:** This filed is only available if you have the Credit Balance feature enabled and the Invoice Settlement feature disabled.  The currency amount of the adjustment applied to the customer&#39;s credit balance.  | [optional] 
**currency** | **str** | A currency defined in the web-based UI administrative settings.  | [optional] 
**due_date** | **date** | The date by which the payment for this invoice is due.   | [optional] 
**id** | **str** | The unique ID of the invoice.  | [optional] 
**invoice_date** | **date** | The date on which to generate the invoice.  | [optional] 
**number** | **str** | The unique identification number of the invoice.  | [optional] 
**posted_by_id** | **str** | The ID of the Zuora user who posted the invoice.  | [optional] 
**posted_on** | **datetime** | The date and time when the invoice was posted, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.   | [optional] 
**status** | **str** | The status of the invoice.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**target_date** | **date** | The target date for the invoice, in &#x60;yyyy-mm-dd&#x60; format. For example, 2017-07-20.   | [optional] 
**tax_amount** | **float** | The amount of taxation.  | [optional] 
**total_tax_exempt_amount** | **float** | The total amount of taxes or VAT for which the customer has an exemption.  | [optional] 
**transferred_to_accounting** | **str** | Whether the invoice was transferred to an external accounting system.  | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the invoice.  | [optional] 
**updated_date** | **datetime** | The date and time when the invoice was last updated, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-02 15:36:10.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


