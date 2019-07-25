# CreatePaymentMethodCreditCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_holder_info** | [**CreatePaymentMethodCardholderInfo**](CreatePaymentMethodCardholderInfo.md) |  | [optional] 
**card_number** | **str** | Credit card number.  | [optional] 
**card_type** | **str** | The type of the credit card.  Possible values include &#x60;Visa&#x60;, &#x60;MasterCard&#x60;, &#x60;AmericanExpress&#x60;, &#x60;Discover&#x60;, &#x60;JCB&#x60;, and &#x60;Diners&#x60;. For more information about credit card types supported by different payment gateways, see [Supported Payment Gateways](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways).  | [optional] 
**expiration_month** | **str** | One or two digit expiration month (1-12) of the credit card.  | [optional] 
**expiration_year** | **str** | Four-digit expiration year of the credit card.  | [optional] 
**mit_consent_agreement_ref** | **str** | Specifies your reference for the stored credential consent agreement that you have established with the customer. Only applicable if you set the &#x60;mitProfileAction&#x60; field.  | [optional] 
**mit_consent_agreement_src** | **str** | Required if you set the &#x60;mitProfileAction&#x60; field.  | [optional] 
**mit_network_transaction_id** | **str** | Specifies the ID of a network transaction. Only applicable if you set the &#x60;mitProfileAction&#x60; field to &#x60;Persist&#x60;.  | [optional] 
**mit_profile_action** | **str** | If you set this field, Zuora creates a stored credential profile within the payment method.  **Note:** This feature is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.  * &#x60;Activate&#x60; - Use this value if you are creating the stored credential profile after receiving the customer&#x27;s consent.    Zuora will create the stored credential profile then send a cardholder-initiated transaction (CIT) to the payment gateway to validate the stored credential profile. If the CIT succeeds, the status of the stored credential profile will be &#x60;Active&#x60;. If the CIT does not succeed, Zuora will not create a stored credential profile.      If the payment gateway does not support the stored credential transaction framework, the status of the stored credential profile will be &#x60;Agreed&#x60;.   * &#x60;Persist&#x60; - Use this value if the stored credential profile represents a stored credential profile in an external system. The status of the payment method&#x27;s stored credential profile will be &#x60;Active&#x60;.  | [optional] 
**mit_profile_agreed_on** | **date** | The date on which the profile is agreed. Required if you set the &#x60;mitProfileAction&#x60; field. The date format is &#x60;yyyy-mm-dd&#x60;.  | [optional] 
**mit_profile_type** | **str** | Required if you set the &#x60;mitProfileAction&#x60; field.  | [optional] 
**security_code** | **str** | CVV or CVV2 security code of the credit card.  To ensure PCI compliance, this value is not stored and cannot be queried.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

