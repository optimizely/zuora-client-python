# CreateSubscriptionTerms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_renew** | **bool** | Specifies whether the subscription automatically renews at the end of the each term. Only applicable if the type of the first term is &#x60;TERMED&#x60;.  | [optional] 
**initial_term** | [**CreateOrderCreateSubscriptionTermsInitialTerm**](CreateOrderCreateSubscriptionTermsInitialTerm.md) |  | 
**renewal_setting** | **str** | Specifies the type of the terms that follow the first term if the subscription is renewed. Only applicable if the type of the first term is &#x60;TERMED&#x60;.  * &#x60;RENEW_WITH_SPECIFIC_TERM&#x60; - Each renewal term has a predefined duration. The first entry in &#x60;renewalTerms&#x60; specifies the duration of the second term of the subscription, the second entry in &#x60;renewalTerms&#x60; specifies the duration of the third term of the subscription, and so on. The last entry in &#x60;renewalTerms&#x60; specifies the ultimate duration of each renewal term. * &#x60;RENEW_TO_EVERGREEN&#x60; - The second term of the subscription does not have a predefined duration.  | [optional] 
**renewal_terms** | [**list[RenewalTerm]**](RenewalTerm.md) | List of renewal terms of the subscription. Only applicable if the type of the first term is &#x60;TERMED&#x60; and the value of the &#x60;renewalSetting&#x60; field is &#x60;RENEW_WITH_SPECIFIC_TERM&#x60;.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


