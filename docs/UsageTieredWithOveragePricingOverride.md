# UsageTieredWithOveragePricingOverride

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_periods** | **int** | Number of periods that Zuora considers when calculating overage charges with overage smoothing.  | [optional] 
**overage_price** | [**BigDecimal**](BigDecimal.md) | Price per overage unit consumed.  | [optional] 
**overage_unused_units_credit_option** | **str** | Specifies whether to credit the customer for unused units.  If the value of this field is &#x60;CreditBySpecificRate&#x60;, use the &#x60;unusedUnitsCreditRates&#x60; field to specify the rate at which to credit the customer for unused units.  | [optional] 
**tiers** | [**list[ChargeTier]**](ChargeTier.md) | List of cumulative pricing tiers in the charge.  | [optional] 
**unused_units_credit_rates** | [**BigDecimal**](BigDecimal.md) | Per-unit rate at which to credit the customer for unused units. Only applicable if the value of the &#x60;overageUnusedUnitsCreditOption&#x60; field is &#x60;CreditBySpecificRate&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

