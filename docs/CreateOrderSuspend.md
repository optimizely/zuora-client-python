# CreateOrderSuspend

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suspend_periods** | **int** | This field is applicable only when the &#x60;suspendPolicy&#x60; field is set to &#x60;FixedPeriodsFromToday&#x60;. It must be used together with the &#x60;suspendPeriodsType&#x60; field.   The total number of the periods used to specify when a subscription suspension takes effect. The subscription suspension will take place after the specified time frame (&#x60;suspendPeriods&#x60; multiplied by &#x60;suspendPeriodsType&#x60;) from today&#39;s date.   | [optional] 
**suspend_periods_type** | **str** | This field is applicable only when the &#x60;suspendPolicy&#x60; field is set to &#x60;FixedPeriodsFromToday&#x60;. It must be used together with the &#x60;suspendPeriods&#x60; field.  The period type used to specify when a subscription suspension takes effect. The subscription suspension will take place after the specified time frame (&#x60;suspendPeriods&#x60; multiplied by &#x60;suspendPeriodsType&#x60;) from today&#39;s date.   | [optional] 
**suspend_policy** | **str** | Suspend methods. Specify a way to suspend a subscription. See [Suspend Date](https://knowledgecenter.zuora.com/BC_Subscription_Management/Subscriptions/Suspend_a_Subscription#Suspend_Date) for more information.  | 
**suspend_specific_date** | **date** | This field is applicable only when the &#x60;suspendPolicy&#x60; field is set to &#x60;SpecificDate&#x60;.  A specific date when the subscription suspension takes effect, in YYYY-MM-DD format. The value should not be earlier than the subscription&#39;s contract effective date or later than the subscription&#39;s term end date.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


