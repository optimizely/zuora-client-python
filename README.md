# swagger-client
  # Introduction Welcome to the reference for the Zuora REST API!  <a href=\"http://en.wikipedia.org/wiki/REST_API\" target=\"_blank\">REST</a> is a web-service protocol that lends itself to rapid development by using everyday HTTP and JSON technology.  The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Production | https://rest.zuora.com   | |US API Sandbox    | https://rest.apisandbox.zuora.com| |US Performance Test | https://rest.pt1.zuora.com | |EU Production | https://rest.eu.zuora.com | |EU Sandbox | https://rest.sandbox.eu.zuora.com |  The Production endpoint provides access to your live user data. API Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision an API Sandbox tenant for you, contact your Zuora representative for assistance.  **Note:** If you have a tenant in the Production Copy Environment, submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints.  If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.  # API Changelog You can find the <a href=\"https://community.zuora.com/t5/Developers/API-Changelog/gpm-p/18092\" target=\"_blank\">Changelog</a> of the API Reference in the Zuora Community.  # Authentication  ## OAuth v2.0  Zuora recommends that you use OAuth v2.0 to authenticate to the Zuora REST API. Currently, OAuth is not available in every environment. See [Zuora Testing Environments](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Environments) for more information.  Zuora recommends you to create a dedicated API user with API write access on a tenant when authenticating via OAuth, and then create an OAuth client for this user. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for how to do this. By creating a dedicated API user, you can control permissions of the API user without affecting other non-API users.  If a user is deactivated, all of the user's OAuth clients will be automatically deactivated.  Authenticating via OAuth requires the following steps: 1. Create a Client 2. Generate a Token 3. Make Authenticated Requests  ### Create a Client  You must first [create an OAuth client](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) in the Zuora UI. To do this, you must be an administrator of your Zuora tenant. This is a one-time operation. You will be provided with a Client ID and a Client Secret. Please note this information down, as it will be required for the next step.  **Note:** The OAuth client will be owned by a Zuora user account. If you want to perform PUT, POST, or DELETE operations using the OAuth client, the owner of the OAuth client must have a Platform role that includes the \"API Write Access\" permission.  ### Generate a Token  After creating a client, you must make a call to obtain a bearer token using the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) operation. This operation requires the following parameters: - `client_id` - the Client ID displayed when you created the OAuth client in the previous step - `client_secret` - the Client Secret displayed when you created the OAuth client in the previous step - `grant_type` - must be set to `client_credentials`  **Note**: The Client ID and Client Secret mentioned above were displayed when you created the OAuth Client in the prior step. The [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response specifies how long the bearer token is valid for. Call [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) again to generate a new bearer token.  ### Make Authenticated Requests  To authenticate subsequent API requests, you must provide a valid bearer token in an HTTP header:  `Authorization: Bearer {bearer_token}`  If you have [Zuora Multi-entity](https://www.zuora.com/developer/api-reference/#tag/Entities) enabled, you need to set an additional header to specify the ID of the entity that you want to access. You can use the `scope` field in the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response to determine whether you need to specify an entity ID.  If the `scope` field contains more than one entity ID, you must specify the ID of the entity that you want to access. For example, if the `scope` field contains `entity.1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` and `entity.c92ed977-510c-4c48-9b51-8d5e848671e9`, specify one of the following headers: - `Zuora-Entity-Ids: 1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` - `Zuora-Entity-Ids: c92ed977-510c-4c48-9b51-8d5e848671e9`  **Note**: For a limited period of time, Zuora will accept the `entityId` header as an alternative to the `Zuora-Entity-Ids` header. If you choose to set the `entityId` header, you must remove all \"-\" characters from the entity ID in the `scope` field.  If the `scope` field contains a single entity ID, you do not need to specify an entity ID.  ## Other Supported Authentication Schemes  Zuora continues to support the following additional legacy means of authentication:    * Use username and password. Include authentication with each request in the header:         * `apiAccessKeyId`      * `apiSecretAccessKey`          Zuora recommends that you create an API user specifically for making API calls. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for more information.      * Use an authorization cookie. The cookie authorizes the user to make calls to the REST API for the duration specified in  **Administration > Security Policies > Session timeout**. The cookie expiration time is reset with this duration after every call to the REST API. To obtain a cookie, call the [Connections](https://www.zuora.com/developer/api-reference/#tag/Connections) resource with the following API user information:         *   ID         *   Password        * For CORS-enabled APIs only: Include a 'single-use' token in the request header, which re-authenticates the user with each request. See below for more details.  ### Entity Id and Entity Name  The `entityId` and `entityName` parameters are only used for [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity \"Zuora Multi-entity\"). These are the legacy parameters that Zuora will only continue to support for a period of time. Zuora recommends you to use the `Zuora-Entity-Ids` parameter instead.   The  `entityId` and `entityName` parameters specify the Id and the [name of the entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/B_Introduction_to_Entity_and_Entity_Hierarchy#Name_and_Display_Name \"Introduction to Entity and Entity Hierarchy\") that you want to access, respectively. Note that you must have permission to access the entity.   You can specify either the `entityId` or `entityName` parameter in the authentication to access and view an entity.    * If both `entityId` and `entityName` are specified in the authentication, an error occurs.    * If neither `entityId` nor `entityName` is specified in the authentication, you will log in to the entity in which your user account is created.      To get the entity Id and entity name, you can use the GET Entities REST call. For more information, see [API User Authentication](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/A_Overview_of_Multi-entity#API_User_Authentication \"API User Authentication\").      ### Token Authentication for CORS-Enabled APIs      The CORS mechanism enables REST API calls to Zuora to be made directly from your customer's browser, with all credit card and security information transmitted directly to Zuora. This minimizes your PCI compliance burden, allows you to implement advanced validation on your payment forms, and  makes your payment forms look just like any other part of your website.    For security reasons, instead of using cookies, an API request via CORS uses **tokens** for authentication.  The token method of authentication is only designed for use with requests that must originate from your customer's browser; **it should  not be considered a replacement to the existing cookie authentication** mechanism.  See [Zuora CORS REST](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Zuora_CORS_REST \"Zuora CORS REST\") for details on how CORS works and how you can begin to implement customer calls to the Zuora REST APIs. See  [HMAC Signatures](https://www.zuora.com/developer/api-reference/#operation/POSTHMACSignature \"HMAC Signatures\") for details on the HMAC method that returns the authentication token.  # Requests and Responses  ## Request IDs  As a general rule, when asked to supply a \"key\" for an account or subscription (accountKey, account-key, subscriptionKey, subscription-key), you can provide either the actual ID or  the number of the entity.  ## HTTP Request Body  Most of the parameters and data accompanying your requests will be contained in the body of the HTTP request.   The Zuora REST API accepts JSON in the HTTP request body. No other data format (e.g., XML) is supported.  ### Data Type  ([Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations only) We recommend that you do not specify the decimal values with quotation marks, commas, and spaces. Use characters of `+-0-9.eE`, for example, `5`, `1.9`, `-8.469`, and `7.7e2`. Also, Zuora does not convert currencies for decimal values.  ## Testing a Request  Use a third party client, such as [curl](https://curl.haxx.se \"curl\"), [Postman](https://www.getpostman.com \"Postman\"), or [Advanced REST Client](https://advancedrestclient.com \"Advanced REST Client\"), to test the Zuora REST API.  You can test the Zuora REST API from the Zuora API Sandbox or Production tenants. If connecting to Production, bear in mind that you are working with your live production data, not sample data or test data.  ## Testing with Credit Cards  Sooner or later it will probably be necessary to test some transactions that involve credit cards. For suggestions on how to handle this, see [Going Live With Your Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards \"C_Zuora_User_Guides/A_Billing_and_Payments/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards\" ).  ## Concurrent Request Limits  Zuora enforces tenant-level concurrent request limits. See <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits\" target=\"_blank\">Concurrent Request Limits</a> for more information.  ## Timeout Limit  If a request does not complete within 120 seconds, the request times out and Zuora returns a Gateway Timeout error.  ## Error Handling  Responses and error codes are detailed in [Responses and errors](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Responses_and_Errors \"Responses and errors\").  # Pagination  When retrieving information (using GET methods), the optional `pageSize` query parameter sets the maximum number of rows to return in a response. The maximum is `40`; larger values are treated as `40`. If this value is empty or invalid, `pageSize` typically defaults to `10`.  The default value for the maximum number of rows retrieved can be overridden at the method level.  If more rows are available, the response will include a `nextPage` element, which contains a URL for requesting the next page.  If this value is not provided, no more rows are available. No \"previous page\" element is explicitly provided; to support backward paging, use the previous call.  ## Array Size  For data items that are not paginated, the REST API supports arrays of up to 300 rows.  Thus, for instance, repeated pagination can retrieve thousands of customer accounts, but within any account an array of no more than 300 rate plans is returned.  # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.  ## Major Version  The major version number of the REST API appears in the REST URL. Currently, Zuora only supports the **v1** major version. For example, `POST https://rest.zuora.com/v1/subscriptions`.  ## Minor Version  Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.   Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not serial. This section documents the changes made to each Zuora REST API minor version.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 196.0 and earlier  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. | | creditTaxItems | 238.0 and earlier | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\") | Container for the taxation items of the credit memo item. | | taxItems | 238.0 and earlier | [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the debit memo item. | | taxationItems | 239.0 and later | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the memo item. |   #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") and [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics  # Zuora Object Model  The following diagram presents a high-level view of the key Zuora objects. Click the image to open it in a new tab to resize it.  <a href=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" target=\"_blank\"><img src=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" alt=\"Zuora Object Model Diagram\"></a>  See the following articles for information about other parts of the Zuora business object model:    * <a href=\"https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/D_Invoice_Settlement_Object_Model\" target=\"_blank\">Invoice Settlement Object Model</a>   * <a href=\"https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/BA_Orders_Object_Model\" target=\"_blank\">Orders Object Model</a>  You can use the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun`</p><p>**Note:** The API name of this object is `BillingRun` in the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation, Export ZOQL queries, and Data Query. Otherwise, the API name of this object is `BillRun`.</p> | | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Feature                                       | `Feature`                                  | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                         | `UpdaterDetail`                            | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Feature                               | `ProductFeature`                           | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Subscription Product Feature                  | `SubscriptionProductFeature`               | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    | 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2019-07-26
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import zuora_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import zuora_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import zuora_client
from zuora_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = zuora_client.AccountingCodesApi(zuora_client.ApiClient(configuration))
ac_id = 'ac_id_example' # str | ID of the accounting code you want to delete.
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)

