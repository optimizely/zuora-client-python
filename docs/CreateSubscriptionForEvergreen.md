# CreateSubscriptionForEvergreen

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_separately** | **bool** | Specifies whether the subscription appears on a separate invoice when Zuora generates invoices.  | [optional] 
**new_subscription_owner_account** | **object** | Information about a new account that will own the subscription. Only available if you have enabled the Owner Transfer feature.  **Note:** The Owner Transfer feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  If you do not set this field or the &#x60;subscriptionOwnerAccountNumber&#x60; field, the account that owns the order will also own the subscription. Zuora will return an error if you set this field and the &#x60;subscriptionOwnerAccountNumber&#x60; field.  | [optional] 
**notes** | **str** | Notes about the subscription. These notes are only visible to Zuora users.  | [optional] 
**subscribe_to_rate_plans** | [**list[RatePlanOverrideForEvergreen]**](RatePlanOverrideForEvergreen.md) | List of rate plans associated with the subscription.  | [optional] 
**subscription_number** | **str** | Subscription number of the subscription. For example, A-S00000001.  If you do not set this field, Zuora will generate the subscription number.  | [optional] 
**subscription_owner_account_number** | **str** | Account number of an existing account that will own the subscription. For example, A00000001.  If you do not set this field or the &#x60;newSubscriptionOwnerAccount&#x60; field, the account that owns the order will also own the subscription. Zuora will return an error if you set this field and the &#x60;newSubscriptionOwnerAccount&#x60; field.  | [optional] 
**terms** | **object** | Container for the terms and renewal settings of the subscription.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

