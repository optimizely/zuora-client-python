# CreateStoredCredentialProfileRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies how Zuora activates the stored credential profile. Only applicable if you set the &#x60;status&#x60; field to &#x60;Active&#x60;.  * &#x60;Activate&#x60; (default) - Use this value if you are creating the stored credential profile after receiving the customer&#x27;s consent.    Zuora will create the stored credential profile then send a cardholder-initiated transaction (CIT) to the payment gateway to validate the stored credential profile. If the CIT succeeds, the status of the stored credential profile will be &#x60;Active&#x60;. If the CIT does not succeed, Zuora will not create a stored credential profile.      If the payment gateway does not support the stored credential transaction framework, the status of the stored credential profile will be &#x60;Agreed&#x60;.   * &#x60;Persist&#x60; - Use this value if the stored credential profile represents a stored credential profile in an external system. The status of the payment method&#x27;s stored credential profile will be &#x60;Active&#x60;.  | [optional] 
**agreed_on** | **date** | The date on which the profile is agreed. The date format is &#x60;yyyy-mm-dd&#x60;.  | [optional] 
**auth_gateway** | **str** | Specifies the ID of the payment gateway that Zuora will use when activating the stored credential profile.  | [optional] 
**consent_agreement_ref** | **str** | Specifies your reference for the consent agreement that you have established with the customer.  | [optional] 
**consent_agreement_src** | **str** |  | 
**status** | **str** | Specifies the status of the stored credential profile.  * &#x60;Active&#x60; - Use this value if you are creating the stored credential profile after receiving the customer&#x27;s consent, or if the stored credential profile represents a stored credential profile in an external system.    You can use the &#x60;action&#x60; field to specify how Zuora activates the stored credential profile.   * &#x60;Agreed&#x60; - Use this value if you are migrating the payment method to the stored credential transaction framework.    In this case, Zuora will not send a cardholder-initiated transaction (CIT) to the payment gateway to validate the stored credential profile.  | 
**type** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

