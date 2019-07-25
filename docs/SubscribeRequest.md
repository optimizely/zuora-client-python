# SubscribeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**SubscribeRequestAccount**](SubscribeRequestAccount.md) |  | 
**bill_to_contact** | [**SubscribeRequestBillToContact**](SubscribeRequestBillToContact.md) |  | [optional] 
**payment_method** | **object** |  This is the object defining the payment details for the Account. The Account will be updated with this payment as the default payment method. Use this field if you are associating an electronic payment method with the account. A payment gateway must be enabled. Values: A valid electronic PaymentMethod. | [optional] 
**preview_options** | **object** | Only used if you want to call this operation in preview mode. After a call in preview mode is completed, Zuora will roll back the subscription and return only the temporary invoice data.  | [optional] 
**sold_to_contact** | [**SubscribeRequestSoldToContact**](SubscribeRequestSoldToContact.md) |  | [optional] 
**subscribe_options** | **object** |  This optional object specifies parameters related to invoicing - whether to immediately generate an invoice and collect payment, and whether the invoice should cover all subscriptions or just this new subscription. The default behavior is to invoice immediately for all the account&#x27;s subscriptions, with the current date as the target date, and immediately collect payment if the account&#x27;s &#x60;AutoPay&#x60; flag is true.   **Values:** A valid SubscribeOptions object.  | [optional] 
**subscription_data** | **object** |  This object contains the information on the contract&#x27;s dates and terms.   **Values:** A valid SubscriptionData object.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

