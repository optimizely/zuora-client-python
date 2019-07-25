# DiscountPricingOverride

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_discount_to** | **str** | Specifies which type of charge the discount charge applies to.  | [optional] 
**discount_amount** | [**BigDecimal**](BigDecimal.md) | Only applicable if the discount charge is a fixed-amount discount.  | [optional] 
**discount_level** | **str** | Application scope of the discount charge. For example, if the value of this field is &#x60;subscription&#x60; and the value of the &#x60;applyDiscountTo&#x60; field is &#x60;RECURRING&#x60;, the discount charge applies to all recurring charges in the same subscription as the discount charge.  | [optional] 
**discount_percentage** | [**BigDecimal**](BigDecimal.md) | Only applicable if the discount charge is a percentage discount.  | [optional] 
**price_change_option** | **str** | Specifies how Zuora changes the price of the charge each time the subscription renews.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

