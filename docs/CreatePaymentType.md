# CreatePaymentType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the payment&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**origin__ns** | **str** | Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the payment was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**transaction__ns** | **str** | Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**account_id** | **str** | The ID of the customer account that the payment is created for.  | [optional] 
**amount** | **float** | The total amount of the payment.  | 
**comment** | **str** | Additional information related to the payment.  | [optional] 
**currency** | **str** | A currency defined in the web-based UI administrative settings.  | 
**debit_memos** | [**list[PaymentDebitMemoApplicationCreateRequestType]**](PaymentDebitMemoApplicationCreateRequestType.md) | Container for debit memos.  | [optional] 
**effective_date** | **date** | The date when the payment takes effect, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**finance_information** | [**CreatePaymentTypeFinanceInformation**](CreatePaymentTypeFinanceInformation.md) |  | [optional] 
**gateway_id** | **str** | The ID of the gateway instance that processes the payment. The ID must be a valid gateway instance ID and this gateway must support the specific payment method.   - When creating electronic payments, this field is required.  - When creating external payments, this field is optional.  | [optional] 
**invoices** | [**list[PaymentInvoiceApplicationCreateRequestType]**](PaymentInvoiceApplicationCreateRequestType.md) | Container for invoices.  | [optional] 
**payment_method_id** | **str** | The unique ID of the payment method that the customer used to make the payment.   If no payment method ID is specified in the request body, the default payment method for the customer account is used automatically. If the default payment method is different from the type of payments that you want to create, an error occurs.  | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway. Use this field to reconcile payments between your gateway and Zuora Payments.  | [optional] 
**type** | **str** | The type of the payment.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


