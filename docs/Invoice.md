# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**adjustment_amount** | **float** |  The amount of the invoice adjustments associated with the invoice. **Character limi**t: 16  **Values**: a valid currency amount  | [optional] 
**amount** | **float** |  The sum of all charges and taxes associated with the invoice.   **Character limit**: 16  **Values**: automatically generated  | [optional] 
**amount_without_tax** | **float** |  The sum of all charges associated with the invoice. Taxes are excluded from this value.   **Character limit**: 16  **Values**: automatically generated  | [optional] 
**balance** | **float** |  The remaining balance of the invoice after all payments, adjustments, and refunds are applied.   **Character limit**: 16  **Values**: automatically generated  | [optional] 
**bill_run_id** | **str** |  The ID of a Bill Run.   **Character limit**: 32  **Values**: a BillRun ID  | [optional] 
**body** | **str** |  Required  | [optional] 
**comments** | **str** |  Additional information related to the invoice that a Zuora user added to the invoice.   **Character limit**: 255  **Values:** a string of 255 characters or fewer  | [optional] 
**created_by_id** | **str** |  The user ID of the person who created the invoice. If a bill run generated the invoice, then the value is the user ID of person who created the bill run.   **Character limit**: 32  **Values**: automatically generated  | [optional] 
**created_date** | **datetime** |  The date when the invoice was generated.   **Character limit**: 29  **Values**: automatically generated  | [optional] 
**credit_balance_adjustment_amount** | **float** |  The currency amount of the adjustment applied to the customer&#x27;s credit balance.   **Character limit**: 16  **Values**: a valid currency amount This field is only available if the [Zuora Global Support](http://support.zuora.com/) to enable this feature.    | [optional] 
**due_date** | **date** |  The date by which the payment for this invoice is due.   **Character limit**: 29  | [optional] 
**includes_one_time** | **bool** |  Specifies whether the invoice includes one-time charges.   **Character limit**: 5  **Values**: automatically generated from one of the following: &#x60;True&#x60; (default), &#x60;False&#x60;  | [optional] 
**includes_recurring** | **bool** |  Specifies whether the invoice includes recurring charges.   **Character limit**: 5  **Values**: automatically generated from one of the following: &#x60;True&#x60; (default), &#x60;False&#x60;  | [optional] 
**includes_usage** | **bool** |  Specifies whether the invoice includes usage charges.   **Character limit**: 5  **Values**: automatically generated from one of the following: &#x60;True &#x60;(default), &#x60;False&#x60;  | [optional] 
**invoice_date** | **date** |  Specifies the date on which to generate the invoice.   **Character limit**: 29  | [optional] 
**invoice_number** | **str** |  The unique identification number for the invoice. This number is returned as a string.   **Character limit**: 32  **Values**: automatically generated  | [optional] 
**last_email_sent_date** | **datetime** |  The date when the invoice was last emailed.   **Character limit**: 29  **Values**: automatically generated  | [optional] 
**payment_amount** | **float** |  The amount of payments applied to the invoice.   **Character limit**: 16 **Value**s: automatically generated  | [optional] 
**posted_by** | **str** |  The user ID of the person who moved the invoice to Posted status.   **Character limit**: 32  **Values**: automatically generated  | [optional] 
**posted_date** | **datetime** |  The date when the invoice was posted.   **Character limit:** 29  **Values**: automatically generated  | [optional] 
**refund_amount** | **float** |  Specifies the amount of a refund that was applied against an earlier payment on the invoice.   **Character limit**: 16  **Values**: automatically generated  | [optional] 
**regenerate_invoice_pdf** | **bool** |  Regenerates a PDF of an invoice that was already generated.  **Character limit**: 5  **Values**: &#x60;True&#x60;, &#x60;False&#x60;  | [optional] 
**status** | **str** |  The status of the invoice in the system. This status is not the status of the payment of the invoice, just the status of the invoice itself.   **Character limit**: 8  **Values**: one of the following:  -  Draft (default, automatically set upon invoice creation)  -  Posted  -  Canceled   | [optional] 
**target_date** | **date** |  This date is used to determine which charges are to be billed. All charges that are to be billed on this date or prior will be included in this bill run.   **Character limit**: 29  | [optional] 
**tax_amount** | **float** |  The total amount of the taxes applied to the invoice.   **Character limit**: 16  **Values**: automatically generated  | [optional] 
**tax_exempt_amount** | **float** |  The total amount of the invoice that is exempt from taxation.   **Character limit**: 16  **Values**: automatically generated  | [optional] 
**transferred_to_accounting** | **str** |  Specifies whether or not the invoice was transferred to an external accounting system, such as NetSuite.   **Character limit**: 10  **Values**: Processing, Yes, Error, Ignore  | [optional] 
**updated_by_id** | **str** |  | [optional] 
**updated_date** | **datetime** |  The date when the invoice was last updated.   **Character limit**: 29  **Values**: automatically generated  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

