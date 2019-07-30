# POSTSettlePaymentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the customer account that the payment is for.  | [optional] 
**amount** | **float** | The total amount of the payment.  | [optional] 
**applied_amount** | **float** | The applied amount of the payment.  | [optional] 
**auth_transaction_id** | **str** | The authorization transaction ID from the payment gateway.  | [optional] 
**bank_identification_number** | **str** | The first six digits of the credit card or debit card used for the payment, when applicable.  | [optional] 
**cancelled_on** | **datetime** | The date and time when the payment was cancelled, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**comment** | **str** | Comments about the payment.  | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the refund.  | [optional] 
**created_date** | **datetime** | The date and time when the chargeback is created, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2019-03-01 15:31:10.  | [optional] 
**credit_balance_amount** | **float** | The amount that the payment transfers to the credit balance. The value is not &#x60;0&#x60; only for those payments that come from legacy payment operations performed without the Invoice Settlement feature.  | [optional] 
**currency** | **str** | A currency defined in the web-based UI administrative settings.  | [optional] 
**effective_date** | **datetime** | The date and time when the payment takes effect, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**finance_information** | [**POSTRejectPaymentResponseFinanceInformation**](POSTRejectPaymentResponseFinanceInformation.md) |  | [optional] 
**gateway_id** | **str** | The ID of the gateway instance that processes the payment.  | [optional] 
**gateway_order_id** | **str** | A merchant-specified natural key value that can be passed to the electronic payment gateway when a payment is created. If not specified, the payment number will be passed in instead.  | [optional] 
**gateway_response** | **str** | The message returned from the payment gateway for the payment. This message is gateway-dependent.  | [optional] 
**gateway_response_code** | **str** | The code returned from the payment gateway for the payment. This code is gateway-dependent.  | [optional] 
**gateway_state** | **str** | The status of the payment in the gateway; used for reconciliation.  | [optional] 
**id** | **str** | The ID of the payment chargeback.  | [optional] 
**marked_for_submission_on** | **datetime** | The date and time when a charge was marked and waiting for batch submission to the payment process, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**number** | **str** | The unique identification number of the payment. For example, P-00000001.  | [optional] 
**payment_method_id** | **str** | The unique ID of the payment method that the customer used to make the payment.  | [optional] 
**payment_method_snapshot_id** | **str** | The unique ID of the payment method snapshot which is a copy of the particular Payment Method used in a transaction.  | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway for an electronic refund. Use this field to reconcile refunds between your gateway and Zuora Payments.  | [optional] 
**refund_amount** | **float** | The amount of the payment that is refunded.  | [optional] 
**second_payment_reference_id** | **str** | The transaction ID returned by the payment gateway if there is an additional transaction for the payment.   | [optional] 
**settled_on** | **datetime** | The date and time when the transaction is settled, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**soft_descriptor** | **str** | A payment gateway-specific field that maps Zuora to other gateways.  | [optional] 
**soft_descriptor_phone** | **str** | A payment gateway-specific field that maps Zuora to other gateways.  | [optional] 
**status** | **str** | The status of the payment.  | [optional] 
**submitted_on** | **datetime** | The date and time when the payment was submitted, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**success** | **bool** | Indicates if the request is processed successfully.  | [optional] 
**type** | **str** | The type of the payment.  | [optional] 
**unapplied_amount** | **float** | The unapplied amount of the payment.  | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the payment.  | [optional] 
**updated_date** | **datetime** | The date and time when the payment was last updated, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2019-03-02 15:36:10.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


