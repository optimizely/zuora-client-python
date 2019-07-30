# GETRevenueEventDetailWithoutSuccessType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | An account ID.  | [optional] 
**created_on** | **datetime** | The date when the record was created in YYYY-MM-DD HH:MM:SS format.  | [optional] 
**currency** | **str** | The type of currency used. | [optional] 
**event_type** | **str** | Label of the revenue event type. Revenue event type labels can be duplicated. You can configure your revenue event type labels by navigating to **Settings &gt; Finance &gt; Configure Revenue Event Types** in the Zuora UI.  Note that &#x60;Credit Memo Posted&#x60; and &#x60;Debit Memo Posted&#x60; are only available if you enable the Invoice Settlement feature.  | [optional] 
**notes** | **str** | Additional information about this record.  | [optional] 
**number** | **str** | The revenue event number created when a revenue event occurs.  | [optional] 
**recognition_end** | **date** | The end date of a recognition period in YYYY-MM-DD format.   The maximum difference of the recognitionStart and recognitionEnd date fields is equal to 250 multiplied by the length of an accounting period.  | [optional] 
**recognition_start** | **date** | The start date of a recognition period in YYYY-MM-DD format.  | [optional] 
**revenue_items** | [**list[GETRevenueItemType]**](GETRevenueItemType.md) | Revenue items are listed in ascending order by the accounting period start date.  | [optional] 
**subscription_charge_id** | **str** | The original subscription charge ID.  | [optional] 
**subscription_id** | **str** | The original subscription ID.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


