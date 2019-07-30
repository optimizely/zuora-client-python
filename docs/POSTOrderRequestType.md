# POSTOrderRequestType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | [**OrderObjectCustomFields**](OrderObjectCustomFields.md) |  | [optional] 
**existing_account_number** | **str** | The account number that this order will be created under. It can be either the accountNumber or the account info provided. It will return an error if both are specified. Note that this actually specifies the invoice owner account of the subscriptions included in this order.  | [optional] 
**new_account** | [**Account**](Account.md) |  | [optional] 
**order_date** | **date** | The date when the order is signed. All the order actions under this order will use this order date as the contract effective date if the contract effective date field is skipped or its value is left as null. | 
**order_number** | **str** | The order number of the new order. If not provided, system will auto-generate a number for this order. | [optional] 
**processing_options** | [**ProcessingOptions**](ProcessingOptions.md) |  | [optional] 
**subscriptions** | [**list[POSTOrderRequestTypeSubscriptions]**](POSTOrderRequestTypeSubscriptions.md) | Each item includes a set of order actions, which will be applied to the same base subscription. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


