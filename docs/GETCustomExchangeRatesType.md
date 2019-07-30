# GETCustomExchangeRatesType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverse** | **bool** | - If &#x60;true&#x60;, the exchange rate in the response is an inverse exchange rate. - If &#x60;false&#x60;, the exchange rate in the response is not an inverse exchange rate. The value is determined by the **Use inverse rate** checkbox in your Zuora Finance Manage Currency Conversion settings.  | [optional] 
**rates** | [**list[GETCustomExchangeRatesDataType]**](GETCustomExchangeRatesDataType.md) | Container for exchange rate data. Contains a set of fields that provide exchange rate data for each day between the specified &#x60;startDate&#x60; and &#x60;endDate&#x60; (inclusive).   | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


