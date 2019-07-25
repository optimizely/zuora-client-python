# PUTPublicEmailTemplateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the email template. | [optional] 
**bcc_email_address** | **str** | Email bcc address. | [optional] 
**cc_email_address** | **str** | Email cc address. | [optional] 
**cc_email_type** | **str** | Email cc type. * When EventType is CDC/External and &#x27;ReferenceObjectType&#x27; in EventType is associated to Account, ccEmailType can be ALL values in enum.  * When EventType is CDC/External and &#x27;ReferenceObjectType&#x27; in EventType is not associated to Account, ccEmailType MUST be TenantAdmin, RunOwner or SpecificEmail. * When EventType is CDC/External and &#x27;ReferenceObjectType&#x27; in EventType is EMPTY, ccEmailType MUST be TenantAdmin, RunOwner or SpecificEmail. | [optional] [default to 'SpecificEmails']
**description** | **str** | The description of the email template. | [optional] 
**email_body** | **str** | The email body. You can add merge fields in the email object using angle brackets.  User can also embed html tags if &#x27;isHtml&#x27; is true. | [optional] 
**email_subject** | **str** | The email subject. You can add merge fields in the email subject using angle brackets. | [optional] 
**encoding_type** | **str** | The endcode type of the email body. | [optional] 
**from_email_address** | **str** | If fromEmailType is SpecificEmail, this field is required | [optional] 
**from_email_type** | **str** | The type of fromEmail. | [optional] 
**from_name** | **str** | The name of email sender. | [optional] 
**is_html** | **bool** | Specifies whether the style of email body is HTML. | [optional] 
**name** | **str** | The name of the email template. | [optional] 
**reply_to_email_address** | **str** | If replyToEmailType is SpecificEmail, this field is required. | [optional] 
**reply_to_email_type** | **str** | The type of the reply email. | [optional] 
**to_email_address** | **str** | If toEmailType is SpecificEmail, this field is required. | [optional] 
**to_email_type** | **str** | Email receive type. * When EventType is CDC/External and &#x27;ReferenceObjectType&#x27; in EventType is associated to Account, toEmailType can be ALL values in enum.  * When EventType is CDC/External and &#x27;ReferenceObjectType&#x27; in EventType is not associated to Account, toEmailType MUST be TenantAdmin, RunOwner or SpecificEmail.  * When EventType is CDC/External and &#x27;ReferenceObjectType&#x27; in EventType is EMPTY, toEmailType MUST be TenantAdmin, RunOwner or SpecificEmail. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

