# ProxyModifyProduct

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the product&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**item_type__ns** | **str** | Type of item that is created in NetSuite for the product. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the product was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**allow_feature_changes** | **bool** |  Controls whether to allow your users to add or remove features while creating or amending a subscription. **Character** **limit**: n/a **Values**: true, false (default)  | [optional] 
**category** | **str** |  Category of the product. Used by Zuora Quotes Guided Product Selector. **Character** **limit**: 100 **Values**: One of the following:  - Base Products - Add On Services - Miscellaneous Products  | [optional] 
**description** | **str** |  A descriptionof the product. **Character limit**: 500 **Values**: a string of 500 characters or fewer  | [optional] 
**effective_end_date** | **date** | The date when the product expires and can&#39;t be subscribed to anymore, in &#x60;yyyy-mm-dd&#x60; format. **Character limit**: 29  | [optional] 
**effective_start_date** | **date** | The date when the product becomes available and can be subscribed to, in &#x60;yyyy-mm-dd&#x60; format. **Character limit**: 29  | [optional] 
**name** | **str** | The name of the product. This information is displayed in the product catalog pages in the web-based UI. **Character limit**: 100 **Values**: a string of 100 characters or fewer  | [optional] 
**sku** | **str** | The unique SKU for the product. **Character limit**: 50 **Values**: one of the following:  - leave null for automatic generated - an alphanumeric string of 50 characters or fewer  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


