# POSTHMACSignatureType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_key** | **str** | Customer account number or ID.  Specifies this field only when creating signatures for Create payment method.  | [optional] 
**method** | **str** | Possible values are: &#39;GET&#39;, &#39;POST&#39;, &#39;PUT&#39;, &#39;DELETE&#39;, &#39;OPTIONS&#39;.  | 
**name** | **str** | Account name.  Specifies this field only when creating signatures for Create account.  | [optional] 
**page_id** | **str** | The page id of your Payment Pages 2.0 form. Click **Show Page Id** next to the Payment Page name in the Hosted Page List to retrieve the page id.  Specifies this field only when creating signatures for RSA Signatures.  | [optional] 
**uri** | **str** | The URI of the API object the customer will make a CORS enabled call to. e.g. \&quot;https://rest.zuora.com/v1/payment-methods/credit-cards\&quot;  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


