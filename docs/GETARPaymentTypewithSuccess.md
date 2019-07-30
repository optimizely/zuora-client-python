# GETARPaymentTypewithSuccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the payment&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**origin__ns** | **str** | Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the payment was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**transaction__ns** | **str** | Related transaction in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**account_id** | **str** | The ID of the customer account that the payment is for.  | [optional] 
**amount** | **float** | The total amount of the payment.  | [optional] 
**applied_amount** | **float** | The applied amount of the payment.  | [optional] 
**auth_transaction_id** | **str** | The authorization transaction ID from the payment gateway.  | [optional] 
**bank_identification_number** | **str** | The first six digits of the credit card or debit card used for the payment, when applicable.  | [optional] 
**cancelled_on** | **datetime** | The date and time when the payment was cancelled, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**comment** | **str** | Comments about the payment.  | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the payment part.  | [optional] 
**created_date** | **datetime** | The date and time when the payment was created, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-01 15:31:10.  | [optional] 
**credit_balance_amount** | **float** | The amount that the payment transfers to the credit balance. The value is not &#x60;0&#x60; only for those payments that come from legacy payment operations performed without the Invoice Settlement feature.  | [optional] 
**currency** | **str** | A currency defined in the web-based UI administrative settings.  For more information about the supported currencies and , see [ISO Currency Codes] (https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Country%2C_State%2C_and_Province_Codes/D_Currencies_and_Their_3-Letter_Codes).  | [optional] 
**effective_date** | **datetime** | The date and time when the payment takes effect, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**finance_information** | [**GETARPaymentTypeFinanceInformation**](GETARPaymentTypeFinanceInformation.md) |  | [optional] 
**gateway_id** | **str** | The ID of the gateway instance that processes the payment.  | [optional] 
**gateway_order_id** | **str** | A merchant-specified natural key value that can be passed to the electronic payment gateway when a payment is created.  | [optional] 
**gateway_response** | **str** | The message returned from the payment gateway for the payment. This message is gateway-dependent.  | [optional] 
**gateway_response_code** | **str** | The code returned from the payment gateway for the payment. This code is gateway-dependent.  | [optional] 
**gateway_state** | **str** | The status of the payment in the gateway; use for reconciliation.   | [optional] 
**id** | **str** | The unique ID of the payment. For example, 4028905f5a87c0ff015a87eb6b75007f.  | [optional] 
**marked_for_submission_on** | **datetime** | The date and time when a payment was marked and waiting for batch submission to the payment process, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**number** | **str** | The unique identification number of the payment. For example, P-00000001.  | [optional] 
**payment_method_id** | **str** | The unique ID of the payment method that the customer used to make the payment.  | [optional] 
**payment_method_snapshot_id** | **str** | The unique ID of the payment method snapshot which is a copy of the particular Payment Method used in a transaction.  | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway. Use this field to reconcile payments between your gateway and Zuora Payments.  | [optional] 
**refund_amount** | **float** | The amount of the payment that is refunded.  | [optional] 
**second_payment_reference_id** | **str** | The transaction ID returned by the payment gateway if there is an additional transaction for the payment. Use this field to reconcile payments between your gateway and Zuora Payments.  | [optional] 
**settled_on** | **datetime** | The date and time when the payment was settled in the payment processor, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. This field is used by the Spectrum gateway only and not applicable to other gateways.  | [optional] 
**soft_descriptor** | **str** | A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi.  | [optional] 
**soft_descriptor_phone** | **str** | A payment gateway-specific field that maps to Zuora for the gateways, Orbital, Vantiv and Verifi.  | [optional] 
**status** | **str** | The status of the payment.  | [optional] 
**submitted_on** | **datetime** | The date and time when the payment was submitted, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**type** | **str** | The type of the payment.  | [optional] 
**unapplied_amount** | **float** | The unapplied amount of the payment.  | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the payment.  | [optional] 
**updated_date** | **datetime** | The date and time when the payment was last updated, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-02 15:36:10.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


