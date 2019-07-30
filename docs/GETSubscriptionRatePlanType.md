# GETSubscriptionRatePlanType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Rate plan ID.  | [optional] 
**last_change_type** | **str** | The last amendment on the rate plan.  Possible Values:  * &#x60;Add&#x60; * &#x60;Update&#x60; * &#x60;Remove&#x60;  | [optional] 
**product_id** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**product_rate_plan_id** | **str** |  | [optional] 
**product_sku** | **str** | The unique SKU for the product.  | [optional] 
**rate_plan_charges** | [**list[GETSubscriptionRatePlanChargesType]**](GETSubscriptionRatePlanChargesType.md) | Container for one or more charges.  | [optional] 
**rate_plan_name** | **str** | Name of the rate plan.  | [optional] 
**subscription_product_features** | [**list[GETSubscriptionProductFeatureType]**](GETSubscriptionProductFeatureType.md) | Container for one or more features.   Only available when the following settings are enabled:  * The Entitlements feature in your tenant.  * The Enable Feature Specification in Product and Subscriptions setting in Zuora Billing Settings | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


