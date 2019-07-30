# EndConditions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date_condition** | **str** | Condition for the charge to become inactive.  If the value of this field is &#x60;Fixed_Period&#x60;, the charge is active for a predefined duration based on the value of the &#x60;upToPeriodsType&#x60; and &#x60;upToPeriods&#x60; fields.  If the value of this field is &#x60;Specific_End_Date&#x60;, use the &#x60;specificEndDate&#x60; field to specify the date when then charge becomes inactive.  | [optional] 
**specific_end_date** | **date** | Date in YYYY-MM-DD format. Only applicable if the value of the &#x60;endDateCondition&#x60; field is &#x60;Specific_End_Date&#x60;.  | [optional] 
**up_to_periods** | **int** | Duration of the charge in billing periods, days, weeks, months, or years, depending on the value of the &#x60;upToPeriodsType&#x60; field. Only applicable if the value of the &#x60;endDateCondition&#x60; field is &#x60;Fixed_Period&#x60;.  | [optional] 
**up_to_periods_type** | **str** | Unit of time that the charge duration is measured in. Only applicable if the value of the &#x60;endDateCondition&#x60; field is &#x60;Fixed_Period&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


