# ProxyGetProductRatePlanChargeTier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_id** | **str** | The ID of the Zuora user who created the ProductRatePlanChargeTier object. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**created_date** | **datetime** | The date when the ProductRatePlanChargeTier object was created. **Character limit**: 29 **Values**: automatically generated  | [optional] 
**currency** | **str** | The code corresponding to the currency for the tier&#39;s price. **Character limit**: 3 **Values**: a valid currency code  | [optional] 
**ending_unit** | **float** | The end number of a range of units for the tier. **Character limit**: 16 **Values**: any positive decimal value  | [optional] 
**id** | **str** | Object identifier. | [optional] 
**price** | **float** |  The price of the tier if the charge is a flat fee, or the price of each unit in the tier if the charge model is tiered pricing. **Character limit**: 16 **Values**: a valid currency value  | [optional] 
**price_format** | **str** | Indicates if pricing is a flat fee or is per unit. This field is for tiered and volume pricing models only. **Character limit**: 8 **Values**: &#x60;FlatFee&#x60;, &#x60;PerUnit&#x60; **Note:** The values &#x60;Flat Fee&#x60; and &#x60;Per Unit&#x60; (with spaces) is valid for create or update calls.  | [optional] 
**starting_unit** | **float** |  The starting number of a range of units for the tier. **Character limit**: 16 **Values**: any positive decimal value  | [optional] 
**tier** | **int** |  A unique number that identifies the tier that the price applies to. **Character limit**: 20 **Values**: automatically generated  | [optional] 
**updated_by_id** | **str** |  The ID of the user who last updated the product rate plan charge tier. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**updated_date** | **datetime** |  The date when the product rate plan charge tier was last updated. **Character limit**: 29 **Values**: automatically generated  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


