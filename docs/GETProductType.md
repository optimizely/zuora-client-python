# GETProductType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the product&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**item_type__ns** | **str** | Type of item that is created in NetSuite for the product. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the product was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**category** | **str** | Category of the product. Used by Zuora Quotes Guided Product Selector.  Possible values are:   - Base Products   - Add On Services   - Miscellaneous Products  | [optional] 
**description** | **str** | Optional product description.  | [optional] 
**effective_end_date** | **date** | The date when the product expires and cannot be subscribed to anymore, as &#x60;yyyy-mm-dd&#x60;.  | [optional] 
**effective_start_date** | **date** | The date when the product becomes available and can be subscribed to, as &#x60;yyyy-mm-dd&#x60;.  | [optional] 
**id** | **str** | Product ID.  | [optional] 
**name** | **str** | Product name, up to 100 characters.  | [optional] 
**product_features** | [**list[GetProductFeatureType]**](GetProductFeatureType.md) | Container for one or more product features. Only available when the following settings are enabled: - The Entitlements feature in your tenant - The Enable Feature Specification in Product and Subscriptions setting in Settings &gt; Billing  | [optional] 
**product_rate_plans** | **str** | URL to retrieve information about all product rate plans of a specific product. For example, &#x60;/v1/rateplan/40289f466463d683016463ef8b7301a0/productRatePlan&#x60;. If you want to view the product rate plan details, call [Get product rate plans](https://www.zuora.com/developer/api-reference/#operation/GET_ProductRatePlans) with the returned URL.  This field is in Zuora REST API version control. If you set the &#x60;zuora-version&#x60; request header to &#x60;230.0&#x60; or later, the value of this field is a URL. Zuora recommends that you use the latest behavior to retrieve product information.  If you do not set the &#x60;zuora-version&#x60; request header or you set this header to &#x60;229.0&#x60; or earlier, the value of this field is an array of product rate plan details. For more information about the array, see the response body of [Get product rate plans](https://www.zuora.com/developer/api-reference/#operation/GET_ProductRatePlans). **Note**: The array contains a maximum of 300 product rate plans. Additionally, across all product rate plans, at most 300 product rate plan charges are returned.  | [optional] 
**sku** | **str** | Unique product SKU, up to 50 characters.  | [optional] 
**tags** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


