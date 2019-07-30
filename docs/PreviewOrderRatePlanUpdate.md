# PreviewOrderRatePlanUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_updates** | [**list[PreviewOrderChargeUpdate]**](PreviewOrderChargeUpdate.md) |  | [optional] 
**custom_fields** | [**RatePlanObjectCustomFields**](RatePlanObjectCustomFields.md) |  | [optional] 
**rate_plan_id** | **str** | The id of the rate plan to be updated. It can be the latest version or any history version id.  | [optional] 
**specific_update_date** | **date** |  The date when the Update Product order action takes effect. This field is only applicable if there is already a future-dated Update Product order action on the subscription. The format of the date is yyyy-mm-dd.  See [Update a Product on Subscription with Future-dated Updates](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AC_Orders_Tutorials/C_Update_a_Product_in_a_Subscription/Update_a_Product_on_Subscription_with_Future-dated_Updates) for more information about this feature.  | [optional] 
**unique_token** | **str** | A unique string to represent the rate plan charge in the order. The unique token is used to perform multiple actions against a newly added rate plan. For example, if you want to add and update a product in the same order, you would assign a unique token to the product rate plan when added and use that token in future order actions.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


