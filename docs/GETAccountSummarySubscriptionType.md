# GETAccountSummarySubscriptionType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpq_bundle_json_id__qt** | **str** | The Bundle product structures from Zuora Quotes if you utilize Bundling in Salesforce. Do not change the value in this field.  | [optional] 
**opportunity_close_date__qt** | **date** | The closing date of the Opportunity. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.  | [optional] 
**opportunity_name__qt** | **str** | The unique identifier of the Opportunity. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.  | [optional] 
**quote_business_type__qt** | **str** | The specific identifier for the type of business transaction the Quote represents such as New, Upsell, Downsell, Renewal or Churn. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.  | [optional] 
**quote_number__qt** | **str** | The unique identifier of the Quote. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.  | [optional] 
**quote_type__qt** | **str** | The Quote type that represents the subscription lifecycle stage such as New, Amendment, Renew or Cancel. This field is used in Zuora data sources to report on Subscription metrics. If the subscription originated from Zuora Quotes, the value is populated with the value from Zuora Quotes.  | [optional] 
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the subscription&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**project__ns** | **str** | The NetSuite project that the subscription was created from. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sales_order__ns** | **str** | The NetSuite sales order than the subscription was created from. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the subscription was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**auto_renew** | **bool** | If &#x60;true&#x60;, auto-renew is enabled. If &#x60;false&#x60;, auto-renew is disabled.  | [optional] 
**id** | **str** | Subscription ID.  | [optional] 
**initial_term** | **str** | Duration of the initial subscription term in whole months.   | [optional] 
**rate_plans** | [**list[GETAccountSummarySubscriptionRatePlanType]**](GETAccountSummarySubscriptionRatePlanType.md) | Container for rate plans for this subscription.  | [optional] 
**renewal_term** | **str** | Duration of the renewal term in whole months.  | [optional] 
**status** | **str** | Subscription status; possible values are: &#x60;Draft&#x60;, &#x60;PendingActivation&#x60;, &#x60;PendingAcceptance&#x60;, &#x60;Active&#x60;, &#x60;Cancelled&#x60;, &#x60;Expired&#x60;.  | [optional] 
**subscription_number** | **str** | Subscription Number.  | [optional] 
**subscription_start_date** | **date** | Subscription start date.  | [optional] 
**term_end_date** | **date** | End date of the subscription term. If the subscription is evergreen, this is either null or equal to the cancellation date, as appropriate.  | [optional] 
**term_start_date** | **date** | Start date of the subscription term. If this is a renewal subscription, this date is different than the subscription start date.  | [optional] 
**term_type** | **str** | Possible values are: &#x60;TERMED&#x60;, &#x60;EVERGREEN&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


