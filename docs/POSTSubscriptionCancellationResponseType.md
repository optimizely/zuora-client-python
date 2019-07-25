# POSTSubscriptionCancellationResponseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled_date** | **date** | The date that the subscription was canceled.  | [optional] 
**credit_memo_id** | **str** | The credit memo ID, if a credit memo is generated during the subscription process.  **Note:** This field is only available if you have the Invoice Settlements feature enabled.  | [optional] 
**invoice_id** | **str** | ID of the invoice, if one is generated.  | [optional] 
**paid_amount** | **str** | Amount paid.  | [optional] 
**payment_id** | **str** | ID of the payment, if a payment is collected.  | [optional] 
**subscription_id** | **str** | The subscription ID.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**total_delta_mrr** | **str** | Change in the subscription monthly recurring revenue as a result of the update.  | [optional] 
**total_delta_tcv** | **str** | Change in the total contracted value of the subscription as a result of the update.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

