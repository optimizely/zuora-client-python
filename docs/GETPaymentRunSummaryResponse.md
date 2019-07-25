# GETPaymentRunSummaryResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_credit_balance_adjustments** | **int** | **Note:** This field is only available if you have the Credit Balance feature enabled.  The number of credit balance adjustments that are successfully processed in the payment run.  | [optional] 
**number_of_credit_memos** | **int** | **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total number of credit memos that are successfully processed in the payment run.  | [optional] 
**number_of_debit_memos** | **int** | **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total number of debit memos that are picked up for processing in the payment run.  | [optional] 
**number_of_errors** | **int** | The number of payments with the status of &#x60;Error&#x60; and &#x60;Processing&#x60;.  | [optional] 
**number_of_invoices** | **int** | **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The total number of invoices that are picked up for processing in the payment run.  | [optional] 
**number_of_payments** | **int** | The number of payments that are successfully processed in the payment run.  | [optional] 
**number_of_receivables** | **int** | The total number of receivables that are picked up for processing in the payment run.  The value of this field is the sum of the value of the &#x60;numberOfInvoices&#x60; field and that of the &#x60;numberOfDebitMemos&#x60; field.  | [optional] 
**number_of_unapplied_payments** | **int** | **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The number of unapplied payments that are successfully processed in the payment run.  | [optional] 
**number_of_unprocessed_debit_memos** | **int** | **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The number of debit memos with remaining positive balances after the payment run is completed.  | [optional] 
**number_of_unprocessed_invoices** | **int** | **Note:** This field is only available if you have the Invoice Settlement feature enabled.  The number of invoices with remaining positive balances after the payment run is completed.  | [optional] 
**number_of_unprocessed_receivables** | **int** | The number of receivables with remaining positive balances after the payment run is completed.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**total_values** | [**list[GETPaymentRunSummaryTotalValues]**](GETPaymentRunSummaryTotalValues.md) | Container for total values.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

