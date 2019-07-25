# ProxyCreateBillRun

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account used for single account bill run.  This field is only required if you create ad hoc bill run for a single customer account.  **Character limit:** 32  | [optional] 
**auto_email** | **bool** | Determines whether to auto send email or not by this bill run once the bill run completes.  **Note:** You must enable the [Support Bill Run Auto-Post Billing](https://knowledgecenter.zuora.com/CB_Billing/Billing_Settings/Define_Billing_Rules) rule to pass this field.  | [optional] [default to False]
**auto_post** | **bool** | Determines whether to auto post bill run or not once the bill run completes.  **Note:** You must enable the [Support Bill Run Auto-Post Billing](https://knowledgecenter.zuora.com/CB_Billing/Billing_Settings/Define_Billing_Rules) rule to pass this field.  | [optional] [default to False]
**auto_renewal** | **bool** | Determines whether to auto renew subscription or not by this bill run once the bill run completes.  | [optional] [default to False]
**batch** | **str** | Batch of accounts for this bill run.   When creating ad hoc bill run for multiple customer accounts, this field is only required if the &#x60;BillCycleDay&#x60;  field is not specified.  **Character limit:** 20  **Values:** AllBatches or Batchn where n is a number between 1 and 50.  | [optional] 
**bill_cycle_day** | **str** | The day of the bill cycle.  When creating ad hoc bill run for multiple customer accounts, this field is only required if the &#x60;Batch&#x60; field is not specified.  **Character limit:** 32  **Values:** &#x60;AllBillCycleDays&#x60; or 01 - 31.  | [optional] 
**charge_type_to_exclude** | **str** | Charge type or types to be excluded, separated with comma.  **Possible Values:** &#x60;OneTime&#x60;, &#x60;Recurring&#x60;, &#x60;Usage&#x60;, or a combination of these values.   **Character limit:** 50  | [optional] 
**invoice_date** | **date** | Invoice date for this bill run.  **Character limit:** 29  | 
**no_email_for_zero_amount_invoice** | **bool** | Determines whether to suppress email for invoices with zero total or not for this bill run once the bill run completes. (Do not email invoices with 0 Invoice Total).  | [optional] [default to False]
**target_date** | **date** | Target date for this bill run. See [Create Bill Run](https://knowledgecenter.zuora.com/CB_Billing/J_Billing_Operations/G_Bill_Runs/Creating_Bill_Runs) for more information.  **Character limit:** 29  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

