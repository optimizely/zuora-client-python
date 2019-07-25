# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The ID of the user who created this order. | [optional] 
**created_date** | **str** | The time that the order gets created in the system, in the &#x60;YYYY-MM-DD HH:MM:SS&#x60; format. | [optional] 
**currency** | **str** | Currency code. | [optional] 
**custom_fields** | [**OrderObjectCustomFields**](OrderObjectCustomFields.md) |  | [optional] 
**existing_account_number** | **str** | The account number that this order has been created under. This is also the invoice owner of the subscriptions included in this order. | [optional] 
**order_date** | **date** | The date when the order is signed. All the order actions under this order will use this order date as the contract effective date if no additinal contractEffectiveDate is provided. | [optional] 
**order_number** | **str** | The order number of the order. | [optional] 
**status** | **str** | The status of the order. If the order contains any &#x60;Pending Activation&#x60; or &#x60;Pending Acceptance&#x60; subscription, the order status will be &#x60;Pending&#x60;; otherwise the order status is &#x60;Completed&#x60;. | [optional] 
**subscriptions** | **list[object]** | Represents a processed subscription, including the origin request (order actions) that create this version of subscription and the processing result (order metrics). The reference part in the request will be overridden with the info in the new subscription version. | [optional] 
**updated_by** | **str** | The ID of the user who updated this order. | [optional] 
**updated_date** | **str** | The time that the order gets updated in the system(for example, an order description update), in the &#x60;YYYY-MM-DD HH:MM:SS&#x60; format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

