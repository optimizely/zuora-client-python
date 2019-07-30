# UsageOveragePricingOverride

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_change_option** | **str** | Specifies how Zuora changes the price of the charge each time the subscription renews.  If the value of this field is &#x60;SpecificPercentageValue&#x60;, use the &#x60;priceIncreasePercentage&#x60; field to specify how much the price of the charge should change.  | [optional] 
**price_increase_percentage** | **float** | Specifies the percentage by which the price of the charge should change each time the subscription renews. Only applicable if the value of the &#x60;priceChangeOption&#x60; field is &#x60;SpecificPercentageValue&#x60;.  | [optional] 
**included_units** | **float** | Number of free units that may be consumed.  | [optional] 
**number_of_periods** | **int** | Number of periods that Zuora considers when calculating overage charges with overage smoothing.  | [optional] 
**overage_price** | **float** | Price per overage unit consumed.  | [optional] 
**overage_unused_units_credit_option** | **str** | Specifies whether to credit the customer for unused units.  If the value of this field is &#x60;CreditBySpecificRate&#x60;, use the &#x60;unusedUnitsCreditRates&#x60; field to specify the rate at which to credit the customer for unused units.  | [optional] 
**unused_units_credit_rates** | **float** | Per-unit rate at which to credit the customer for unused units. Only applicable if the value of the &#x60;overageUnusedUnitsCreditOption&#x60; field is &#x60;CreditBySpecificRate&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


