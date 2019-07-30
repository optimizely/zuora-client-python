# ProxyModifyPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the payment&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**origin__ns** | **str** | Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the payment was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**transaction__ns** | **str** | Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**account_id** | **str** | The unique account ID for the customer that the payment is for.  | [optional] 
**accounting_code** | **str** | The aacccounting code for the payment. Accounting codes group transactions that contain similar accounting attributes.  | [optional] 
**amount** | **float** | The amount of the payment.  | [optional] 
**comment** | **str** | Additional information related to the payment.  | [optional] 
**effective_date** | **date** | The date when the payment takes effect.  | [optional] 
**payment_method_id** | **str** | The ID of the payment method used for the payment.   | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway. Use this field to reconcile payments between your gateway and Zuora Payments.  | [optional] 
**status** | **str** | The status of the payment in Zuora. The value depends on the type of payment.  For electronic payments, the status can be &#x60;Processed&#x60;, &#x60;Error&#x60;, or &#x60;Voided&#x60;. For external payments, the status can be &#x60;Processed&#x60; or &#x60;Canceled&#x60;.  | [optional] 
**transferred_to_accounting** | **str** | Whether the refund was transferred to an external accounting system. Use this field for integration with accounting systems, such as NetSuite.  | [optional] 
**type** | **str** | The type of the payment, whether the payment is external or electronic.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


