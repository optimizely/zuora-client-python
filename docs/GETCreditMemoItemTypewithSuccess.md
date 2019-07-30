# GETCreditMemoItemTypewithSuccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the credit memo item. For tax-inclusive credit memo items, the amount indicates the credit memo item amount including tax. For tax-exclusive credit memo items, the amount indicates the credit memo item amount excluding tax.  | [optional] 
**amount_without_tax** | **float** | The credit memo item amount excluding tax.  | [optional] 
**applied_amount** | **float** | The applied amount of the credit memo item.  | [optional] 
**comment** | **str** | Comments about the credit memo item.  | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the credit memo item.  | [optional] 
**created_date** | **datetime** | The date and time when the credit memo item was created, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-01 15:31:10.  | [optional] 
**credit_tax_items** | [**list[GETCMTaxItemType]**](GETCMTaxItemType.md) | Container for the taxation items of the credit memo item.   **Note**: This field is not available if you set the &#x60;zuora-version&#x60; request header to &#x60;239.0&#x60; or later.  | [optional] 
**finance_information** | [**GETCreditMemoItemTypewithSuccessFinanceInformation**](GETCreditMemoItemTypewithSuccessFinanceInformation.md) |  | [optional] 
**id** | **str** | The ID of the credit memo item.  | [optional] 
**refund_amount** | **float** | The amount of the refund on the credit memo item.  | [optional] 
**service_end_date** | **date** | The service end date of the credit memo item.   | [optional] 
**service_start_date** | **date** | The service start date of the credit memo item.  | [optional] 
**sku** | **str** | The SKU for the product associated with the credit memo item.  | [optional] 
**sku_name** | **str** | The name of the SKU.  | [optional] 
**source_item_id** | **str** | The ID of the source item.  | [optional] 
**source_item_type** | **str** | The type of the source item.  | [optional] 
**subscription_id** | **str** | The ID of the subscription associated with the credit memo item.  | [optional] 
**taxation_items** | [**GETCreditMemoItemTypeTaxationItems**](GETCreditMemoItemTypeTaxationItems.md) |  | [optional] 
**unapplied_amount** | **float** | The unapplied amount of the credit memo item.  | [optional] 
**updated_by_id** | **str** | The ID of the Zuora user who last updated the credit memo item.  | [optional] 
**updated_date** | **datetime** | The date and time when the credit memo item was last updated, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format. For example, 2017-03-02 15:36:10.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


