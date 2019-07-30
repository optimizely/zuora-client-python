# PUTAllocateManuallyType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | Label of the revenue event type. Revenue event type labels can be duplicated. You can configure your revenue event type labels by navigating to **Settings &gt; Finance &gt; Configure Revenue Event Types** in the Zuora UI.  Note that &#x60;Credit Memo Posted&#x60; and &#x60;Debit Memo Posted&#x60; are only available if you enable the Invoice Settlement feature.  | [optional] 
**event_type_system_id** | **str** | System ID of the revenue event type. Each eventType has a unique system ID. You can configure your revenue event type system IDs by navigating to **Settings &gt; Finance &gt; Configure Revenue Event Types** in the Zuora UI.  Cannot be duplicated.  | [optional] 
**notes** | **str** | Additional information about this record.  | [optional] 
**revenue_distributions** | [**list[POSTDistributionItemType]**](POSTDistributionItemType.md) | An array of revenue distributions. Represents how you want to distribute revenue for this revenue schedule. You can distribute revenue into a maximum of 250 accounting periods with one revenue schedule.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


