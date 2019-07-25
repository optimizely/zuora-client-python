# POSTOrderPreviewRequestType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | [**OrderObjectCustomFields**](OrderObjectCustomFields.md) |  | [optional] 
**existing_account_number** | **str** | The account number that this order will be created under. It can be either the accountNumber or the account info. It will return an error if both are specified. Note that invoice owner account of the subscriptions included in this order should be the same with the account of the order.  | [optional] 
**order_date** | **date** | The date when the order is signed. All of the order actions under this order will use this order date as the contract effective date. | 
**order_number** | **str** | The order number of this order. | [optional] 
**preview_account_info** | [**PreviewAccountInfo**](PreviewAccountInfo.md) |  | [optional] 
**preview_options** | [**PreviewOptions**](PreviewOptions.md) |  | 
**subscriptions** | **list[object]** | Each item includes a set of order actions, which will be applied to the same base subscription. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

