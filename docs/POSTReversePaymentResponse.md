# POSTReversePaymentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the customer account that the payment is for.  | [optional] 
**amount** | **float** | The total amount of the payment.  | [optional] 
**cancelled_on** | **datetime** | The date and time when the payment was cancelled, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**comment** | **str** | Comments about the payment.  | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the refund.  | [optional] 
**created_date** | **datetime** | The date and time when the chargeback is created, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2019-03-01 15:31:10.  | [optional] 
**credit_memo_id** | **str** | The ID of the credit memo that is refunded.  | [optional] 
**finance_information** | **object** | Container for the finance information related to the refund.  | [optional] 
**gateway_id** | **str** | The ID of the gateway instance that processes the payment.  | [optional] 
**gateway_response** | **str** | The message returned from the payment gateway for the payment. This message is gateway-dependent.  | [optional] 
**gateway_response_code** | **str** | The code returned from the payment gateway for the payment. This code is gateway-dependent.  | [optional] 
**gateway_state** | **str** | The status of the payment in the gateway; used for reconciliation.  | [optional] 
**id** | **str** | The ID of the payment chargeback.  | [optional] 
**marked_for_submission_on** | **datetime** | The date and time when a charge was marked and waiting for batch submission to the payment process, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**method_type** | **str** | How an external refund was issued to a customer.   | [optional] 
**number** | **str** | The unique identification number of the payment. For example, P-00000001.  | [optional] 
**payment_id** | **str** | The ID of the payment that is refunded.  | [optional] 
**payment_method_id** | **str** | The unique ID of the payment method that the customer used to make the payment.  | [optional] 
**payment_method_snapshot_id** | **str** | The unique ID of the payment method snapshot which is a copy of the particular Payment Method used in a transaction.  | [optional] 
**reason_code** | **str** | A code identifying the reason for the transaction.     | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway for an electronic refund. Use this field to reconcile refunds between your gateway and Zuora Payments.  | [optional] 
**refund_date** | **date** | The date when the refund takes effect, in &#x60;yyyy-mm-dd&#x60; format. For example, 2017-03-01.  | [optional] 
**refund_transaction_time** | **datetime** | The date and time when the refund was issued, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**second_refund_reference_id** | **str** | The transaction ID returned by the payment gateway if there is an additional refund.   | [optional] 
**settled_on** | **datetime** | The date and time when the transaction is settled, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**soft_descriptor** | **str** | A payment gateway-specific field that maps Zuora to other gateways.  | [optional] 
**soft_descriptor_phone** | **str** | A payment gateway-specific field that maps Zuora to other gateways.            | [optional] 
**status** | **str** | The status of the payment.  | [optional] 
**submitted_on** | **datetime** | The date and time when the payment was submitted, in yyyy-mm-dd hh:mm:ss format.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**type** | **str** | The type of the payment.  | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the payment.  | [optional] 
**updated_date** | **datetime** | The date and time when the payment was last updated, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2019-03-02 15:36:10.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

