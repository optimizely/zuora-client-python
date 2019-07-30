# PreviewOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_thru_type** | **str** | The options on how the preview through date is calculated. Available for preview only. The &#39;TermEnd&#39; option is invalid when any subscription included in this order is evergreen.    If set the value of this field to &#39;SpecificDate&#39;, you must specify a specific date in the &#39;specificPreviewThruDate&#39; field.  | [optional] 
**preview_types** | **list[str]** | One or more types of the preview. It can include:  * ChargeMetrics: charge level metrics will be returned in the response, including: &#x60;cmrr&#x60;, &#x60;tcv&#x60;, &#x60;tcb&#x60;, and &#x60;tax&#x60;. * BillingDocs: &#x60;invoices&#x60; and &#x60;creditMemos&#x60; will be returned in the response. Note &#x60;creditMemos&#x60; is only available if the Invoice Settlement feature is enabled. * OrderMetrics: order metrics will be returned in the response, including: &#x60;quantity&#x60;, &#x60;mrr&#x60;, &#x60;tcb&#x60;, &#x60;tcv&#x60;, and &#x60;elp&#x60;.  | [optional] 
**specific_preview_thru_date** | **date** | The end date of the order preview. You can preview the invoice charges through the preview through date. (Invoice preview only)   **Note:** This field is only applicable if the &#39;previewThruType&#39; field is set to &#39;SpecificDate&#39;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


