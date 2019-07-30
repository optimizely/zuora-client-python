# POSTTaxationItemForCMType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exempt_amount** | **float** | The amount of taxes or VAT for which the customer has an exemption.  | [optional] 
**finance_information** | [**POSTTaxationItemForCMTypeFinanceInformation**](POSTTaxationItemForCMTypeFinanceInformation.md) |  | [optional] 
**jurisdiction** | **str** | The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.  | 
**location_code** | **str** | The identifier for the location based on the value of the &#x60;taxCode&#x60; field.  | [optional] 
**memo_item_id** | **str** | The ID of the credit memo that the taxation item is created for.  | [optional] 
**name** | **str** | The name of the taxation item.  | 
**source_tax_item_id** | **str** | The ID of the taxation item of the invoice, which the credit memo is created from.   If you want to use this REST API to create taxation items for a credit memo created from an invoice, the taxation items of the invoice must be created or imported through the SOAP API call.  **Note:**    - This field is only used if the credit memo is created from an invoice.    - If you do not contain this field in the request body, Zuora will automatically set a value for the &#x60;sourceTaxItemId&#x60; field based on the tax location code, tax jurisdiction, and tax rate.  | [optional] 
**tax_amount** | **float** | The amount of the tax applied to the credit memo.  | 
**tax_code** | **str** | The tax code identifies which tax rules and tax rates to apply to a specific credit memo.  | [optional] 
**tax_code_description** | **str** | The description of the tax code.  | [optional] 
**tax_date** | **date** | The date when the tax is applied to the credit memo.  | [optional] 
**tax_rate** | **float** | The tax rate applied to the credit memo.  | 
**tax_rate_description** | **str** | The description of the tax rate.  | [optional] 
**tax_rate_type** | **str** | The type of the tax rate applied to the credit memo.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


