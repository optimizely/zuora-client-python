# ProxyCreateTaxationItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_code** | **str** |  The Chart of Accounts  | [optional] 
**exempt_amount** | **float** |  The amount of taxes or VAT for which the customer has an exemption. **Character limit**: 16 **Values**: a decimal value  | [optional] 
**invoice_item_id** | **str** |  The ID of the specific invoice item that the taxation information applies to. **Character limit**: 32 **Values**: a valid invoice item ID  | 
**jurisdiction** | **str** |  The jurisdiction that applies the tax or VAT. This value is typically a state, province, county, or city. **Character limit**: 32 **Values**: a string of 32 characterrs or fewer  | 
**location_code** | **str** |  The identifier for the location based on the value of the &#x60;TaxCode&#x60; field. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**name** | **str** |  The name of the tax rate, such as sales tax or GST. This name is displayed on invoices. **Character limit**: 128 **Values**: a string of 128 characters or fewer  | 
**tax_amount** | **float** |  The amount of the tax applied to the charge. **Character limit**: 16 **Values**: a decimal value  | 
**tax_code** | **str** |  The tax code identifies which tax rules and tax rates to apply to a specific charge. **Character limit**: 32 **Values**: a string of 32 characters or fewer  | [optional] 
**tax_code_description** | **str** |  The description for the tax code. **Character limit**: 255 **Values**: a string of 255 characters or fewer  | [optional] 
**tax_date** | **date** |  The date that the tax is applied to the charge, in &#x60;yyyy-mm-dd&#x60; format. **Character limit**: 29  | 
**tax_rate** | **float** |  The tax rate applied to the charge. **Character limit**: 16 **Values**: a valid decimal value  | 
**tax_rate_description** | **str** |  The description of the tax rate. **Character limit**: 255 **Values**: a string of 255 characters or fewer  | [optional] 
**tax_rate_type** | **str** |  The type of the tax rate applied to the charge. **Character limit**: 10 **Values**: &#x60;Percentage&#x60;, &#x60;FlatFee&#x60;  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


