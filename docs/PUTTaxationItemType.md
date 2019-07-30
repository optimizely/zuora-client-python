# PUTTaxationItemType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exempt_amount** | **float** | The amount of taxes or VAT for which the customer has an exemption.  | [optional] 
**finance_information** | [**POSTTaxationItemForCMTypeFinanceInformation**](POSTTaxationItemForCMTypeFinanceInformation.md) |  | [optional] 
**jurisdiction** | **str** | The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.  | 
**location_code** | **str** | The identifier for the location based on the value of the &#x60;taxCode&#x60; field.   | [optional] 
**name** | **str** | The name of the taxation item to be updated.  | 
**tax_amount** | **float** | The amount of the tax applied to the credit or debit memo.  | 
**tax_code** | **str** | The tax code identifies which tax rules and tax rates to apply to a specific credit or debit memo.  | [optional] 
**tax_code_description** | **str** | The description of the tax code.  | [optional] 
**tax_date** | **date** | The date when the tax is applied to the credit or debit memo.  | [optional] 
**tax_rate** | **float** | The tax rate applied to the credit or debit memo.  | 
**tax_rate_description** | **str** | The description of the tax rate.   | [optional] 
**tax_rate_type** | **str** | The type of the tax rate applied to the credit or debit memo.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


