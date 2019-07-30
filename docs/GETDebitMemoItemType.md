# GETDebitMemoItemType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the debit memo item. For tax-inclusive debit memo items, the amount indicates the debit memo item amount including tax. For tax-exclusive debit memo items, the amount indicates the debit memo item amount excluding tax.  | [optional] 
**amount_without_tax** | **float** | The debit memo item amount excluding tax.  | [optional] 
**balance** | **float** | The balance of the debit memo item.  | [optional] 
**be_applied_amount** | **float** | The applied amount of the debit memo item.  | [optional] 
**comment** | **str** | Comments about the debit memo item.  | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the debit memo item.  | [optional] 
**created_date** | **datetime** | The date and time when the debit memo item was created, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-01 15:31:10.  | [optional] 
**finance_information** | [**GETDebitMemoItemTypeFinanceInformation**](GETDebitMemoItemTypeFinanceInformation.md) |  | [optional] 
**id** | **str** | The ID of the debit memo item.  | [optional] 
**service_end_date** | **date** | The end date of the service period associated with this debit memo item. Service ends one second before the date specified in this field.  | [optional] 
**service_start_date** | **date** | The start date of the service period associated with this debit memo item. If the associated charge is a one-time fee, this date is the date of that charge.  | [optional] 
**sku** | **str** | The SKU for the product associated with the debit memo item.  | [optional] 
**sku_name** | **str** | The name of the SKU.  | [optional] 
**source_item_id** | **str** | The ID of the source item.  | [optional] 
**source_item_type** | **str** | The type of the source item.   | [optional] 
**subscription_id** | **str** | The ID of the subscription associated with the debit memo item.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully. | [optional] 
**tax_items** | [**list[GETDMTaxItemType]**](GETDMTaxItemType.md) | Container for the taxation items of the debit memo item..   **Note**: This field is not available if you set the &#x60;zuora-version&#x60; request header to &#x60;239.0&#x60; or later.  | [optional] 
**taxation_items** | [**GETDebitMemoItemTypeTaxationItems**](GETDebitMemoItemTypeTaxationItems.md) |  | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the debit memo item.  | [optional] 
**updated_date** | **datetime** | The date and time when the debit memo item was last updated, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-02 15:36:10.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


