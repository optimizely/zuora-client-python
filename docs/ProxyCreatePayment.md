# ProxyCreatePayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the payment&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**origin__ns** | **str** | Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the payment was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**transaction__ns** | **str** | Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**account_id** | **str** | The unique account ID for the customer that the payment is for.  | 
**accounting_code** | **str** | The aacccounting code for the payment. Accounting codes group transactions that contain similar accounting attributes.  | [optional] 
**amount** | **float** | The amount of the payment.  | [optional] 
**applied_credit_balance_amount** | **float** | The amount of the payment to apply to a credit balance. This field is only required if the &#x60;AppliedInvoiceAmount&#x60; field value is null.  | [optional] 
**applied_invoice_amount** | **float** | The amount of the payment to apply to an invoice. This field is only required if either the &#x60;InvoiceId&#x60; or &#x60;InvoiceNumber&#x60; field is not null.  | [optional] 
**auth_transaction_id** | **str** | The authorization transaction ID from the payment gateway. Use this field for electronic payments, such as credit cards.  | [optional] 
**comment** | **str** | Additional information related to the payment.  | [optional] 
**effective_date** | **date** | The date when the payment takes effect.  | 
**gateway** | **str** | The name of the gateway instance that processes the payment. When creating a payment, the value of this field must be a valid gateway instance name, and this gateway must support the specific payment method. If no value is specified, the default gateway on the Account will be used.  | [optional] 
**gateway_option_data** | [**ProxyCreatePaymentGatewayOptionData**](ProxyCreatePaymentGatewayOptionData.md) |  | [optional] 
**gateway_order_id** | **str** | A merchant-specified natural key value that can be passed to the electronic payment gateway when a payment is created. If not specified, the payment number will be passed in instead.  Gateways check duplicates on the gateway order ID to ensure that the merchant do not accidentally enter the same transaction twice. This ID can also be used to do reconciliation and tie the payment to a natural key in external systems. The source of this ID varies by merchant. Some merchants use their shopping cart order IDs, and others use something different. Merchants use this ID to track transactions in their eCommerce systems.  | [optional] 
**gateway_response** | **str** | The message returned from the payment gateway for the payment. This message is gateway-dependent.  | [optional] 
**gateway_response_code** | **str** | The code returned from the payment gateway for the payment. This code is gateway-dependent.  | [optional] 
**gateway_state** | **str** | The status of the payment in the gateway; use for reconciliation.  | [optional] 
**invoice_id** | **str** | The ID of the invoice that the payment is applied to. When applying a payment to a single invoice, this field is only required if the &#x60;InvoiceNumber&#x60; field is null.  | [optional] 
**invoice_number** | **str** | The unique identification number for the invoice that the payment is applied to. When applying a payment to a single invoice, this field is only required if the &#x60;InvoiceId&#x60; field is null.  | [optional] 
**invoice_payment_data** | [**InvoicePaymentData**](InvoicePaymentData.md) |  | [optional] 
**payment_method_id** | **str** | The ID of the payment method used for the payment.   | 
**payment_number** | **str** | The unique identification number of the payment. For example, P-00000028.  | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway. Use this field to reconcile payments between your gateway and Zuora Payments.  | [optional] 
**soft_descriptor** | **str** | A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi.   Zuora passes this field to Verifi directly without verification. In general, this field will be defaulted by the gateway. For Orbital, this field contains two fields separated by an asterisk, &#x60;SDMerchantName&#x60; and &#x60;SDProductionInfo&#x60;. For more information, contact your payment gateway.  | [optional] 
**soft_descriptor_phone** | **str** | A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi.  Verifi and Orbital determine how to format this string. For more information, contact your payment gateway.  | [optional] 
**status** | **str** | The status of the payment in Zuora. The value depends on the type of payment.  For electronic payments, the status can be &#x60;Processed&#x60;, &#x60;Error&#x60;, or &#x60;Voided&#x60;. For external payments, the status can be &#x60;Processed&#x60; or &#x60;Canceled&#x60;.  | 
**type** | **str** | The type of the payment, whether the payment is external or electronic.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


