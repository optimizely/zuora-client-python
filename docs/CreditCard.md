# CreditCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_holder_info** | [**AccountCreditCardHolder**](AccountCreditCardHolder.md) |  | [optional] 
**card_number** | **str** | Card number. Once set, you cannot update or query the value of this field. The value of this field is only available in masked format. For example, XXXX-XXXX-XXXX-1234.  | [optional] 
**card_type** | **str** | Type of card.  | [optional] 
**expiration_month** | **int** | Expiration date of the card.  | [optional] 
**expiration_year** | **int** | Expiration year of the card.  | [optional] 
**security_code** | **str** | CVV or CVV2 security code of the card. To ensure PCI compliance, Zuora does not store the value of this field.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

