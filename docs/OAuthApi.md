# zuora_client.OAuthApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](OAuthApi.md#create_token) | **POST** /oauth/token | Generate an OAuth token


# **create_token**
> TokenResponse create_token(client_id, client_secret, grant_type, zuora_track_id=zuora_track_id)

Generate an OAuth token

Generates a bearer token that enables an OAuth client to authenticate with the Zuora REST API. The OAuth client must have been created using the Zuora UI. See [Authentication](https://www.zuora.com/developer/api-reference/#section/Authentication) for more information.  **Note:** When using this operation, do not set any authentication headers such as `Authorization`, `apiAccessKeyId`, or `apiSecretAccessKey`.  You should not use this operation to generate a large number of bearer tokens in a short period of time; each token should be used until it expires. If you receive a 429 Too Many Requests response when using this operation, reduce the frequency of requests. This endpoint is rate limited by IP address. 

### Example
```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.OAuthApi()
client_id = 'client_id_example' # str | The Client ID of the OAuth client. 
client_secret = 'client_secret_example' # str | The Client Secret that was displayed when the OAuth client was created. 
grant_type = 'grant_type_example' # str | The OAuth grant type that will be used to generate the token. The value of this parameter must be `client_credentials`. 
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Generate an OAuth token
    api_response = api_instance.create_token(client_id, client_secret, grant_type, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuthApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The Client ID of the OAuth client.  | 
 **client_secret** | **str**| The Client Secret that was displayed when the OAuth client was created.  | 
 **grant_type** | **str**| The OAuth grant type that will be used to generate the token. The value of this parameter must be &#x60;client_credentials&#x60;.  | 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

