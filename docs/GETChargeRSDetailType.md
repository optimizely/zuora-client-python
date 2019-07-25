# GETChargeRSDetailType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | An account ID.  | [optional] 
**amount** | **str** | The revenue schedule amount, which is the sum of all revenue items. This field cannot be null and must be formatted based on the currency, such as *JPY 30* or USD *30.15*. Test out the currency to ensure you are using the proper formatting otherwise, the response will fail and this error message is returned:  *\&quot;Allocation amount with wrong decimal places.\&quot;*  | [optional] 
**currency** | **str** | The type of currency used.   | [optional] 
**notes** | **str** | Additional information about this record.  | [optional] 
**number** | **str** | The charge revenue summary number.  | [optional] 
**recognition_rule_name** | **str** | The name of the recognition rule.  | [optional] 
**recognized_revenue** | **str** | The revenue that was distributed in a closed accounting period.  | [optional] 
**revenue_items** | [**list[GETRevenueItemType]**](GETRevenueItemType.md) | Revenue items are listed in ascending order by the accounting period start date.  | [optional] 
**subscription_charge_id** | **str** | The original subscription charge ID.  | [optional] 
**subscription_id** | **str** | The original subscription ID.  | [optional] 
**success** | **bool** | Returns &#x60;true&#x60; if the request was processed successfully.  | [optional] 
**undistributed_unrecognized_revenue** | **str** | Revenue in the open-ended accounting period.  | [optional] 
**unrecognized_revenue** | **str** | Revenue distributed in all open accounting periods, which includes the open-ended accounting period.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

