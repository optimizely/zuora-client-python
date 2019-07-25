# CreditMemoTaxItemFromInvoiceTaxItemType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the credit memo taxation item.  | [optional] 
**finance_information** | **object** | Container for the finance information related to the source taxation item.  | [optional] 
**jurisdiction** | **str** | The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.   | [optional] 
**location_code** | **str** | The identifier for the location based on the value of the &#x60;taxCode&#x60; field.  | [optional] 
**source_tax_item_id** | **str** | The ID of the source taxation item.  | [optional] 
**tax_code** | **str** | The tax code identifies which tax rules and tax rates to apply to a specific credit memo.   | [optional] 
**tax_code_description** | **str** | The description of the tax code.  | [optional] 
**tax_date** | **date** | The date that the tax is applied to the credit memo, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**tax_exempt_amount** | **float** | The amount of taxes or VAT for which the customer has an exemption.  | [optional] 
**tax_name** | **str** | The name of taxation.  | [optional] 
**tax_rate** | **float** | The tax rate applied to the credit memo.  | [optional] 
**tax_rate_description** | **str** | The description of the tax rate.   | [optional] 
**tax_rate_type** | **str** | The type of the tax rate applied to the credit memo.   | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

