# PostGenerateBillingDocumentType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_post** | **bool** | Whether to automatically post the billing documents after the draft billing documents are generated.   If an error occurs during posting billing documents, the draft billing documents are not generated too.  | [optional] [default to False]
**auto_renew** | **bool** | Whether to automatically renew the subscriptions with **Auto Renew** set to **Yes**.   | [optional] [default to False]
**charge_type_to_exclude** | **list[str]** | The types of the charges to be excluded from the generation of billing documents. The field values are case insensitive. Supported values include &#x60;onetime&#x60;, &#x60;recurring&#x60;, and &#x60;usage&#x60;.   | [optional] 
**effective_date** | **date** | The date on which to generate the billing documents, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**subscription_ids** | **list[str]** | The IDs of the subscriptions that you want to create the billing documents for.   | [optional] 
**target_date** | **date** | The date used to determine which charges are to be billed, in &#x60;yyyy-mm-dd&#x60; format.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

