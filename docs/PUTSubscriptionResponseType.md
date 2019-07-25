# PUTSubscriptionResponseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Invoice amount. Preview mode only.  | [optional] 
**amount_without_tax** | **str** | Invoice amount minus tax. Preview mode only.  | [optional] 
**charge_metrics** | **object** | Container for charge metrics.  | [optional] 
**credit_memo** | **object** | Container for credit memos.  **Note:** This container is only available if you set the Zuora REST API minor version to 207.0 or later in the request header, and you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   | [optional] 
**credit_memo_id** | **str** | The credit memo ID, if a credit memo is generated during the subscription process.  **Note:** This field is only available if you have the Invoice Settlements feature enabled.  | [optional] 
**invoice** | **object** | Container for invoices.    **Note:** This field is only available if you set the Zuora REST API minor version to 207.0 or later in the request header. Also, the response structure is changed and the following invoice related response fields are moved to this **invoice** container:       * amount    * amountWithoutTax    * taxAmount    * invoiceItems    * targetDate    * chargeMetrics  | [optional] 
**invoice_id** | **str** | Invoice ID, if an invoice is generated during the update.  | [optional] 
**invoice_items** | [**list[PUTSubscriptionPreviewInvoiceItemsType]**](PUTSubscriptionPreviewInvoiceItemsType.md) | Container for invoice items.  | [optional] 
**invoice_target_date** | **date** | Date through which charges are calculated on the invoice, as yyyy-mm-dd. Preview mode only.  **Note:** This field is only available if you do not specify the Zuora REST API minor version or specify the minor version to 186.0, 187.0, 188.0, 189.0, and 196.0. See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.  | [optional] 
**paid_amount** | **str** | Payment amount, if a payment is collected  | [optional] 
**payment_id** | **str** | Payment ID, if a payment is collected.  | [optional] 
**preview_charge_metrics_response** | **str** |  | [optional] 
**subscription_id** | **str** | The ID of the resulting new subscription.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**target_date** | **date** | Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.  **Note:** This field is only available if you set the Zuora REST API minor version to 207.0 or later in the request header. See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.  | [optional] 
**tax_amount** | **str** | Tax amount on the invoice.  | [optional] 
**total_delta_mrr** | **str** | Change in the subscription monthly recurring revenue as a result of the update.  | [optional] 
**total_delta_tcv** | **str** | Change in the total contracted value of the subscription as a result of the update.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

