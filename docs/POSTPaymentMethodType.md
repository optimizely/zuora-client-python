# POSTPaymentMethodType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_key** | **str** | ID of the customer account to update.  **Note:** You can create a credit card payment method without assocating it with a customer account if you want. To do it and change the &#x60;accountKey&#x60; field to optional in this operation, submit a request at [Zuora Global Support](http://support.zuora.com/).  | 
**card_holder_info** | [**CreatePaymentMethodCardholderInfo**](CreatePaymentMethodCardholderInfo.md) |  | [optional] 
**credit_card_number** | **str** | Credit card number, a string of up to 16 characters. This field can only be set when creating a new payment method; it cannot be queried or updated.  | 
**credit_card_type** | **str** | The type of the credit card.  Possible values  include &#x60;Visa&#x60;, &#x60;MasterCard&#x60;, &#x60;AmericanExpress&#x60;, &#x60;Discover&#x60;, &#x60;JCB&#x60;, and &#x60;Diners&#x60;. For more information about credit card types supported by different payment gateways, see [Supported Payment Gateways](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways).  | 
**default_payment_method** | **bool** | Specify true to make this card the default payment method; otherwise, omit this parameter to keep the current default payment method.  | [optional] 
**expiration_month** | **str** | One or two digits expiration month (1-12).  | 
**expiration_year** | **str** | Four-digit expiration year.  | 
**mit_consent_agreement_ref** | **str** | Specifies your reference for the stored credential consent agreement that you have established with the customer. Only applicable if you set the &#x60;mitProfileAction&#x60; field.  | [optional] 
**mit_consent_agreement_src** | **str** | Required if you set the &#x60;mitProfileAction&#x60; field.  | [optional] 
**mit_network_transaction_id** | **str** | Specifies the ID of a network transaction. Only applicable if you set the &#x60;mitProfileAction&#x60; field to &#x60;Persist&#x60;.  | [optional] 
**mit_profile_action** | **str** | If you set this field, Zuora creates a stored credential profile within the payment method.  **Note:** This feature is in **Limited Availability**. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.  * &#x60;Activate&#x60; - Use this value if you are creating the stored credential profile after receiving the customer&#39;s consent.    Zuora will create the stored credential profile then send a cardholder-initiated transaction (CIT) to the payment gateway to validate the stored credential profile. If the CIT succeeds, the status of the stored credential profile will be &#x60;Active&#x60;. If the CIT does not succeed, Zuora will not create a stored credential profile.      If the payment gateway does not support the stored credential transaction framework, the status of the stored credential profile will be &#x60;Agreed&#x60;.   * &#x60;Persist&#x60; - Use this value if the stored credential profile represents a stored credential profile in an external system. The status of the payment method&#39;s stored credential profile will be &#x60;Active&#x60;.  | [optional] 
**mit_profile_agreed_on** | **date** | The date on which the profile is agreed. Required if you set the &#x60;mitProfileAction&#x60; field. The date format is &#x60;yyyy-mm-dd&#x60;.    | [optional] 
**mit_profile_type** | **str** | Required if you set the &#x60;mitProfileAction&#x60; field.  | [optional] 
**num_consecutive_failures** | **int** | The number of consecutive failed payments for this payment method. It is reset to &#x60;0&#x60; upon successful payment.   | [optional] 
**security_code** | **str** | The CVV or CVV2 security code for the credit card or debit card. Only required if changing expirationMonth, expirationYear, or cardHolderName. To ensure PCI compliance, this value isn&#39;t stored and can&#39;t be queried.   | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


