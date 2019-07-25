# GetOrderSuspend

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suspend_date** | **date** | The suspend date when the suspension takes effect.   | [optional] 
**suspend_periods** | **int** | This field is applicable only when the &#x60;suspendPolicy&#x60; field is set to &#x60;FixedPeriodsFromToday&#x60;. It must be used together with the &#x60;suspendPeriodsType&#x60; field. Note this field is not applicable in a Suspend order action auto-created by the Order Metrics migration.  The total number of the periods used to specify when a subscription suspension takes effect. The subscription suspension will take place after the specified time frame (&#x60;suspendPeriods&#x60; multiplied by &#x60;suspendPeriodsType&#x60;) from today&#x27;s date.   | [optional] 
**suspend_periods_type** | **str** | This field is applicable only when the &#x60;suspendPolicy&#x60; field is set to &#x60;FixedPeriodsFromToday&#x60;. It must be used together with the &#x60;suspendPeriods&#x60; field. Note this field is not applicable in a Suspend order action auto-created by the Order Metrics migration.  The period type used to specify when a subscription suspension takes effect. The subscription suspension will take place after the specified time frame (&#x60;suspendPeriods&#x60; multiplied by &#x60;suspendPeriodsType&#x60;) from today&#x27;s date.   | [optional] 
**suspend_policy** | **str** | Suspend methods. Specify a way to suspend a subscription. See [Suspend Date](https://knowledgecenter.zuora.com/BC_Subscription_Management/Subscriptions/Suspend_a_Subscription#Suspend_Date) for more information. Note this field is not applicable in a Suspend order action auto-created by the Order Metrics migration.  | [optional] 
**suspend_specific_date** | **date** | This field is applicable only when the &#x60;suspendPolicy&#x60; field is set to &#x60;SpecificDate&#x60;. Note this field is not applicable in a Suspend order action auto-created by the Order Metrics migration.  A specific date when the subscription suspension takes effect, in YYYY-MM-DD format. The value should not be earlier than the subscription&#x27;s contract effective date or later than the subscription&#x27;s term end date.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

