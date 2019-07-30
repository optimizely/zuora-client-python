# POSTPaymentMethodDecryption

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the customer account associated with this payment method.  **Note:** You can create a payment method without assocating it with a customer account if you want. To do it and change the &#x60;accountID&#x60; field to optional in this operation, submit a request at [Zuora Global Support](http://support.zuora.com/). | 
**card_holder_info** | [**POSTPaymentMethodDecryptionCardHolderInfo**](POSTPaymentMethodDecryptionCardHolderInfo.md) |  | [optional] 
**integration_type** | **str** | Field to identify the token decryption type.  **Note:** The only value at this time is &#x60;ApplePay&#x60;.   | 
**invoice_id** | **str** | The id of invoice this payment will apply to.  **Note:** When &#x60;processPayment&#x60; is &#x60;true&#x60;, this field is required. Only one invoice can be paid; for scenarios where you want to pay for multiple invoices, set &#x60;processPayment&#x60; to &#x60;false&#x60; and call payment API separately.  | [optional] 
**merchant_id** | **str** | The Merchant ID that was configured for use with Apple Pay in the Apple iOS Developer Center.  | 
**payment_gateway** | **str** | The label name of the gateway instance configured in Zuora that should process the payment. When creating a Payment, this must be a valid gateway instance ID and this gateway must support the specific payment method. If not specified, the default gateway on the Account will be used.  **Note:** When &#x60;processPayment&#x60; is &#x60;true&#x60;, this field is required.  | [optional] 
**payment_token** | **object** | The complete JSON Object representing the encrypted payment token payload returned in the response from the Apple Pay session.   | 
**process_payment** | **bool** | A boolean flag to control whether a payment should be processed after creating payment method. The payment amount will be equivalent to the amount the merchant supplied in the ApplePay session. Default is false.  When &#x60;processPayment&#x60; is set to &#x60;false&#x60;, it must be followed by a separate subscribe or payment API call.    **Note:** If you set this field to &#x60;true&#x60;, you must specify the &#x60;paymentGateway&#x60; field with the payment gateway instance name. If you set this field to &#x60;false&#x60;, you must select the **Verify new credit card** check box on the gateway instance settings page. Otherwise, the cryptogram will not be sent to the gateway.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


