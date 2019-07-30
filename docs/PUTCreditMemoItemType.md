# PUTCreditMemoItemType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the credit memo item. For tax-inclusive credit memo items, the amount indicates the credit memo item amount including tax. For tax-exclusive credit memo items, the amount indicates the credit memo item amount excluding tax  | [optional] 
**comment** | **str** | Comments about the credit memo item.  | [optional] 
**finance_information** | [**CreditMemoItemFromWriteOffInvoiceFinanceInformation**](CreditMemoItemFromWriteOffInvoiceFinanceInformation.md) |  | [optional] 
**id** | **str** | The ID of the credit memo item.  | 
**service_end_date** | **date** | The service end date of the credit memo item.  | [optional] 
**service_start_date** | **date** | The service start date of the credit memo item.  | [optional] 
**sku_name** | **str** | The name of the SKU.  | [optional] 
**tax_items** | [**list[PutCreditMemoTaxItemType]**](PutCreditMemoTaxItemType.md) | Container for credit memo taxation items.  | [optional] 
**unit_of_measure** | **str** | The definable unit that you measure when determining charges.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


