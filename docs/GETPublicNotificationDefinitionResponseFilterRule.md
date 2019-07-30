# GETPublicNotificationDefinitionResponseFilterRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | The filter rule conditions, written in [JEXL](http://commons.apache.org/proper/commons-jexl/). The rule might contain event context merge fields and data source merge fields. Data source merge fields must be from [the base object of the event or from the joined objects of the base object](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL#Data_Sources_and_Objects). Notifications with invalid merge fields will fail to evaluate, thus will not be invoked. For example, to trigger an event when an invoice is posted with the amount over 1000, you would define the following condition on the &#x60;Invoice&#x60; object:  &#x60;&#x60;&#x60;changeType &#x3D;&#x3D; &#39;UPDATE&#39; &amp;&amp; Invoice.Status &#x3D;&#x3D; &#39;Posted&#39; &amp;&amp; Invoice.Status_old !&#x3D; &#39;Posted&#39; &amp;&amp; Invoice.Amount &gt; 1000&#x60;&#x60;&#x60;  There are conventions and keywords you need to be aware of. For example:  * &#x60;changeType&#x60; is a keyword to specify what kind of change happened to the object. Allowed values are &#x60;INSERT&#x60;, &#x60;UPDATE&#x60; or &#x60;DELETE&#x60;.  * &#x60;Invoice.Status&#x60; refers to field &#x60;Status&#x60; of the Zuora object &#x60;Invoice&#x60;.  * A variable with the &#x60;_old&#x60; suffix means it’s a previous value of the corresponding object field. The \&quot;_old\&quot; fields are only available on the base objects.  | [optional] 
**description** | **str** | The description of the filter rule. | [optional] 
**event_type_name** | **str** | The value is &#x60;null&#x60;. | [optional] 
**id** | **str** | The ID of the filter rule. If not specified or null, the notification definition is always qualified to process events of \&quot;eventType\&quot;. | [optional] 
**parameters** | [**FilterRuleParameterDefinitions**](FilterRuleParameterDefinitions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


