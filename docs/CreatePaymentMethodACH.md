# CreatePaymentMethodACH

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ach_bank_account_name** | **str** | The name of the account holder, which can be either a person or a company. This field is only required if the &#x60;type&#x60; field is set to &#x60;ACH&#x60;.  | [optional] 
**ach_bank_account_number** | **str** | The bank account number associated with the ACH payment. This field is only required if the &#x60;type&#x60; field is set to &#x60;ACH&#x60;.  | [optional] 
**ach_bank_account_type** | **str** | The type of bank account associated with the ACH payment. This field is only required if the &#x60;type&#x60; field is set to &#x60;ACH&#x60;.  | [optional] 
**ach_bank_name** | **str** | The name of the bank where the ACH payment account is held. This field is only required if the &#x60;type&#x60; field is set to &#x60;ACH&#x60;.  | [optional] 
**address_line1** | **str** | First address line, 255 characters or less.  | [optional] 
**address_line2** | **str** | Second address line, 255 characters or less.  | [optional] 
**bank_aba_code** | **str** | The nine-digit routing number or ABA number used by banks. This field is only required if the &#x60;type&#x60; field is set to &#x60;ACH&#x60;.  | [optional] 
**city** | **str** | City, 40 characters or less.       | [optional] 
**country** | **str** | Country, must be a valid country name or abbreviation.  | [optional] 
**phone** | **str** | Phone number, 40 characters or less.  | [optional] 
**state** | **str** | State, must be a valid state name or 2-character abbreviation.  | [optional] 
**zip_code** | **str** | Zip code, 20 characters or less.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


