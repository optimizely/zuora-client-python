# ProxyGetPayment

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
**applied_credit_balance_amount** | **float** | The amount of the payment to apply to a credit balance.  | [optional] 
**auth_transaction_id** | **str** | The authorization transaction ID from the payment gateway.   | [optional] 
**bank_identification_number** | **str** | The first six digits of the credit card or debit card used for the payment, when applicable.   | [optional] 
**cancelled_on** | **datetime** | The date and time when the payment was canceled.  | [optional] 
**comment** | **str** | Additional information related to the payment.  | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the payment.  | [optional] 
**created_date** | **datetime** | The date and time when the payment was created.  | [optional] 
**effective_date** | **date** | The date when the payment takes effect.  | [optional] 
**gateway** | **str** | The name of the gateway instance that processes the payment.   | [optional] 
**gateway_order_id** | **str** | A merchant-specified natural key value that can be passed to the electronic payment gateway when a payment is created. If not specified, the payment number will be passed in instead.  | [optional] 
**gateway_response** | **str** | The message returned from the payment gateway for the payment. This message is gateway-dependent.  | [optional] 
**gateway_response_code** | **str** | The code returned from the payment gateway for the payment. This code is gateway-dependent.  | [optional] 
**gateway_state** | **str** | The status of the payment in the gateway; use for reconciliation.  | [optional] 
**id** | **str** | The unique ID of a payment. For example, 2c92c095592623ea01596621ada84352.  | [optional] 
**marked_for_submission_on** | **datetime** | The date and time when a payment was marked and waiting for batch submission to the payment process.   | [optional] 
**payment_method_id** | **str** | The ID of the payment method used for the payment.   | [optional] 
**payment_method_snapshot_id** | **str** | The unique ID of the payment method snapshot which is a copy of the particular payment method used in a transaction.  | [optional] 
**payment_number** | **str** | The unique identification number of the payment. For example, P-00000028.  | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway. Use this field to reconcile payments between your gateway and Zuora Payments.  | [optional] 
**refund_amount** | **float** | The amount of the payment that is refunded. The value of this field is &#x60;0&#x60; if no refund is made against the payment.  | [optional] 
**second_payment_reference_id** | **str** | The transaction ID returned by the payment gateway if there is an additional transaction for the payment. Use this field to reconcile payments between your gateway and Zuora Payments.  | [optional] 
**settled_on** | **datetime** | The date and time when the payment was settled in the payment processor. This field is used by the Spectrum gateway only and not applicable to other gateways.  | [optional] 
**soft_descriptor** | **str** | A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi.   | [optional] 
**soft_descriptor_phone** | **str** | A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi.  | [optional] 
**source** | **str** | How the payment was created, whether through the API, manually, import, or payment run.  | [optional] 
**source_name** | **str** | The name of the source. The value is a Payment Run number or a file name.  | [optional] 
**status** | **str** | The status of the payment in Zuora. The value depends on the type of payment.  For electronic payments, the status can be &#x60;Processed&#x60;, &#x60;Processing&#x60;, &#x60;Error&#x60;, or &#x60;Voided&#x60;. For external payments, the status can be &#x60;Processed&#x60; or &#x60;Canceled&#x60;.  | [optional] 
**submitted_on** | **datetime** | The date and time when the payment was submitted.  | [optional] 
**transferred_to_accounting** | **str** | Indicates if the payment was transferred to an external accounting system. Use this field for integration with accounting systems, such as NetSuite.  | [optional] 
**type** | **str** | The type of the payment, whether the payment is external or electronic.  | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the payment.  | [optional] 
**updated_date** | **datetime** | The date and time when the payment was last updated.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


