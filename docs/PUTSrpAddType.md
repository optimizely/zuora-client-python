# PUTSrpAddType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_overrides** | [**list[PUTScAddType]**](PUTScAddType.md) | This optional container is used to override the quantity of one or more product rate plan charges for this subscription.  | [optional] 
**contract_effective_date** | **date** | The date when the amendment changes take effect. The format of the date is yyyy-mm-dd.  If there is already a future-dated Update Product amendment on the subscription, the &#x60;specificUpdateDate&#x60; field will be used instead of this field to specify when the Update Product amendment takes effect.  | 
**customer_acceptance_date** | **date** | The date when the customer accepts the contract in yyyy-mm-dd format.  If this field is not set:  * If the &#x60;serviceActivationDate&#x60; field is not set, the value of this field is set to be the contract effective date. * If the &#x60;serviceActivationDate&#x60; field is set, the value of this field is set to be the service activation date.  The billing trigger dates must follow this rule:  contractEffectiveDate &lt;&#x3D; serviceActivationDate &lt;&#x3D; contractAcceptanceDate  | [optional] 
**product_rate_plan_id** | **str** | ID of a product rate plan for this subscription  | 
**service_activation_date** | **date** | The date when the new product in the subscription is activated in yyyy-mm-dd format.  You must specify a Service Activation date if the Customer Acceptance date is set. If the Customer Acceptance date is not set, the value of the &#x60;serviceActivationDate&#x60; field defaults to be the Contract Effective Date.  The billing trigger dates must follow this rule:  contractEffectiveDate &lt;&#x3D; serviceActivationDate &lt;&#x3D; contractAcceptanceDate  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


