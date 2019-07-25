# POSTQuoteDocType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiuser** | **str** | If not using Salesforce locale, this API Zuora user will be used to retrieve the locale from Zuora.  | [optional] 
**document_type** | **str** | Type of the document to generate: &#x60;PDF&#x60; or &#x60;DOC&#x60;.  | 
**locale** | **str** | Salesforce locale value to use.  | [optional] 
**password** | **str** |  | [optional] 
**quote_id** | **str** | ｜ Id of the quote。 | 
**sandbox** | **str** |  | [optional] 
**server_url** | **str** | SOAP URL used to login to Salesforce to get data. You can get the value with the following code in a Visualforce page: &#x60;{!$Api.Partner_Server_URL_100}&#x60;  | 
**session_id** | **str** | Salesforce session id used to log in to Salesforce to get data. You can get the value with the following code in a Visualforce page: *{!$Api.Session_ID}*  | 
**template_id** | **str** | Id of the quote template in Zuora.  | 
**token** | **str** |  | [optional] 
**use_sfdc_locale** | **str** | If using Salesforce org locale, set this to a value that is not null.  | [optional] 
**username** | **str** |  | [optional] 
**zquotes_major_version** | **str** | The major version number of Zuora Quotes you are generating the quote document in. You can use a quote template with hierarchy sizes bigger than 3 if this is set to 7 or higher.  | [optional] 
**zquotes_minor_version** | **str** | The minor version number of Zuora Quotes you are generating the quote document in.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

