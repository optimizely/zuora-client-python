# ProxyCreateUsage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  The ID of the account associated with the usage data. This field is only required if no value is specified for the &#x60;AccountNumber&#x60; field. **Character limit**: 32 **Values**: a valid account ID.  | [optional] 
**account_number** | **str** |  The number of the account associated with the usage data. This field is only required if no value is specified for the &#x60;AccountId&#x60; field. **Character limit**: 50 **Values**: a valid account number.  | [optional] 
**charge_id** | **str** |  The OrginalId of the rate plan charge related to the usage record, e.g., &#x60;2c9081a03c63c94c013c6873357a0117&#x60; **Character limit**: 32 **Values**: a valid rate plan charge OriginalID.  | [optional] 
**charge_number** | **str** | A unique number for the rate plan charge related to the usage record. For example, C-00000007.  | [optional] 
**description** | **str** | A description of the usage record.  | [optional] 
**end_date_time** | **datetime** |  The end date and time of a range of time when usage is tracked. Use this field for reporting; this field doesn&#39;t affect usage calculation. **Character limit**: 29 **Values**: a valid date and time value.  | [optional] 
**quantity** | **float** |  Indicates the number of units used. **Character limit**: 16 **Values**: a valid decimal amount equal to or greater than 0  | 
**start_date_time** | **datetime** |  The start date and time of a range of time when usage is tracked. Zuora uses this field value to determine the usage date. Unlike the &#x60;EndDateTime&#x60;, the &#x60;StartDateTime&#x60; field does affect usage calculation. **Character limit**: 29 **Values**: a valid date and time value  | 
**submission_date_time** | **datetime** |  The date when usage was submitted. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**subscription_id** | **str** | The ID of the subscription that contains the fees related to the usage data.  The ID of a subscription might change when you create amendments to the subscription. It is good practice to use the unique subscription number that you can specify in the &#x60;SubscriptionNumber&#x60; field.  | [optional] 
**subscription_number** | **str** | The unique identifier number of the subscription that contains the fees related to the usage data.  It is good practice to use this field when creating usage records.  | [optional] 
**uom** | **str** |  Specifies the units to measure usage. Units of measure are configured in the web-based UI. Your values depend on your configuration in **Billing Settings**. **Character limit**: **Values**: a valid unit of measure  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


