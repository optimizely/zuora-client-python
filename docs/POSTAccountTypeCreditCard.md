# POSTAccountTypeCreditCard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_holder_info** | [**POSTAccountTypeCreditCardCardHolderInfo**](POSTAccountTypeCreditCardCardHolderInfo.md) |  | 
**card_number** | **str** | Card number, up to 16 characters. Once created, this field can&#39;t be updated or queried, and is only available in masked format (e.g., XXXX-XXXX-XXXX-1234).  | 
**card_type** | **str** | The type of the credit card.  Possible values  include &#x60;Visa&#x60;, &#x60;MasterCard&#x60;, &#x60;AmericanExpress&#x60;, &#x60;Discover&#x60;, &#x60;JCB&#x60;, and &#x60;Diners&#x60;. For more information about credit card types supported by different payment gateways, see [Supported Payment Gateways](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/Supported_Payment_Gateways).  | 
**expiration_month** | **str** | Two-digit expiration month (01-12).  | 
**expiration_year** | **str** | Four-digit expiration year.  | 
**security_code** | **str** | The CVV or CVV2 security code of the card. To ensure PCI compliance, this value is not stored and cannot be queried.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


