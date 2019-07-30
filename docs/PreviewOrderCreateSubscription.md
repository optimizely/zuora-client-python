# PreviewOrderCreateSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_separately** | **bool** | Specifies whether the subscription appears on a separate invoice when Zuora generates invoices.  | [optional] 
**new_subscription_owner_account** | [**PreviewOrderCreateSubscriptionNewSubscriptionOwnerAccount**](PreviewOrderCreateSubscriptionNewSubscriptionOwnerAccount.md) |  | [optional] 
**notes** | **str** | Notes about the subscription. These notes are only visible to Zuora users.  | [optional] 
**subscribe_to_rate_plans** | [**list[PreviewOrderRatePlanOverride]**](PreviewOrderRatePlanOverride.md) | List of rate plans associated with the subscription.  | [optional] 
**subscription_number** | **str** | Subscription number of the subscription. For example, A-S00000001.  If you do not set this field, Zuora will generate the subscription number.  | [optional] 
**subscription_owner_account_number** | **str** | Account number of an existing account that will own the subscription. For example, A00000001.  If you do not set this field or the &#x60;newSubscriptionOwnerAccount&#x60; field, the account that owns the order will also own the subscription. Zuora will return an error if you set this field and the &#x60;newSubscriptionOwnerAccount&#x60; field.  | [optional] 
**terms** | [**CreateOrderCreateSubscriptionTerms**](CreateOrderCreateSubscriptionTerms.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


