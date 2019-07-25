# PreviewOrderRatePlanUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_updates** | [**list[PreviewOrderChargeUpdate]**](PreviewOrderChargeUpdate.md) |  | [optional] 
**custom_fields** | [**RatePlanObjectCustomFields**](RatePlanObjectCustomFields.md) |  | [optional] 
**rate_plan_id** | **str** | The id of the rate plan to be updated. It can be the latest version or any history version id.  | [optional] 
**specific_update_date** | **date** | Used for the &#x27;update before update&#x27; and &#x27;update before remove&#x27; cases. | [optional] 
**unique_token** | **str** | A unique string to represent the rate plan charge in the order. The unique token is used to perform multiple actions against a newly added rate plan. For example, if you want to add and update a product in the same order, you would assign a unique token to the product rate plan when added and use that token in future order actions.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

