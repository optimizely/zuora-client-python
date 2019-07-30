# PostOrderResponseType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_id** | **str** | The Id of the process that handle the operation.  | [optional] 
**reasons** | [**list[CommonResponseTypeReasons]**](CommonResponseTypeReasons.md) |  | [optional] 
**success** | **bool** | Indicates whether the call succeeded.  | [optional] 
**account_number** | **str** | The account number for the order. | [optional] 
**credit_memo_numbers** | **list[str]** | An array of the credit memo numbers generated in this order request. The credit memo is only available if you have the Avdanced AR Settlement feature enabled. | [optional] 
**invoice_numbers** | **list[str]** | An array of the invoice numbers generated in this order request. Normally it includes one invoice number only, but can include multiple items when a subscription was tagged as invoice separately. | [optional] 
**order_number** | **str** | The order number of the order created. | [optional] 
**paid_amount** | **str** | The total amount collected in this order request. | [optional] 
**payment_number** | **str** | The payment number that collected in this order request. | [optional] 
**status** | **str** | Status of the order. &#x60;Pending&#x60; is only applicable for an order that contains a &#x60;CreateSubscription&#x60; order action. | [optional] 
**subscription_numbers** | **list[str]** | **Note:** This field is in Zuora REST API version control. Supported minor versions are 222.4 or earlier. To use this field in the method, you must set the &#x60;zuora-version&#x60; parameter to the minor version number in the request header.  Container for the subscription numbers of the subscriptions in an order.  | [optional] 
**subscriptions** | [**list[PostOrderResponseTypeSubscriptions]**](PostOrderResponseTypeSubscriptions.md) | **Note:** This field is in Zuora REST API version control. Supported minor versions are 223.0 or later. To use this field in the method, you must set the &#x60;zuora-version&#x60; parameter to the minor version number in the request header.  Container for the subscription numbers and statuses in an order.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


