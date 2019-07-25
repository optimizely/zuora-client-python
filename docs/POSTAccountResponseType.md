# POSTAccountResponseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Auto-generated account ID.  | [optional] 
**account_number** | **str** | Account number.  | [optional] 
**bill_to_contact_id** | **str** | The ID of the bill-to contact.  | [optional] 
**contracted_mrr** | **str** | Contracted monthly recurring revenue of the subscription.  | [optional] 
**credit_memo_id** | **str** | The credit memo ID, if a credit memo is generated during the subscription process.  **Note:** This field is only available if you have the Invoice Settlements feature enabled.  | [optional] 
**invoice_id** | **str** | ID of the invoice generated at account creation, if applicable.  | [optional] 
**paid_amount** | **str** | Amount collected on the invoice generated at account creation, if applicable.  | [optional] 
**payment_id** | **str** | ID of the payment collected on the invoice generated at account creation, if applicable.  | [optional] 
**payment_method_id** | **str** | ID of the payment method that was set up at account creation, which automatically becomes the default payment method for this account.  | [optional] 
**sold_to_contact_id** | **str** | The ID of the sold-to contact.  | [optional] 
**subscription_id** | **str** | ID of the subscription that was set up at account creation, if applicable.  | [optional] 
**subscription_number** | **str** | Number of the subscription that was set up at account creation, if applicable.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**total_contracted_value** | **str** | Total contracted value of the subscription.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

