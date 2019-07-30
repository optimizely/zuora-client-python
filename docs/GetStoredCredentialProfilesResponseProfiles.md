# GetStoredCredentialProfilesResponseProfiles

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_on** | **datetime** | The date when the stored credential profile was activated (if applicable).  | [optional] 
**agreed_on** | **datetime** | The date when the stored credential profile was created.  | [optional] 
**brand** | **str** | The stored credential transaction framework. For example, Visa.  | [optional] 
**cancelled_on** | **datetime** | The date when the stored credential profile was cancelled (if applicable).  | [optional] 
**consent_agreement_ref** | **str** | Your reference for the consent agreement that you have established with the customer.  | [optional] 
**consent_agreement_src** | **str** |  | [optional] 
**expired_on** | **datetime** | The date when the stored credential profile was expired (if applicable).  | [optional] 
**number** | **int** | The number that identifies the stored credential profile within the payment method.  | [optional] 
**payment_method_id** | **str** | ID of the payment method.  | [optional] 
**status** | **str** | The status of the stored credential profile.  * &#x60;Agreed&#x60; - The stored credential profile has not been validated via an authorization transaction with the payment gateway. * &#x60;Active&#x60; - The stored credential profile has been validated via an authorization transaction with the payment gateway. * &#x60;Cancelled&#x60; - The stored credentials are no longer valid, per a customer request. Zuora cannot use the stored credentials in transactions. * &#x60;Expired&#x60; - The stored credentials are no longer valid, per an expiration policy in the stored credential transaction framework. Zuora cannot use the stored credentials in transactions.  | [optional] 
**type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


