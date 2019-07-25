# RatePlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendment_id** | **str** |  The ID of the amendment associated with the rate plan. This field only applies to amendment rate plans.   **Character limit**: 32  **Values**: a valid amendment ID  | [optional] 
**amendment_subscription_rate_plan_id** | **str** | The ID of the subscription rate plan modified by the amendment. This field only applies to amendment rate plans.  **Character limit**: 32  **Values**: a valid rate plan ID  | [optional] 
**amendment_type** | **str** | The type of amendment associated with the rate plan. This field only applies to amendment rate plans.  **Character limit**: 18  **Values**: inherited from &#x60;Amendment.Type&#x60;  | [optional] 
**created_by_id** | **str** | The ID of the Zuora user who created the RatePlan object.  **Character limit**: 32  **Values**: automatically generated  | [optional] 
**created_date** | **datetime** | The date when the &#x60;RatePlan&#x60; object was last updated.  **Character limit**: 29  **Values**: automatically generated  | [optional] 
**name** | **str** | The name of the rate plan. Leave this null in a subscribe call to inherited the &#x60;ProductRatePlan.Name&#x60; field value.  **Character limit**: 100  **Values**: a string of 100 characters or fewer or inherited from ProductRatePlan.Name  | [optional] 
**product_rate_plan_id** | **str** | The ID of the associated product rate plan.  **Character limit**: 32  **Values**: a valid product rate plan ID  | 
**subscription_id** | **str** | The ID of the subscription that the rate plan belongs to.  **Character limit**: 32  **Values**: a valid subscription ID  | [optional] 
**updated_by_id** | **str** |  The ID of the user who last updated the rate plan.   **Character limit**: 32  **Values**: automatically generated  | [optional] 
**updated_date** | **datetime** |  The date when the rate plan was last updated.   **Character limit**: 29  **Values**: automatically generated  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

