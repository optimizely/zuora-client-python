# POSTSubscriptionPreviewResponseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Invoice amount.  | [optional] 
**amount_without_tax** | **str** | Invoice amount minus tax.  | [optional] 
**charge_metrics** | **object** | Container for charge metrics.  | [optional] 
**contracted_mrr** | **str** | Monthly recurring revenue of the subscription.  | [optional] 
**credit_memo** | **object** |  Container for credit memos.  **Note:** This container is only available if you set the Zuora REST API minor version to 207.0 or later in the request header, and you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   | [optional] 
**invoice** | **object** | Container for invoices.    **Note:** This field is only available if you set the Zuora REST API minor version to 207.0 or later in the request header. Also, the response structure is changed and the following invoice related response fields are moved to this **invoice** container:       * amount    * amountWithoutTax    * taxAmount    * invoiceItems    * targetDate    * chargeMetrics      | [optional] 
**invoice_items** | [**list[POSTSubscriptionPreviewInvoiceItemsType]**](POSTSubscriptionPreviewInvoiceItemsType.md) | Container for invoice items.  | [optional] 
**invoice_target_date** | **date** | Date through which charges are calculated on the invoice, as yyyy-mm-dd.  **Note:** This field is only available if you do not specify the Zuora REST API minor version or specify the minor version to 186.0, 187.0, 188.0, 189.0, and 196.0. See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.  | [optional] 
**preview_charge_metrics_response** | **str** |  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**target_date** | **date** | Date through which to calculate charges if an invoice is generated, as yyyy-mm-dd. Default is current date.  **Note:** This field is only available if you set the Zuora REST API minor version to 207.0 or later in the request header. See [Zuora REST API Versions](https://www.zuora.com/developer/api-reference/#section/API-Versions) for more information.  | [optional] 
**tax_amount** | **str** | Tax amount on the invoice.  | [optional] 
**total_contracted_value** | **str** | Total contracted value of the subscription.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

