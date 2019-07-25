# ProxyGetPaymentTransactionLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avs_response_code** | **str** | The response code returned by the payment gateway referring to the AVS international response of the payment transaction.  | [optional] 
**batch_id** | **str** | The ID of the batch used to send the transaction if the request was sent in a batch.  | [optional] 
**cvv_response_code** | **str** | The response code returned by the payment gateway referring to the CVV international response of the payment transaction.  | [optional] 
**gateway** | **str** | The name of the payment gateway used to transact the current payment transaction log.  | [optional] 
**gateway_reason_code** | **str** | The code returned by the payment gateway for the payment. This code is gateway-dependent.  | [optional] 
**gateway_reason_code_description** | **str** | The message returned by the payment gateway for the payment. This message is gateway-dependent.   | [optional] 
**gateway_state** | **str** | The state of the transaction at the payment gateway.  | [optional] 
**gateway_transaction_type** | **str** | The type of the transaction, either making a payment, or canceling a payment.   | [optional] 
**id** | **str** | The ID of the payment transaction log.  | [optional] 
**payment_id** | **str** | The ID of the payment wherein the payment transaction log was recorded.   | [optional] 
**request_string** | **str** | The payment transaction request string sent to the payment gateway.   | [optional] 
**response_string** | **str** | The payment transaction response string returned by the payment gateway.   | [optional] 
**transaction_date** | **datetime** | The transaction date when the payment was performed.   | [optional] 
**transaction_id** | **str** | The transaction ID returned by the payment gateway. This field is used to reconcile payment transactions between the payment gateway and records in Zuora.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

