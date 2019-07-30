# GETTaxationItemType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_id** | **str** | The ID of the Zuora user who created the taxation item.   | [optional] 
**created_date** | **datetime** | The date and time when the taxation item was created in the Zuora system, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**exempt_amount** | **float** | The amount of taxes or VAT for which the customer has an exemption.  | [optional] 
**finance_information** | [**GETCMTaxItemTypeFinanceInformation**](GETCMTaxItemTypeFinanceInformation.md) |  | [optional] 
**id** | **str** | The ID of the taxation item.  | [optional] 
**jurisdiction** | **str** | The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city.  | [optional] 
**location_code** | **str** | The identifier for the location based on the value of the &#x60;taxCode&#x60; field.   | [optional] 
**memo_item_id** | **str** | The ID of the credit or debit memo associated with the taxation item.  | [optional] 
**name** | **str** | The name of the taxation item.  | [optional] 
**source_tax_item_id** | **str** | The ID of the taxation item of the invoice, which the credit or debit memo is created from.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully. | [optional] 
**tax_amount** | **float** | The amount of the tax applied to the credit or debit memo.  | [optional] 
**tax_code** | **str** | The tax code identifies which tax rules and tax rates to apply to a specific credit or debit memo.  | [optional] 
**tax_code_description** | **str** | The description of the tax code.  | [optional] 
**tax_date** | **date** | The date when the tax is applied to the credit or debit memo.  | [optional] 
**tax_rate** | **float** | The tax rate applied to the credit or debit memo.  | [optional] 
**tax_rate_description** | **str** | The description of the tax rate.  | [optional] 
**tax_rate_type** | **str** | The type of the tax rate applied to the credit or debit memo.  | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the taxation item.  | [optional] 
**updated_date** | **datetime** | The date and time when the taxation item was last updated, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.   | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


