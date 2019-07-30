# ProxyGetImport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_id** | **str** |  The user ID of the person who created the import.  **Character limit**: 32  **Values**: automatically generated  | [optional] 
**created_date** | **datetime** |  The date when the import was created.  **Character limit**: 29  **Values**: automatically generated  | [optional] 
**id** | **str** | Object identifier. | [optional] 
**import_type** | **str** |  The type of item imported.  **Character limit**: 7  **Values**: Usage  | [optional] 
**imported_count** | **int** | The number of records successfully imported.  **Values**: automatically generated  | [optional] 
**md5** | **str** |  A check to validate the import file&#39;s integrity.  **Character limit:** 32  **System-generated:** no  **Values**: a string of 32 characters or fewer  | [optional] 
**name** | **str** |  A descriptive name for the import.  **Character limit:** 100  **Values:** one of the following:  - a string of 100 characters or fewer - if NULL default is: &#x60;import &lt;ImportType_value&gt;&#x60;  | [optional] 
**original_resource_url** | **str** |  The URL for your import file, which contains your records for upload. When you upload the file, Zuora assigns it to this address.  **Values:** automatic dynamically-generated URL  | [optional] 
**result_resource_url** | **str** |  The URL for the import result file, which is a zipped CSV file.  **Values**: automatic dynamically-generated URL  | [optional] 
**status** | **str** | The status of the import process.  **Values**: automatically generated using one of the following values:  - Pending - Processing - Completed - Failed  | [optional] 
**status_reason** | **str** |  The reason for the system-generated status. Use this information if the import fails.  **Character limit**: 2000  **Values**: automatically generated error message  | [optional] 
**total_count** | **int** |  The number of records in the import file.  **Character limit**:  **Values**: automatically generated  | [optional] 
**updated_by_id** | **str** |  The ID of the user who last updated the import.  **Character limit**: 32  **Values**: automatically generated  | [optional] 
**updated_date** | **datetime** |  The date when the import was last updated. **Character limit**: 29 **Values**: automatically generated  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


