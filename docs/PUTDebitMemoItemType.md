# PUTDebitMemoItemType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the debit memo item. For tax-inclusive debit memo items, the amount indicates the debit memo item amount including tax. For tax-exclusive debit memo items, the amount indicates the debit memo item amount excluding tax.  | [optional] 
**comment** | **str** | Comments about the debit memo item.  | [optional] 
**finance_information** | [**PUTDebitMemoItemTypeFinanceInformation**](PUTDebitMemoItemTypeFinanceInformation.md) |  | [optional] 
**id** | **str** | The ID of the debit memo item.  | 
**service_end_date** | **date** | The service end date of the debit memo item.  | [optional] 
**service_start_date** | **date** | The service start date of the debit memo item.   | [optional] 
**sku_name** | **str** | The name of the SKU.  | [optional] 
**tax_items** | [**list[PutDebitMemoTaxItemType]**](PutDebitMemoTaxItemType.md) | Container for debit memo taxation items.  | [optional] 
**unit_of_measure** | **str** | The definable unit that you measure when determining charges.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


