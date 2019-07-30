# ProxyCreateUnitOfMeasure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  Indicates if the UOM is available for new product rate plans. The default value is &#x60;true&#x60;. **Character limit**: 5 **Values**: &#x60;true&#x60;, &#x60;false &#x60;  | [optional] 
**decimal_places** | **int** | The number of digits to the right of the decimal point that you want to measure for the unit. To use whole numbers only, set this value to 0. You can&#39;t change this value after this &#x60;UOM&#x60; is used in any product, subscription, or usage. **Character limit**: 1 **Values**: an integer between 0 and 9, exclusive  | 
**displayed_as** | **str** | The name of the UOM that you want displayed on invoices. The default value is the &#x60;UomName&#x60; field value. **Character limit**: 50 **Values**: A string of 50 characters or fewer  | [optional] 
**rounding_mode** | **str** |  Specifies whether to round the UOM value up or down when the value exceeds the &#x60;DecimalPlaces&#x60; field value. The default value is &#x60;Up&#x60;. **Character limit**: 4 **Values**: &#x60;Up&#x60;, &#x60;Down&#x60;  | [optional] 
**uom_name** | **str** |  The name of the UOM, such as license or GB. This name is displayed in query results and in the web-based UI labels. If you want a different name to be displayed on invoices, then use the &#x60;DisplayedAs&#x60; field to provide the invoice label. **Character limit**: 50 **Values**: a string of 50 characters or fewer  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


