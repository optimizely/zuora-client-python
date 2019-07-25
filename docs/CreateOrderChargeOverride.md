# CreateOrderChargeOverride

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing** | **object** | Billing information about the charge.  | [optional] 
**charge_number** | **str** | Charge number of the charge. For example, C-00000307.  If you do not set this field, Zuora will generate the charge number.  | [optional] 
**custom_fields** | [**RatePlanChargeObjectCustomFields**](RatePlanChargeObjectCustomFields.md) |  | [optional] 
**description** | **str** | Description of the charge.  | [optional] 
**end_date** | [**EndConditions**](EndConditions.md) |  | [optional] 
**pricing** | **object** | Pricing information about the charge.  | [optional] 
**product_rate_plan_charge_id** | **str** | Internal identifier of the product rate plan charge that the charge is based on.  | 
**rev_rec_code** | **str** | Revenue Recognition Code  | [optional] 
**rev_rec_trigger_condition** | **str** | Specifies the revenue recognition trigger condition.    * &#x60;Contract Effective Date&#x60;    * &#x60;Service Activation Date&#x60;   * &#x60;Customer Acceptance Date&#x60;  | [optional] 
**revenue_recognition_rule_name** | **str** | Specifies the revenue recognition rule.    * &#x60;Recognize upon invoicing&#x60;    * &#x60;Recognize daily over time&#x60;  | [optional] 
**start_date** | [**TriggerParams**](TriggerParams.md) |  | [optional] 
**unique_token** | **str** | Unique identifier for the charge. This identifier enables you to refer to the charge before the charge has an internal identifier in Zuora.  For instance, suppose that you want to use a single order to add a product to a subscription and later update the same product. When you add the product, you can set a unique identifier for the charge. Then when you update the product, you can use the same unique identifier to specify which charge to modify.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