try:
    # Delete accounting code
    api_response = api_instance.d_elete_accounting_code(ac_id, zuora_entity_ids=zuora_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCodesApi->d_elete_accounting_code: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://rest.zuora.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountingCodesApi* | [**d_elete_accounting_code**](docs/AccountingCodesApi.md#d_elete_accounting_code) | **DELETE** /v1/accounting-codes/{ac-id} | Delete accounting code
*AccountingCodesApi* | [**g_et_accounting_code**](docs/AccountingCodesApi.md#g_et_accounting_code) | **GET** /v1/accounting-codes/{ac-id} | Query an accounting code
*AccountingCodesApi* | [**g_et_all_accounting_codes**](docs/AccountingCodesApi.md#g_et_all_accounting_codes) | **GET** /v1/accounting-codes | Get all accounting codes
*AccountingCodesApi* | [**p_ost_accounting_code**](docs/AccountingCodesApi.md#p_ost_accounting_code) | **POST** /v1/accounting-codes | Create accounting code
*AccountingCodesApi* | [**p_ut_accounting_code**](docs/AccountingCodesApi.md#p_ut_accounting_code) | **PUT** /v1/accounting-codes/{ac-id} | Update an accounting code
*AccountingCodesApi* | [**p_ut_activate_accounting_code**](docs/AccountingCodesApi.md#p_ut_activate_accounting_code) | **PUT** /v1/accounting-codes/{ac-id}/activate | Activate accounting code
*AccountingCodesApi* | [**p_ut_deactivate_accounting_code**](docs/AccountingCodesApi.md#p_ut_deactivate_accounting_code) | **PUT** /v1/accounting-codes/{ac-id}/deactivate | Deactivate accounting code
*AccountingPeriodsApi* | [**d_elete_accounting_period**](docs/AccountingPeriodsApi.md#d_elete_accounting_period) | **DELETE** /v1/accounting-periods/{ap-id} | Delete accounting period
*AccountingPeriodsApi* | [**g_et_accounting_period**](docs/AccountingPeriodsApi.md#g_et_accounting_period) | **GET** /v1/accounting-periods/{ap-id} | Get accounting period
*AccountingPeriodsApi* | [**g_et_all_accounting_periods**](docs/AccountingPeriodsApi.md#g_et_all_accounting_periods) | **GET** /v1/accounting-periods | Get all accounting periods
*AccountingPeriodsApi* | [**p_ost_accounting_period**](docs/AccountingPeriodsApi.md#p_ost_accounting_period) | **POST** /v1/accounting-periods | Create accounting period
*AccountingPeriodsApi* | [**p_ut_close_accounting_period**](docs/AccountingPeriodsApi.md#p_ut_close_accounting_period) | **PUT** /v1/accounting-periods/{ap-id}/close | Close accounting period
*AccountingPeriodsApi* | [**p_ut_pending_close_accounting_period**](docs/AccountingPeriodsApi.md#p_ut_pending_close_accounting_period) | **PUT** /v1/accounting-periods/{ap-id}/pending-close | Set accounting period to pending close
*AccountingPeriodsApi* | [**p_ut_reopen_accounting_period**](docs/AccountingPeriodsApi.md#p_ut_reopen_accounting_period) | **PUT** /v1/accounting-periods/{ap-id}/reopen | Re-open accounting period
*AccountingPeriodsApi* | [**p_ut_run_trial_balance**](docs/AccountingPeriodsApi.md#p_ut_run_trial_balance) | **PUT** /v1/accounting-periods/{ap-id}/run-trial-balance | Run trial balance
*AccountingPeriodsApi* | [**p_ut_update_accounting_period**](docs/AccountingPeriodsApi.md#p_ut_update_accounting_period) | **PUT** /v1/accounting-periods/{ap-id} | Update accounting period
*AccountsApi* | [**g_et_account**](docs/AccountsApi.md#g_et_account) | **GET** /v1/accounts/{account-key} | Get account
*AccountsApi* | [**g_et_account_summary**](docs/AccountsApi.md#g_et_account_summary) | **GET** /v1/accounts/{account-key}/summary | Get account summary
*AccountsApi* | [**g_et_billing_document_files_deletion_job**](docs/AccountsApi.md#g_et_billing_document_files_deletion_job) | **GET** /v1/accounts/billing-documents/files/deletion-jobs/{jobId} | Get job of hard deleting billing document files
*AccountsApi* | [**object_delete_account**](docs/AccountsApi.md#object_delete_account) | **DELETE** /v1/object/account/{id} | CRUD: Delete account
*AccountsApi* | [**object_get_account**](docs/AccountsApi.md#object_get_account) | **GET** /v1/object/account/{id} | CRUD: Get account
*AccountsApi* | [**object_post_account**](docs/AccountsApi.md#object_post_account) | **POST** /v1/object/account | CRUD: Create account
*AccountsApi* | [**object_put_account**](docs/AccountsApi.md#object_put_account) | **PUT** /v1/object/account/{id} | CRUD: Update account
*AccountsApi* | [**p_ost_account**](docs/AccountsApi.md#p_ost_account) | **POST** /v1/accounts | Create account
*AccountsApi* | [**p_ost_billing_document_files_deletion_job**](docs/AccountsApi.md#p_ost_billing_document_files_deletion_job) | **POST** /v1/accounts/billing-documents/files/deletion-jobs | Create job to hard delete billing document files
*AccountsApi* | [**p_ost_generate_billing_documents**](docs/AccountsApi.md#p_ost_generate_billing_documents) | **POST** /v1/accounts/{id}/billing-documents/generate | Generate billing documents by account
*AccountsApi* | [**p_ut_account**](docs/AccountsApi.md#p_ut_account) | **PUT** /v1/accounts/{account-key} | Update account
*ActionsApi* | [**action_pos_tamend**](docs/ActionsApi.md#action_pos_tamend) | **POST** /v1/action/amend | Amend
*ActionsApi* | [**action_pos_tcreate**](docs/ActionsApi.md#action_pos_tcreate) | **POST** /v1/action/create | Create
*ActionsApi* | [**action_pos_tdelete**](docs/ActionsApi.md#action_pos_tdelete) | **POST** /v1/action/delete | Delete
*ActionsApi* | [**action_pos_texecute**](docs/ActionsApi.md#action_pos_texecute) | **POST** /v1/action/execute | Execute
*ActionsApi* | [**action_pos_tgenerate**](docs/ActionsApi.md#action_pos_tgenerate) | **POST** /v1/action/generate | Generate
*ActionsApi* | [**action_pos_tquery**](docs/ActionsApi.md#action_pos_tquery) | **POST** /v1/action/query | Query
*ActionsApi* | [**action_pos_tquery_more**](docs/ActionsApi.md#action_pos_tquery_more) | **POST** /v1/action/queryMore | QueryMore
*ActionsApi* | [**action_pos_tsubscribe**](docs/ActionsApi.md#action_pos_tsubscribe) | **POST** /v1/action/subscribe | Subscribe
*ActionsApi* | [**action_pos_tupdate**](docs/ActionsApi.md#action_pos_tupdate) | **POST** /v1/action/update | Update
*AmendmentsApi* | [**g_et_amendments_by_key**](docs/AmendmentsApi.md#g_et_amendments_by_key) | **GET** /v1/amendments/{amendment-key} | Get amendments by key
*AmendmentsApi* | [**g_et_amendments_by_subscription_id**](docs/AmendmentsApi.md#g_et_amendments_by_subscription_id) | **GET** /v1/amendments/subscriptions/{subscription-id} | Get amendments by subscription ID
*AmendmentsApi* | [**object_delete_amendment**](docs/AmendmentsApi.md#object_delete_amendment) | **DELETE** /v1/object/amendment/{id} | CRUD: Delete amendment
*AmendmentsApi* | [**object_get_amendment**](docs/AmendmentsApi.md#object_get_amendment) | **GET** /v1/object/amendment/{id} | CRUD: Get amendment
*AmendmentsApi* | [**object_put_amendment**](docs/AmendmentsApi.md#object_put_amendment) | **PUT** /v1/object/amendment/{id} | CRUD: Update amendment
*AttachmentsApi* | [**d_elete_attachments**](docs/AttachmentsApi.md#d_elete_attachments) | **DELETE** /v1/attachments/{attachment-id} | Delete attachments
*AttachmentsApi* | [**g_et_attachments**](docs/AttachmentsApi.md#g_et_attachments) | **GET** /v1/attachments/{attachment-id} | View attachments
*AttachmentsApi* | [**g_et_attachments_list**](docs/AttachmentsApi.md#g_et_attachments_list) | **GET** /v1/attachments/{object-type}/{object-key} | View attachments list
*AttachmentsApi* | [**p_ost_attachments**](docs/AttachmentsApi.md#p_ost_attachments) | **POST** /v1/attachments | Add attachments
*AttachmentsApi* | [**p_ut_attachments**](docs/AttachmentsApi.md#p_ut_attachments) | **PUT** /v1/attachments/{attachment-id} | Edit attachments
*BillRunApi* | [**object_delete_bill_run**](docs/BillRunApi.md#object_delete_bill_run) | **DELETE** /v1/object/bill-run/{id} | CRUD: Delete bill run
*BillRunApi* | [**object_get_bill_run**](docs/BillRunApi.md#object_get_bill_run) | **GET** /v1/object/bill-run/{id} | CRUD: Get bill run
*BillRunApi* | [**object_post_bill_run**](docs/BillRunApi.md#object_post_bill_run) | **POST** /v1/object/bill-run | CRUD: Create bill run
*BillRunApi* | [**object_put_bill_run**](docs/BillRunApi.md#object_put_bill_run) | **PUT** /v1/object/bill-run/{id} | CRUD: Post or Cancel bill run
*BillRunApi* | [**p_ost_email_billing_documentsfrom_bill_run**](docs/BillRunApi.md#p_ost_email_billing_documentsfrom_bill_run) | **POST** /v1/bill-runs/{billRunId}/emails | Email billing documents generated from bill run
*BillingDocumentsApi* | [**g_et_billing_documents**](docs/BillingDocumentsApi.md#g_et_billing_documents) | **GET** /v1/billing-documents | Get billing documents
*BillingPreviewRunApi* | [**g_et_billing_preview_run**](docs/BillingPreviewRunApi.md#g_et_billing_preview_run) | **GET** /v1/billing-preview-runs/{billingPreviewRunId} | Get Billing Preview Run
*BillingPreviewRunApi* | [**p_ost_billing_preview_run**](docs/BillingPreviewRunApi.md#p_ost_billing_preview_run) | **POST** /v1/billing-preview-runs | Create Billing Preview Run
*CatalogApi* | [**g_et_catalog**](docs/CatalogApi.md#g_et_catalog) | **GET** /v1/catalog/products | Get product catalog
*CatalogApi* | [**g_et_product**](docs/CatalogApi.md#g_et_product) | **GET** /v1/catalog/product/{product-id} | Get product
*CatalogApi* | [**p_ost_catalog**](docs/CatalogApi.md#p_ost_catalog) | **POST** /v1/catalog/products/{product-id}/share | Multi-entity: Share a product with an Entity
*ChargeRevenueSummariesApi* | [**g_etcrs_by_charge_id**](docs/ChargeRevenueSummariesApi.md#g_etcrs_by_charge_id) | **GET** /v1/charge-revenue-summaries/subscription-charges/{charge-key} | Get charge summary details by charge ID
*ChargeRevenueSummariesApi* | [**g_etcrs_by_crs_number**](docs/ChargeRevenueSummariesApi.md#g_etcrs_by_crs_number) | **GET** /v1/charge-revenue-summaries/{crs-number} | Get charge summary details by CRS number
*CommunicationProfilesApi* | [**object_get_communication_profile**](docs/CommunicationProfilesApi.md#object_get_communication_profile) | **GET** /v1/object/communication-profile/{id} | CRUD: Retrieve CommunicationProfile
*ConnectionsApi* | [**p_ost_connections**](docs/ConnectionsApi.md#p_ost_connections) | **POST** /v1/connections | Establish connection to Zuora REST API service
*ContactsApi* | [**object_delete_contact**](docs/ContactsApi.md#object_delete_contact) | **DELETE** /v1/object/contact/{id} | CRUD: Delete contact
*ContactsApi* | [**object_get_contact**](docs/ContactsApi.md#object_get_contact) | **GET** /v1/object/contact/{id} | CRUD: Get contact
*ContactsApi* | [**object_post_contact**](docs/ContactsApi.md#object_post_contact) | **POST** /v1/object/contact | CRUD: Create contact
*ContactsApi* | [**object_put_contact**](docs/ContactsApi.md#object_put_contact) | **PUT** /v1/object/contact/{id} | CRUD: Update contact
*ContactsApi* | [**p_ut_scrub_contact**](docs/ContactsApi.md#p_ut_scrub_contact) | **PUT** /v1/contacts/{contactId}/scrub | Scrub contact
*CreditBalanceAdjustmentsApi* | [**object_get_credit_balance_adjustment**](docs/CreditBalanceAdjustmentsApi.md#object_get_credit_balance_adjustment) | **GET** /v1/object/credit-balance-adjustment/{id} | CRUD: Retrieve CreditBalanceAdjustment
*CreditBalanceAdjustmentsApi* | [**object_post_credit_balance_adjustment**](docs/CreditBalanceAdjustmentsApi.md#object_post_credit_balance_adjustment) | **POST** /v1/object/credit-balance-adjustment | CRUD: Create CreditBalanceAdjustment
*CreditBalanceAdjustmentsApi* | [**object_put_credit_balance_adjustment**](docs/CreditBalanceAdjustmentsApi.md#object_put_credit_balance_adjustment) | **PUT** /v1/object/credit-balance-adjustment/{id} | CRUD: Update CreditBalanceAdjustment
*CreditMemosApi* | [**d_elete_credit_memo**](docs/CreditMemosApi.md#d_elete_credit_memo) | **DELETE** /v1/creditmemos/{creditMemoId} | Delete credit memo
*CreditMemosApi* | [**g_et_breakdown_credit_memo_by_order**](docs/CreditMemosApi.md#g_et_breakdown_credit_memo_by_order) | **GET** /v1/creditmemos/{creditMemoNumber}/amountBreakdownByOrder | Get breakdown of credit memo by order
*CreditMemosApi* | [**g_et_credit_memo**](docs/CreditMemosApi.md#g_et_credit_memo) | **GET** /v1/creditmemos/{creditMemoId} | Get credit memo
*CreditMemosApi* | [**g_et_credit_memo_item**](docs/CreditMemosApi.md#g_et_credit_memo_item) | **GET** /v1/creditmemos/{creditMemoId}/items/{cmitemid} | Get credit memo item
*CreditMemosApi* | [**g_et_credit_memo_item_part**](docs/CreditMemosApi.md#g_et_credit_memo_item_part) | **GET** /v1/creditmemos/{creditMemoId}/parts/{partid}/itemparts/{itempartid} | Get credit memo part item
*CreditMemosApi* | [**g_et_credit_memo_item_parts**](docs/CreditMemosApi.md#g_et_credit_memo_item_parts) | **GET** /v1/creditmemos/{creditMemoId}/parts/{partid}/itemparts | Get credit memo part items
*CreditMemosApi* | [**g_et_credit_memo_items**](docs/CreditMemosApi.md#g_et_credit_memo_items) | **GET** /v1/creditmemos/{creditMemoId}/items | Get credit memo items
*CreditMemosApi* | [**g_et_credit_memo_part**](docs/CreditMemosApi.md#g_et_credit_memo_part) | **GET** /v1/creditmemos/{creditMemoId}/parts/{partid} | Get credit memo part
*CreditMemosApi* | [**g_et_credit_memo_parts**](docs/CreditMemosApi.md#g_et_credit_memo_parts) | **GET** /v1/creditmemos/{creditMemoId}/parts | Get credit memo parts
*CreditMemosApi* | [**g_et_credit_memos**](docs/CreditMemosApi.md#g_et_credit_memos) | **GET** /v1/creditmemos | Get credit memos
*CreditMemosApi* | [**g_et_taxation_items_of_credit_memo_item**](docs/CreditMemosApi.md#g_et_taxation_items_of_credit_memo_item) | **GET** /v1/creditmemos/{creditMemoId}/items/{cmitemid}/taxation-items | Get taxation items of credit memo item
*CreditMemosApi* | [**p_ost_credit_memo_from_prpc**](docs/CreditMemosApi.md#p_ost_credit_memo_from_prpc) | **POST** /v1/creditmemos | Create credit memo from charge
*CreditMemosApi* | [**p_ost_credit_memo_pdf**](docs/CreditMemosApi.md#p_ost_credit_memo_pdf) | **POST** /v1/creditmemos/{creditMemoId}/pdfs | Create credit memo PDF
*CreditMemosApi* | [**p_ost_email_credit_memo**](docs/CreditMemosApi.md#p_ost_email_credit_memo) | **POST** /v1/creditmemos/{creditMemoId}/emails | Email credit memo
*CreditMemosApi* | [**p_ost_refund_credit_memo**](docs/CreditMemosApi.md#p_ost_refund_credit_memo) | **POST** /v1/creditmemos/{creditmemoId}/refunds | Refund credit memo
*CreditMemosApi* | [**p_ost_request_breakdown_credit_memo_items_by_order**](docs/CreditMemosApi.md#p_ost_request_breakdown_credit_memo_items_by_order) | **POST** /v1/creditmemos/items/amountBreakdownByOrder | Request breakdown of credit memo items by order
*CreditMemosApi* | [**p_ost_upload_file_for_credit_memo**](docs/CreditMemosApi.md#p_ost_upload_file_for_credit_memo) | **POST** /v1/creditmemos/{creditMemoId}/files | Upload file for credit memo
*CreditMemosApi* | [**p_ostcm_taxation_items**](docs/CreditMemosApi.md#p_ostcm_taxation_items) | **POST** /v1/creditmemos/{creditMemoId}/taxationitems | Create taxation items for credit memo
*CreditMemosApi* | [**p_ut_apply_credit_memo**](docs/CreditMemosApi.md#p_ut_apply_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId}/apply | Apply credit memo
*CreditMemosApi* | [**p_ut_cancel_credit_memo**](docs/CreditMemosApi.md#p_ut_cancel_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId}/cancel | Cancel credit memo
*CreditMemosApi* | [**p_ut_post_credit_memo**](docs/CreditMemosApi.md#p_ut_post_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId}/post | Post credit memo
*CreditMemosApi* | [**p_ut_unapply_credit_memo**](docs/CreditMemosApi.md#p_ut_unapply_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId}/unapply | Unapply credit memo
*CreditMemosApi* | [**p_ut_unpost_credit_memo**](docs/CreditMemosApi.md#p_ut_unpost_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId}/unpost | Unpost credit memo
*CreditMemosApi* | [**p_ut_update_credit_memo**](docs/CreditMemosApi.md#p_ut_update_credit_memo) | **PUT** /v1/creditmemos/{creditMemoId} | Update credit memo
*CustomExchangeRatesApi* | [**g_et_custom_exchange_rates**](docs/CustomExchangeRatesApi.md#g_et_custom_exchange_rates) | **GET** /v1/custom-exchange-rates/{currency} | Get custom foreign currency exchange rates
*DataQueriesApi* | [**d_elete_data_query_job**](docs/DataQueriesApi.md#d_elete_data_query_job) | **DELETE** /query/jobs/{job-id} | Cancel data query job
*DataQueriesApi* | [**g_et_data_query_job**](docs/DataQueriesApi.md#g_et_data_query_job) | **GET** /query/jobs/{job-id} | Get data query job
*DataQueriesApi* | [**g_et_data_query_jobs**](docs/DataQueriesApi.md#g_et_data_query_jobs) | **GET** /query/jobs | Get data query jobs
*DataQueriesApi* | [**p_ost_data_query_job**](docs/DataQueriesApi.md#p_ost_data_query_job) | **POST** /query/jobs | Submit data query
*DebitMemosApi* | [**d_elete_debit_memo**](docs/DebitMemosApi.md#d_elete_debit_memo) | **DELETE** /v1/debitmemos/{debitMemoId} | Delete debit memo
*DebitMemosApi* | [**g_et_debit_memo**](docs/DebitMemosApi.md#g_et_debit_memo) | **GET** /v1/debitmemos/{debitMemoId} | Get debit memo
*DebitMemosApi* | [**g_et_debit_memo_application_parts**](docs/DebitMemosApi.md#g_et_debit_memo_application_parts) | **GET** /v1/debitmemos/{debitMemoId}/application-parts | Get debit memo application parts
*DebitMemosApi* | [**g_et_debit_memo_item**](docs/DebitMemosApi.md#g_et_debit_memo_item) | **GET** /v1/debitmemos/{debitMemoId}/items/{dmitemid} | Get debit memo item
*DebitMemosApi* | [**g_et_debit_memo_items**](docs/DebitMemosApi.md#g_et_debit_memo_items) | **GET** /v1/debitmemos/{debitMemoId}/items | Get debit memo items
*DebitMemosApi* | [**g_et_debit_memos**](docs/DebitMemosApi.md#g_et_debit_memos) | **GET** /v1/debitmemos | Get debit memos
*DebitMemosApi* | [**g_et_taxation_items_of_debit_memo_item**](docs/DebitMemosApi.md#g_et_taxation_items_of_debit_memo_item) | **GET** /v1/debitmemos/{debitMemoId}/items/{dmitemid}/taxation-items | Get taxation items of debit memo item
*DebitMemosApi* | [**p_ost_debit_memo_from_prpc**](docs/DebitMemosApi.md#p_ost_debit_memo_from_prpc) | **POST** /v1/debitmemos | Create debit memo from charge
*DebitMemosApi* | [**p_ost_debit_memo_pdf**](docs/DebitMemosApi.md#p_ost_debit_memo_pdf) | **POST** /v1/debitmemos/{debitMemoId}/pdfs | Create debit memo PDF
*DebitMemosApi* | [**p_ost_email_debit_memo**](docs/DebitMemosApi.md#p_ost_email_debit_memo) | **POST** /v1/debitmemos/{debitMemoId}/emails | Email debit memo
*DebitMemosApi* | [**p_ost_upload_file_for_debit_memo**](docs/DebitMemosApi.md#p_ost_upload_file_for_debit_memo) | **POST** /v1/debitmemos/{debitMemoId}/files | Upload file for debit memo
*DebitMemosApi* | [**p_ostdm_taxation_items**](docs/DebitMemosApi.md#p_ostdm_taxation_items) | **POST** /v1/debitmemos/{debitMemoId}/taxationitems | Create taxation items for debit memo
*DebitMemosApi* | [**p_ut_batch_update_debit_memos**](docs/DebitMemosApi.md#p_ut_batch_update_debit_memos) | **PUT** /v1/debitmemos | Update debit memos
*DebitMemosApi* | [**p_ut_cancel_debit_memo**](docs/DebitMemosApi.md#p_ut_cancel_debit_memo) | **PUT** /v1/debitmemos/{debitMemoId}/cancel | Cancel debit memo
*DebitMemosApi* | [**p_ut_debit_memo**](docs/DebitMemosApi.md#p_ut_debit_memo) | **PUT** /v1/debitmemos/{debitMemoId} | Update debit memo
*DebitMemosApi* | [**p_ut_post_debit_memo**](docs/DebitMemosApi.md#p_ut_post_debit_memo) | **PUT** /v1/debitmemos/{debitMemoId}/post | Post debit memo
*DebitMemosApi* | [**p_ut_unpost_debit_memo**](docs/DebitMemosApi.md#p_ut_unpost_debit_memo) | **PUT** /v1/debitmemos/{debitMemoId}/unpost | Unpost debit memo
*DescribeApi* | [**g_et_describe**](docs/DescribeApi.md#g_et_describe) | **GET** /v1/describe/{object} | Describe object
*DocumentPropertiesApi* | [**d_elete_document_properties**](docs/DocumentPropertiesApi.md#d_elete_document_properties) | **DELETE** /v1/document-properties/{documentPropertiesId} | Delete document properties
*DocumentPropertiesApi* | [**g_et_document_properies**](docs/DocumentPropertiesApi.md#g_et_document_properies) | **GET** /v1/document-properties/{documentType}/{documentId} | Get document properties
*DocumentPropertiesApi* | [**p_ost_document_properties**](docs/DocumentPropertiesApi.md#p_ost_document_properties) | **POST** /v1/document-properties | Create document properties
*DocumentPropertiesApi* | [**p_ut_document_properties**](docs/DocumentPropertiesApi.md#p_ut_document_properties) | **PUT** /v1/document-properties/{documentPropertiesId} | Update document properties
*EntitiesApi* | [**d_elete_entities**](docs/EntitiesApi.md#d_elete_entities) | **DELETE** /v1/entities/{id} | Multi-entity: Delete entity
*EntitiesApi* | [**g_et_entities**](docs/EntitiesApi.md#g_et_entities) | **GET** /v1/entities | Multi-entity: Get entities
*EntitiesApi* | [**g_et_entity_by_id**](docs/EntitiesApi.md#g_et_entity_by_id) | **GET** /v1/entities/{id} | Multi-entity: Get entity by Id
*EntitiesApi* | [**p_ost_entities**](docs/EntitiesApi.md#p_ost_entities) | **POST** /v1/entities | Multi-entity: Create entity
*EntitiesApi* | [**p_ut_entities**](docs/EntitiesApi.md#p_ut_entities) | **PUT** /v1/entities/{id} | Multi-entity: Update entity
*EntitiesApi* | [**p_ut_provision_entity**](docs/EntitiesApi.md#p_ut_provision_entity) | **PUT** /v1/entities/{id}/provision | Multi-entity: Provision entity
*EntityConnectionsApi* | [**g_et_entity_connections**](docs/EntityConnectionsApi.md#g_et_entity_connections) | **GET** /v1/entity-connections | Multi-entity: Get connections
*EntityConnectionsApi* | [**p_ost_entity_connections**](docs/EntityConnectionsApi.md#p_ost_entity_connections) | **POST** /v1/entity-connections | Multi-entity: Initiate connection
*EntityConnectionsApi* | [**p_ut_entity_connections_accept**](docs/EntityConnectionsApi.md#p_ut_entity_connections_accept) | **PUT** /v1/entity-connections/{connection-id}/accept | Multi-entity: Accept connection
*EntityConnectionsApi* | [**p_ut_entity_connections_deny**](docs/EntityConnectionsApi.md#p_ut_entity_connections_deny) | **PUT** /v1/entity-connections/{connection-id}/deny | Multi-entity: Deny connection
*EntityConnectionsApi* | [**p_ut_entity_connections_disconnect**](docs/EntityConnectionsApi.md#p_ut_entity_connections_disconnect) | **PUT** /v1/entity-connections/{connection-id}/disconnect | Multi-entity: Disconnect connection
*EventTriggersApi* | [**d_elete_event_trigger**](docs/EventTriggersApi.md#d_elete_event_trigger) | **DELETE** /events/event-triggers/{id} | Remove an event trigger
*EventTriggersApi* | [**g_et_event_trigger**](docs/EventTriggersApi.md#g_et_event_trigger) | **GET** /events/event-triggers/{id} | Get an event trigger by ID
*EventTriggersApi* | [**g_et_event_triggers**](docs/EventTriggersApi.md#g_et_event_triggers) | **GET** /events/event-triggers | Query event triggers
*EventTriggersApi* | [**p_ost_event_trigger**](docs/EventTriggersApi.md#p_ost_event_trigger) | **POST** /events/event-triggers | Create an event trigger
*EventTriggersApi* | [**p_ut_event_trigger**](docs/EventTriggersApi.md#p_ut_event_trigger) | **PUT** /events/event-triggers/{id} | Update an event trigger
*ExportsApi* | [**object_get_export**](docs/ExportsApi.md#object_get_export) | **GET** /v1/object/export/{id} | CRUD: Retrieve Export
*ExportsApi* | [**object_post_export**](docs/ExportsApi.md#object_post_export) | **POST** /v1/object/export | CRUD: Create Export
*FeaturesApi* | [**object_delete_feature**](docs/FeaturesApi.md#object_delete_feature) | **DELETE** /v1/object/feature/{id} | CRUD: Delete Feature
*FeaturesApi* | [**object_get_feature**](docs/FeaturesApi.md#object_get_feature) | **GET** /v1/object/feature/{id} | CRUD: Retrieve Feature
*GetFilesApi* | [**g_et_files**](docs/GetFilesApi.md#g_et_files) | **GET** /v1/files/{file-id} | Get files
*HMACSignaturesApi* | [**p_osthmac_signatures**](docs/HMACSignaturesApi.md#p_osthmac_signatures) | **POST** /v1/hmac-signatures | Return HMAC signatures
*HostedPagesApi* | [**get_hosted_pages**](docs/HostedPagesApi.md#get_hosted_pages) | **GET** /v1/hostedpages | Return hosted pages
*ImportsApi* | [**object_get_import**](docs/ImportsApi.md#object_get_import) | **GET** /v1/object/import/{id} | CRUD: Retrieve Import
*ImportsApi* | [**object_post_import**](docs/ImportsApi.md#object_post_import) | **POST** /v1/object/import | CRUD: Create Import
*InvoiceAdjustmentsApi* | [**object_delete_invoice_adjustment**](docs/InvoiceAdjustmentsApi.md#object_delete_invoice_adjustment) | **DELETE** /v1/object/invoice-adjustment/{id} | CRUD: Delete InvoiceAdjustment
*InvoiceAdjustmentsApi* | [**object_get_invoice_adjustment**](docs/InvoiceAdjustmentsApi.md#object_get_invoice_adjustment) | **GET** /v1/object/invoice-adjustment/{id} | CRUD: Retrieve InvoiceAdjustment
*InvoiceAdjustmentsApi* | [**object_post_invoice_adjustment**](docs/InvoiceAdjustmentsApi.md#object_post_invoice_adjustment) | **POST** /v1/object/invoice-adjustment | CRUD: Create InvoiceAdjustment
*InvoiceAdjustmentsApi* | [**object_put_invoice_adjustment**](docs/InvoiceAdjustmentsApi.md#object_put_invoice_adjustment) | **PUT** /v1/object/invoice-adjustment/{id} | CRUD: Update InvoiceAdjustment
*InvoiceItemAdjustmentsApi* | [**object_delete_invoice_item_adjustment**](docs/InvoiceItemAdjustmentsApi.md#object_delete_invoice_item_adjustment) | **DELETE** /v1/object/invoice-item-adjustment/{id} | CRUD: Delete InvoiceItemAdjustment
*InvoiceItemAdjustmentsApi* | [**object_get_invoice_item_adjustment**](docs/InvoiceItemAdjustmentsApi.md#object_get_invoice_item_adjustment) | **GET** /v1/object/invoice-item-adjustment/{id} | CRUD: Retrieve InvoiceItemAdjustment
*InvoiceItemsApi* | [**object_get_invoice_item**](docs/InvoiceItemsApi.md#object_get_invoice_item) | **GET** /v1/object/invoice-item/{id} | CRUD: Retrieve InvoiceItem
*InvoicePaymentsApi* | [**object_get_invoice_payment**](docs/InvoicePaymentsApi.md#object_get_invoice_payment) | **GET** /v1/object/invoice-payment/{id} | CRUD: Retrieve InvoicePayment
*InvoicePaymentsApi* | [**object_post_invoice_payment**](docs/InvoicePaymentsApi.md#object_post_invoice_payment) | **POST** /v1/object/invoice-payment | CRUD: Create InvoicePayment
*InvoicePaymentsApi* | [**object_put_invoice_payment**](docs/InvoicePaymentsApi.md#object_put_invoice_payment) | **PUT** /v1/object/invoice-payment/{id} | CRUD: Update InvoicePayment
*InvoiceSplitItemsApi* | [**object_get_invoice_split_item**](docs/InvoiceSplitItemsApi.md#object_get_invoice_split_item) | **GET** /v1/object/invoice-split-item/{id} | CRUD: Retrieve InvoiceSplitItem
*InvoiceSplitsApi* | [**object_get_invoice_split**](docs/InvoiceSplitsApi.md#object_get_invoice_split) | **GET** /v1/object/invoice-split/{id} | CRUD: Retrieve InvoiceSplit
*InvoicesApi* | [**g_et_invoice_application_parts**](docs/InvoicesApi.md#g_et_invoice_application_parts) | **GET** /v1/invoices/{invoiceId}/application-parts | Get invoice application parts
*InvoicesApi* | [**g_et_invoice_files**](docs/InvoicesApi.md#g_et_invoice_files) | **GET** /v1/invoices/{invoiceId}/files | Get invoice files
*InvoicesApi* | [**g_et_invoice_items**](docs/InvoicesApi.md#g_et_invoice_items) | **GET** /v1/invoices/{invoiceId}/items | Get invoice items
*InvoicesApi* | [**g_et_taxation_items_of_invoice_item**](docs/InvoicesApi.md#g_et_taxation_items_of_invoice_item) | **GET** /v1/invoices/{invoiceId}/items/{itemId}/taxation-items | Get taxation items of invoice item
*InvoicesApi* | [**object_delete_invoice**](docs/InvoicesApi.md#object_delete_invoice) | **DELETE** /v1/object/invoice/{id} | CRUD: Delete invoice
*InvoicesApi* | [**object_get_invoice**](docs/InvoicesApi.md#object_get_invoice) | **GET** /v1/object/invoice/{id} | CRUD: Get invoice
*InvoicesApi* | [**object_put_invoice**](docs/InvoicesApi.md#object_put_invoice) | **PUT** /v1/object/invoice/{id} | CRUD: Update invoice
*InvoicesApi* | [**p_ost_credit_memo_from_invoice**](docs/InvoicesApi.md#p_ost_credit_memo_from_invoice) | **POST** /v1/invoices/{invoiceId}/creditmemos | Create credit memo from invoice
*InvoicesApi* | [**p_ost_debit_memo_from_invoice**](docs/InvoicesApi.md#p_ost_debit_memo_from_invoice) | **POST** /v1/invoices/{invoiceId}/debitmemos | Create debit memo from invoice
*InvoicesApi* | [**p_ost_email_invoice**](docs/InvoicesApi.md#p_ost_email_invoice) | **POST** /v1/invoices/{invoiceId}/emails | Email invoice
*InvoicesApi* | [**p_ost_upload_file_for_invoice**](docs/InvoicesApi.md#p_ost_upload_file_for_invoice) | **POST** /v1/invoices/{invoiceId}/files | Upload file for invoice
*InvoicesApi* | [**p_ut_batch_update_invoices**](docs/InvoicesApi.md#p_ut_batch_update_invoices) | **PUT** /v1/invoices | Update invoices
*InvoicesApi* | [**p_ut_reverse_invoice**](docs/InvoicesApi.md#p_ut_reverse_invoice) | **PUT** /v1/invoices/{invoiceId}/reverse | Reverse invoice
*InvoicesApi* | [**p_ut_update_invoice**](docs/InvoicesApi.md#p_ut_update_invoice) | **PUT** /v1/invoices/{invoiceId} | Update invoice
*InvoicesApi* | [**p_ut_write_off_invoice**](docs/InvoicesApi.md#p_ut_write_off_invoice) | **PUT** /v1/invoices/{invoiceId}/write-off | Write off invoice
*JournalRunsApi* | [**d_elete_journal_run**](docs/JournalRunsApi.md#d_elete_journal_run) | **DELETE** /v1/journal-runs/{jr-number} | Delete journal run
*JournalRunsApi* | [**g_et_journal_run**](docs/JournalRunsApi.md#g_et_journal_run) | **GET** /v1/journal-runs/{jr-number} | Get journal run
*JournalRunsApi* | [**p_ost_journal_run**](docs/JournalRunsApi.md#p_ost_journal_run) | **POST** /v1/journal-runs | Create journal run
*JournalRunsApi* | [**p_ut_journal_run**](docs/JournalRunsApi.md#p_ut_journal_run) | **PUT** /v1/journal-runs/{jr-number}/cancel | Cancel journal run
*MassUpdaterApi* | [**g_et_mass_updater**](docs/MassUpdaterApi.md#g_et_mass_updater) | **GET** /v1/bulk/{bulk-key} | Get mass action result
*MassUpdaterApi* | [**p_ost_mass_updater**](docs/MassUpdaterApi.md#p_ost_mass_updater) | **POST** /v1/bulk | Perform mass action
*MassUpdaterApi* | [**p_ut_mass_updater**](docs/MassUpdaterApi.md#p_ut_mass_updater) | **PUT** /v1/bulk/{bulk-key}/stop | Stop mass action
*NotificationsApi* | [**d_elete_delete_email_template**](docs/NotificationsApi.md#d_elete_delete_email_template) | **DELETE** /notifications/email-templates/{id} | Delete an email template
*NotificationsApi* | [**d_elete_delete_notification_definition**](docs/NotificationsApi.md#d_elete_delete_notification_definition) | **DELETE** /notifications/notification-definitions/{id} | Delete a notification definition
*NotificationsApi* | [**g_et_callout_history**](docs/NotificationsApi.md#g_et_callout_history) | **GET** /v1/notification-history/callout | Get callout notification histories
*NotificationsApi* | [**g_et_email_history**](docs/NotificationsApi.md#g_et_email_history) | **GET** /v1/notification-history/email | Get email notification histories
*NotificationsApi* | [**g_et_get_email_template**](docs/NotificationsApi.md#g_et_get_email_template) | **GET** /notifications/email-templates/{id} | Get an email template
*NotificationsApi* | [**g_et_get_notification_definition**](docs/NotificationsApi.md#g_et_get_notification_definition) | **GET** /notifications/notification-definitions/{id} | Get a notification definition
*NotificationsApi* | [**g_et_query_email_templates**](docs/NotificationsApi.md#g_et_query_email_templates) | **GET** /notifications/email-templates | Query email templates
*NotificationsApi* | [**g_et_query_notification_definitions**](docs/NotificationsApi.md#g_et_query_notification_definitions) | **GET** /notifications/notification-definitions | Query notification definitions
*NotificationsApi* | [**p_ost_create_email_template**](docs/NotificationsApi.md#p_ost_create_email_template) | **POST** /notifications/email-templates | Create an email template
*NotificationsApi* | [**p_ost_create_notification_definition**](docs/NotificationsApi.md#p_ost_create_notification_definition) | **POST** /notifications/notification-definitions | Create a notification definition
*NotificationsApi* | [**p_ut_update_email_template**](docs/NotificationsApi.md#p_ut_update_email_template) | **PUT** /notifications/email-templates/{id} | Update an email template
*NotificationsApi* | [**p_ut_update_notification_definition**](docs/NotificationsApi.md#p_ut_update_notification_definition) | **PUT** /notifications/notification-definitions/{id} | Update a notification definition
*OAuthApi* | [**create_token**](docs/OAuthApi.md#create_token) | **POST** /oauth/token | Generate an OAuth token
*OperationsApi* | [**p_ost_billing_preview**](docs/OperationsApi.md#p_ost_billing_preview) | **POST** /v1/operations/billing-preview | Create billing preview
*OperationsApi* | [**p_ost_transaction_invoice_payment**](docs/OperationsApi.md#p_ost_transaction_invoice_payment) | **POST** /v1/operations/invoice-collect | Invoice and collect
*OrdersApi* | [**d_elete_order**](docs/OrdersApi.md#d_elete_order) | **DELETE** /v1/orders/{orderNumber} | Delete order
*OrdersApi* | [**g_et_all_orders**](docs/OrdersApi.md#g_et_all_orders) | **GET** /v1/orders | Get all orders
*OrdersApi* | [**g_et_breakdown_invoice_by_order**](docs/OrdersApi.md#g_et_breakdown_invoice_by_order) | **GET** /v1/invoices/{invoiceNumber}/amountBreakdownByOrder | Get breakdown of invoice by order
*OrdersApi* | [**g_et_job_status_and_response**](docs/OrdersApi.md#g_et_job_status_and_response) | **GET** /v1/async-jobs/{jobId} | Get job status and response
*OrdersApi* | [**g_et_order**](docs/OrdersApi.md#g_et_order) | **GET** /v1/orders/{orderNumber} | Get an order
*OrdersApi* | [**g_et_order_billing_info**](docs/OrdersApi.md#g_et_order_billing_info) | **GET** /v1/orders/{orderNumber}/billingInfo | Get billing information for order
*OrdersApi* | [**g_et_order_metricsfor_evergreen_subscription**](docs/OrdersApi.md#g_et_order_metricsfor_evergreen_subscription) | **GET** /v1/orders/{orderNumber}/evergreenMetrics/{subscriptionNumber} | Get order metrics for evergreen subscription
*OrdersApi* | [**g_et_order_rated_result**](docs/OrdersApi.md#g_et_order_rated_result) | **GET** /v1/orders/{orderNumber}/ratedResults | Get rated result for order
*OrdersApi* | [**g_et_orders_by_invoice_owner**](docs/OrdersApi.md#g_et_orders_by_invoice_owner) | **GET** /v1/orders/invoiceOwner/{accountNumber} | Get orders by invoice owner
*OrdersApi* | [**g_et_orders_by_subscription_number**](docs/OrdersApi.md#g_et_orders_by_subscription_number) | **GET** /v1/orders/subscription/{subscriptionNumber} | Get orders by subscription number
*OrdersApi* | [**g_et_orders_by_subscription_owner**](docs/OrdersApi.md#g_et_orders_by_subscription_owner) | **GET** /v1/orders/subscriptionOwner/{accountNumber} | Get orders by subscription owner
*OrdersApi* | [**g_et_subscription_term_info**](docs/OrdersApi.md#g_et_subscription_term_info) | **GET** /v1/orders/term/{subscriptionNumber} | Get term information for subscription
*OrdersApi* | [**p_ost_create_order_asynchronously**](docs/OrdersApi.md#p_ost_create_order_asynchronously) | **POST** /v1/async/orders | Create order asynchronously
*OrdersApi* | [**p_ost_order**](docs/OrdersApi.md#p_ost_order) | **POST** /v1/orders | Create order
*OrdersApi* | [**p_ost_preview_order**](docs/OrdersApi.md#p_ost_preview_order) | **POST** /v1/orders/preview | Preview order
*OrdersApi* | [**p_ost_preview_order_asynchronously**](docs/OrdersApi.md#p_ost_preview_order_asynchronously) | **POST** /v1/async/orders/preview | Preview order asynchronously
*OrdersApi* | [**p_ost_request_breakdown_invoice_items_by_order**](docs/OrdersApi.md#p_ost_request_breakdown_invoice_items_by_order) | **POST** /v1/invoices/items/amountBreakdownByOrder | Request breakdown of invoice items by order
*OrdersApi* | [**p_ut_order_trigger_dates**](docs/OrdersApi.md#p_ut_order_trigger_dates) | **PUT** /v1/orders/{orderNumber}/triggerDates | Update order action trigger dates
*OrdersApi* | [**p_ut_update_order_custom_fields**](docs/OrdersApi.md#p_ut_update_order_custom_fields) | **PUT** /v1/orders/{orderNumber}/customFields | Update order custom fields
*OrdersApi* | [**p_ut_update_subscription_custom_fields**](docs/OrdersApi.md#p_ut_update_subscription_custom_fields) | **PUT** /v1/subscriptions/{subscriptionNumber}/customFields | Update subscription custom fields
*PaymentGatewayReconciliationApi* | [**p_ost_reject_payment**](docs/PaymentGatewayReconciliationApi.md#p_ost_reject_payment) | **POST** /v1/gateway-settlement/payments/{payment-id}/reject | Reject Payment
*PaymentGatewayReconciliationApi* | [**p_ost_reverse_payment**](docs/PaymentGatewayReconciliationApi.md#p_ost_reverse_payment) | **POST** /v1/gateway-settlement/payments/{payment-id}/chargeback | Reverse Payment
*PaymentGatewayReconciliationApi* | [**p_ost_settle_payment**](docs/PaymentGatewayReconciliationApi.md#p_ost_settle_payment) | **POST** /v1/gateway-settlement/payments/{payment-id}/settle | Settle Payment
*PaymentGatewaysApi* | [**g_et_paymentgateways**](docs/PaymentGatewaysApi.md#g_et_paymentgateways) | **GET** /v1/paymentgateways | Get payment gateways
*PaymentMethodSnapshotsApi* | [**object_delete_payment_method_snapshot**](docs/PaymentMethodSnapshotsApi.md#object_delete_payment_method_snapshot) | **DELETE** /v1/object/payment-method-snapshot/{id} | CRUD: Delete payment method snapshot
*PaymentMethodSnapshotsApi* | [**object_get_payment_method_snapshot**](docs/PaymentMethodSnapshotsApi.md#object_get_payment_method_snapshot) | **GET** /v1/object/payment-method-snapshot/{id} | CRUD: Get payment method snapshot
*PaymentMethodTransactionLogsApi* | [**object_get_payment_method_transaction_log**](docs/PaymentMethodTransactionLogsApi.md#object_get_payment_method_transaction_log) | **GET** /v1/object/payment-method-transaction-log/{id} | CRUD: Retrieve PaymentMethodTransactionLog
*PaymentMethodsApi* | [**d_elete_payment_methods**](docs/PaymentMethodsApi.md#d_elete_payment_methods) | **DELETE** /v1/payment-methods/{payment-method-id} | Delete payment method
*PaymentMethodsApi* | [**g_et_payment_methods_credit_card**](docs/PaymentMethodsApi.md#g_et_payment_methods_credit_card) | **GET** /v1/payment-methods/credit-cards/accounts/{account-key} | Get credit card payment methods for account
*PaymentMethodsApi* | [**g_et_stored_credential_profiles**](docs/PaymentMethodsApi.md#g_et_stored_credential_profiles) | **GET** /v1/payment-methods/{payment-method-id}/profiles | Get stored credential profiles
*PaymentMethodsApi* | [**object_delete_payment_method**](docs/PaymentMethodsApi.md#object_delete_payment_method) | **DELETE** /v1/object/payment-method/{id} | CRUD: Delete payment method
*PaymentMethodsApi* | [**object_get_payment_method**](docs/PaymentMethodsApi.md#object_get_payment_method) | **GET** /v1/object/payment-method/{id} | CRUD: Get payment method
*PaymentMethodsApi* | [**object_post_payment_method**](docs/PaymentMethodsApi.md#object_post_payment_method) | **POST** /v1/object/payment-method | CRUD: Create payment method
*PaymentMethodsApi* | [**object_put_payment_method**](docs/PaymentMethodsApi.md#object_put_payment_method) | **PUT** /v1/object/payment-method/{id} | CRUD: Update payment method
*PaymentMethodsApi* | [**p_ost_cancel_authorization**](docs/PaymentMethodsApi.md#p_ost_cancel_authorization) | **POST** /v1/payment-methods/{payment-method-id}/voidAuthorize | Cancel authorization
*PaymentMethodsApi* | [**p_ost_cancel_stored_credential_profile**](docs/PaymentMethodsApi.md#p_ost_cancel_stored_credential_profile) | **POST** /v1/payment-methods/{payment-method-id}/profiles/{profile-number}/cancel | Cancel stored credential profile
*PaymentMethodsApi* | [**p_ost_create_authorization**](docs/PaymentMethodsApi.md#p_ost_create_authorization) | **POST** /v1/payment-methods/{payment-method-id}/authorize | Create authorization
*PaymentMethodsApi* | [**p_ost_create_stored_credential_profile**](docs/PaymentMethodsApi.md#p_ost_create_stored_credential_profile) | **POST** /v1/payment-methods/{payment-method-id}/profiles | Create stored credential profile
*PaymentMethodsApi* | [**p_ost_expire_stored_credential_profile**](docs/PaymentMethodsApi.md#p_ost_expire_stored_credential_profile) | **POST** /v1/payment-methods/{payment-method-id}/profiles/{profile-number}/expire | Expire stored credential profile
*PaymentMethodsApi* | [**p_ost_payment_methods**](docs/PaymentMethodsApi.md#p_ost_payment_methods) | **POST** /v1/payment-methods | Create payment method
*PaymentMethodsApi* | [**p_ost_payment_methods_credit_card**](docs/PaymentMethodsApi.md#p_ost_payment_methods_credit_card) | **POST** /v1/payment-methods/credit-cards | Create credit card payment method
*PaymentMethodsApi* | [**p_ost_payment_methods_decryption**](docs/PaymentMethodsApi.md#p_ost_payment_methods_decryption) | **POST** /v1/payment-methods/decryption | Create Apple Pay payment method
*PaymentMethodsApi* | [**p_ut_payment_methods_credit_card**](docs/PaymentMethodsApi.md#p_ut_payment_methods_credit_card) | **PUT** /v1/payment-methods/credit-cards/{payment-method-id} | Update credit card payment method
*PaymentMethodsApi* | [**p_ut_scrub_payment_methods**](docs/PaymentMethodsApi.md#p_ut_scrub_payment_methods) | **PUT** /v1/payment-methods/{payment-method-id}/scrub | Scrub payment method
*PaymentMethodsApi* | [**p_ut_verify_payment_methods**](docs/PaymentMethodsApi.md#p_ut_verify_payment_methods) | **PUT** /v1/payment-methods/{payment-method-id}/verify | Verify payment method
*PaymentRunsApi* | [**d_elete_payment_run**](docs/PaymentRunsApi.md#d_elete_payment_run) | **DELETE** /v1/payment-runs/{paymentRunId} | Delete payment run
*PaymentRunsApi* | [**g_et_payment_run**](docs/PaymentRunsApi.md#g_et_payment_run) | **GET** /v1/payment-runs/{paymentRunId} | Get payment run
*PaymentRunsApi* | [**g_et_payment_run_summary**](docs/PaymentRunsApi.md#g_et_payment_run_summary) | **GET** /v1/payment-runs/{paymentRunId}/summary | Get payment run summary
*PaymentRunsApi* | [**g_et_payment_runs**](docs/PaymentRunsApi.md#g_et_payment_runs) | **GET** /v1/payment-runs | Get payment runs
*PaymentRunsApi* | [**p_ost_payment_run**](docs/PaymentRunsApi.md#p_ost_payment_run) | **POST** /v1/payment-runs | Create payment run
*PaymentRunsApi* | [**p_ut_payment_run**](docs/PaymentRunsApi.md#p_ut_payment_run) | **PUT** /v1/payment-runs/{paymentRunId} | Update payment run
*PaymentTransactionLogsApi* | [**object_get_payment_transaction_log**](docs/PaymentTransactionLogsApi.md#object_get_payment_transaction_log) | **GET** /v1/object/payment-transaction-log/{id} | CRUD: Get payment transaction log
*PaymentsApi* | [**d_elete_payment**](docs/PaymentsApi.md#d_elete_payment) | **DELETE** /v1/payments/{paymentId} | Delete payment
*PaymentsApi* | [**g_et_payment**](docs/PaymentsApi.md#g_et_payment) | **GET** /v1/payments/{paymentId} | Get payment
*PaymentsApi* | [**g_et_payment_item_part**](docs/PaymentsApi.md#g_et_payment_item_part) | **GET** /v1/payments/{paymentId}/parts/{partid}/itemparts/{itempartid} | Get payment part item
*PaymentsApi* | [**g_et_payment_item_parts**](docs/PaymentsApi.md#g_et_payment_item_parts) | **GET** /v1/payments/{paymentId}/parts/{partid}/itemparts | Get payment part items
*PaymentsApi* | [**g_et_payment_part**](docs/PaymentsApi.md#g_et_payment_part) | **GET** /v1/payments/{paymentId}/parts/{partid} | Get payment part
*PaymentsApi* | [**g_et_payment_parts**](docs/PaymentsApi.md#g_et_payment_parts) | **GET** /v1/payments/{paymentId}/parts | Get payment parts
*PaymentsApi* | [**g_et_retrieve_all_payments**](docs/PaymentsApi.md#g_et_retrieve_all_payments) | **GET** /v1/payments | Get all payments
*PaymentsApi* | [**object_delete_payment**](docs/PaymentsApi.md#object_delete_payment) | **DELETE** /v1/object/payment/{id} | CRUD: Delete payment
*PaymentsApi* | [**object_get_payment**](docs/PaymentsApi.md#object_get_payment) | **GET** /v1/object/payment/{id} | CRUD: Get payment
*PaymentsApi* | [**object_post_payment**](docs/PaymentsApi.md#object_post_payment) | **POST** /v1/object/payment | CRUD: Create payment
*PaymentsApi* | [**object_put_payment**](docs/PaymentsApi.md#object_put_payment) | **PUT** /v1/object/payment/{id} | CRUD: Update payment
*PaymentsApi* | [**p_ost_create_payment**](docs/PaymentsApi.md#p_ost_create_payment) | **POST** /v1/payments | Create payment
*PaymentsApi* | [**p_ost_refund_payment**](docs/PaymentsApi.md#p_ost_refund_payment) | **POST** /v1/payments/{paymentId}/refunds | Refund payment
*PaymentsApi* | [**p_ut_apply_payment**](docs/PaymentsApi.md#p_ut_apply_payment) | **PUT** /v1/payments/{paymentId}/apply | Apply payment
*PaymentsApi* | [**p_ut_cancel_payment**](docs/PaymentsApi.md#p_ut_cancel_payment) | **PUT** /v1/payments/{paymentId}/cancel | Cancel payment
*PaymentsApi* | [**p_ut_transfer_payment**](docs/PaymentsApi.md#p_ut_transfer_payment) | **PUT** /v1/payments/{paymentId}/transfer | Transfer payment
*PaymentsApi* | [**p_ut_unapply_payment**](docs/PaymentsApi.md#p_ut_unapply_payment) | **PUT** /v1/payments/{paymentId}/unapply | Unapply payment
*PaymentsApi* | [**p_ut_update_payment**](docs/PaymentsApi.md#p_ut_update_payment) | **PUT** /v1/payments/{paymentId} | Update payment
*ProductFeaturesApi* | [**object_delete_product_feature**](docs/ProductFeaturesApi.md#object_delete_product_feature) | **DELETE** /v1/object/product-feature/{id} | CRUD: Delete ProductFeature
*ProductFeaturesApi* | [**object_get_product_feature**](docs/ProductFeaturesApi.md#object_get_product_feature) | **GET** /v1/object/product-feature/{id} | CRUD: Retrieve ProductFeature
*ProductRatePlanChargeTiersApi* | [**object_get_product_rate_plan_charge_tier**](docs/ProductRatePlanChargeTiersApi.md#object_get_product_rate_plan_charge_tier) | **GET** /v1/object/product-rate-plan-charge-tier/{id} | CRUD: Retrieve ProductRatePlanChargeTier
*ProductRatePlanChargesApi* | [**object_delete_product_rate_plan_charge**](docs/ProductRatePlanChargesApi.md#object_delete_product_rate_plan_charge) | **DELETE** /v1/object/product-rate-plan-charge/{id} | CRUD: Delete product rate plan charge
*ProductRatePlanChargesApi* | [**object_get_product_rate_plan_charge**](docs/ProductRatePlanChargesApi.md#object_get_product_rate_plan_charge) | **GET** /v1/object/product-rate-plan-charge/{id} | CRUD: Get product rate plan charge
*ProductRatePlanChargesApi* | [**object_post_product_rate_plan_charge**](docs/ProductRatePlanChargesApi.md#object_post_product_rate_plan_charge) | **POST** /v1/object/product-rate-plan-charge | CRUD: Create product rate plan charge
*ProductRatePlanChargesApi* | [**object_put_product_rate_plan_charge**](docs/ProductRatePlanChargesApi.md#object_put_product_rate_plan_charge) | **PUT** /v1/object/product-rate-plan-charge/{id} | CRUD: Update product rate plan charge
*ProductRatePlansApi* | [**g_et_product_rate_plans**](docs/ProductRatePlansApi.md#g_et_product_rate_plans) | **GET** /v1/rateplan/{product_id}/productRatePlan | Get product rate plans
*ProductRatePlansApi* | [**object_delete_product_rate_plan**](docs/ProductRatePlansApi.md#object_delete_product_rate_plan) | **DELETE** /v1/object/product-rate-plan/{id} | CRUD: Delete ProductRatePlan
*ProductRatePlansApi* | [**object_get_product_rate_plan**](docs/ProductRatePlansApi.md#object_get_product_rate_plan) | **GET** /v1/object/product-rate-plan/{id} | CRUD: Retrieve ProductRatePlan
*ProductRatePlansApi* | [**object_post_product_rate_plan**](docs/ProductRatePlansApi.md#object_post_product_rate_plan) | **POST** /v1/object/product-rate-plan | CRUD: Create ProductRatePlan
*ProductRatePlansApi* | [**object_put_product_rate_plan**](docs/ProductRatePlansApi.md#object_put_product_rate_plan) | **PUT** /v1/object/product-rate-plan/{id} | CRUD: Update ProductRatePlan
*ProductsApi* | [**object_delete_product**](docs/ProductsApi.md#object_delete_product) | **DELETE** /v1/object/product/{id} | CRUD: Delete Product
*ProductsApi* | [**object_get_product**](docs/ProductsApi.md#object_get_product) | **GET** /v1/object/product/{id} | CRUD: Retrieve Product
*ProductsApi* | [**object_post_product**](docs/ProductsApi.md#object_post_product) | **POST** /v1/object/product | CRUD: Create Product
*ProductsApi* | [**object_put_product**](docs/ProductsApi.md#object_put_product) | **PUT** /v1/object/product/{id} | CRUD: Update Product
*QuotesDocumentApi* | [**p_ost_quotes_document**](docs/QuotesDocumentApi.md#p_ost_quotes_document) | **POST** /v1/quotes/document | Generate quotes document
*RSASignaturesApi* | [**p_ost_decrypt_rsa_signatures**](docs/RSASignaturesApi.md#p_ost_decrypt_rsa_signatures) | **POST** /v1/rsa-signatures/decrypt | Decrypt RSA signature
*RSASignaturesApi* | [**p_ostrsa_signatures**](docs/RSASignaturesApi.md#p_ostrsa_signatures) | **POST** /v1/rsa-signatures | Generate RSA signature
*RatePlanChargeTiersApi* | [**object_get_rate_plan_charge_tier**](docs/RatePlanChargeTiersApi.md#object_get_rate_plan_charge_tier) | **GET** /v1/object/rate-plan-charge-tier/{id} | CRUD: Retrieve RatePlanChargeTier
*RatePlanChargesApi* | [**object_get_rate_plan_charge**](docs/RatePlanChargesApi.md#object_get_rate_plan_charge) | **GET** /v1/object/rate-plan-charge/{id} | CRUD: Get rate plan charge
*RatePlansApi* | [**object_get_rate_plan**](docs/RatePlansApi.md#object_get_rate_plan) | **GET** /v1/object/rate-plan/{id} | CRUD: Retrieve RatePlan
*RefundInvoicePaymentsApi* | [**object_get_refund_invoice_payment**](docs/RefundInvoicePaymentsApi.md#object_get_refund_invoice_payment) | **GET** /v1/object/refund-invoice-payment/{id} | CRUD: Retrieve RefundInvoicePayment
*RefundTransactionLogsApi* | [**object_get_refund_transaction_log**](docs/RefundTransactionLogsApi.md#object_get_refund_transaction_log) | **GET** /v1/object/refund-transaction-log/{id} | CRUD: Retrieve RefundTransactionLog
*RefundsApi* | [**d_elete_refund**](docs/RefundsApi.md#d_elete_refund) | **DELETE** /v1/refunds/{refundId} | Delete refund
*RefundsApi* | [**g_et_refund**](docs/RefundsApi.md#g_et_refund) | **GET** /v1/refunds/{refundId} | Get refund
*RefundsApi* | [**g_et_refund_item_part**](docs/RefundsApi.md#g_et_refund_item_part) | **GET** /v1/refunds/{refundId}/parts/{refundpartid}/itemparts/{itempartid} | Get refund part item
*RefundsApi* | [**g_et_refund_item_parts**](docs/RefundsApi.md#g_et_refund_item_parts) | **GET** /v1/refunds/{refundId}/parts/{refundpartid}/itemparts | Get refund part items
*RefundsApi* | [**g_et_refund_part**](docs/RefundsApi.md#g_et_refund_part) | **GET** /v1/refunds/{refundId}/parts/{refundpartid} | Get refund part
*RefundsApi* | [**g_et_refund_parts**](docs/RefundsApi.md#g_et_refund_parts) | **GET** /v1/refunds/{refundId}/parts | Get refund parts
*RefundsApi* | [**g_et_refunds**](docs/RefundsApi.md#g_et_refunds) | **GET** /v1/refunds | Get all refunds
*RefundsApi* | [**object_delete_refund**](docs/RefundsApi.md#object_delete_refund) | **DELETE** /v1/object/refund/{id} | CRUD: Delete refund
*RefundsApi* | [**object_get_refund**](docs/RefundsApi.md#object_get_refund) | **GET** /v1/object/refund/{id} | CRUD: Get refund
*RefundsApi* | [**object_post_refund**](docs/RefundsApi.md#object_post_refund) | **POST** /v1/object/refund | CRUD: Create refund
*RefundsApi* | [**object_put_refund**](docs/RefundsApi.md#object_put_refund) | **PUT** /v1/object/refund/{id} | CRUD: Update refund
*RefundsApi* | [**p_ut_cancel_refund**](docs/RefundsApi.md#p_ut_cancel_refund) | **PUT** /v1/refunds/{refundId}/cancel | Cancel refund
*RefundsApi* | [**p_ut_update_refund**](docs/RefundsApi.md#p_ut_update_refund) | **PUT** /v1/refunds/{refundId} | Update refund
*RevenueEventsApi* | [**g_et_revenue_event_details**](docs/RevenueEventsApi.md#g_et_revenue_event_details) | **GET** /v1/revenue-events/{event-number} | Get revenue event details
*RevenueEventsApi* | [**g_et_revenue_event_for_revenue_schedule**](docs/RevenueEventsApi.md#g_et_revenue_event_for_revenue_schedule) | **GET** /v1/revenue-events/revenue-schedules/{rs-number} | Get revenue events for a revenue schedule
*RevenueItemsApi* | [**g_et_revenue_items_by_charge_revenue_event_number**](docs/RevenueItemsApi.md#g_et_revenue_items_by_charge_revenue_event_number) | **GET** /v1/revenue-items/revenue-events/{event-number} | Get revenue items by revenue event number
*RevenueItemsApi* | [**g_et_revenue_items_by_charge_revenue_summary_number**](docs/RevenueItemsApi.md#g_et_revenue_items_by_charge_revenue_summary_number) | **GET** /v1/revenue-items/charge-revenue-summaries/{crs-number} | Get revenue items by charge revenue summary number
*RevenueItemsApi* | [**g_et_revenue_items_by_revenue_schedule**](docs/RevenueItemsApi.md#g_et_revenue_items_by_revenue_schedule) | **GET** /v1/revenue-items/revenue-schedules/{rs-number} | Get revenue items by revenue schedule
*RevenueItemsApi* | [**p_ut_custom_fieldson_revenue_items_by_revenue_event**](docs/RevenueItemsApi.md#p_ut_custom_fieldson_revenue_items_by_revenue_event) | **PUT** /v1/revenue-items/revenue-events/{event-number} | Update custom fields on revenue items by revenue event number
*RevenueItemsApi* | [**p_ut_custom_fieldson_revenue_items_by_revenue_schedule**](docs/RevenueItemsApi.md#p_ut_custom_fieldson_revenue_items_by_revenue_schedule) | **PUT** /v1/revenue-items/revenue-schedules/{rs-number} | Update custom fields on revenue items by revenue schedule number
*RevenueRulesApi* | [**g_et_revenue_rec_ruleby_product_rate_plan_charge**](docs/RevenueRulesApi.md#g_et_revenue_rec_ruleby_product_rate_plan_charge) | **GET** /v1/revenue-recognition-rules/product-charges/{charge-key} | Get revenue recognition rule by product rate plan charge
*RevenueRulesApi* | [**g_et_revenue_rec_rules**](docs/RevenueRulesApi.md#g_et_revenue_rec_rules) | **GET** /v1/revenue-recognition-rules/subscription-charges/{charge-key} | Get revenue recognition rule by subscription charge
*RevenueSchedulesApi* | [**d_eleters**](docs/RevenueSchedulesApi.md#d_eleters) | **DELETE** /v1/revenue-schedules/{rs-number} | Delete revenue schedule
*RevenueSchedulesApi* | [**g_etr_sby_credit_memo_item**](docs/RevenueSchedulesApi.md#g_etr_sby_credit_memo_item) | **GET** /v1/revenue-schedules/credit-memo-items/{cmi-id} | Get revenue schedule by credit memo item ID 
*RevenueSchedulesApi* | [**g_etr_sby_debit_memo_item**](docs/RevenueSchedulesApi.md#g_etr_sby_debit_memo_item) | **GET** /v1/revenue-schedules/debit-memo-items/{dmi-id} | Get revenue schedule by debit memo item ID 
*RevenueSchedulesApi* | [**g_etr_sby_invoice_item**](docs/RevenueSchedulesApi.md#g_etr_sby_invoice_item) | **GET** /v1/revenue-schedules/invoice-items/{invoice-item-id} | Get revenue schedule by invoice item ID
*RevenueSchedulesApi* | [**g_etr_sby_invoice_item_adjustment**](docs/RevenueSchedulesApi.md#g_etr_sby_invoice_item_adjustment) | **GET** /v1/revenue-schedules/invoice-item-adjustments/{invoice-item-adj-key} | Get revenue schedule by invoice item adjustment
*RevenueSchedulesApi* | [**g_etr_sby_product_charge_and_billing_account**](docs/RevenueSchedulesApi.md#g_etr_sby_product_charge_and_billing_account) | **GET** /v1/revenue-schedules/product-charges/{charge-key}/{account-key} | Get all revenue schedules of product charge by charge ID and billing account ID 
*RevenueSchedulesApi* | [**g_etr_sfor_subsc_charge**](docs/RevenueSchedulesApi.md#g_etr_sfor_subsc_charge) | **GET** /v1/revenue-schedules/subscription-charges/{charge-key} | Get revenue schedule by subscription charge
*RevenueSchedulesApi* | [**g_etrs**](docs/RevenueSchedulesApi.md#g_etrs) | **GET** /v1/revenue-schedules/{rs-number} | Get revenue schedule details
*RevenueSchedulesApi* | [**p_ostr_sfor_credit_memo_item_distribute_by_date_range**](docs/RevenueSchedulesApi.md#p_ostr_sfor_credit_memo_item_distribute_by_date_range) | **POST** /v1/revenue-schedules/credit-memo-items/{cmi-id}/distribute-revenue-with-date-range | Create revenue schedule for credit memo item (distribute by date range) 
*RevenueSchedulesApi* | [**p_ostr_sfor_credit_memo_item_manual_distribution**](docs/RevenueSchedulesApi.md#p_ostr_sfor_credit_memo_item_manual_distribution) | **POST** /v1/revenue-schedules/credit-memo-items/{cmi-id} | Create revenue schedule for credit memo item (manual distribution) 
*RevenueSchedulesApi* | [**p_ostr_sfor_debit_memo_item_distribute_by_date_range**](docs/RevenueSchedulesApi.md#p_ostr_sfor_debit_memo_item_distribute_by_date_range) | **POST** /v1/revenue-schedules/debit-memo-items/{dmi-id}/distribute-revenue-with-date-range | Create revenue schedule for debit memo item (distribute by date range) 
*RevenueSchedulesApi* | [**p_ostr_sfor_debit_memo_item_manual_distribution**](docs/RevenueSchedulesApi.md#p_ostr_sfor_debit_memo_item_manual_distribution) | **POST** /v1/revenue-schedules/debit-memo-items/{dmi-id} | Create revenue schedule for debit memo item (manual distribution) 
*RevenueSchedulesApi* | [**p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range**](docs/RevenueSchedulesApi.md#p_ostr_sfor_invoice_item_adjustment_distribute_by_date_range) | **POST** /v1/revenue-schedules/invoice-item-adjustments/{invoice-item-adj-key}/distribute-revenue-with-date-range | Create revenue schedule for Invoice Item Adjustment (distribute by date range)
*RevenueSchedulesApi* | [**p_ostr_sfor_invoice_item_adjustment_manual_distribution**](docs/RevenueSchedulesApi.md#p_ostr_sfor_invoice_item_adjustment_manual_distribution) | **POST** /v1/revenue-schedules/invoice-item-adjustments/{invoice-item-adj-key} | Create revenue schedule for Invoice Item Adjustment (manual distribution)
*RevenueSchedulesApi* | [**p_ostr_sfor_invoice_item_distribute_by_date_range**](docs/RevenueSchedulesApi.md#p_ostr_sfor_invoice_item_distribute_by_date_range) | **POST** /v1/revenue-schedules/invoice-items/{invoice-item-id}/distribute-revenue-with-date-range | Create revenue schedule for Invoice Item (distribute by date range)
*RevenueSchedulesApi* | [**p_ostr_sfor_invoice_item_manual_distribution**](docs/RevenueSchedulesApi.md#p_ostr_sfor_invoice_item_manual_distribution) | **POST** /v1/revenue-schedules/invoice-items/{invoice-item-id} | Create revenue schedule for Invoice Item (manual distribution)
*RevenueSchedulesApi* | [**p_ostr_sfor_subsc_charge**](docs/RevenueSchedulesApi.md#p_ostr_sfor_subsc_charge) | **POST** /v1/revenue-schedules/subscription-charges/{charge-key} | Create revenue schedule on subscription charge
*RevenueSchedulesApi* | [**p_ut_revenue_across_ap**](docs/RevenueSchedulesApi.md#p_ut_revenue_across_ap) | **PUT** /v1/revenue-schedules/{rs-number}/distribute-revenue-across-accounting-periods | Distribute revenue across accounting periods
*RevenueSchedulesApi* | [**p_ut_revenue_by_recognition_startand_end_dates**](docs/RevenueSchedulesApi.md#p_ut_revenue_by_recognition_startand_end_dates) | **PUT** /v1/revenue-schedules/{rs-number}/distribute-revenue-with-date-range | Distribute revenue by recognition start and end dates
*RevenueSchedulesApi* | [**p_ut_revenue_specific_date**](docs/RevenueSchedulesApi.md#p_ut_revenue_specific_date) | **PUT** /v1/revenue-schedules/{rs-number}/distribute-revenue-on-specific-date | Distribute revenue on specific date
*RevenueSchedulesApi* | [**p_utrs_basic_info**](docs/RevenueSchedulesApi.md#p_utrs_basic_info) | **PUT** /v1/revenue-schedules/{rs-number}/basic-information | Update revenue schedule basic information
*SequenceSetsApi* | [**d_elete_sequence_set**](docs/SequenceSetsApi.md#d_elete_sequence_set) | **DELETE** /v1/sequence-sets/{id} | Delete sequence set
*SequenceSetsApi* | [**g_et_sequence_set**](docs/SequenceSetsApi.md#g_et_sequence_set) | **GET** /v1/sequence-sets/{id} | Get sequence set
*SequenceSetsApi* | [**g_et_sequence_sets**](docs/SequenceSetsApi.md#g_et_sequence_sets) | **GET** /v1/sequence-sets | Get sequence sets
*SequenceSetsApi* | [**p_ost_sequence_sets**](docs/SequenceSetsApi.md#p_ost_sequence_sets) | **POST** /v1/sequence-sets | Create sequence sets
*SequenceSetsApi* | [**p_ut_sequence_set**](docs/SequenceSetsApi.md#p_ut_sequence_set) | **PUT** /v1/sequence-sets/{id} | Update sequence set
*SettingsApi* | [**g_et_revenue_automation_start_date**](docs/SettingsApi.md#g_et_revenue_automation_start_date) | **GET** /v1/settings/finance/revenue-automation-start-date | Get the revenue automation start date
*SubscriptionProductFeaturesApi* | [**object_get_subscription_product_feature**](docs/SubscriptionProductFeaturesApi.md#object_get_subscription_product_feature) | **GET** /v1/object/subscription-product-feature/{id} | CRUD: Retrieve SubscriptionProductFeature
*SubscriptionsApi* | [**g_et_subscriptions_by_account**](docs/SubscriptionsApi.md#g_et_subscriptions_by_account) | **GET** /v1/subscriptions/accounts/{account-key} | Get subscriptions by account
*SubscriptionsApi* | [**g_et_subscriptions_by_key**](docs/SubscriptionsApi.md#g_et_subscriptions_by_key) | **GET** /v1/subscriptions/{subscription-key} | Get subscriptions by key
*SubscriptionsApi* | [**g_et_subscriptions_by_key_and_version**](docs/SubscriptionsApi.md#g_et_subscriptions_by_key_and_version) | **GET** /v1/subscriptions/{subscription-key}/versions/{version} | Get subscriptions by key and version
*SubscriptionsApi* | [**object_delete_subscription**](docs/SubscriptionsApi.md#object_delete_subscription) | **DELETE** /v1/object/subscription/{id} | CRUD: Delete Subscription
*SubscriptionsApi* | [**object_get_subscription**](docs/SubscriptionsApi.md#object_get_subscription) | **GET** /v1/object/subscription/{id} | CRUD: Retrieve Subscription
*SubscriptionsApi* | [**object_put_subscription**](docs/SubscriptionsApi.md#object_put_subscription) | **PUT** /v1/object/subscription/{id} | CRUD: Update Subscription
*SubscriptionsApi* | [**p_ost_preview_subscription**](docs/SubscriptionsApi.md#p_ost_preview_subscription) | **POST** /v1/subscriptions/preview | Preview subscription
*SubscriptionsApi* | [**p_ost_subscription**](docs/SubscriptionsApi.md#p_ost_subscription) | **POST** /v1/subscriptions | Create subscription
*SubscriptionsApi* | [**p_ut_cancel_subscription**](docs/SubscriptionsApi.md#p_ut_cancel_subscription) | **PUT** /v1/subscriptions/{subscription-key}/cancel | Cancel subscription
*SubscriptionsApi* | [**p_ut_renew_subscription**](docs/SubscriptionsApi.md#p_ut_renew_subscription) | **PUT** /v1/subscriptions/{subscription-key}/renew | Renew subscription
*SubscriptionsApi* | [**p_ut_resume_subscription**](docs/SubscriptionsApi.md#p_ut_resume_subscription) | **PUT** /v1/subscriptions/{subscription-key}/resume | Resume subscription
*SubscriptionsApi* | [**p_ut_subscription**](docs/SubscriptionsApi.md#p_ut_subscription) | **PUT** /v1/subscriptions/{subscription-key} | Update subscription
*SubscriptionsApi* | [**p_ut_suspend_subscription**](docs/SubscriptionsApi.md#p_ut_suspend_subscription) | **PUT** /v1/subscriptions/{subscription-key}/suspend | Suspend subscription
*SummaryJournalEntriesApi* | [**d_elete_summary_journal_entry**](docs/SummaryJournalEntriesApi.md#d_elete_summary_journal_entry) | **DELETE** /v1/journal-entries/{je-number} | Delete summary journal entry
*SummaryJournalEntriesApi* | [**g_et_all_summary_journal_entries**](docs/SummaryJournalEntriesApi.md#g_et_all_summary_journal_entries) | **GET** /v1/journal-entries/journal-runs/{jr-number} | Get all summary journal entries in a journal run
*SummaryJournalEntriesApi* | [**g_et_summary_journal_entry**](docs/SummaryJournalEntriesApi.md#g_et_summary_journal_entry) | **GET** /v1/journal-entries/{je-number} | Get summary journal entry
*SummaryJournalEntriesApi* | [**p_ost_summary_journal_entry**](docs/SummaryJournalEntriesApi.md#p_ost_summary_journal_entry) | **POST** /v1/journal-entries | Create summary journal entry
*SummaryJournalEntriesApi* | [**p_ut_basic_summary_journal_entry**](docs/SummaryJournalEntriesApi.md#p_ut_basic_summary_journal_entry) | **PUT** /v1/journal-entries/{je-number}/basic-information | Update basic information of a summary journal entry
*SummaryJournalEntriesApi* | [**p_ut_summary_journal_entry**](docs/SummaryJournalEntriesApi.md#p_ut_summary_journal_entry) | **PUT** /v1/journal-entries/{je-number}/cancel | Cancel summary journal entry
*TaxationItemsApi* | [**d_elete_taxation_item**](docs/TaxationItemsApi.md#d_elete_taxation_item) | **DELETE** /v1/taxationitems/{id} | Delete taxation item
*TaxationItemsApi* | [**g_et_taxation_item**](docs/TaxationItemsApi.md#g_et_taxation_item) | **GET** /v1/taxationitems/{id} | Get taxation item 
*TaxationItemsApi* | [**object_delete_taxation_item**](docs/TaxationItemsApi.md#object_delete_taxation_item) | **DELETE** /v1/object/taxation-item/{id} | CRUD: Delete TaxationItem
*TaxationItemsApi* | [**object_get_taxation_item**](docs/TaxationItemsApi.md#object_get_taxation_item) | **GET** /v1/object/taxation-item/{id} | CRUD: Retrieve TaxationItem
*TaxationItemsApi* | [**object_post_taxation_item**](docs/TaxationItemsApi.md#object_post_taxation_item) | **POST** /v1/object/taxation-item | CRUD: Create TaxationItem
*TaxationItemsApi* | [**object_put_taxation_item**](docs/TaxationItemsApi.md#object_put_taxation_item) | **PUT** /v1/object/taxation-item/{id} | CRUD: Update TaxationItem
*TaxationItemsApi* | [**p_ut_taxation_item**](docs/TaxationItemsApi.md#p_ut_taxation_item) | **PUT** /v1/taxationitems/{id} | Update taxation item
*TransactionsApi* | [**g_et_transaction_invoice**](docs/TransactionsApi.md#g_et_transaction_invoice) | **GET** /v1/transactions/invoices/accounts/{account-key} | Get invoices
*TransactionsApi* | [**g_et_transaction_payment**](docs/TransactionsApi.md#g_et_transaction_payment) | **GET** /v1/transactions/payments/accounts/{account-key} | Get payments
*UnitOfMeasureApi* | [**object_delete_unit_of_measure**](docs/UnitOfMeasureApi.md#object_delete_unit_of_measure) | **DELETE** /v1/object/unit-of-measure/{id} | CRUD: Delete UnitOfMeasure
*UnitOfMeasureApi* | [**object_get_unit_of_measure**](docs/UnitOfMeasureApi.md#object_get_unit_of_measure) | **GET** /v1/object/unit-of-measure/{id} | CRUD: Retrieve UnitOfMeasure
*UnitOfMeasureApi* | [**object_post_unit_of_measure**](docs/UnitOfMeasureApi.md#object_post_unit_of_measure) | **POST** /v1/object/unit-of-measure | CRUD: Create UnitOfMeasure
*UnitOfMeasureApi* | [**object_put_unit_of_measure**](docs/UnitOfMeasureApi.md#object_put_unit_of_measure) | **PUT** /v1/object/unit-of-measure/{id} | CRUD: Update UnitOfMeasure
*UsageApi* | [**g_et_usage**](docs/UsageApi.md#g_et_usage) | **GET** /v1/usage/accounts/{account-key} | Get usage
*UsageApi* | [**object_delete_usage**](docs/UsageApi.md#object_delete_usage) | **DELETE** /v1/object/usage/{id} | CRUD: Delete usage
*UsageApi* | [**object_get_usage**](docs/UsageApi.md#object_get_usage) | **GET** /v1/object/usage/{id} | CRUD: Get usage
*UsageApi* | [**object_post_usage**](docs/UsageApi.md#object_post_usage) | **POST** /v1/object/usage | CRUD: Create usage
*UsageApi* | [**object_put_usage**](docs/UsageApi.md#object_put_usage) | **PUT** /v1/object/usage/{id} | CRUD: Update usage
*UsageApi* | [**p_ost_usage**](docs/UsageApi.md#p_ost_usage) | **POST** /v1/usage | Post usage
*UsersApi* | [**g_et_entities_user_accessible**](docs/UsersApi.md#g_et_entities_user_accessible) | **GET** /v1/users/{username}/accessible-entities | Multi-entity: Get entities that a user can access
*UsersApi* | [**p_ut_accept_user_access**](docs/UsersApi.md#p_ut_accept_user_access) | **PUT** /v1/users/{username}/accept-access | Multi-entity: Accept user access
*UsersApi* | [**p_ut_deny_user_access**](docs/UsersApi.md#p_ut_deny_user_access) | **PUT** /v1/users/{username}/deny-access | Multi-entity: Deny user access
*UsersApi* | [**p_ut_send_user_access_requests**](docs/UsersApi.md#p_ut_send_user_access_requests) | **PUT** /v1/users/{username}/request-access | Multi-entity: Send user access requests


## Documentation For Models

 - [AccountCreditCardHolder](docs/AccountCreditCardHolder.md)
 - [AccountObjectCustomFields](docs/AccountObjectCustomFields.md)
 - [AccountObjectNSFields](docs/AccountObjectNSFields.md)
 - [AccountingCodeObjectCustomFields](docs/AccountingCodeObjectCustomFields.md)
 - [AccountingPeriodObjectCustomFields](docs/AccountingPeriodObjectCustomFields.md)
 - [ActionsErrorResponse](docs/ActionsErrorResponse.md)
 - [AmendRequest](docs/AmendRequest.md)
 - [AmendRequestAmendOptions](docs/AmendRequestAmendOptions.md)
 - [AmendRequestPreviewOptions](docs/AmendRequestPreviewOptions.md)
 - [AmendResult](docs/AmendResult.md)
 - [Amendment](docs/Amendment.md)
 - [AmendmentObjectCustomFields](docs/AmendmentObjectCustomFields.md)
 - [AmendmentRatePlanChargeData](docs/AmendmentRatePlanChargeData.md)
 - [AmendmentRatePlanChargeTier](docs/AmendmentRatePlanChargeTier.md)
 - [AmendmentRatePlanData](docs/AmendmentRatePlanData.md)
 - [ApplyCreditMemoType](docs/ApplyCreditMemoType.md)
 - [ApplyPaymentType](docs/ApplyPaymentType.md)
 - [BatchDebitMemoType](docs/BatchDebitMemoType.md)
 - [BatchInvoiceType](docs/BatchInvoiceType.md)
 - [BillingDocumentQueryResponseElementType](docs/BillingDocumentQueryResponseElementType.md)
 - [BillingOptions](docs/BillingOptions.md)
 - [BillingPreviewResult](docs/BillingPreviewResult.md)
 - [BillingUpdate](docs/BillingUpdate.md)
 - [BreakdownDetail](docs/BreakdownDetail.md)
 - [CalloutAuth](docs/CalloutAuth.md)
 - [CalloutMergeFields](docs/CalloutMergeFields.md)
 - [CancelSubscription](docs/CancelSubscription.md)
 - [ChargeMetricsData](docs/ChargeMetricsData.md)
 - [ChargeOverride](docs/ChargeOverride.md)
 - [ChargeOverrideBilling](docs/ChargeOverrideBilling.md)
 - [ChargeOverrideForEvergreen](docs/ChargeOverrideForEvergreen.md)
 - [ChargeOverridePricing](docs/ChargeOverridePricing.md)
 - [ChargePreviewMetrics](docs/ChargePreviewMetrics.md)
 - [ChargePreviewMetricsCmrr](docs/ChargePreviewMetricsCmrr.md)
 - [ChargePreviewMetricsTax](docs/ChargePreviewMetricsTax.md)
 - [ChargePreviewMetricsTcb](docs/ChargePreviewMetricsTcb.md)
 - [ChargePreviewMetricsTcv](docs/ChargePreviewMetricsTcv.md)
 - [ChargeRatedResult](docs/ChargeRatedResult.md)
 - [ChargeTier](docs/ChargeTier.md)
 - [ChargeUpdate](docs/ChargeUpdate.md)
 - [ChargeUpdateForEvergreen](docs/ChargeUpdateForEvergreen.md)
 - [CommonResponseType](docs/CommonResponseType.md)
 - [CommonResponseTypeReasons](docs/CommonResponseTypeReasons.md)
 - [Contact](docs/Contact.md)
 - [ContactObjectCustomFields](docs/ContactObjectCustomFields.md)
 - [CreateEntityResponseType](docs/CreateEntityResponseType.md)
 - [CreateEntityType](docs/CreateEntityType.md)
 - [CreateOrderChargeOverride](docs/CreateOrderChargeOverride.md)
 - [CreateOrderChargeUpdate](docs/CreateOrderChargeUpdate.md)
 - [CreateOrderCreateSubscription](docs/CreateOrderCreateSubscription.md)
 - [CreateOrderCreateSubscriptionTerms](docs/CreateOrderCreateSubscriptionTerms.md)
 - [CreateOrderCreateSubscriptionTermsInitialTerm](docs/CreateOrderCreateSubscriptionTermsInitialTerm.md)
 - [CreateOrderOrderAction](docs/CreateOrderOrderAction.md)
 - [CreateOrderPricingUpdate](docs/CreateOrderPricingUpdate.md)
 - [CreateOrderRatePlanOverride](docs/CreateOrderRatePlanOverride.md)
 - [CreateOrderRatePlanUpdate](docs/CreateOrderRatePlanUpdate.md)
 - [CreateOrderResume](docs/CreateOrderResume.md)
 - [CreateOrderSuspend](docs/CreateOrderSuspend.md)
 - [CreatePMPayPalECPayPalNativeEC](docs/CreatePMPayPalECPayPalNativeEC.md)
 - [CreatePaymentMethodACH](docs/CreatePaymentMethodACH.md)
 - [CreatePaymentMethodCardholderInfo](docs/CreatePaymentMethodCardholderInfo.md)
 - [CreatePaymentMethodCommon](docs/CreatePaymentMethodCommon.md)
 - [CreatePaymentMethodCreditCard](docs/CreatePaymentMethodCreditCard.md)
 - [CreatePaymentMethodPayPalAdaptive](docs/CreatePaymentMethodPayPalAdaptive.md)
 - [CreatePaymentTypeFinanceInformation](docs/CreatePaymentTypeFinanceInformation.md)
 - [CreateStoredCredentialProfileRequest](docs/CreateStoredCredentialProfileRequest.md)
 - [CreateSubscription](docs/CreateSubscription.md)
 - [CreateSubscriptionForEvergreen](docs/CreateSubscriptionForEvergreen.md)
 - [CreateSubscriptionNewSubscriptionOwnerAccount](docs/CreateSubscriptionNewSubscriptionOwnerAccount.md)
 - [CreateSubscriptionTerms](docs/CreateSubscriptionTerms.md)
 - [CreditBalanceAdjustmentObjectCustomFields](docs/CreditBalanceAdjustmentObjectCustomFields.md)
 - [CreditBalanceAdjustmentObjectNSFields](docs/CreditBalanceAdjustmentObjectNSFields.md)
 - [CreditCard](docs/CreditCard.md)
 - [CreditMemoApplyDebitMemoItemRequestType](docs/CreditMemoApplyDebitMemoItemRequestType.md)
 - [CreditMemoApplyDebitMemoRequestType](docs/CreditMemoApplyDebitMemoRequestType.md)
 - [CreditMemoApplyInvoiceItemRequestType](docs/CreditMemoApplyInvoiceItemRequestType.md)
 - [CreditMemoApplyInvoiceRequestType](docs/CreditMemoApplyInvoiceRequestType.md)
 - [CreditMemoEntityPrefix](docs/CreditMemoEntityPrefix.md)
 - [CreditMemoFromChargeDetailTypeFinanceInformation](docs/CreditMemoFromChargeDetailTypeFinanceInformation.md)
 - [CreditMemoItemBreakdown](docs/CreditMemoItemBreakdown.md)
 - [CreditMemoItemFromInvoiceItemTypeFinanceInformation](docs/CreditMemoItemFromInvoiceItemTypeFinanceInformation.md)
 - [CreditMemoItemFromWriteOffInvoiceFinanceInformation](docs/CreditMemoItemFromWriteOffInvoiceFinanceInformation.md)
 - [CreditMemoItemObjectCustomFields](docs/CreditMemoItemObjectCustomFields.md)
 - [CreditMemoObjectCustomFields](docs/CreditMemoObjectCustomFields.md)
 - [CreditMemoObjectNSFields](docs/CreditMemoObjectNSFields.md)
 - [CreditMemoResponseType](docs/CreditMemoResponseType.md)
 - [CreditMemoTaxItemFromInvoiceTaxItemType](docs/CreditMemoTaxItemFromInvoiceTaxItemType.md)
 - [CreditMemoTaxItemFromInvoiceTaxItemTypeFinanceInformation](docs/CreditMemoTaxItemFromInvoiceTaxItemTypeFinanceInformation.md)
 - [CreditMemoUnapplyDebitMemoItemRequestType](docs/CreditMemoUnapplyDebitMemoItemRequestType.md)
 - [CreditMemoUnapplyDebitMemoRequestType](docs/CreditMemoUnapplyDebitMemoRequestType.md)
 - [CreditMemoUnapplyInvoiceItemRequestType](docs/CreditMemoUnapplyInvoiceItemRequestType.md)
 - [CreditMemoUnapplyInvoiceRequestType](docs/CreditMemoUnapplyInvoiceRequestType.md)
 - [DELETEntityResponseType](docs/DELETEntityResponseType.md)
 - [DataAccessControlField](docs/DataAccessControlField.md)
 - [DataQueryErrorResponse](docs/DataQueryErrorResponse.md)
 - [DataQueryJobCommon](docs/DataQueryJobCommon.md)
 - [DebitMemoEntityPrefix](docs/DebitMemoEntityPrefix.md)
 - [DebitMemoFromChargeDetailTypeFinanceInformation](docs/DebitMemoFromChargeDetailTypeFinanceInformation.md)
 - [DebitMemoItemFromInvoiceItemTypeFinanceInformation](docs/DebitMemoItemFromInvoiceItemTypeFinanceInformation.md)
 - [DebitMemoItemObjectCustomFields](docs/DebitMemoItemObjectCustomFields.md)
 - [DebitMemoObjectCustomFields](docs/DebitMemoObjectCustomFields.md)
 - [DebitMemoObjectNSFields](docs/DebitMemoObjectNSFields.md)
 - [DebitMemoTaxItemFromInvoiceTaxItemType](docs/DebitMemoTaxItemFromInvoiceTaxItemType.md)
 - [DebitMemoTaxItemFromInvoiceTaxItemTypeFinanceInformation](docs/DebitMemoTaxItemFromInvoiceTaxItemTypeFinanceInformation.md)
 - [DeleteDataQueryJobResponse](docs/DeleteDataQueryJobResponse.md)
 - [DeleteResult](docs/DeleteResult.md)
 - [DiscountPricingOverride](docs/DiscountPricingOverride.md)
 - [DiscountPricingUpdate](docs/DiscountPricingUpdate.md)
 - [ElectronicPaymentOptions](docs/ElectronicPaymentOptions.md)
 - [EndConditions](docs/EndConditions.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorResponseReasons](docs/ErrorResponseReasons.md)
 - [EventTrigger](docs/EventTrigger.md)
 - [EventType](docs/EventType.md)
 - [ExecuteResult](docs/ExecuteResult.md)
 - [ExternalPaymentOptions](docs/ExternalPaymentOptions.md)
 - [FeatureObjectCustomFields](docs/FeatureObjectCustomFields.md)
 - [FilterRuleParameterDefinition](docs/FilterRuleParameterDefinition.md)
 - [FilterRuleParameterDefinitions](docs/FilterRuleParameterDefinitions.md)
 - [FilterRuleParameterValues](docs/FilterRuleParameterValues.md)
 - [FinanceInformation](docs/FinanceInformation.md)
 - [GETAPaymentGatwayResponse](docs/GETAPaymentGatwayResponse.md)
 - [GETARPaymentTypeFinanceInformation](docs/GETARPaymentTypeFinanceInformation.md)
 - [GETAccountSummaryInvoiceType](docs/GETAccountSummaryInvoiceType.md)
 - [GETAccountSummaryPaymentInvoiceType](docs/GETAccountSummaryPaymentInvoiceType.md)
 - [GETAccountSummaryPaymentType](docs/GETAccountSummaryPaymentType.md)
 - [GETAccountSummarySubscriptionRatePlanType](docs/GETAccountSummarySubscriptionRatePlanType.md)
 - [GETAccountSummaryType](docs/GETAccountSummaryType.md)
 - [GETAccountSummaryTypeBasicInfoDefaultPaymentMethod](docs/GETAccountSummaryTypeBasicInfoDefaultPaymentMethod.md)
 - [GETAccountSummaryTypeTaxInfo](docs/GETAccountSummaryTypeTaxInfo.md)
 - [GETAccountSummaryUsageType](docs/GETAccountSummaryUsageType.md)
 - [GETAccountType](docs/GETAccountType.md)
 - [GETAccountTypeBillingAndPayment](docs/GETAccountTypeBillingAndPayment.md)
 - [GETAccountTypeMetrics](docs/GETAccountTypeMetrics.md)
 - [GETAccountingCodesType](docs/GETAccountingCodesType.md)
 - [GETAccountingPeriodTypeFileIds](docs/GETAccountingPeriodTypeFileIds.md)
 - [GETAccountingPeriodsType](docs/GETAccountingPeriodsType.md)
 - [GETAmendmentType](docs/GETAmendmentType.md)
 - [GETAttachmentResponseType](docs/GETAttachmentResponseType.md)
 - [GETAttachmentResponseWithoutSuccessType](docs/GETAttachmentResponseWithoutSuccessType.md)
 - [GETAttachmentsResponseType](docs/GETAttachmentsResponseType.md)
 - [GETBillingDocumentFilesDeletionJobResponse](docs/GETBillingDocumentFilesDeletionJobResponse.md)
 - [GETBillingDocumentsResponseType](docs/GETBillingDocumentsResponseType.md)
 - [GETCMTaxItemType](docs/GETCMTaxItemType.md)
 - [GETCMTaxItemTypeFinanceInformation](docs/GETCMTaxItemTypeFinanceInformation.md)
 - [GETCMTaxItemTypeNew](docs/GETCMTaxItemTypeNew.md)
 - [GETCalloutHistoryVOType](docs/GETCalloutHistoryVOType.md)
 - [GETCalloutHistoryVOsType](docs/GETCalloutHistoryVOsType.md)
 - [GETCatalogType](docs/GETCatalogType.md)
 - [GETChargeRSDetailType](docs/GETChargeRSDetailType.md)
 - [GETCreditMemoCollectionType](docs/GETCreditMemoCollectionType.md)
 - [GETCreditMemoItemPartType](docs/GETCreditMemoItemPartType.md)
 - [GETCreditMemoItemPartTypewithSuccess](docs/GETCreditMemoItemPartTypewithSuccess.md)
 - [GETCreditMemoItemPartsCollectionType](docs/GETCreditMemoItemPartsCollectionType.md)
 - [GETCreditMemoItemTypeFinanceInformation](docs/GETCreditMemoItemTypeFinanceInformation.md)
 - [GETCreditMemoItemTypeTaxationItems](docs/GETCreditMemoItemTypeTaxationItems.md)
 - [GETCreditMemoItemTypewithSuccessFinanceInformation](docs/GETCreditMemoItemTypewithSuccessFinanceInformation.md)
 - [GETCreditMemoItemsListType](docs/GETCreditMemoItemsListType.md)
 - [GETCreditMemoPartType](docs/GETCreditMemoPartType.md)
 - [GETCreditMemoPartTypewithSuccess](docs/GETCreditMemoPartTypewithSuccess.md)
 - [GETCreditMemoPartsCollectionType](docs/GETCreditMemoPartsCollectionType.md)
 - [GETCustomExchangeRatesDataType](docs/GETCustomExchangeRatesDataType.md)
 - [GETCustomExchangeRatesType](docs/GETCustomExchangeRatesType.md)
 - [GETDMTaxItemType](docs/GETDMTaxItemType.md)
 - [GETDMTaxItemTypeFinanceInformation](docs/GETDMTaxItemTypeFinanceInformation.md)
 - [GETDMTaxItemTypeNew](docs/GETDMTaxItemTypeNew.md)
 - [GETDebitMemoCollectionType](docs/GETDebitMemoCollectionType.md)
 - [GETDebitMemoItemCollectionType](docs/GETDebitMemoItemCollectionType.md)
 - [GETDebitMemoItemTypeFinanceInformation](docs/GETDebitMemoItemTypeFinanceInformation.md)
 - [GETDebitMemoItemTypeTaxationItems](docs/GETDebitMemoItemTypeTaxationItems.md)
 - [GETDebitMemoItemTypewithSuccessTaxationItems](docs/GETDebitMemoItemTypewithSuccessTaxationItems.md)
 - [GETDiscountApplyDetailsType](docs/GETDiscountApplyDetailsType.md)
 - [GETDocumentPropertiesResponseType](docs/GETDocumentPropertiesResponseType.md)
 - [GETEmailHistoryVOType](docs/GETEmailHistoryVOType.md)
 - [GETEmailHistoryVOsType](docs/GETEmailHistoryVOsType.md)
 - [GETEntitiesResponseType](docs/GETEntitiesResponseType.md)
 - [GETEntitiesResponseTypeWithId](docs/GETEntitiesResponseTypeWithId.md)
 - [GETEntitiesType](docs/GETEntitiesType.md)
 - [GETEntitiesUserAccessibleResponseType](docs/GETEntitiesUserAccessibleResponseType.md)
 - [GETEntityConnectionsArrayItemsType](docs/GETEntityConnectionsArrayItemsType.md)
 - [GETEntityConnectionsResponseType](docs/GETEntityConnectionsResponseType.md)
 - [GETInvoiceFileWrapper](docs/GETInvoiceFileWrapper.md)
 - [GETInvoiceFilesResponse](docs/GETInvoiceFilesResponse.md)
 - [GETInvoiceItemsResponse](docs/GETInvoiceItemsResponse.md)
 - [GETInvoiceTaxItemType](docs/GETInvoiceTaxItemType.md)
 - [GETInvoiceTaxationItemsResponse](docs/GETInvoiceTaxationItemsResponse.md)
 - [GETJournalEntriesInJournalRunType](docs/GETJournalEntriesInJournalRunType.md)
 - [GETJournalEntrySegmentType](docs/GETJournalEntrySegmentType.md)
 - [GETJournalRunTransactionType](docs/GETJournalRunTransactionType.md)
 - [GETJournalRunType](docs/GETJournalRunType.md)
 - [GETMassUpdateType](docs/GETMassUpdateType.md)
 - [GETPaidInvoicesType](docs/GETPaidInvoicesType.md)
 - [GETPaymentGatwaysResponse](docs/GETPaymentGatwaysResponse.md)
 - [GETPaymentItemPartCollectionType](docs/GETPaymentItemPartCollectionType.md)
 - [GETPaymentItemPartType](docs/GETPaymentItemPartType.md)
 - [GETPaymentItemPartTypewithSuccess](docs/GETPaymentItemPartTypewithSuccess.md)
 - [GETPaymentMethodType](docs/GETPaymentMethodType.md)
 - [GETPaymentMethodTypeCardHolderInfo](docs/GETPaymentMethodTypeCardHolderInfo.md)
 - [GETPaymentMethodsType](docs/GETPaymentMethodsType.md)
 - [GETPaymentPartType](docs/GETPaymentPartType.md)
 - [GETPaymentPartTypewithSuccess](docs/GETPaymentPartTypewithSuccess.md)
 - [GETPaymentPartsCollectionType](docs/GETPaymentPartsCollectionType.md)
 - [GETPaymentRunCollectionType](docs/GETPaymentRunCollectionType.md)
 - [GETPaymentRunSummaryResponse](docs/GETPaymentRunSummaryResponse.md)
 - [GETPaymentRunSummaryTotalValues](docs/GETPaymentRunSummaryTotalValues.md)
 - [GETPaymentRunType](docs/GETPaymentRunType.md)
 - [GETPaymentsType](docs/GETPaymentsType.md)
 - [GETProductDiscountApplyDetailsType](docs/GETProductDiscountApplyDetailsType.md)
 - [GETProductRatePlanChargePricingTierType](docs/GETProductRatePlanChargePricingTierType.md)
 - [GETProductRatePlanChargePricingType](docs/GETProductRatePlanChargePricingType.md)
 - [GETProductRatePlansResponse](docs/GETProductRatePlansResponse.md)
 - [GETPublicEmailTemplateResponse](docs/GETPublicEmailTemplateResponse.md)
 - [GETPublicNotificationDefinitionResponse](docs/GETPublicNotificationDefinitionResponse.md)
 - [GETPublicNotificationDefinitionResponseCallout](docs/GETPublicNotificationDefinitionResponseCallout.md)
 - [GETPublicNotificationDefinitionResponseFilterRule](docs/GETPublicNotificationDefinitionResponseFilterRule.md)
 - [GETRSDetailsByChargeType](docs/GETRSDetailsByChargeType.md)
 - [GETRSDetailsByProductChargeType](docs/GETRSDetailsByProductChargeType.md)
 - [GETRefundCollectionType](docs/GETRefundCollectionType.md)
 - [GETRefundCreditMemoTypeFinanceInformation](docs/GETRefundCreditMemoTypeFinanceInformation.md)
 - [GETRefundItemPartCollectionType](docs/GETRefundItemPartCollectionType.md)
 - [GETRefundItemPartType](docs/GETRefundItemPartType.md)
 - [GETRefundItemPartTypewithSuccess](docs/GETRefundItemPartTypewithSuccess.md)
 - [GETRefundPartCollectionType](docs/GETRefundPartCollectionType.md)
 - [GETRevenueEventDetailsType](docs/GETRevenueEventDetailsType.md)
 - [GETRevenueItemsType](docs/GETRevenueItemsType.md)
 - [GETRevenueRecognitionRuleAssociationType](docs/GETRevenueRecognitionRuleAssociationType.md)
 - [GETRevenueStartDateSettingType](docs/GETRevenueStartDateSettingType.md)
 - [GETRsRevenueItemsType](docs/GETRsRevenueItemsType.md)
 - [GETSequenceSetResponse](docs/GETSequenceSetResponse.md)
 - [GETSequenceSetsResponse](docs/GETSequenceSetsResponse.md)
 - [GETSubscriptionProductFeatureType](docs/GETSubscriptionProductFeatureType.md)
 - [GETSubscriptionWrapper](docs/GETSubscriptionWrapper.md)
 - [GETTaxationItemListType](docs/GETTaxationItemListType.md)
 - [GETTaxationItemsOfCreditMemoItemType](docs/GETTaxationItemsOfCreditMemoItemType.md)
 - [GETTaxationItemsOfDebitMemoItemType](docs/GETTaxationItemsOfDebitMemoItemType.md)
 - [GETTierType](docs/GETTierType.md)
 - [GETUsageWrapper](docs/GETUsageWrapper.md)
 - [GatewayOption](docs/GatewayOption.md)
 - [GenerateBillingDocumentResponseType](docs/GenerateBillingDocumentResponseType.md)
 - [GetAllOrdersResponseType](docs/GetAllOrdersResponseType.md)
 - [GetBillingPreviewRunResponse](docs/GetBillingPreviewRunResponse.md)
 - [GetDataQueryJobResponse](docs/GetDataQueryJobResponse.md)
 - [GetDataQueryJobsResponse](docs/GetDataQueryJobsResponse.md)
 - [GetDebitMemoApplicationPartCollectionType](docs/GetDebitMemoApplicationPartCollectionType.md)
 - [GetDebitMemoApplicationPartType](docs/GetDebitMemoApplicationPartType.md)
 - [GetHostedPageType](docs/GetHostedPageType.md)
 - [GetHostedPagesType](docs/GetHostedPagesType.md)
 - [GetInvoiceApplicationPartCollectionType](docs/GetInvoiceApplicationPartCollectionType.md)
 - [GetInvoiceApplicationPartType](docs/GetInvoiceApplicationPartType.md)
 - [GetOrderBillingInfoResponseTypeBillingInfo](docs/GetOrderBillingInfoResponseTypeBillingInfo.md)
 - [GetOrderResume](docs/GetOrderResume.md)
 - [GetOrderSuspend](docs/GetOrderSuspend.md)
 - [GetStoredCredentialProfilesResponse](docs/GetStoredCredentialProfilesResponse.md)
 - [GetStoredCredentialProfilesResponseProfiles](docs/GetStoredCredentialProfilesResponseProfiles.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse202](docs/InlineResponse202.md)
 - [Invoice](docs/Invoice.md)
 - [InvoiceAdjustmentObjectCustomFields](docs/InvoiceAdjustmentObjectCustomFields.md)
 - [InvoiceData](docs/InvoiceData.md)
 - [InvoiceEntityPrefix](docs/InvoiceEntityPrefix.md)
 - [InvoiceFile](docs/InvoiceFile.md)
 - [InvoiceItemAdjustmentObjectCustomFields](docs/InvoiceItemAdjustmentObjectCustomFields.md)
 - [InvoiceItemAdjustmentObjectNSFields](docs/InvoiceItemAdjustmentObjectNSFields.md)
 - [InvoiceItemBreakdown](docs/InvoiceItemBreakdown.md)
 - [InvoiceItemObjectCustomFields](docs/InvoiceItemObjectCustomFields.md)
 - [InvoiceItemObjectNSFields](docs/InvoiceItemObjectNSFields.md)
 - [InvoiceItemPreviewResult](docs/InvoiceItemPreviewResult.md)
 - [InvoiceItemPreviewResultAdditionalInfo](docs/InvoiceItemPreviewResultAdditionalInfo.md)
 - [InvoiceItemTaxationItems](docs/InvoiceItemTaxationItems.md)
 - [InvoiceObjectCustomFields](docs/InvoiceObjectCustomFields.md)
 - [InvoiceObjectNSFields](docs/InvoiceObjectNSFields.md)
 - [InvoicePayment](docs/InvoicePayment.md)
 - [InvoicePaymentData](docs/InvoicePaymentData.md)
 - [InvoiceProcessingOptions](docs/InvoiceProcessingOptions.md)
 - [InvoiceResponseType](docs/InvoiceResponseType.md)
 - [JobResultSubscriptions](docs/JobResultSubscriptions.md)
 - [JournalEntryItemObjectCustomFields](docs/JournalEntryItemObjectCustomFields.md)
 - [JournalEntryObjectCustomFields](docs/JournalEntryObjectCustomFields.md)
 - [LastTerm](docs/LastTerm.md)
 - [ListOfExchangeRates](docs/ListOfExchangeRates.md)
 - [ModifiedStoredCredentialProfileResponse](docs/ModifiedStoredCredentialProfileResponse.md)
 - [NewChargeMetrics](docs/NewChargeMetrics.md)
 - [OneTimeFlatFeePricingOverride](docs/OneTimeFlatFeePricingOverride.md)
 - [OneTimePerUnitPricingOverride](docs/OneTimePerUnitPricingOverride.md)
 - [OneTimeTieredPricingOverride](docs/OneTimeTieredPricingOverride.md)
 - [OneTimeVolumePricingOverride](docs/OneTimeVolumePricingOverride.md)
 - [Order](docs/Order.md)
 - [OrderAction](docs/OrderAction.md)
 - [OrderActionForEvergreen](docs/OrderActionForEvergreen.md)
 - [OrderActionObjectCustomFields](docs/OrderActionObjectCustomFields.md)
 - [OrderForEvergreen](docs/OrderForEvergreen.md)
 - [OrderForEvergreenSubscriptions](docs/OrderForEvergreenSubscriptions.md)
 - [OrderItem](docs/OrderItem.md)
 - [OrderMetric](docs/OrderMetric.md)
 - [OrderMetricsForEvergreen](docs/OrderMetricsForEvergreen.md)
 - [OrderObjectCustomFields](docs/OrderObjectCustomFields.md)
 - [OrderRatedResult](docs/OrderRatedResult.md)
 - [OrderSubscriptions](docs/OrderSubscriptions.md)
 - [OwnerTransfer](docs/OwnerTransfer.md)
 - [POSTAccountResponseType](docs/POSTAccountResponseType.md)
 - [POSTAccountTypeCreditCardCardHolderInfo](docs/POSTAccountTypeCreditCardCardHolderInfo.md)
 - [POSTAccountTypeTaxInfo](docs/POSTAccountTypeTaxInfo.md)
 - [POSTAccountingCodeResponseType](docs/POSTAccountingCodeResponseType.md)
 - [POSTAccountingPeriodResponseType](docs/POSTAccountingPeriodResponseType.md)
 - [POSTAttachmentResponseType](docs/POSTAttachmentResponseType.md)
 - [POSTAuthorizeResponse](docs/POSTAuthorizeResponse.md)
 - [POSTBillingDocumentFilesDeletionJobRequest](docs/POSTBillingDocumentFilesDeletionJobRequest.md)
 - [POSTBillingDocumentFilesDeletionJobResponse](docs/POSTBillingDocumentFilesDeletionJobResponse.md)
 - [POSTBillingPreviewCreditMemoItem](docs/POSTBillingPreviewCreditMemoItem.md)
 - [POSTBillingPreviewInvoiceItem](docs/POSTBillingPreviewInvoiceItem.md)
 - [POSTCatalogType](docs/POSTCatalogType.md)
 - [POSTCreditMemoItemsForOrderBreakdown](docs/POSTCreditMemoItemsForOrderBreakdown.md)
 - [POSTDecryptResponseType](docs/POSTDecryptResponseType.md)
 - [POSTDecryptionType](docs/POSTDecryptionType.md)
 - [POSTDelayAuthorizeCapture](docs/POSTDelayAuthorizeCapture.md)
 - [POSTDistributionItemType](docs/POSTDistributionItemType.md)
 - [POSTDocumentPropertiesType](docs/POSTDocumentPropertiesType.md)
 - [POSTEmailBillingDocfromBillRunType](docs/POSTEmailBillingDocfromBillRunType.md)
 - [POSTEntityConnectionsResponseType](docs/POSTEntityConnectionsResponseType.md)
 - [POSTEntityConnectionsType](docs/POSTEntityConnectionsType.md)
 - [POSTHMACSignatureResponseType](docs/POSTHMACSignatureResponseType.md)
 - [POSTHMACSignatureType](docs/POSTHMACSignatureType.md)
 - [POSTInvoiceCollectCreditMemosType](docs/POSTInvoiceCollectCreditMemosType.md)
 - [POSTInvoiceCollectInvoicesType](docs/POSTInvoiceCollectInvoicesType.md)
 - [POSTInvoiceCollectResponseType](docs/POSTInvoiceCollectResponseType.md)
 - [POSTInvoiceCollectType](docs/POSTInvoiceCollectType.md)
 - [POSTInvoiceItemsForOrderBreakdown](docs/POSTInvoiceItemsForOrderBreakdown.md)
 - [POSTJournalEntryResponseType](docs/POSTJournalEntryResponseType.md)
 - [POSTJournalEntrySegmentType](docs/POSTJournalEntrySegmentType.md)
 - [POSTJournalRunResponseType](docs/POSTJournalRunResponseType.md)
 - [POSTJournalRunTransactionType](docs/POSTJournalRunTransactionType.md)
 - [POSTJournalRunType](docs/POSTJournalRunType.md)
 - [POSTMassUpdateResponseType](docs/POSTMassUpdateResponseType.md)
 - [POSTMemoPdfResponse](docs/POSTMemoPdfResponse.md)
 - [POSTOrderPreviewRequestType](docs/POSTOrderPreviewRequestType.md)
 - [POSTOrderPreviewRequestTypeSubscriptions](docs/POSTOrderPreviewRequestTypeSubscriptions.md)
 - [POSTOrderRequestType](docs/POSTOrderRequestType.md)
 - [POSTOrderRequestTypeSubscriptions](docs/POSTOrderRequestTypeSubscriptions.md)
 - [POSTPaymentMethodDecryption](docs/POSTPaymentMethodDecryption.md)
 - [POSTPaymentMethodDecryptionCardHolderInfo](docs/POSTPaymentMethodDecryptionCardHolderInfo.md)
 - [POSTPaymentMethodResponseDecryption](docs/POSTPaymentMethodResponseDecryption.md)
 - [POSTPaymentMethodResponseReasons](docs/POSTPaymentMethodResponseReasons.md)
 - [POSTPaymentMethodResponseType](docs/POSTPaymentMethodResponseType.md)
 - [POSTPaymentRunRequest](docs/POSTPaymentRunRequest.md)
 - [POSTPublicEmailTemplateRequest](docs/POSTPublicEmailTemplateRequest.md)
 - [POSTPublicNotificationDefinitionRequest](docs/POSTPublicNotificationDefinitionRequest.md)
 - [POSTPublicNotificationDefinitionRequestCallout](docs/POSTPublicNotificationDefinitionRequestCallout.md)
 - [POSTPublicNotificationDefinitionRequestFilterRule](docs/POSTPublicNotificationDefinitionRequestFilterRule.md)
 - [POSTQuoteDocResponseType](docs/POSTQuoteDocResponseType.md)
 - [POSTQuoteDocType](docs/POSTQuoteDocType.md)
 - [POSTRSASignatureResponseType](docs/POSTRSASignatureResponseType.md)
 - [POSTRSASignatureType](docs/POSTRSASignatureType.md)
 - [POSTRejectPaymentRequest](docs/POSTRejectPaymentRequest.md)
 - [POSTRejectPaymentResponse](docs/POSTRejectPaymentResponse.md)
 - [POSTRejectPaymentResponseFinanceInformation](docs/POSTRejectPaymentResponseFinanceInformation.md)
 - [POSTRevenueScheduleByChargeResponseType](docs/POSTRevenueScheduleByChargeResponseType.md)
 - [POSTRevenueScheduleByTransactionResponseType](docs/POSTRevenueScheduleByTransactionResponseType.md)
 - [POSTReversePaymentRequest](docs/POSTReversePaymentRequest.md)
 - [POSTReversePaymentResponse](docs/POSTReversePaymentResponse.md)
 - [POSTSequenceSetRequest](docs/POSTSequenceSetRequest.md)
 - [POSTSequenceSetsRequest](docs/POSTSequenceSetsRequest.md)
 - [POSTSequenceSetsResponse](docs/POSTSequenceSetsResponse.md)
 - [POSTSettlePaymentRequest](docs/POSTSettlePaymentRequest.md)
 - [POSTSettlePaymentResponse](docs/POSTSettlePaymentResponse.md)
 - [POSTSubscriptionCancellationResponseType](docs/POSTSubscriptionCancellationResponseType.md)
 - [POSTSubscriptionCancellationType](docs/POSTSubscriptionCancellationType.md)
 - [POSTSubscriptionPreviewCreditMemoItemsType](docs/POSTSubscriptionPreviewCreditMemoItemsType.md)
 - [POSTSubscriptionPreviewInvoiceItemsType](docs/POSTSubscriptionPreviewInvoiceItemsType.md)
 - [POSTSubscriptionPreviewResponseType](docs/POSTSubscriptionPreviewResponseType.md)
 - [POSTSubscriptionPreviewResponseTypeChargeMetrics](docs/POSTSubscriptionPreviewResponseTypeChargeMetrics.md)
 - [POSTSubscriptionPreviewResponseTypeCreditMemo](docs/POSTSubscriptionPreviewResponseTypeCreditMemo.md)
 - [POSTSubscriptionPreviewTypePreviewAccountInfoBillToContact](docs/POSTSubscriptionPreviewTypePreviewAccountInfoBillToContact.md)
 - [POSTSubscriptionResponseType](docs/POSTSubscriptionResponseType.md)
 - [POSTTaxationItemForCMTypeFinanceInformation](docs/POSTTaxationItemForCMTypeFinanceInformation.md)
 - [POSTTaxationItemForDMTypeFinanceInformation](docs/POSTTaxationItemForDMTypeFinanceInformation.md)
 - [POSTTaxationItemListForCMType](docs/POSTTaxationItemListForCMType.md)
 - [POSTTaxationItemListForDMType](docs/POSTTaxationItemListForDMType.md)
 - [POSTTierType](docs/POSTTierType.md)
 - [POSTUploadFileResponse](docs/POSTUploadFileResponse.md)
 - [POSTUsageResponseType](docs/POSTUsageResponseType.md)
 - [POSTVoidAuthorize](docs/POSTVoidAuthorize.md)
 - [POSTVoidAuthorizeResponse](docs/POSTVoidAuthorizeResponse.md)
 - [PUTAcceptUserAccessResponseType](docs/PUTAcceptUserAccessResponseType.md)
 - [PUTAttachmentType](docs/PUTAttachmentType.md)
 - [PUTBatchDebitMemosRequest](docs/PUTBatchDebitMemosRequest.md)
 - [PUTDebitMemoItemTypeFinanceInformation](docs/PUTDebitMemoItemTypeFinanceInformation.md)
 - [PUTDenyUserAccessResponseType](docs/PUTDenyUserAccessResponseType.md)
 - [PUTDocumentPropertiesType](docs/PUTDocumentPropertiesType.md)
 - [PUTEntityConnectionsAcceptResponseType](docs/PUTEntityConnectionsAcceptResponseType.md)
 - [PUTEntityConnectionsDenyResponseType](docs/PUTEntityConnectionsDenyResponseType.md)
 - [PUTEntityConnectionsDisconnectResponseType](docs/PUTEntityConnectionsDisconnectResponseType.md)
 - [PUTEventRIDetailType](docs/PUTEventRIDetailType.md)
 - [PUTOrderActionTriggerDatesRequestType](docs/PUTOrderActionTriggerDatesRequestType.md)
 - [PUTOrderActionTriggerDatesRequestTypeCharges](docs/PUTOrderActionTriggerDatesRequestTypeCharges.md)
 - [PUTOrderActionTriggerDatesRequestTypeOrderActions](docs/PUTOrderActionTriggerDatesRequestTypeOrderActions.md)
 - [PUTOrderActionTriggerDatesRequestTypeSubscriptions](docs/PUTOrderActionTriggerDatesRequestTypeSubscriptions.md)
 - [PUTOrderActionTriggerDatesRequestTypeTriggerDates](docs/PUTOrderActionTriggerDatesRequestTypeTriggerDates.md)
 - [PUTOrderPatchRequestType](docs/PUTOrderPatchRequestType.md)
 - [PUTOrderPatchRequestTypeOrderActions](docs/PUTOrderPatchRequestTypeOrderActions.md)
 - [PUTOrderPatchRequestTypeSubscriptions](docs/PUTOrderPatchRequestTypeSubscriptions.md)
 - [PUTOrderTriggerDatesResponseTypeSubscriptions](docs/PUTOrderTriggerDatesResponseTypeSubscriptions.md)
 - [PUTPaymentMethodResponseType](docs/PUTPaymentMethodResponseType.md)
 - [PUTPaymentRunRequest](docs/PUTPaymentRunRequest.md)
 - [PUTPublicCalloutOptionsRequest](docs/PUTPublicCalloutOptionsRequest.md)
 - [PUTPublicEmailTemplateRequest](docs/PUTPublicEmailTemplateRequest.md)
 - [PUTPublicNotificationDefinitionRequest](docs/PUTPublicNotificationDefinitionRequest.md)
 - [PUTPublicNotificationDefinitionRequestCallout](docs/PUTPublicNotificationDefinitionRequestCallout.md)
 - [PUTPublicNotificationDefinitionRequestFilterRule](docs/PUTPublicNotificationDefinitionRequestFilterRule.md)
 - [PUTRefundTypeFinanceInformation](docs/PUTRefundTypeFinanceInformation.md)
 - [PUTRenewSubscriptionResponseType](docs/PUTRenewSubscriptionResponseType.md)
 - [PUTRenewSubscriptionType](docs/PUTRenewSubscriptionType.md)
 - [PUTRevenueScheduleResponseType](docs/PUTRevenueScheduleResponseType.md)
 - [PUTScheduleRIDetailType](docs/PUTScheduleRIDetailType.md)
 - [PUTSendUserAccessRequestResponseType](docs/PUTSendUserAccessRequestResponseType.md)
 - [PUTSendUserAccessRequestType](docs/PUTSendUserAccessRequestType.md)
 - [PUTSequenceSetRequest](docs/PUTSequenceSetRequest.md)
 - [PUTSequenceSetResponse](docs/PUTSequenceSetResponse.md)
 - [PUTSrpRemoveType](docs/PUTSrpRemoveType.md)
 - [PUTSubscriptionPatchRequestType](docs/PUTSubscriptionPatchRequestType.md)
 - [PUTSubscriptionPatchRequestTypeCharges](docs/PUTSubscriptionPatchRequestTypeCharges.md)
 - [PUTSubscriptionPatchRequestTypeRatePlans](docs/PUTSubscriptionPatchRequestTypeRatePlans.md)
 - [PUTSubscriptionPreviewInvoiceItemsType](docs/PUTSubscriptionPreviewInvoiceItemsType.md)
 - [PUTSubscriptionResponseType](docs/PUTSubscriptionResponseType.md)
 - [PUTSubscriptionResponseTypeChargeMetrics](docs/PUTSubscriptionResponseTypeChargeMetrics.md)
 - [PUTSubscriptionResponseTypeCreditMemo](docs/PUTSubscriptionResponseTypeCreditMemo.md)
 - [PUTSubscriptionResumeResponseType](docs/PUTSubscriptionResumeResponseType.md)
 - [PUTSubscriptionResumeType](docs/PUTSubscriptionResumeType.md)
 - [PUTSubscriptionSuspendResponseType](docs/PUTSubscriptionSuspendResponseType.md)
 - [PUTSubscriptionSuspendType](docs/PUTSubscriptionSuspendType.md)
 - [PUTVerifyPaymentMethodResponseType](docs/PUTVerifyPaymentMethodResponseType.md)
 - [PUTVerifyPaymentMethodType](docs/PUTVerifyPaymentMethodType.md)
 - [PUTVerifyPaymentMethodTypeGatewayOptions](docs/PUTVerifyPaymentMethodTypeGatewayOptions.md)
 - [PUTWriteOffInvoiceResponse](docs/PUTWriteOffInvoiceResponse.md)
 - [PUTWriteOffInvoiceResponseCreditMemo](docs/PUTWriteOffInvoiceResponseCreditMemo.md)
 - [PaymentCollectionResponseType](docs/PaymentCollectionResponseType.md)
 - [PaymentDebitMemoApplicationApplyRequestType](docs/PaymentDebitMemoApplicationApplyRequestType.md)
 - [PaymentDebitMemoApplicationCreateRequestType](docs/PaymentDebitMemoApplicationCreateRequestType.md)
 - [PaymentDebitMemoApplicationItemApplyRequestType](docs/PaymentDebitMemoApplicationItemApplyRequestType.md)
 - [PaymentDebitMemoApplicationItemCreateRequestType](docs/PaymentDebitMemoApplicationItemCreateRequestType.md)
 - [PaymentDebitMemoApplicationItemUnapplyRequestType](docs/PaymentDebitMemoApplicationItemUnapplyRequestType.md)
 - [PaymentDebitMemoApplicationUnapplyRequestType](docs/PaymentDebitMemoApplicationUnapplyRequestType.md)
 - [PaymentInvoiceApplicationApplyRequestType](docs/PaymentInvoiceApplicationApplyRequestType.md)
 - [PaymentInvoiceApplicationCreateRequestType](docs/PaymentInvoiceApplicationCreateRequestType.md)
 - [PaymentInvoiceApplicationItemApplyRequestType](docs/PaymentInvoiceApplicationItemApplyRequestType.md)
 - [PaymentInvoiceApplicationItemCreateRequestType](docs/PaymentInvoiceApplicationItemCreateRequestType.md)
 - [PaymentInvoiceApplicationItemUnapplyRequestType](docs/PaymentInvoiceApplicationItemUnapplyRequestType.md)
 - [PaymentInvoiceApplicationUnapplyRequestType](docs/PaymentInvoiceApplicationUnapplyRequestType.md)
 - [PaymentMethodObjectCustomFields](docs/PaymentMethodObjectCustomFields.md)
 - [PaymentObjectCustomFields](docs/PaymentObjectCustomFields.md)
 - [PaymentObjectNSFields](docs/PaymentObjectNSFields.md)
 - [PostBillingPreviewParam](docs/PostBillingPreviewParam.md)
 - [PostBillingPreviewRunParam](docs/PostBillingPreviewRunParam.md)
 - [PostCreditMemoEmailRequestType](docs/PostCreditMemoEmailRequestType.md)
 - [PostDebitMemoEmailType](docs/PostDebitMemoEmailType.md)
 - [PostEventTriggerRequest](docs/PostEventTriggerRequest.md)
 - [PostGenerateBillingDocumentType](docs/PostGenerateBillingDocumentType.md)
 - [PostInvoiceEmailRequestType](docs/PostInvoiceEmailRequestType.md)
 - [PostNonRefRefundTypeFinanceInformation](docs/PostNonRefRefundTypeFinanceInformation.md)
 - [PostOrderResponseTypeSubscriptions](docs/PostOrderResponseTypeSubscriptions.md)
 - [PostRefundTypeFinanceInformation](docs/PostRefundTypeFinanceInformation.md)
 - [PreviewAccountInfo](docs/PreviewAccountInfo.md)
 - [PreviewContactInfo](docs/PreviewContactInfo.md)
 - [PreviewOptions](docs/PreviewOptions.md)
 - [PreviewOrderChargeOverride](docs/PreviewOrderChargeOverride.md)
 - [PreviewOrderChargeUpdate](docs/PreviewOrderChargeUpdate.md)
 - [PreviewOrderCreateSubscription](docs/PreviewOrderCreateSubscription.md)
 - [PreviewOrderCreateSubscriptionNewSubscriptionOwnerAccount](docs/PreviewOrderCreateSubscriptionNewSubscriptionOwnerAccount.md)
 - [PreviewOrderOrderAction](docs/PreviewOrderOrderAction.md)
 - [PreviewOrderPricingUpdate](docs/PreviewOrderPricingUpdate.md)
 - [PreviewOrderRatePlanOverride](docs/PreviewOrderRatePlanOverride.md)
 - [PreviewOrderRatePlanUpdate](docs/PreviewOrderRatePlanUpdate.md)
 - [PreviewResult](docs/PreviewResult.md)
 - [PreviewResultChargeMetrics](docs/PreviewResultChargeMetrics.md)
 - [PreviewResultCreditMemos](docs/PreviewResultCreditMemos.md)
 - [PreviewResultInvoices](docs/PreviewResultInvoices.md)
 - [PreviewResultOrderActions](docs/PreviewResultOrderActions.md)
 - [PreviewResultOrderMetrics](docs/PreviewResultOrderMetrics.md)
 - [PriceChangeParams](docs/PriceChangeParams.md)
 - [PricingUpdate](docs/PricingUpdate.md)
 - [PricingUpdateForEvergreen](docs/PricingUpdateForEvergreen.md)
 - [ProcessingOptions](docs/ProcessingOptions.md)
 - [ProcessingOptionsElectronicPaymentOptions](docs/ProcessingOptionsElectronicPaymentOptions.md)
 - [ProductFeatureObjectCustomFields](docs/ProductFeatureObjectCustomFields.md)
 - [ProductObjectCustomFields](docs/ProductObjectCustomFields.md)
 - [ProductObjectNSFields](docs/ProductObjectNSFields.md)
 - [ProductRatePlanChargeObjectCustomFields](docs/ProductRatePlanChargeObjectCustomFields.md)
 - [ProductRatePlanChargeObjectNSFields](docs/ProductRatePlanChargeObjectNSFields.md)
 - [ProductRatePlanObjectCustomFields](docs/ProductRatePlanObjectCustomFields.md)
 - [ProductRatePlanObjectNSFields](docs/ProductRatePlanObjectNSFields.md)
 - [ProvisionEntityResponseType](docs/ProvisionEntityResponseType.md)
 - [ProxyActionamendRequest](docs/ProxyActionamendRequest.md)
 - [ProxyActionamendResponse](docs/ProxyActionamendResponse.md)
 - [ProxyActioncreateRequest](docs/ProxyActioncreateRequest.md)
 - [ProxyActiondeleteRequest](docs/ProxyActiondeleteRequest.md)
 - [ProxyActionexecuteRequest](docs/ProxyActionexecuteRequest.md)
 - [ProxyActiongenerateRequest](docs/ProxyActiongenerateRequest.md)
 - [ProxyActionqueryMoreRequest](docs/ProxyActionqueryMoreRequest.md)
 - [ProxyActionqueryMoreResponse](docs/ProxyActionqueryMoreResponse.md)
 - [ProxyActionqueryRequest](docs/ProxyActionqueryRequest.md)
 - [ProxyActionqueryRequestConf](docs/ProxyActionqueryRequestConf.md)
 - [ProxyActionqueryResponse](docs/ProxyActionqueryResponse.md)
 - [ProxyActionsubscribeRequest](docs/ProxyActionsubscribeRequest.md)
 - [ProxyActionupdateRequest](docs/ProxyActionupdateRequest.md)
 - [ProxyBadRequestResponse](docs/ProxyBadRequestResponse.md)
 - [ProxyBadRequestResponseErrors](docs/ProxyBadRequestResponseErrors.md)
 - [ProxyCreateBillRun](docs/ProxyCreateBillRun.md)
 - [ProxyCreateExport](docs/ProxyCreateExport.md)
 - [ProxyCreateInvoicePayment](docs/ProxyCreateInvoicePayment.md)
 - [ProxyCreateOrModifyResponse](docs/ProxyCreateOrModifyResponse.md)
 - [ProxyCreatePaymentGatewayOptionData](docs/ProxyCreatePaymentGatewayOptionData.md)
 - [ProxyCreateRefundRefundInvoicePaymentData](docs/ProxyCreateRefundRefundInvoicePaymentData.md)
 - [ProxyCreateUnitOfMeasure](docs/ProxyCreateUnitOfMeasure.md)
 - [ProxyDeleteResponse](docs/ProxyDeleteResponse.md)
 - [ProxyGetBillRun](docs/ProxyGetBillRun.md)
 - [ProxyGetCommunicationProfile](docs/ProxyGetCommunicationProfile.md)
 - [ProxyGetExport](docs/ProxyGetExport.md)
 - [ProxyGetImport](docs/ProxyGetImport.md)
 - [ProxyGetInvoicePayment](docs/ProxyGetInvoicePayment.md)
 - [ProxyGetInvoiceSplit](docs/ProxyGetInvoiceSplit.md)
 - [ProxyGetInvoiceSplitItem](docs/ProxyGetInvoiceSplitItem.md)
 - [ProxyGetPaymentMethod](docs/ProxyGetPaymentMethod.md)
 - [ProxyGetPaymentMethodSnapshot](docs/ProxyGetPaymentMethodSnapshot.md)
 - [ProxyGetPaymentMethodTransactionLog](docs/ProxyGetPaymentMethodTransactionLog.md)
 - [ProxyGetPaymentTransactionLog](docs/ProxyGetPaymentTransactionLog.md)
 - [ProxyGetProductRatePlanChargeTier](docs/ProxyGetProductRatePlanChargeTier.md)
 - [ProxyGetRatePlanChargeTier](docs/ProxyGetRatePlanChargeTier.md)
 - [ProxyGetRefundInvoicePayment](docs/ProxyGetRefundInvoicePayment.md)
 - [ProxyGetRefundTransactionLog](docs/ProxyGetRefundTransactionLog.md)
 - [ProxyGetUnitOfMeasure](docs/ProxyGetUnitOfMeasure.md)
 - [ProxyModifyBillRun](docs/ProxyModifyBillRun.md)
 - [ProxyModifyInvoicePayment](docs/ProxyModifyInvoicePayment.md)
 - [ProxyModifyUnitOfMeasure](docs/ProxyModifyUnitOfMeasure.md)
 - [ProxyNoDataResponse](docs/ProxyNoDataResponse.md)
 - [ProxyPostImport](docs/ProxyPostImport.md)
 - [ProxyUnauthorizedResponse](docs/ProxyUnauthorizedResponse.md)
 - [PutBatchInvoiceType](docs/PutBatchInvoiceType.md)
 - [PutCreditMemoTaxItemType](docs/PutCreditMemoTaxItemType.md)
 - [PutCreditMemoTaxItemTypeFinanceInformation](docs/PutCreditMemoTaxItemTypeFinanceInformation.md)
 - [PutDebitMemoTaxItemType](docs/PutDebitMemoTaxItemType.md)
 - [PutDebitMemoTaxItemTypeFinanceInformation](docs/PutDebitMemoTaxItemTypeFinanceInformation.md)
 - [PutEventTriggerRequest](docs/PutEventTriggerRequest.md)
 - [PutEventTriggerRequestEventType](docs/PutEventTriggerRequestEventType.md)
 - [PutInvoiceType](docs/PutInvoiceType.md)
 - [PutReverseInvoiceResponseType](docs/PutReverseInvoiceResponseType.md)
 - [PutReverseInvoiceResponseTypeCreditMemo](docs/PutReverseInvoiceResponseTypeCreditMemo.md)
 - [PutReverseInvoiceType](docs/PutReverseInvoiceType.md)
 - [RatePlan](docs/RatePlan.md)
 - [RatePlanChargeData](docs/RatePlanChargeData.md)
 - [RatePlanChargeDataInRatePlanData](docs/RatePlanChargeDataInRatePlanData.md)
 - [RatePlanChargeDataInRatePlanDataRatePlanCharge](docs/RatePlanChargeDataInRatePlanDataRatePlanCharge.md)
 - [RatePlanChargeObjectCustomFields](docs/RatePlanChargeObjectCustomFields.md)
 - [RatePlanChargeTier](docs/RatePlanChargeTier.md)
 - [RatePlanData](docs/RatePlanData.md)
 - [RatePlanDataSubscriptionProductFeatureList](docs/RatePlanDataSubscriptionProductFeatureList.md)
 - [RatePlanObjectCustomFields](docs/RatePlanObjectCustomFields.md)
 - [RatePlanOverride](docs/RatePlanOverride.md)
 - [RatePlanOverrideForEvergreen](docs/RatePlanOverrideForEvergreen.md)
 - [RatePlanUpdate](docs/RatePlanUpdate.md)
 - [RatePlanUpdateForEvergreen](docs/RatePlanUpdateForEvergreen.md)
 - [RatedItem](docs/RatedItem.md)
 - [RefundCreditMemoItemType](docs/RefundCreditMemoItemType.md)
 - [RefundInvoicePayment](docs/RefundInvoicePayment.md)
 - [RefundObjectCustomFields](docs/RefundObjectCustomFields.md)
 - [RefundObjectNSFields](docs/RefundObjectNSFields.md)
 - [RefundPartResponseType](docs/RefundPartResponseType.md)
 - [RefundPartResponseTypewithSuccess](docs/RefundPartResponseTypewithSuccess.md)
 - [RemoveProduct](docs/RemoveProduct.md)
 - [RenewalTerm](docs/RenewalTerm.md)
 - [RevenueEventItemObjectCustomFields](docs/RevenueEventItemObjectCustomFields.md)
 - [RevenueEventObjectCustomFields](docs/RevenueEventObjectCustomFields.md)
 - [RevenueScheduleItemObjectCustomFields](docs/RevenueScheduleItemObjectCustomFields.md)
 - [RevenueScheduleObjectCustomFields](docs/RevenueScheduleObjectCustomFields.md)
 - [SaveResult](docs/SaveResult.md)
 - [SubmitDataQueryRequest](docs/SubmitDataQueryRequest.md)
 - [SubmitDataQueryRequestOutput](docs/SubmitDataQueryRequestOutput.md)
 - [SubmitDataQueryResponse](docs/SubmitDataQueryResponse.md)
 - [SubscribeRequest](docs/SubscribeRequest.md)
 - [SubscribeRequestPaymentMethod](docs/SubscribeRequestPaymentMethod.md)
 - [SubscribeRequestPaymentMethodGatewayOptionData](docs/SubscribeRequestPaymentMethodGatewayOptionData.md)
 - [SubscribeRequestPreviewOptions](docs/SubscribeRequestPreviewOptions.md)
 - [SubscribeRequestSubscribeOptions](docs/SubscribeRequestSubscribeOptions.md)
 - [SubscribeRequestSubscribeOptionsElectronicPaymentOptions](docs/SubscribeRequestSubscribeOptionsElectronicPaymentOptions.md)
 - [SubscribeRequestSubscribeOptionsExternalPaymentOptions](docs/SubscribeRequestSubscribeOptionsExternalPaymentOptions.md)
 - [SubscribeRequestSubscribeOptionsSubscribeInvoiceProcessingOptions](docs/SubscribeRequestSubscribeOptionsSubscribeInvoiceProcessingOptions.md)
 - [SubscribeRequestSubscriptionData](docs/SubscribeRequestSubscriptionData.md)
 - [SubscribeResult](docs/SubscribeResult.md)
 - [SubscribeResultChargeMetricsData](docs/SubscribeResultChargeMetricsData.md)
 - [SubscribeResultInvoiceResult](docs/SubscribeResultInvoiceResult.md)
 - [SubscribeResultInvoiceResultInvoice](docs/SubscribeResultInvoiceResultInvoice.md)
 - [SubscriptionObjectCustomFields](docs/SubscriptionObjectCustomFields.md)
 - [SubscriptionObjectNSFields](docs/SubscriptionObjectNSFields.md)
 - [SubscriptionObjectQTFields](docs/SubscriptionObjectQTFields.md)
 - [SubscriptionProductFeatureList](docs/SubscriptionProductFeatureList.md)
 - [SubscriptionProductFeatureObjectCustomFields](docs/SubscriptionProductFeatureObjectCustomFields.md)
 - [SubscriptionRatedResult](docs/SubscriptionRatedResult.md)
 - [TaxInfo](docs/TaxInfo.md)
 - [TaxationItemObjectCustomFields](docs/TaxationItemObjectCustomFields.md)
 - [Term](docs/Term.md)
 - [TermsAndConditions](docs/TermsAndConditions.md)
 - [TimeSlicedElpNetMetrics](docs/TimeSlicedElpNetMetrics.md)
 - [TimeSlicedMetrics](docs/TimeSlicedMetrics.md)
 - [TimeSlicedMetricsForEvergreen](docs/TimeSlicedMetricsForEvergreen.md)
 - [TimeSlicedNetMetrics](docs/TimeSlicedNetMetrics.md)
 - [TimeSlicedNetMetricsForEvergreen](docs/TimeSlicedNetMetricsForEvergreen.md)
 - [TimeSlicedTcbNetMetrics](docs/TimeSlicedTcbNetMetrics.md)
 - [TimeSlicedTcbNetMetricsForEvergreen](docs/TimeSlicedTcbNetMetricsForEvergreen.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [TransferPaymentType](docs/TransferPaymentType.md)
 - [TriggerDate](docs/TriggerDate.md)
 - [TriggerParams](docs/TriggerParams.md)
 - [UnapplyCreditMemoType](docs/UnapplyCreditMemoType.md)
 - [UnapplyPaymentType](docs/UnapplyPaymentType.md)
 - [UpdateEntityResponseType](docs/UpdateEntityResponseType.md)
 - [UpdateEntityType](docs/UpdateEntityType.md)
 - [UsageObjectCustomFields](docs/UsageObjectCustomFields.md)
 - [ZObject](docs/ZObject.md)
 - [Account](docs/Account.md)
 - [AmendmentRatePlanChargeDataRatePlanCharge](docs/AmendmentRatePlanChargeDataRatePlanCharge.md)
 - [BillToContact](docs/BillToContact.md)
 - [BillToContactPostOrder](docs/BillToContactPostOrder.md)
 - [CreateOrderCreateSubscriptionNewSubscriptionOwnerAccount](docs/CreateOrderCreateSubscriptionNewSubscriptionOwnerAccount.md)
 - [CreatePaymentType](docs/CreatePaymentType.md)
 - [CreditMemoFromChargeDetailType](docs/CreditMemoFromChargeDetailType.md)
 - [CreditMemoFromChargeType](docs/CreditMemoFromChargeType.md)
 - [CreditMemoFromInvoiceType](docs/CreditMemoFromInvoiceType.md)
 - [CreditMemoItemFromInvoiceItemType](docs/CreditMemoItemFromInvoiceItemType.md)
 - [CreditMemoItemFromWriteOffInvoice](docs/CreditMemoItemFromWriteOffInvoice.md)
 - [DataQueryJob](docs/DataQueryJob.md)
 - [DataQueryJobCancelled](docs/DataQueryJobCancelled.md)
 - [DebitMemoFromChargeDetailType](docs/DebitMemoFromChargeDetailType.md)
 - [DebitMemoFromChargeType](docs/DebitMemoFromChargeType.md)
 - [DebitMemoFromInvoiceType](docs/DebitMemoFromInvoiceType.md)
 - [DebitMemoItemFromInvoiceItemType](docs/DebitMemoItemFromInvoiceItemType.md)
 - [EventRevenueItemType](docs/EventRevenueItemType.md)
 - [GETARPaymentType](docs/GETARPaymentType.md)
 - [GETARPaymentTypewithSuccess](docs/GETARPaymentTypewithSuccess.md)
 - [GETAccountSummarySubscriptionType](docs/GETAccountSummarySubscriptionType.md)
 - [GETAccountSummaryTypeBasicInfo](docs/GETAccountSummaryTypeBasicInfo.md)
 - [GETAccountSummaryTypeBillToContact](docs/GETAccountSummaryTypeBillToContact.md)
 - [GETAccountSummaryTypeSoldToContact](docs/GETAccountSummaryTypeSoldToContact.md)
 - [GETAccountTypeBasicInfo](docs/GETAccountTypeBasicInfo.md)
 - [GETAccountTypeBillToContact](docs/GETAccountTypeBillToContact.md)
 - [GETAccountTypeSoldToContact](docs/GETAccountTypeSoldToContact.md)
 - [GETAccountingCodeItemType](docs/GETAccountingCodeItemType.md)
 - [GETAccountingCodeItemWithoutSuccessType](docs/GETAccountingCodeItemWithoutSuccessType.md)
 - [GETAccountingPeriodType](docs/GETAccountingPeriodType.md)
 - [GETAccountingPeriodWithoutSuccessType](docs/GETAccountingPeriodWithoutSuccessType.md)
 - [GETCreditMemoItemType](docs/GETCreditMemoItemType.md)
 - [GETCreditMemoItemTypewithSuccess](docs/GETCreditMemoItemTypewithSuccess.md)
 - [GETCreditMemoType](docs/GETCreditMemoType.md)
 - [GETCreditMemoTypewithSuccess](docs/GETCreditMemoTypewithSuccess.md)
 - [GETDebitMemoItemType](docs/GETDebitMemoItemType.md)
 - [GETDebitMemoItemTypewithSuccess](docs/GETDebitMemoItemTypewithSuccess.md)
 - [GETDebitMemoType](docs/GETDebitMemoType.md)
 - [GETDebitMemoTypewithSuccess](docs/GETDebitMemoTypewithSuccess.md)
 - [GETInvoiceType](docs/GETInvoiceType.md)
 - [GETJournalEntryDetailType](docs/GETJournalEntryDetailType.md)
 - [GETJournalEntryDetailTypeWithoutSuccess](docs/GETJournalEntryDetailTypeWithoutSuccess.md)
 - [GETJournalEntryItemType](docs/GETJournalEntryItemType.md)
 - [GETPaymentType](docs/GETPaymentType.md)
 - [GETProductRatePlanChargeType](docs/GETProductRatePlanChargeType.md)
 - [GETProductRatePlanType](docs/GETProductRatePlanType.md)
 - [GETProductType](docs/GETProductType.md)
 - [GETRSDetailForProductChargeType](docs/GETRSDetailForProductChargeType.md)
 - [GETRSDetailType](docs/GETRSDetailType.md)
 - [GETRSDetailWithoutSuccessType](docs/GETRSDetailWithoutSuccessType.md)
 - [GETRefundCreditMemoType](docs/GETRefundCreditMemoType.md)
 - [GETRefundPaymentType](docs/GETRefundPaymentType.md)
 - [GETRefundType](docs/GETRefundType.md)
 - [GETRefundTypewithSuccess](docs/GETRefundTypewithSuccess.md)
 - [GETRevenueEventDetailType](docs/GETRevenueEventDetailType.md)
 - [GETRevenueEventDetailWithoutSuccessType](docs/GETRevenueEventDetailWithoutSuccessType.md)
 - [GETRevenueItemType](docs/GETRevenueItemType.md)
 - [GETRsRevenueItemType](docs/GETRsRevenueItemType.md)
 - [GETSubscriptionRatePlanChargesType](docs/GETSubscriptionRatePlanChargesType.md)
 - [GETSubscriptionRatePlanType](docs/GETSubscriptionRatePlanType.md)
 - [GETSubscriptionType](docs/GETSubscriptionType.md)
 - [GETSubscriptionTypeWithSuccess](docs/GETSubscriptionTypeWithSuccess.md)
 - [GETTaxationItemType](docs/GETTaxationItemType.md)
 - [GETTaxationItemTypewithSuccess](docs/GETTaxationItemTypewithSuccess.md)
 - [GETUsageType](docs/GETUsageType.md)
 - [GetCreditMemoAmountBreakdownByOrderResponse](docs/GetCreditMemoAmountBreakdownByOrderResponse.md)
 - [GetInvoiceAmountBreakdownByOrderResponse](docs/GetInvoiceAmountBreakdownByOrderResponse.md)
 - [GetOrderBillingInfoResponseType](docs/GetOrderBillingInfoResponseType.md)
 - [GetOrderRatedResultResponseType](docs/GetOrderRatedResultResponseType.md)
 - [GetOrderResponse](docs/GetOrderResponse.md)
 - [GetOrderResponseForEvergreen](docs/GetOrderResponseForEvergreen.md)
 - [GetOrdersResponse](docs/GetOrdersResponse.md)
 - [GetProductFeatureType](docs/GetProductFeatureType.md)
 - [GetSubscriptionTermInfoResponseType](docs/GetSubscriptionTermInfoResponseType.md)
 - [InvoiceDataInvoice](docs/InvoiceDataInvoice.md)
 - [InvoiceItem](docs/InvoiceItem.md)
 - [JobResult](docs/JobResult.md)
 - [POSTAccountType](docs/POSTAccountType.md)
 - [POSTAccountTypeBillToContact](docs/POSTAccountTypeBillToContact.md)
 - [POSTAccountTypeCreditCard](docs/POSTAccountTypeCreditCard.md)
 - [POSTAccountTypeSoldToContact](docs/POSTAccountTypeSoldToContact.md)
 - [POSTAccountTypeSubscription](docs/POSTAccountTypeSubscription.md)
 - [POSTAccountingCodeType](docs/POSTAccountingCodeType.md)
 - [POSTAccountingPeriodType](docs/POSTAccountingPeriodType.md)
 - [POSTJournalEntryItemType](docs/POSTJournalEntryItemType.md)
 - [POSTJournalEntryType](docs/POSTJournalEntryType.md)
 - [POSTPaymentMethodRequest](docs/POSTPaymentMethodRequest.md)
 - [POSTPaymentMethodResponse](docs/POSTPaymentMethodResponse.md)
 - [POSTPaymentMethodType](docs/POSTPaymentMethodType.md)
 - [POSTRevenueScheduleByChargeType](docs/POSTRevenueScheduleByChargeType.md)
 - [POSTRevenueScheduleByChargeTypeRevenueEvent](docs/POSTRevenueScheduleByChargeTypeRevenueEvent.md)
 - [POSTRevenueScheduleByDateRangeType](docs/POSTRevenueScheduleByDateRangeType.md)
 - [POSTRevenueScheduleByDateRangeTypeRevenueEvent](docs/POSTRevenueScheduleByDateRangeTypeRevenueEvent.md)
 - [POSTRevenueScheduleByTransactionRatablyCMType](docs/POSTRevenueScheduleByTransactionRatablyCMType.md)
 - [POSTRevenueScheduleByTransactionRatablyDMType](docs/POSTRevenueScheduleByTransactionRatablyDMType.md)
 - [POSTRevenueScheduleByTransactionRatablyTypeRevenueEvent](docs/POSTRevenueScheduleByTransactionRatablyTypeRevenueEvent.md)
 - [POSTRevenueScheduleByTransactionType](docs/POSTRevenueScheduleByTransactionType.md)
 - [POSTRevenueScheduleByTransactionTypeRevenueEvent](docs/POSTRevenueScheduleByTransactionTypeRevenueEvent.md)
 - [POSTScCreateType](docs/POSTScCreateType.md)
 - [POSTSrpCreateType](docs/POSTSrpCreateType.md)
 - [POSTSubscriptionPreviewType](docs/POSTSubscriptionPreviewType.md)
 - [POSTSubscriptionPreviewTypePreviewAccountInfo](docs/POSTSubscriptionPreviewTypePreviewAccountInfo.md)
 - [POSTSubscriptionType](docs/POSTSubscriptionType.md)
 - [POSTTaxationItemForCMType](docs/POSTTaxationItemForCMType.md)
 - [POSTTaxationItemForDMType](docs/POSTTaxationItemForDMType.md)
 - [PUTAccountType](docs/PUTAccountType.md)
 - [PUTAccountTypeBillToContact](docs/PUTAccountTypeBillToContact.md)
 - [PUTAccountTypeSoldToContact](docs/PUTAccountTypeSoldToContact.md)
 - [PUTAccountingCodeType](docs/PUTAccountingCodeType.md)
 - [PUTAccountingPeriodType](docs/PUTAccountingPeriodType.md)
 - [PUTAllocateManuallyType](docs/PUTAllocateManuallyType.md)
 - [PUTBasicSummaryJournalEntryType](docs/PUTBasicSummaryJournalEntryType.md)
 - [PUTCreditMemoItemType](docs/PUTCreditMemoItemType.md)
 - [PUTCreditMemoType](docs/PUTCreditMemoType.md)
 - [PUTDebitMemoItemType](docs/PUTDebitMemoItemType.md)
 - [PUTDebitMemoType](docs/PUTDebitMemoType.md)
 - [PUTJournalEntryItemType](docs/PUTJournalEntryItemType.md)
 - [PUTOrderTriggerDatesResponseType](docs/PUTOrderTriggerDatesResponseType.md)
 - [PUTPaymentMethodType](docs/PUTPaymentMethodType.md)
 - [PUTRSBasicInfoType](docs/PUTRSBasicInfoType.md)
 - [PUTRSTermType](docs/PUTRSTermType.md)
 - [PUTRefundType](docs/PUTRefundType.md)
 - [PUTScAddType](docs/PUTScAddType.md)
 - [PUTScUpdateType](docs/PUTScUpdateType.md)
 - [PUTSpecificDateAllocationType](docs/PUTSpecificDateAllocationType.md)
 - [PUTSrpAddType](docs/PUTSrpAddType.md)
 - [PUTSrpUpdateType](docs/PUTSrpUpdateType.md)
 - [PUTSubscriptionType](docs/PUTSubscriptionType.md)
 - [PUTTaxationItemType](docs/PUTTaxationItemType.md)
 - [PUTWriteOffInvoiceRequest](docs/PUTWriteOffInvoiceRequest.md)
 - [PostNonRefRefundType](docs/PostNonRefRefundType.md)
 - [PostOrderPreviewResponseType](docs/PostOrderPreviewResponseType.md)
 - [PostOrderResponseType](docs/PostOrderResponseType.md)
 - [PostRefundType](docs/PostRefundType.md)
 - [ProxyCreateAccount](docs/ProxyCreateAccount.md)
 - [ProxyCreateContact](docs/ProxyCreateContact.md)
 - [ProxyCreateCreditBalanceAdjustment](docs/ProxyCreateCreditBalanceAdjustment.md)
 - [ProxyCreateInvoiceAdjustment](docs/ProxyCreateInvoiceAdjustment.md)
 - [ProxyCreatePayment](docs/ProxyCreatePayment.md)
 - [ProxyCreatePaymentMethod](docs/ProxyCreatePaymentMethod.md)
 - [ProxyCreateProduct](docs/ProxyCreateProduct.md)
 - [ProxyCreateProductRatePlan](docs/ProxyCreateProductRatePlan.md)
 - [ProxyCreateProductRatePlanCharge](docs/ProxyCreateProductRatePlanCharge.md)
 - [ProxyCreateRefund](docs/ProxyCreateRefund.md)
 - [ProxyCreateTaxationItem](docs/ProxyCreateTaxationItem.md)
 - [ProxyCreateUsage](docs/ProxyCreateUsage.md)
 - [ProxyGetAccount](docs/ProxyGetAccount.md)
 - [ProxyGetAmendment](docs/ProxyGetAmendment.md)
 - [ProxyGetContact](docs/ProxyGetContact.md)
 - [ProxyGetCreditBalanceAdjustment](docs/ProxyGetCreditBalanceAdjustment.md)
 - [ProxyGetFeature](docs/ProxyGetFeature.md)
 - [ProxyGetInvoice](docs/ProxyGetInvoice.md)
 - [ProxyGetInvoiceAdjustment](docs/ProxyGetInvoiceAdjustment.md)
 - [ProxyGetInvoiceItem](docs/ProxyGetInvoiceItem.md)
 - [ProxyGetInvoiceItemAdjustment](docs/ProxyGetInvoiceItemAdjustment.md)
 - [ProxyGetPayment](docs/ProxyGetPayment.md)
 - [ProxyGetProduct](docs/ProxyGetProduct.md)
 - [ProxyGetProductFeature](docs/ProxyGetProductFeature.md)
 - [ProxyGetProductRatePlan](docs/ProxyGetProductRatePlan.md)
 - [ProxyGetProductRatePlanCharge](docs/ProxyGetProductRatePlanCharge.md)
 - [ProxyGetRatePlan](docs/ProxyGetRatePlan.md)
 - [ProxyGetRatePlanCharge](docs/ProxyGetRatePlanCharge.md)
 - [ProxyGetRefund](docs/ProxyGetRefund.md)
 - [ProxyGetSubscription](docs/ProxyGetSubscription.md)
 - [ProxyGetSubscriptionProductFeature](docs/ProxyGetSubscriptionProductFeature.md)
 - [ProxyGetTaxationItem](docs/ProxyGetTaxationItem.md)
 - [ProxyGetUsage](docs/ProxyGetUsage.md)
 - [ProxyModifyAccount](docs/ProxyModifyAccount.md)
 - [ProxyModifyAmendment](docs/ProxyModifyAmendment.md)
 - [ProxyModifyContact](docs/ProxyModifyContact.md)
 - [ProxyModifyCreditBalanceAdjustment](docs/ProxyModifyCreditBalanceAdjustment.md)
 - [ProxyModifyInvoice](docs/ProxyModifyInvoice.md)
 - [ProxyModifyInvoiceAdjustment](docs/ProxyModifyInvoiceAdjustment.md)
 - [ProxyModifyPayment](docs/ProxyModifyPayment.md)
 - [ProxyModifyPaymentMethod](docs/ProxyModifyPaymentMethod.md)
 - [ProxyModifyProduct](docs/ProxyModifyProduct.md)
 - [ProxyModifyProductRatePlan](docs/ProxyModifyProductRatePlan.md)
 - [ProxyModifyProductRatePlanCharge](docs/ProxyModifyProductRatePlanCharge.md)
 - [ProxyModifyRefund](docs/ProxyModifyRefund.md)
 - [ProxyModifySubscription](docs/ProxyModifySubscription.md)
 - [ProxyModifyTaxationItem](docs/ProxyModifyTaxationItem.md)
 - [ProxyModifyUsage](docs/ProxyModifyUsage.md)
 - [PutInvoiceResponseType](docs/PutInvoiceResponseType.md)
 - [RatePlanChargeDataRatePlanCharge](docs/RatePlanChargeDataRatePlanCharge.md)
 - [RatePlanDataRatePlan](docs/RatePlanDataRatePlan.md)
 - [RecurringFlatFeePricingOverride](docs/RecurringFlatFeePricingOverride.md)
 - [RecurringFlatFeePricingUpdate](docs/RecurringFlatFeePricingUpdate.md)
 - [RecurringPerUnitPricingOverride](docs/RecurringPerUnitPricingOverride.md)
 - [RecurringPerUnitPricingUpdate](docs/RecurringPerUnitPricingUpdate.md)
 - [RecurringTieredPricingOverride](docs/RecurringTieredPricingOverride.md)
 - [RecurringTieredPricingUpdate](docs/RecurringTieredPricingUpdate.md)
 - [RecurringVolumePricingOverride](docs/RecurringVolumePricingOverride.md)
 - [RecurringVolumePricingUpdate](docs/RecurringVolumePricingUpdate.md)
 - [RevenueScheduleItemType](docs/RevenueScheduleItemType.md)
 - [SoldToContact](docs/SoldToContact.md)
 - [SoldToContactPostOrder](docs/SoldToContactPostOrder.md)
 - [SubscribeRequestAccount](docs/SubscribeRequestAccount.md)
 - [SubscribeRequestBillToContact](docs/SubscribeRequestBillToContact.md)
 - [SubscribeRequestSoldToContact](docs/SubscribeRequestSoldToContact.md)
 - [SubscribeRequestSubscriptionDataSubscription](docs/SubscribeRequestSubscriptionDataSubscription.md)
 - [SubscriptionProductFeature](docs/SubscriptionProductFeature.md)
 - [UpdatePaymentType](docs/UpdatePaymentType.md)
 - [UsageFlatFeePricingOverride](docs/UsageFlatFeePricingOverride.md)
 - [UsageFlatFeePricingUpdate](docs/UsageFlatFeePricingUpdate.md)
 - [UsageOveragePricingOverride](docs/UsageOveragePricingOverride.md)
 - [UsageOveragePricingUpdate](docs/UsageOveragePricingUpdate.md)
 - [UsagePerUnitPricingOverride](docs/UsagePerUnitPricingOverride.md)
 - [UsagePerUnitPricingUpdate](docs/UsagePerUnitPricingUpdate.md)
 - [UsageTieredPricingOverride](docs/UsageTieredPricingOverride.md)
 - [UsageTieredPricingUpdate](docs/UsageTieredPricingUpdate.md)
 - [UsageTieredWithOveragePricingOverride](docs/UsageTieredWithOveragePricingOverride.md)
 - [UsageTieredWithOveragePricingUpdate](docs/UsageTieredWithOveragePricingUpdate.md)
 - [UsageVolumePricingOverride](docs/UsageVolumePricingOverride.md)
 - [UsageVolumePricingUpdate](docs/UsageVolumePricingUpdate.md)
 - [ZObjectUpdate](docs/ZObjectUpdate.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

docs@zuora.com

