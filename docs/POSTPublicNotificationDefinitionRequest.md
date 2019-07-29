# POSTPublicNotificationDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The status of the notification definition. The default value is true. | [optional] [default to True]
**callout** | **object** |  | [optional] 
**callout_active** | **bool** | The status of the callout action. Default value is false. | [optional] [default to False]
**communication_profile_id** | **str** | The profile that notification definition belongs to.   You can use the [Query Action](https://www.zuora.com/developer/api-reference/#operation/Action_POSTquery) to get the communication profile Id. See the following request sample:  &#x60;{     \&quot;queryString\&quot;: \&quot;select Id, ProfileName from CommunicationProfile\&quot;  }&#x60;  If you do not pass the communicationProfileId, notification service will be automatically added to the &#x27;Default Profile&#x27;.  | [optional] 
**description** | **str** | The description of the notification definition. | [optional] 
**email_active** | **bool** | The status of the email action. The default value is false. | [optional] [default to False]
**email_template_id** | **str** | The ID of the email template. If emailActive is true, an email template is required. And EventType of the email template MUST be the same as the eventType. | [optional] 
**event_type_name** | **str** | The name of the event type.   | 
**event_type_namespace** | **str** | The namespace of the &#x60;eventTypeName&#x60; field. The &#x60;eventTypeName&#x60; has the &#x60;user.notification&#x60; namespace by default.   Note that if the &#x60;eventTypeName&#x60; is a standard event type, you must specify the &#x60;com.zuora.notification&#x60; namespace; otherwise, you will get an error.  For example, if you want to create a notification definition on the &#x60;OrderActionProcessed&#x60; event, you must specify &#x60;com.zuora.notification&#x60; for this field.  | [optional] 
**filter_rule** | **object** |  | [optional] 
**filter_rule_params** | [**FilterRuleParameterValues**](FilterRuleParameterValues.md) |  | [optional] 
**name** | **str** | The name of the notification definition, unique per communication profile. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

