# GETAmendmentType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_renew** | **bool** | Determines whether the subscription is automatically renewed, or whether it expires at the end of the term and needs to be manually renewed.   | [optional] 
**base_rate_plan_id** | **str** | The rate plan ID on which changes are made. Only the Update or Remove amendment returns a base rate plan ID.  | [optional] 
**base_subscription_id** | **str** | The ID of the subscription based on which the amendment is created.  | [optional] 
**code** | **str** | The amendment code.  | [optional] 
**contract_effective_date** | **date** | The date when the amendment becomes effective for billing purposes, as &#x60;yyyy-mm-dd&#x60;.  | [optional] 
**current_term** | **int** | The length of the period for the current subscription term.   | [optional] 
**current_term_period_type** | **str** | The period type for the current subscription term. Possible values are:  - Month - Year - Day - Week  | [optional] 
**customer_acceptance_date** | **date** | The date when the customer accepts the amendment changes to the subscription, as &#x60;yyyy-mm-dd&#x60;.  | [optional] 
**description** | **str** | Description of the amendment.  | [optional] 
**destination_account_id** | **str** | The ID of the account that the subscription is being transferred to.  | [optional] 
**destination_invoice_owner_id** | **str** | The ID of the invoice that the subscription is being transferred to.  | [optional] 
**effective_date** | **date** | The date when the amendment changes take effective.   | [optional] 
**id** | **str** | The amendment ID.  | [optional] 
**name** | **str** | The name of the amendment.  | [optional] 
**new_rate_plan_id** | **str** | The ID of the rate plan charge on which amendment is made. Only the Add or Update amendment returns a new rate plan ID.  | [optional] 
**new_subscription_id** | **str** | The ID of the subscription that the amendment changes.  | [optional] 
**renewal_setting** | **str** | Specifies whether a termed subscription will remain termed or change to evergreen when it is renewed. Possible values are:  - RENEW_WITH_SPECIFIC_TERM - RENEW_TO_EVERGREEN  | [optional] 
**renewal_term** | **int** | The term of renewal for the amended subscription.  | [optional] 
**renewal_term_period_type** | **str** | The period type for the subscription renewal term. Possible values are:  - Month - Year - Day - Week  | [optional] 
**resume_date** | **date** | The date when the subscription resumption takes effect, as &#x60;yyyy-mm-dd&#x60;.  **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  | [optional] 
**service_activation_date** | **date** | The date when service is activated, as &#x60;yyyy-mm-dd&#x60;.  | [optional] 
**specific_update_date** | **date** | The date when the Update Product amendment takes effect.  Only for the Update Product amendments if there is already a future-dated Update Product amendment on the subscription.  | [optional] 
**status** | **str** | The status of the amendment. Possible values are:  - Draft  - Pending Activation - Pending Acceptance - Completed  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**suspend_date** | **date** | The date when the subscription suspension takes effect, as &#x60;yyyy-mm-dd&#x60;.  **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  | [optional] 
**term_start_date** | **date** | The date when the new terms and conditions take effect.  | [optional] 
**term_type** | **str** | Indicates if the subscription is &#x60;TERMED&#x60; or &#x60;EVERGREEN&#x60;.  | [optional] 
**type** | **str** | Type of the amendment. Possible values are:  - Cancellation - NewProduct - OwnerTransfer - RemoveProduct - Renewal - UpdateProduct - TermsAndConditions  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

