# GETRSDetailWithoutSuccessType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | An account ID.  | [optional] 
**amount** | **str** | The revenue schedule amount, which is the sum of all revenue items. This field cannot be null and must be formatted based on the currency, such as &#x60;JPY 30&#x60; or &#x60;USD 30.15&#x60;. Test out the currency to ensure you are using the proper formatting otherwise, the response will fail and this error message is returned: &#x60;Allocation amount with wrong decimal places.&#x60;  | [optional] 
**created_on** | **datetime** | The date and time when the record was created, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 
**currency** | **str** | The type of currency used.  | [optional] 
**linked_transaction_id** | **str** | The linked transaction ID for billing transactions. This field is used for all rules except for the custom unlimited or manual recognition rule models. If using the custom unlimited rule model, then the field value must be null. If the field is not null, then the referenceId field must be null.  | [optional] 
**linked_transaction_number** | **str** | The number for the linked invoice item or invoice item adjustment transaction. This field is used for all rules except for the custom unlimited or manual recognition rule models. If using the custom unlimited or manual recognition rule models, then the field value is null.  | [optional] 
**linked_transaction_type** | **str** | The type of linked transaction for billing transactions, which can be invoice item or invoice item adjustment. This field is used for all rules except for the custom unlimited or manual recognition rule models.  | [optional] 
**notes** | **str** | Additional information about this record.  | [optional] 
**number** | **str** | Revenue schedule number. The revenue schedule number is always prefixed with \&quot;RS\&quot;, for example, \&quot;RS-00000001\&quot;.  | [optional] 
**recognition_rule_name** | **str** | The name of the recognition rule.  | [optional] 
**recognized_revenue** | **str** | The revenue that was distributed in a closed accounting period.  | [optional] 
**reference_id** | **str** | Reference ID is used only in the custom unlimited rule to create a revenue schedule. In this scenario, the revenue schedule is not linked to an invoice item or invoice item adjustment.  | [optional] 
**revenue_items** | [**list[GETRsRevenueItemType]**](GETRsRevenueItemType.md) | Revenue items are listed in ascending order by the accounting period start date.  | [optional] 
**revenue_schedule_date** | **date** | The effective date of the revenue schedule. For example, the revenue schedule date for bookings-based revenue recognition is typically set to the order date or contract date.  The date cannot be in a closed accounting period. The date must be in the &#x60;yyyy-mm-dd&#x60; format.  | [optional] 
**subscription_charge_id** | **str** | The original subscription charge ID.  | [optional] 
**subscription_id** | **str** | The original subscription ID.  | [optional] 
**undistributed_unrecognized_revenue** | **str** | Revenue in the open-ended accounting period.  | [optional] 
**unrecognized_revenue** | **str** | Revenue distributed in all open accounting periods, which includes the open-ended accounting period.  | [optional] 
**updated_on** | **datetime** | The date when the revenue automation start date was set, in &#x60;yyyy-mm-dd hh:mm:ss&#x60; format.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


