# ProxyGetInvoiceSplitItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_id** | **str** |  The ID of the Zuora user who created the InvoiceSplitItem object. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**created_date** | **datetime** |  The date when the InvoiceSplitItem was created. **Values**: automatically generated  | [optional] 
**id** | **str** | Object identifier. | [optional] 
**invoice_date** | **date** |  The generation date of the new split invoice, in &#x60;yyyy-mm-dd&#x60; format. **Character limit**: 29  | [optional] 
**invoice_id** | **str** |  The new invoice after the split. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**invoice_split_id** | **str** |  The ID of the invoice split associated with the individual invoice split item. **Character limit**: 32 **Values**: a valid invoice split ID  | [optional] 
**payment_term** | **str** |  Indicates when the customer pays the split invoice. **Values**: a valid, active payment term  | [optional] 
**split_percentage** | **float** |  Specifies the percentage of the original invoice that you want to be the balance of the split invoice. The total of the SplitPercentage field values for all of the InvoiceSplitItem objects in an InvoiceSplit object must equal 100. **Values**:  | [optional] 
**updated_by_id** | **str** |  The ID of the Zuora user who last updated the invoice split. **Character limit**: 32 **Values**: automatically generated  | [optional] 
**updated_date** | **datetime** |  The date when the invoice split was last updated. **Values**: automatically generated  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


