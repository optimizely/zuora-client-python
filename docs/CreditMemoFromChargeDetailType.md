# CreditMemoFromChargeDetailType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the credit memo item.  **Note**: This field is only available if you set the &#x60;zuora-version&#x60; request header to &#x60;224.0&#x60; or later.  | [optional] 
**charge_id** | **str** | The ID of the product rate plan charge that the credit memo is created from.  | 
**comment** | **str** | Comments about the product rate plan charge.  | [optional] 
**finance_information** | [**CreditMemoFromChargeDetailTypeFinanceInformation**](CreditMemoFromChargeDetailTypeFinanceInformation.md) |  | [optional] 
**memo_item_amount** | **float** | The amount of the credit memo item.  **Note**: This field is not available if you set the &#x60;zuora-version&#x60; request header to &#x60;224.0&#x60; or later.  | [optional] 
**service_end_date** | **date** | The service end date of the credit memo item. If not specified, the effective end date of the corresponding product rate plan will be used.  | [optional] 
**service_start_date** | **date** | The service start date of the credit memo item. If not specified, the effective start date of the corresponding product rate plan will be used.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


