# POSTAccountingCodeType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_account_name** | **str** | Name of the account in your general ledger.  Field only available if you have Zuora Finance enabled. Maximum of 255 characters.  | [optional] 
**gl_account_number** | **str** | Account number in your general ledger.  Field only available if you have Zuora Finance enabled. Maximum of 255 characters.  | [optional] 
**name** | **str** | Name of the accounting code.  Accounting code name must be unique. Maximum of 100 characters.  | 
**notes** | **str** | Maximum of 2,000 characters.  | [optional] 
**type** | **str** | Accounting code type. You cannot create new accounting codes of type &#x60;AccountsReceivable&#x60;.   Note that &#x60;On-Account Receivable&#x60; is only available if you enable the Invoice Settlement feature.   | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


