# POSTAccountTypeTaxInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vat_id** | **str** | EU Value Added Tax ID.   **Note:** This feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](https://support.zuora.com).  | [optional] 
**company_code** | **str** | Unique code that identifies a company account in Avalara. Use this field to calculate taxes based on origin and sold-to addresses in Avalara.  **Note:** This feature is in Limited Availability. If you wish to have access to the feature, submit a request at [Zuora Global Support](https://support.zuora.com).   | [optional] 
**exempt_certificate_id** | **str** | ID of the customer tax exemption certificate. Requires Zuora Tax.  | [optional] 
**exempt_certificate_type** | **str** | Type of tax exemption certificate that the customer holds. Requires Zuora Tax.  | [optional] 
**exempt_description** | **str** | Description of the tax exemption certificate that the customer holds. Requires Zuora Tax.  | [optional] 
**exempt_effective_date** | **date** | Date when the customer tax exemption starts. Requires Zuora Tax.  Format: &#x60;yyyy-mm-dd&#x60;. Defaults to the current date.  | [optional] 
**exempt_entity_use_code** | **str** | A unique entity use code to apply exemptions in Avalara AvaTax.  This account-level field is required only when you choose Avalara as your tax engine. See [Exempt Transactions](https://developer.avalara.com/avatax/handling-tax-exempt-customers/)for more details.  | [optional] 
**exempt_expiration_date** | **date** | Date when the customer tax exemption expires. Requires Zuora Tax.  Format: &#x60;yyyy-mm-dd&#x60;. Defaults to the current date.  | [optional] 
**exempt_issuing_jurisdiction** | **str** | Jurisdiction in which the customer tax exemption certificate was issued.  | [optional] 
**exempt_status** | **str** | Status of the account tax exemption. Requires Zuora Tax.  Required if you use Zuora Tax. This field is unavailable if Zuora Tax is not used.  Values: &#x60;Yes&#x60;, &#x60;No&#x60;, &#x60;pendingVerification&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


