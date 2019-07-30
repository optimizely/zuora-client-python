# GETInvoiceType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the invoice&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the invoice was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**account_id** | **str** | Customer account ID.  | [optional] 
**account_name** | **str** | Customer account name.  | [optional] 
**account_number** | **str** | Customer account number.  | [optional] 
**amount** | **str** | Amount of the invoice before adjustments, discounts, and similar items.  | [optional] 
**balance** | **str** | Balance remaining due on the invoice (after adjustments, discounts, etc.)  | [optional] 
**body** | **str** | The REST URL of the invoice PDF file.  | [optional] 
**created_by** | **str** | User ID of the person who created the invoice. If a bill run generated the invoice, then this is the user ID of person who created the bill run.  | [optional] 
**credit_balance_adjustment_amount** | **str** |  | [optional] 
**due_date** | **date** | Payment due date as _yyyy-mm-dd_.  | [optional] 
**id** | **str** | Invoice ID.  | [optional] 
**invoice_date** | **date** | Invoice date as _yyyy-mm-dd_  | [optional] 
**invoice_files** | **str** | URL to retrieve information about all files of a specific invoice if any file exists; otherwise absent. For example, &#x60;https://rest.zuora.com/v1/invoices/2c92c095511f5b4401512682dcfd7987/files&#x60;. If you want to view the invoice file details, call [Get invoice files](https://www.zuora.com/developer/api-reference/#operation/GET_InvoiceFiles) with the returned URL.  If your tenant was created before Zuora Release 228 (R228), July 2018, the value of this field is an array of invoice file details. For more information about the array, see the response body of [Get invoice files](https://www.zuora.com/developer/api-reference/#operation/GET_InvoiceFiles).   Zuora recommends that you use the latest behavior to retrieve invoice information. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/) asking for invoice item and file references to be enabled in the REST API.  | [optional] 
**invoice_items** | **str** | URL to retrieve information about all items of a specific invoice. For example, &#x60;https://rest.zuora.com/v1/invoices/2c92c095511f5b4401512682dcfd7987/items&#x60;. If you want to view the invoice item details, call [Get invoice items](https://www.zuora.com/developer/api-reference/#operation/GET_InvoiceItems) with the returned URL.  If your tenant was created before Zuora Release 228 (R228), July 2018, the value of this field is an array of invoice item details. For more information about the array, see the response body of [Get invoice items](https://www.zuora.com/developer/api-reference/#operation/GET_InvoiceItems).   Zuora recommends that you use the latest behavior to retrieve invoice information. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/) asking for invoice item and file references to be enabled in the REST API.   | [optional] 
**invoice_number** | **str** | Unique invoice ID, returned as a string.  | [optional] 
**invoice_target_date** | **date** | Date through which charges on this invoice are calculated, as _yyyy-mm-dd_.  | [optional] 
**reversed** | **bool** | Whether the invoice is reversed.  | [optional] 
**status** | **str** | Status of the invoice in the system - not the payment status, but the status of the invoice itself. Possible values are: &#x60;Posted&#x60;, &#x60;Draft&#x60;, &#x60;Canceled&#x60;, &#x60;Error&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


