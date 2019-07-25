# PUTSubscriptionResumeResponseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_memo_id** | **str** | The credit memo ID, if a credit memo is generated during the subscription process.  **Note:** This field is only available if you have the Invoice Settlements feature enabled.  | [optional] 
**invoice_id** | **str** | Invoice ID, if an invoice is generated during the subscription process.  | [optional] 
**paid_amount** | **str** | Payment amount, if a payment is collected.  | [optional] 
**payment_id** | **str** | Payment ID, if a payment is collected.  | [optional] 
**resume_date** | **date** | The date when subscription resumption takes effect, as yyyy-mm-dd.  | [optional] 
**subscription_id** | **str** | The subscription ID.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**term_end_date** | **date** | The date when the new subscription term ends, as yyyy-mm-dd.  | [optional] 
**total_delta_tcv** | **str** | Change in the total contracted value of the subscription as a result of the update.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

