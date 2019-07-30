# TaxInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vat_id** | **str** | EU Value Added Tax ID.  **Note:** This feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](https://support.zuora.com).  | [optional] 
**company_code** | **str** | Unique code that identifies a company account in Avalara. Use this field to calculate taxes based on origin and sold-to addresses in Avalara.  **Note:** This feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](https://support.zuora.com).  | [optional] 
**exempt_certificate_id** | **str** | ID of the customer tax exemption certificate. Only applicable if you use Zuora Tax.  | [optional] 
**exempt_certificate_type** | **str** | Type of tax exemption certificate that the customer holds. Only applicable if you use Zuora Tax.  | [optional] 
**exempt_description** | **str** | Description of the tax exemption certificate that the customer holds. Only applicable if you use Zuora Tax.  | [optional] 
**exempt_effective_date** | **date** | Date when the customer tax exemption starts, in YYYY-MM-DD format. Only applicable if you use Zuora Tax.  | [optional] 
**exempt_expiration_date** | **date** | Date when the customer tax exemption expires, in YYYY-MM-DD format. Only applicable if you use Zuora Tax.  | [optional] 
**exempt_issuing_jurisdiction** | **str** | Jurisdiction in which the customer tax exemption certificate was issued.  | [optional] 
**exempt_status** | **str** | Status of the account tax exemption. Required if you use Zuora Tax. Only applicable if you use Zuora Tax.  | [optional] [default to 'No']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


