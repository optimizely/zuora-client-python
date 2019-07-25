# coding: utf-8

"""
    Zuora API Reference

      # Introduction Welcome to the reference for the Zuora REST API!  <a href=\"http://en.wikipedia.org/wiki/REST_API\" target=\"_blank\">REST</a> is a web-service protocol that lends itself to rapid development by using everyday HTTP and JSON technology.  The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Production | https://rest.zuora.com   | |US API Sandbox    | https://rest.apisandbox.zuora.com| |US Performance Test | https://rest.pt1.zuora.com | |EU Production | https://rest.eu.zuora.com | |EU Sandbox | https://rest.sandbox.eu.zuora.com |  The Production endpoint provides access to your live user data. API Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision an API Sandbox tenant for you, contact your Zuora representative for assistance.  **Note:** If you have a tenant in the Production Copy Environment, submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints.  If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.  # API Changelog You can find the <a href=\"https://community.zuora.com/t5/Developers/API-Changelog/gpm-p/18092\" target=\"_blank\">Changelog</a> of the API Reference in the Zuora Community.  # Authentication  ## OAuth v2.0  Zuora recommends that you use OAuth v2.0 to authenticate to the Zuora REST API. Currently, OAuth is not available in every environment. See [Zuora Testing Environments](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Environments) for more information.  Zuora recommends you to create a dedicated API user with API write access on a tenant when authenticating via OAuth, and then create an OAuth client for this user. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for how to do this. By creating a dedicated API user, you can control permissions of the API user without affecting other non-API users.  If a user is deactivated, all of the user's OAuth clients will be automatically deactivated.  Authenticating via OAuth requires the following steps: 1. Create a Client 2. Generate a Token 3. Make Authenticated Requests  ### Create a Client  You must first [create an OAuth client](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) in the Zuora UI. To do this, you must be an administrator of your Zuora tenant. This is a one-time operation. You will be provided with a Client ID and a Client Secret. Please note this information down, as it will be required for the next step.  **Note:** The OAuth client will be owned by a Zuora user account. If you want to perform PUT, POST, or DELETE operations using the OAuth client, the owner of the OAuth client must have a Platform role that includes the \"API Write Access\" permission.  ### Generate a Token  After creating a client, you must make a call to obtain a bearer token using the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) operation. This operation requires the following parameters: - `client_id` - the Client ID displayed when you created the OAuth client in the previous step - `client_secret` - the Client Secret displayed when you created the OAuth client in the previous step - `grant_type` - must be set to `client_credentials`  **Note**: The Client ID and Client Secret mentioned above were displayed when you created the OAuth Client in the prior step. The [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response specifies how long the bearer token is valid for. Call [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) again to generate a new bearer token.  ### Make Authenticated Requests  To authenticate subsequent API requests, you must provide a valid bearer token in an HTTP header:  `Authorization: Bearer {bearer_token}`  If you have [Zuora Multi-entity](https://www.zuora.com/developer/api-reference/#tag/Entities) enabled, you need to set an additional header to specify the ID of the entity that you want to access. You can use the `scope` field in the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response to determine whether you need to specify an entity ID.  If the `scope` field contains more than one entity ID, you must specify the ID of the entity that you want to access. For example, if the `scope` field contains `entity.1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` and `entity.c92ed977-510c-4c48-9b51-8d5e848671e9`, specify one of the following headers: - `Zuora-Entity-Ids: 1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` - `Zuora-Entity-Ids: c92ed977-510c-4c48-9b51-8d5e848671e9`  **Note**: For a limited period of time, Zuora will accept the `entityId` header as an alternative to the `Zuora-Entity-Ids` header. If you choose to set the `entityId` header, you must remove all \"-\" characters from the entity ID in the `scope` field.  If the `scope` field contains a single entity ID, you do not need to specify an entity ID.  ## Other Supported Authentication Schemes  Zuora continues to support the following additional legacy means of authentication:    * Use username and password. Include authentication with each request in the header:         * `apiAccessKeyId`      * `apiSecretAccessKey`          Zuora recommends that you create an API user specifically for making API calls. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for more information.      * Use an authorization cookie. The cookie authorizes the user to make calls to the REST API for the duration specified in  **Administration > Security Policies > Session timeout**. The cookie expiration time is reset with this duration after every call to the REST API. To obtain a cookie, call the [Connections](https://www.zuora.com/developer/api-reference/#tag/Connections) resource with the following API user information:         *   ID         *   Password        * For CORS-enabled APIs only: Include a 'single-use' token in the request header, which re-authenticates the user with each request. See below for more details.  ### Entity Id and Entity Name  The `entityId` and `entityName` parameters are only used for [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity \"Zuora Multi-entity\"). These are the legacy parameters that Zuora will only continue to support for a period of time. Zuora recommends you to use the `Zuora-Entity-Ids` parameter instead.   The  `entityId` and `entityName` parameters specify the Id and the [name of the entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/B_Introduction_to_Entity_and_Entity_Hierarchy#Name_and_Display_Name \"Introduction to Entity and Entity Hierarchy\") that you want to access, respectively. Note that you must have permission to access the entity.   You can specify either the `entityId` or `entityName` parameter in the authentication to access and view an entity.    * If both `entityId` and `entityName` are specified in the authentication, an error occurs.    * If neither `entityId` nor `entityName` is specified in the authentication, you will log in to the entity in which your user account is created.      To get the entity Id and entity name, you can use the GET Entities REST call. For more information, see [API User Authentication](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/A_Overview_of_Multi-entity#API_User_Authentication \"API User Authentication\").      ### Token Authentication for CORS-Enabled APIs      The CORS mechanism enables REST API calls to Zuora to be made directly from your customer's browser, with all credit card and security information transmitted directly to Zuora. This minimizes your PCI compliance burden, allows you to implement advanced validation on your payment forms, and  makes your payment forms look just like any other part of your website.    For security reasons, instead of using cookies, an API request via CORS uses **tokens** for authentication.  The token method of authentication is only designed for use with requests that must originate from your customer's browser; **it should  not be considered a replacement to the existing cookie authentication** mechanism.  See [Zuora CORS REST](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Zuora_CORS_REST \"Zuora CORS REST\") for details on how CORS works and how you can begin to implement customer calls to the Zuora REST APIs. See  [HMAC Signatures](https://www.zuora.com/developer/api-reference/#operation/POSTHMACSignature \"HMAC Signatures\") for details on the HMAC method that returns the authentication token.  # Requests and Responses  ## Request IDs  As a general rule, when asked to supply a \"key\" for an account or subscription (accountKey, account-key, subscriptionKey, subscription-key), you can provide either the actual ID or  the number of the entity.  ## HTTP Request Body  Most of the parameters and data accompanying your requests will be contained in the body of the HTTP request.   The Zuora REST API accepts JSON in the HTTP request body. No other data format (e.g., XML) is supported.  ### Data Type  ([Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations only) We recommend that you do not specify the decimal values with quotation marks, commas, and spaces. Use characters of `+-0-9.eE`, for example, `5`, `1.9`, `-8.469`, and `7.7e2`. Also, Zuora does not convert currencies for decimal values.  ## Testing a Request  Use a third party client, such as [curl](https://curl.haxx.se \"curl\"), [Postman](https://www.getpostman.com \"Postman\"), or [Advanced REST Client](https://advancedrestclient.com \"Advanced REST Client\"), to test the Zuora REST API.  You can test the Zuora REST API from the Zuora API Sandbox or Production tenants. If connecting to Production, bear in mind that you are working with your live production data, not sample data or test data.  ## Testing with Credit Cards  Sooner or later it will probably be necessary to test some transactions that involve credit cards. For suggestions on how to handle this, see [Going Live With Your Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards \"C_Zuora_User_Guides/A_Billing_and_Payments/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards\" ).  ## Concurrent Request Limits  Zuora enforces tenant-level concurrent request limits. See <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits\" target=\"_blank\">Concurrent Request Limits</a> for more information.  ## Timeout Limit  If a request does not complete within 120 seconds, the request times out and Zuora returns a Gateway Timeout error.  ## Error Handling  Responses and error codes are detailed in [Responses and errors](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Responses_and_Errors \"Responses and errors\").  # Pagination  When retrieving information (using GET methods), the optional `pageSize` query parameter sets the maximum number of rows to return in a response. The maximum is `40`; larger values are treated as `40`. If this value is empty or invalid, `pageSize` typically defaults to `10`.  The default value for the maximum number of rows retrieved can be overridden at the method level.  If more rows are available, the response will include a `nextPage` element, which contains a URL for requesting the next page.  If this value is not provided, no more rows are available. No \"previous page\" element is explicitly provided; to support backward paging, use the previous call.  ## Array Size  For data items that are not paginated, the REST API supports arrays of up to 300 rows.  Thus, for instance, repeated pagination can retrieve thousands of customer accounts, but within any account an array of no more than 300 rate plans is returned.  # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.  ## Major Version  The major version number of the REST API appears in the REST URL. Currently, Zuora only supports the **v1** major version. For example, `POST https://rest.zuora.com/v1/subscriptions`.  ## Minor Version  Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.   Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not serial. This section documents the changes made to each Zuora REST API minor version.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 196.0 and earlier  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. | | creditTaxItems | 238.0 and earlier | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\") | Container for the taxation items of the credit memo item. | | taxItems | 238.0 and earlier | [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the debit memo item. | | taxationItems | 239.0 and later | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the memo item. |   #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") and [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics  # Zuora Object Model  The following diagram presents a high-level view of the key Zuora objects. Click the image to open it in a new tab to resize it.  <a href=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" target=\"_blank\"><img src=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" alt=\"Zuora Object Model Diagram\"></a>  See the following articles for information about other parts of the Zuora business object model:    * <a href=\"https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/D_Invoice_Settlement_Object_Model\" target=\"_blank\">Invoice Settlement Object Model</a>   * <a href=\"https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/BA_Orders_Object_Model\" target=\"_blank\">Orders Object Model</a>  You can use the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun`</p><p>**Note:** The API name of this object is `BillingRun` in the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation, Export ZOQL queries, and Data Query. Otherwise, the API name of this object is `BillRun`.</p> | | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Feature                                       | `Feature`                                  | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                         | `UpdaterDetail`                            | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Feature                               | `ProductFeature`                           | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Subscription Product Feature                  | `SubscriptionProductFeature`               | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    |   # noqa: E501

    OpenAPI spec version: 2019-05-27-codegen-workaround
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class POSTPublicEmailTemplateRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'active': 'bool',
        'bcc_email_address': 'str',
        'cc_email_address': 'str',
        'cc_email_type': 'str',
        'description': 'str',
        'email_body': 'str',
        'email_subject': 'str',
        'encoding_type': 'str',
        'event_type_name': 'str',
        'event_type_namespace': 'str',
        'from_email_address': 'str',
        'from_email_type': 'str',
        'from_name': 'str',
        'is_html': 'bool',
        'name': 'str',
        'reply_to_email_address': 'str',
        'reply_to_email_type': 'str',
        'to_email_address': 'str',
        'to_email_type': 'str'
    }

    attribute_map = {
        'active': 'active',
        'bcc_email_address': 'bccEmailAddress',
        'cc_email_address': 'ccEmailAddress',
        'cc_email_type': 'ccEmailType',
        'description': 'description',
        'email_body': 'emailBody',
        'email_subject': 'emailSubject',
        'encoding_type': 'encodingType',
        'event_type_name': 'eventTypeName',
        'event_type_namespace': 'eventTypeNamespace',
        'from_email_address': 'fromEmailAddress',
        'from_email_type': 'fromEmailType',
        'from_name': 'fromName',
        'is_html': 'isHtml',
        'name': 'name',
        'reply_to_email_address': 'replyToEmailAddress',
        'reply_to_email_type': 'replyToEmailType',
        'to_email_address': 'toEmailAddress',
        'to_email_type': 'toEmailType'
    }

    def __init__(self, active=True, bcc_email_address=None, cc_email_address=None, cc_email_type='SpecificEmails', description=None, email_body=None, email_subject=None, encoding_type='UTF8', event_type_name=None, event_type_namespace=None, from_email_address=None, from_email_type=None, from_name=None, is_html=False, name=None, reply_to_email_address=None, reply_to_email_type=None, to_email_address=None, to_email_type=None):  # noqa: E501
        """POSTPublicEmailTemplateRequest - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._bcc_email_address = None
        self._cc_email_address = None
        self._cc_email_type = None
        self._description = None
        self._email_body = None
        self._email_subject = None
        self._encoding_type = None
        self._event_type_name = None
        self._event_type_namespace = None
        self._from_email_address = None
        self._from_email_type = None
        self._from_name = None
        self._is_html = None
        self._name = None
        self._reply_to_email_address = None
        self._reply_to_email_type = None
        self._to_email_address = None
        self._to_email_type = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if bcc_email_address is not None:
            self.bcc_email_address = bcc_email_address
        if cc_email_address is not None:
            self.cc_email_address = cc_email_address
        if cc_email_type is not None:
            self.cc_email_type = cc_email_type
        if description is not None:
            self.description = description
        self.email_body = email_body
        self.email_subject = email_subject
        if encoding_type is not None:
            self.encoding_type = encoding_type
        self.event_type_name = event_type_name
        if event_type_namespace is not None:
            self.event_type_namespace = event_type_namespace
        if from_email_address is not None:
            self.from_email_address = from_email_address
        self.from_email_type = from_email_type
        if from_name is not None:
            self.from_name = from_name
        if is_html is not None:
            self.is_html = is_html
        self.name = name
        if reply_to_email_address is not None:
            self.reply_to_email_address = reply_to_email_address
        if reply_to_email_type is not None:
            self.reply_to_email_type = reply_to_email_type
        if to_email_address is not None:
            self.to_email_address = to_email_address
        self.to_email_type = to_email_type

    @property
    def active(self):
        """Gets the active of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The status of the email template. The default value is true.  # noqa: E501

        :return: The active of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this POSTPublicEmailTemplateRequest.

        The status of the email template. The default value is true.  # noqa: E501

        :param active: The active of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def bcc_email_address(self):
        """Gets the bcc_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The email bcc address.  # noqa: E501

        :return: The bcc_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._bcc_email_address

    @bcc_email_address.setter
    def bcc_email_address(self, bcc_email_address):
        """Sets the bcc_email_address of this POSTPublicEmailTemplateRequest.

        The email bcc address.  # noqa: E501

        :param bcc_email_address: The bcc_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._bcc_email_address = bcc_email_address

    @property
    def cc_email_address(self):
        """Gets the cc_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The email CC address.  # noqa: E501

        :return: The cc_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._cc_email_address

    @cc_email_address.setter
    def cc_email_address(self, cc_email_address):
        """Sets the cc_email_address of this POSTPublicEmailTemplateRequest.

        The email CC address.  # noqa: E501

        :param cc_email_address: The cc_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._cc_email_address = cc_email_address

    @property
    def cc_email_type(self):
        """Gets the cc_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501

        Email CC type: * When EventType is CDC/External and 'ReferenceObjectType' in EventType is associated to Account, ccEmailType can be ALL values in enum.  * When EventType is CDC/External and 'ReferenceObjectType' in EventType is not associated to Account, ccEmailType MUST be TenantAdmin, RunOwner or SpecificEmail.  * When EventType is CDC/External and 'ReferenceObjectType' in EventType is EMPTY, ccEmailType MUST be TenantAdmin, RunOwner or SpecificEmail.  # noqa: E501

        :return: The cc_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._cc_email_type

    @cc_email_type.setter
    def cc_email_type(self, cc_email_type):
        """Sets the cc_email_type of this POSTPublicEmailTemplateRequest.

        Email CC type: * When EventType is CDC/External and 'ReferenceObjectType' in EventType is associated to Account, ccEmailType can be ALL values in enum.  * When EventType is CDC/External and 'ReferenceObjectType' in EventType is not associated to Account, ccEmailType MUST be TenantAdmin, RunOwner or SpecificEmail.  * When EventType is CDC/External and 'ReferenceObjectType' in EventType is EMPTY, ccEmailType MUST be TenantAdmin, RunOwner or SpecificEmail.  # noqa: E501

        :param cc_email_type: The cc_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["BillToContact", "SoldToContact", "SpecificEmails", "TenantAdmin", "BillToAndSoldToContacts", "RunOwner", "AllContacts", "InvoiceOwnerBillToContact", "InvoiceOwnerSoldToContact", "InvoiceOwnerBillToAndSoldToContacts", "InvoiceOwnerAllContacts"]  # noqa: E501
        if cc_email_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cc_email_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cc_email_type, allowed_values)
            )

        self._cc_email_type = cc_email_type

    @property
    def description(self):
        """Gets the description of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The description of the email template.  # noqa: E501

        :return: The description of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this POSTPublicEmailTemplateRequest.

        The description of the email template.  # noqa: E501

        :param description: The description of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_body(self):
        """Gets the email_body of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The email body. You can add merge fields in the email object using angle brackets.  You can also embed HTML tags if 'isHtml' is true.  # noqa: E501

        :return: The email_body of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_body

    @email_body.setter
    def email_body(self, email_body):
        """Sets the email_body of this POSTPublicEmailTemplateRequest.

        The email body. You can add merge fields in the email object using angle brackets.  You can also embed HTML tags if 'isHtml' is true.  # noqa: E501

        :param email_body: The email_body of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """
        if email_body is None:
            raise ValueError("Invalid value for `email_body`, must not be `None`")  # noqa: E501

        self._email_body = email_body

    @property
    def email_subject(self):
        """Gets the email_subject of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The email subject. Users can add merge fields in the email subject using angle brackets.  # noqa: E501

        :return: The email_subject of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """Sets the email_subject of this POSTPublicEmailTemplateRequest.

        The email subject. Users can add merge fields in the email subject using angle brackets.  # noqa: E501

        :param email_subject: The email_subject of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """
        if email_subject is None:
            raise ValueError("Invalid value for `email_subject`, must not be `None`")  # noqa: E501

        self._email_subject = email_subject

    @property
    def encoding_type(self):
        """Gets the encoding_type of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The endcode type of the email body.  # noqa: E501

        :return: The encoding_type of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._encoding_type

    @encoding_type.setter
    def encoding_type(self, encoding_type):
        """Sets the encoding_type of this POSTPublicEmailTemplateRequest.

        The endcode type of the email body.  # noqa: E501

        :param encoding_type: The encoding_type of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["UTF8", "Shift_JIS", "ISO_2022_JP", "EUC_JP", "X_SJIS_0213"]  # noqa: E501
        if encoding_type not in allowed_values:
            raise ValueError(
                "Invalid value for `encoding_type` ({0}), must be one of {1}"  # noqa: E501
                .format(encoding_type, allowed_values)
            )

        self._encoding_type = encoding_type

    @property
    def event_type_name(self):
        """Gets the event_type_name of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The name of the event type.    # noqa: E501

        :return: The event_type_name of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._event_type_name

    @event_type_name.setter
    def event_type_name(self, event_type_name):
        """Sets the event_type_name of this POSTPublicEmailTemplateRequest.

        The name of the event type.    # noqa: E501

        :param event_type_name: The event_type_name of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """
        if event_type_name is None:
            raise ValueError("Invalid value for `event_type_name`, must not be `None`")  # noqa: E501

        self._event_type_name = event_type_name

    @property
    def event_type_namespace(self):
        """Gets the event_type_namespace of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The namespace of the `eventTypeName` field. The `eventTypeName` has the `user.notification` namespace by default.   Note that if the `eventTypeName` is a standard event type, you must specify the `com.zuora.notification` namespace; otherwise, you will get an error.  For example, if you want to create an email template on the `OrderActionProcessed` event, you must specify `com.zuora.notification` for this field.            # noqa: E501

        :return: The event_type_namespace of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._event_type_namespace

    @event_type_namespace.setter
    def event_type_namespace(self, event_type_namespace):
        """Sets the event_type_namespace of this POSTPublicEmailTemplateRequest.

        The namespace of the `eventTypeName` field. The `eventTypeName` has the `user.notification` namespace by default.   Note that if the `eventTypeName` is a standard event type, you must specify the `com.zuora.notification` namespace; otherwise, you will get an error.  For example, if you want to create an email template on the `OrderActionProcessed` event, you must specify `com.zuora.notification` for this field.            # noqa: E501

        :param event_type_namespace: The event_type_namespace of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._event_type_namespace = event_type_namespace

    @property
    def from_email_address(self):
        """Gets the from_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501

        If fromEmailType is SpecificEmail, this field is required.  # noqa: E501

        :return: The from_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._from_email_address

    @from_email_address.setter
    def from_email_address(self, from_email_address):
        """Sets the from_email_address of this POSTPublicEmailTemplateRequest.

        If fromEmailType is SpecificEmail, this field is required.  # noqa: E501

        :param from_email_address: The from_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._from_email_address = from_email_address

    @property
    def from_email_type(self):
        """Gets the from_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The type of the email.  # noqa: E501

        :return: The from_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._from_email_type

    @from_email_type.setter
    def from_email_type(self, from_email_type):
        """Sets the from_email_type of this POSTPublicEmailTemplateRequest.

        The type of the email.  # noqa: E501

        :param from_email_type: The from_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """
        if from_email_type is None:
            raise ValueError("Invalid value for `from_email_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TenantEmail", "SpecificEmail"]  # noqa: E501
        if from_email_type not in allowed_values:
            raise ValueError(
                "Invalid value for `from_email_type` ({0}), must be one of {1}"  # noqa: E501
                .format(from_email_type, allowed_values)
            )

        self._from_email_type = from_email_type

    @property
    def from_name(self):
        """Gets the from_name of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The name of the email sender.  # noqa: E501

        :return: The from_name of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this POSTPublicEmailTemplateRequest.

        The name of the email sender.  # noqa: E501

        :param from_name: The from_name of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def is_html(self):
        """Gets the is_html of this POSTPublicEmailTemplateRequest.  # noqa: E501

        Specifies whether the style of email body is HTML. The default value is false.  # noqa: E501

        :return: The is_html of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_html

    @is_html.setter
    def is_html(self, is_html):
        """Sets the is_html of this POSTPublicEmailTemplateRequest.

        Specifies whether the style of email body is HTML. The default value is false.  # noqa: E501

        :param is_html: The is_html of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: bool
        """

        self._is_html = is_html

    @property
    def name(self):
        """Gets the name of this POSTPublicEmailTemplateRequest.  # noqa: E501

        The name of the email template, a unique name in a tenant.  # noqa: E501

        :return: The name of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this POSTPublicEmailTemplateRequest.

        The name of the email template, a unique name in a tenant.  # noqa: E501

        :param name: The name of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def reply_to_email_address(self):
        """Gets the reply_to_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501

        If replyToEmailType is SpecificEmail, this field is required.  # noqa: E501

        :return: The reply_to_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._reply_to_email_address

    @reply_to_email_address.setter
    def reply_to_email_address(self, reply_to_email_address):
        """Sets the reply_to_email_address of this POSTPublicEmailTemplateRequest.

        If replyToEmailType is SpecificEmail, this field is required.  # noqa: E501

        :param reply_to_email_address: The reply_to_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._reply_to_email_address = reply_to_email_address

    @property
    def reply_to_email_type(self):
        """Gets the reply_to_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501

        Type of the replyTo email.  # noqa: E501

        :return: The reply_to_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._reply_to_email_type

    @reply_to_email_type.setter
    def reply_to_email_type(self, reply_to_email_type):
        """Sets the reply_to_email_type of this POSTPublicEmailTemplateRequest.

        Type of the replyTo email.  # noqa: E501

        :param reply_to_email_type: The reply_to_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["TenantEmail", "SpecificEmail"]  # noqa: E501
        if reply_to_email_type not in allowed_values:
            raise ValueError(
                "Invalid value for `reply_to_email_type` ({0}), must be one of {1}"  # noqa: E501
                .format(reply_to_email_type, allowed_values)
            )

        self._reply_to_email_type = reply_to_email_type

    @property
    def to_email_address(self):
        """Gets the to_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501

        If toEmailType is SpecificEmail, this field is required.  # noqa: E501

        :return: The to_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._to_email_address

    @to_email_address.setter
    def to_email_address(self, to_email_address):
        """Sets the to_email_address of this POSTPublicEmailTemplateRequest.

        If toEmailType is SpecificEmail, this field is required.  # noqa: E501

        :param to_email_address: The to_email_address of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """

        self._to_email_address = to_email_address

    @property
    def to_email_type(self):
        """Gets the to_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501

        Email receive type. * When EventType is CDC/External and 'ReferenceObjectType' in EventType is associated to Account, toEmailType can be ALL values in enum.  * When EventType is CDC/External and 'ReferenceObjectType' in EventType is not associated to Account, toEmailType MUST be TenantAdmin, RunOwner or SpecificEmail. * When EventType is CDC/External and 'ReferenceObjectType' in EventType is EMPTY, toEmailType MUST be TenantAdmin, RunOwner or SpecificEmail.  # noqa: E501

        :return: The to_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._to_email_type

    @to_email_type.setter
    def to_email_type(self, to_email_type):
        """Sets the to_email_type of this POSTPublicEmailTemplateRequest.

        Email receive type. * When EventType is CDC/External and 'ReferenceObjectType' in EventType is associated to Account, toEmailType can be ALL values in enum.  * When EventType is CDC/External and 'ReferenceObjectType' in EventType is not associated to Account, toEmailType MUST be TenantAdmin, RunOwner or SpecificEmail. * When EventType is CDC/External and 'ReferenceObjectType' in EventType is EMPTY, toEmailType MUST be TenantAdmin, RunOwner or SpecificEmail.  # noqa: E501

        :param to_email_type: The to_email_type of this POSTPublicEmailTemplateRequest.  # noqa: E501
        :type: str
        """
        if to_email_type is None:
            raise ValueError("Invalid value for `to_email_type`, must not be `None`")  # noqa: E501
        allowed_values = ["BillToContact", "SoldToContact", "SpecificEmails", "TenantAdmin", "BillToAndSoldToContacts", "RunOwner", "AllContacts", "InvoiceOwnerBillToContact", "InvoiceOwnerSoldToContact", "InvoiceOwnerBillToAndSoldToContacts", "InvoiceOwnerAllContacts"]  # noqa: E501
        if to_email_type not in allowed_values:
            raise ValueError(
                "Invalid value for `to_email_type` ({0}), must be one of {1}"  # noqa: E501
                .format(to_email_type, allowed_values)
            )

        self._to_email_type = to_email_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(POSTPublicEmailTemplateRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, POSTPublicEmailTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
