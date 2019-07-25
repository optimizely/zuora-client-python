# PreviewOrderRatePlanOverride

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_overrides** | [**list[PreviewOrderChargeOverride]**](PreviewOrderChargeOverride.md) | List of charges associated with the rate plan.  | [optional] 
**custom_fields** | [**RatePlanObjectCustomFields**](RatePlanObjectCustomFields.md) |  | [optional] 
**product_rate_plan_id** | **str** | Internal identifier of the product rate plan that the rate plan is based on.  | 
**unique_token** | **str** | Unique identifier for the rate plan. This identifier enables you to refer to the rate plan before the rate plan has an internal identifier in Zuora.  For instance, suppose that you want to use a single order to add a product to a subscription and later update the same product. When you add the product, you can set a unique identifier for the rate plan. Then when you update the product, you can use the same unique identifier to specify which rate plan to modify.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

