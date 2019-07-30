# POSTAccountTypeSubscription

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
**auto_renew** | **bool** | If &#x60;true&#x60;, auto-renew is enabled. Default is &#x60;false&#x60;.  | [optional] 
**contract_effective_date** | **date** | Effective contract date for this subscription, as &#x60;yyyy-mm-dd&#x60;.  | 
**customer_acceptance_date** | **date** | The date on which the services or products within a subscription have been accepted by the customer, as &#x60;yyyy-mm-dd&#x60;.  Default value is dependent on the value of other fields. See Notes section for more details.  | [optional] 
**initial_term** | **int** | Duration of the initial subscription term in whole months.  Default is 0.   | [optional] 
**invoice_owner_account_key** | **str** | Invoice owner account number or ID.  **Note:** This feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](https://support.zuora.com).   | [optional] 
**invoice_separately** | **bool** | Separates a single subscription from other subscriptions and invoices the charge independently.   If the value is &#x60;true&#x60;, the subscription is billed separately from other subscriptions. If the value is &#x60;false&#x60;, the subscription is included with other subscriptions in the account invoice. The default value is &#x60;false&#x60;.  Prerequisite: The default subscription setting &#x60;Enable Subscriptions to be Invoiced Separately&#x60; must be set to &#x60;Yes&#x60;.  | [optional] 
**notes** | **str** |  | [optional] 
**renewal_term** | **int** | Duration of the renewal term in whole months. Default is 0.  | [optional] 
**service_activation_date** | **date** | The date on which the services or products within a subscription have been activated and access has been provided to the customer, as &#x60;yyyy-mm-dd&#x60;.  Default value is dependent on the value of other fields. See Notes section for more details.  | [optional] 
**subscribe_to_rate_plans** | [**list[POSTSrpCreateType]**](POSTSrpCreateType.md) | Container for one or more rate plans for this subscription.  | [optional] 
**subscription_number** | **str** | Subscription Number. The value can be up to 1000 characters.  If you do not specify a subscription number when creating a subscription for the new account, Zuora will generate a subscription number automatically.  If the account is created successfully, the subscription number is returned in the &#x60;subscriptionNumber&#x60; response field.  | [optional] 
**term_start_date** | **date** | The date on which the subscription term begins, as &#x60;yyyy-mm-dd&#x60;. If this is a renewal subscription, this date is different from the subscription start date.  | [optional] 
**term_type** | **str** | Possible values are: &#x60;TERMED&#x60;, &#x60;EVERGREEN&#x60;.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


