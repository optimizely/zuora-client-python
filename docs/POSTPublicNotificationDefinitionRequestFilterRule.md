# POSTPublicNotificationDefinitionRequestFilterRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | The filter rule conditions, written in [JEXL](http://commons.apache.org/proper/commons-jexl/). The rule might contain event context merge fields and data source merge fields. Data source merge fields must be from [the base object of the event or from the joined objects of the base object](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL#Data_Sources_and_Objects). Notifications with invalid merge fields will fail to evaluate, thus will not be invoked. For example, to filter an invoice posted notification to only invoices with an amount over 1000, you would define the following condition:  &#x60;&#x60;&#x60;Invoice.Amount &gt; 1000&#x60;&#x60;&#x60;  There are conventions and keywords you need to be aware of. For example:  * &#x60;Invoice.Amount&#x60; refers to the &#x60;Amount&#x60; field of the Zuora object &#x60;Invoice&#x60;.  * Unlike Event Triggers, there is no access to variables with the &#x60;_old&#x60; suffix. Fields with the &#x60;_old&#x60; suffix are only available on Event Trigger conditions.  | 
**description** | **str** | The description of the filter rule. | [optional] 
**parameters** | [**FilterRuleParameterDefinitions**](FilterRuleParameterDefinitions.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


