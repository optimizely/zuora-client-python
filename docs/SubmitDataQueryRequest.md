# SubmitDataQueryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression** | **str** | Specifies whether Zuora compresses the query results.  | 
**encryption_key** | **str** | Base-64 encoded public key of an RSA key-pair.  If you set this field, Zuora encrypts the query results using the provided public key. You must use the corresponding private key to decrypt the query results.  | [optional] 
**output** | [**SubmitDataQueryRequestOutput**](SubmitDataQueryRequestOutput.md) |  | 
**output_format** | **str** | Specifies the format of the query results.  * &#x60;JSON&#x60; - Each row in the query results will be a JSON object. The query results will not be wrapped in a JSON array. * &#x60;CSV&#x60; - Each row in the query results will be a comma-separated list of values.  | 
**query** | **str** | The query to perform. See [SQL Queries in Data Query](https://knowledgecenter.zuora.com/DC_Developers/BA_Data_Query/BA_SQL_Queries_in_Data_Query) for more information.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


