# PUTPublicNotificationDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the notification definition. The default value is true. | [optional] [default to True]
**callout** | **object** |  | [optional] 
**callout_active** | **bool** | The status of the callout action. The default value is false. | [optional] [default to False]
**communication_profile_id** | **str** | The profile that notification definition belongs to. If you want to update the notification to a system notification, you should pass &#x27;SystemNotification&#x27;. &#x27;  * When EventType is CDC/External and &#x27;ReferenceObjectType&#x27; in EventType is associated to Account, comunicationProfileId can be &#x27;SystemNotification&#x27;/Empty/UUID.   * When EventType is CDC/External and &#x27;ReferenceObjectType&#x27; in EventType is not  associated to Account, comunicationProfileId can be &#x27;SystemNotification&#x27;/Empty.   * When EventType is CDC/External and &#x27;ReferenceObjectType&#x27; in EventType is EMPTY, comunicationProfileId can be &#x27;SystemNotification&#x27;/Empty.  | [optional] 
**description** | **str** | The description of the notification definition. | [optional] 
**email_active** | **bool** | The status of the email action. The default is false. | [optional] [default to False]
**email_template_id** | **str** | The ID of the email template. If emailActive is updated from false to true, an email template is required, and the EventType of the email template MUST be the same as the EventType of the notification definition.  | [optional] 
**filter_rule** | **object** |  | [optional] 
**filter_rule_params** | [**FilterRuleParameterValues**](FilterRuleParameterValues.md) |  | [optional] 
**name** | **str** | The name of the notification definition, which is unique in the profile. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

