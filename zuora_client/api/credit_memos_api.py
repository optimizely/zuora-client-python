# coding: utf-8

"""
    Zuora API Reference

      # Introduction Welcome to the reference for the Zuora REST API!  <a href=\"http://en.wikipedia.org/wiki/REST_API\" target=\"_blank\">REST</a> is a web-service protocol that lends itself to rapid development by using everyday HTTP and JSON technology.  The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Production | https://rest.zuora.com   | |US API Sandbox    | https://rest.apisandbox.zuora.com| |US Performance Test | https://rest.pt1.zuora.com | |EU Production | https://rest.eu.zuora.com | |EU Sandbox | https://rest.sandbox.eu.zuora.com |  The Production endpoint provides access to your live user data. API Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision an API Sandbox tenant for you, contact your Zuora representative for assistance.  **Note:** If you have a tenant in the Production Copy Environment, submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints.  If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.  # API Changelog You can find the <a href=\"https://community.zuora.com/t5/Developers/API-Changelog/gpm-p/18092\" target=\"_blank\">Changelog</a> of the API Reference in the Zuora Community.  # Authentication  ## OAuth v2.0  Zuora recommends that you use OAuth v2.0 to authenticate to the Zuora REST API. Currently, OAuth is not available in every environment. See [Zuora Testing Environments](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Environments) for more information.  Zuora recommends you to create a dedicated API user with API write access on a tenant when authenticating via OAuth, and then create an OAuth client for this user. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for how to do this. By creating a dedicated API user, you can control permissions of the API user without affecting other non-API users.  If a user is deactivated, all of the user's OAuth clients will be automatically deactivated.  Authenticating via OAuth requires the following steps: 1. Create a Client 2. Generate a Token 3. Make Authenticated Requests  ### Create a Client  You must first [create an OAuth client](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) in the Zuora UI. To do this, you must be an administrator of your Zuora tenant. This is a one-time operation. You will be provided with a Client ID and a Client Secret. Please note this information down, as it will be required for the next step.  **Note:** The OAuth client will be owned by a Zuora user account. If you want to perform PUT, POST, or DELETE operations using the OAuth client, the owner of the OAuth client must have a Platform role that includes the \"API Write Access\" permission.  ### Generate a Token  After creating a client, you must make a call to obtain a bearer token using the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) operation. This operation requires the following parameters: - `client_id` - the Client ID displayed when you created the OAuth client in the previous step - `client_secret` - the Client Secret displayed when you created the OAuth client in the previous step - `grant_type` - must be set to `client_credentials`  **Note**: The Client ID and Client Secret mentioned above were displayed when you created the OAuth Client in the prior step. The [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response specifies how long the bearer token is valid for. Call [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) again to generate a new bearer token.  ### Make Authenticated Requests  To authenticate subsequent API requests, you must provide a valid bearer token in an HTTP header:  `Authorization: Bearer {bearer_token}`  If you have [Zuora Multi-entity](https://www.zuora.com/developer/api-reference/#tag/Entities) enabled, you need to set an additional header to specify the ID of the entity that you want to access. You can use the `scope` field in the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response to determine whether you need to specify an entity ID.  If the `scope` field contains more than one entity ID, you must specify the ID of the entity that you want to access. For example, if the `scope` field contains `entity.1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` and `entity.c92ed977-510c-4c48-9b51-8d5e848671e9`, specify one of the following headers: - `Zuora-Entity-Ids: 1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` - `Zuora-Entity-Ids: c92ed977-510c-4c48-9b51-8d5e848671e9`  **Note**: For a limited period of time, Zuora will accept the `entityId` header as an alternative to the `Zuora-Entity-Ids` header. If you choose to set the `entityId` header, you must remove all \"-\" characters from the entity ID in the `scope` field.  If the `scope` field contains a single entity ID, you do not need to specify an entity ID.  ## Other Supported Authentication Schemes  Zuora continues to support the following additional legacy means of authentication:    * Use username and password. Include authentication with each request in the header:         * `apiAccessKeyId`      * `apiSecretAccessKey`          Zuora recommends that you create an API user specifically for making API calls. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for more information.      * Use an authorization cookie. The cookie authorizes the user to make calls to the REST API for the duration specified in  **Administration > Security Policies > Session timeout**. The cookie expiration time is reset with this duration after every call to the REST API. To obtain a cookie, call the [Connections](https://www.zuora.com/developer/api-reference/#tag/Connections) resource with the following API user information:         *   ID         *   Password        * For CORS-enabled APIs only: Include a 'single-use' token in the request header, which re-authenticates the user with each request. See below for more details.  ### Entity Id and Entity Name  The `entityId` and `entityName` parameters are only used for [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity \"Zuora Multi-entity\"). These are the legacy parameters that Zuora will only continue to support for a period of time. Zuora recommends you to use the `Zuora-Entity-Ids` parameter instead.   The  `entityId` and `entityName` parameters specify the Id and the [name of the entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/B_Introduction_to_Entity_and_Entity_Hierarchy#Name_and_Display_Name \"Introduction to Entity and Entity Hierarchy\") that you want to access, respectively. Note that you must have permission to access the entity.   You can specify either the `entityId` or `entityName` parameter in the authentication to access and view an entity.    * If both `entityId` and `entityName` are specified in the authentication, an error occurs.    * If neither `entityId` nor `entityName` is specified in the authentication, you will log in to the entity in which your user account is created.      To get the entity Id and entity name, you can use the GET Entities REST call. For more information, see [API User Authentication](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/A_Overview_of_Multi-entity#API_User_Authentication \"API User Authentication\").      ### Token Authentication for CORS-Enabled APIs      The CORS mechanism enables REST API calls to Zuora to be made directly from your customer's browser, with all credit card and security information transmitted directly to Zuora. This minimizes your PCI compliance burden, allows you to implement advanced validation on your payment forms, and  makes your payment forms look just like any other part of your website.    For security reasons, instead of using cookies, an API request via CORS uses **tokens** for authentication.  The token method of authentication is only designed for use with requests that must originate from your customer's browser; **it should  not be considered a replacement to the existing cookie authentication** mechanism.  See [Zuora CORS REST](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Zuora_CORS_REST \"Zuora CORS REST\") for details on how CORS works and how you can begin to implement customer calls to the Zuora REST APIs. See  [HMAC Signatures](https://www.zuora.com/developer/api-reference/#operation/POSTHMACSignature \"HMAC Signatures\") for details on the HMAC method that returns the authentication token.  # Requests and Responses  ## Request IDs  As a general rule, when asked to supply a \"key\" for an account or subscription (accountKey, account-key, subscriptionKey, subscription-key), you can provide either the actual ID or  the number of the entity.  ## HTTP Request Body  Most of the parameters and data accompanying your requests will be contained in the body of the HTTP request.   The Zuora REST API accepts JSON in the HTTP request body. No other data format (e.g., XML) is supported.  ### Data Type  ([Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations only) We recommend that you do not specify the decimal values with quotation marks, commas, and spaces. Use characters of `+-0-9.eE`, for example, `5`, `1.9`, `-8.469`, and `7.7e2`. Also, Zuora does not convert currencies for decimal values.  ## Testing a Request  Use a third party client, such as [curl](https://curl.haxx.se \"curl\"), [Postman](https://www.getpostman.com \"Postman\"), or [Advanced REST Client](https://advancedrestclient.com \"Advanced REST Client\"), to test the Zuora REST API.  You can test the Zuora REST API from the Zuora API Sandbox or Production tenants. If connecting to Production, bear in mind that you are working with your live production data, not sample data or test data.  ## Testing with Credit Cards  Sooner or later it will probably be necessary to test some transactions that involve credit cards. For suggestions on how to handle this, see [Going Live With Your Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards \"C_Zuora_User_Guides/A_Billing_and_Payments/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards\" ).  ## Concurrent Request Limits  Zuora enforces tenant-level concurrent request limits. See <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits\" target=\"_blank\">Concurrent Request Limits</a> for more information.  ## Timeout Limit  If a request does not complete within 120 seconds, the request times out and Zuora returns a Gateway Timeout error.  ## Error Handling  Responses and error codes are detailed in [Responses and errors](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Responses_and_Errors \"Responses and errors\").  # Pagination  When retrieving information (using GET methods), the optional `pageSize` query parameter sets the maximum number of rows to return in a response. The maximum is `40`; larger values are treated as `40`. If this value is empty or invalid, `pageSize` typically defaults to `10`.  The default value for the maximum number of rows retrieved can be overridden at the method level.  If more rows are available, the response will include a `nextPage` element, which contains a URL for requesting the next page.  If this value is not provided, no more rows are available. No \"previous page\" element is explicitly provided; to support backward paging, use the previous call.  ## Array Size  For data items that are not paginated, the REST API supports arrays of up to 300 rows.  Thus, for instance, repeated pagination can retrieve thousands of customer accounts, but within any account an array of no more than 300 rate plans is returned.  # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.  ## Major Version  The major version number of the REST API appears in the REST URL. Currently, Zuora only supports the **v1** major version. For example, `POST https://rest.zuora.com/v1/subscriptions`.  ## Minor Version  Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.   Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not serial. This section documents the changes made to each Zuora REST API minor version.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 196.0 and earlier  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. | | creditTaxItems | 238.0 and earlier | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\") | Container for the taxation items of the credit memo item. | | taxItems | 238.0 and earlier | [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the debit memo item. | | taxationItems | 239.0 and later | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the memo item. |   #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") and [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics  # Zuora Object Model  The following diagram presents a high-level view of the key Zuora objects. Click the image to open it in a new tab to resize it.  <a href=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" target=\"_blank\"><img src=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" alt=\"Zuora Object Model Diagram\"></a>  See the following articles for information about other parts of the Zuora business object model:    * <a href=\"https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/D_Invoice_Settlement_Object_Model\" target=\"_blank\">Invoice Settlement Object Model</a>   * <a href=\"https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/BA_Orders_Object_Model\" target=\"_blank\">Orders Object Model</a>  You can use the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun`</p><p>**Note:** The API name of this object is `BillingRun` in the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation, Export ZOQL queries, and Data Query. Otherwise, the API name of this object is `BillRun`.</p> | | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Feature                                       | `Feature`                                  | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                         | `UpdaterDetail`                            | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Feature                               | `ProductFeature`                           | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Subscription Product Feature                  | `SubscriptionProductFeature`               | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    |   # noqa: E501

    OpenAPI spec version: 2019-07-26
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from zuora_client.api_client import ApiClient


class CreditMemosApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def d_elete_credit_memo(self, credit_memo_id, **kwargs):  # noqa: E501
        """Delete credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Deletes a credit memo. Only credit memos with the Cancelled status can be deleted.   You can delete a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.d_elete_credit_memo(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.d_elete_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.d_elete_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
            return data

    def d_elete_credit_memo_with_http_info(self, credit_memo_id, **kwargs):  # noqa: E501
        """Delete credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Deletes a credit memo. Only credit memos with the Cancelled status can be deleted.   You can delete a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.d_elete_credit_memo_with_http_info(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method d_elete_credit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `d_elete_credit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_breakdown_credit_memo_by_order(self, credit_memo_number, **kwargs):  # noqa: E501
        """Get breakdown of credit memo by order  # noqa: E501

        **Note:** This feature is in Limited Availability.   Retrieves a specified credit memo that is broken down by orders. One credit memo item might be broken down into a list of order related items.  You can only use this operation to retrieve breakdowns of credit memos whose source value is `BillRun` or `API`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_breakdown_credit_memo_by_order(credit_memo_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_number: Number of credit memo to be broken down. (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GetCreditMemoAmountBreakdownByOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_breakdown_credit_memo_by_order_with_http_info(credit_memo_number, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_breakdown_credit_memo_by_order_with_http_info(credit_memo_number, **kwargs)  # noqa: E501
            return data

    def g_et_breakdown_credit_memo_by_order_with_http_info(self, credit_memo_number, **kwargs):  # noqa: E501
        """Get breakdown of credit memo by order  # noqa: E501

        **Note:** This feature is in Limited Availability.   Retrieves a specified credit memo that is broken down by orders. One credit memo item might be broken down into a list of order related items.  You can only use this operation to retrieve breakdowns of credit memos whose source value is `BillRun` or `API`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_breakdown_credit_memo_by_order_with_http_info(credit_memo_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_number: Number of credit memo to be broken down. (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GetCreditMemoAmountBreakdownByOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_memo_number', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_breakdown_credit_memo_by_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credit_memo_number' is set
        if ('credit_memo_number' not in params or
                params['credit_memo_number'] is None):
            raise ValueError("Missing the required parameter `credit_memo_number` when calling `g_et_breakdown_credit_memo_by_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_number' in params:
            path_params['creditMemoNumber'] = params['credit_memo_number']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoNumber}/amountBreakdownByOrder', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetCreditMemoAmountBreakdownByOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_credit_memo(self, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific credit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_credit_memo_with_http_info(self, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific credit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_with_http_info(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_credit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `g_et_credit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_credit_memo_item(self, cmitemid, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo item  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the information about a specific item of a credit memo. A credit memo item is a single line item in a credit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_item(cmitemid, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cmitemid: The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * creditTaxItems * taxationItems 
        :return: GETCreditMemoItemType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_credit_memo_item_with_http_info(cmitemid, credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_credit_memo_item_with_http_info(cmitemid, credit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_credit_memo_item_with_http_info(self, cmitemid, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo item  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the information about a specific item of a credit memo. A credit memo item is a single line item in a credit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_item_with_http_info(cmitemid, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cmitemid: The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * creditTaxItems * taxationItems 
        :return: GETCreditMemoItemType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cmitemid', 'credit_memo_id', 'zuora_entity_ids', 'zuora_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_credit_memo_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cmitemid' is set
        if ('cmitemid' not in params or
                params['cmitemid'] is None):
            raise ValueError("Missing the required parameter `cmitemid` when calling `g_et_credit_memo_item`")  # noqa: E501
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `g_et_credit_memo_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cmitemid' in params:
            path_params['cmitemid'] = params['cmitemid']  # noqa: E501
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501
        if 'zuora_version' in params:
            header_params['zuora-version'] = params['zuora_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/items/{cmitemid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoItemType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_credit_memo_item_part(self, partid, itempartid, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo part item  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the information about a specific credit memo part item.  A credit memo part item is a single line item in a credit memo part. A credit memo part can consist of several different types of items.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_item_part(partid, itempartid, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str partid: The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts).  (required)
        :param str itempartid: The unique ID of a specific credit memo part item. You can get the credit memo part item ID from the response of [Get credit memo part items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItemParts).  (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoItemPartType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_credit_memo_item_part_with_http_info(partid, itempartid, credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_credit_memo_item_part_with_http_info(partid, itempartid, credit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_credit_memo_item_part_with_http_info(self, partid, itempartid, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo part item  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the information about a specific credit memo part item.  A credit memo part item is a single line item in a credit memo part. A credit memo part can consist of several different types of items.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_item_part_with_http_info(partid, itempartid, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str partid: The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts).  (required)
        :param str itempartid: The unique ID of a specific credit memo part item. You can get the credit memo part item ID from the response of [Get credit memo part items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItemParts).  (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoItemPartType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['partid', 'itempartid', 'credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_credit_memo_item_part" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'partid' is set
        if ('partid' not in params or
                params['partid'] is None):
            raise ValueError("Missing the required parameter `partid` when calling `g_et_credit_memo_item_part`")  # noqa: E501
        # verify the required parameter 'itempartid' is set
        if ('itempartid' not in params or
                params['itempartid'] is None):
            raise ValueError("Missing the required parameter `itempartid` when calling `g_et_credit_memo_item_part`")  # noqa: E501
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `g_et_credit_memo_item_part`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'partid' in params:
            path_params['partid'] = params['partid']  # noqa: E501
        if 'itempartid' in params:
            path_params['itempartid'] = params['itempartid']  # noqa: E501
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/parts/{partid}/itemparts/{itempartid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoItemPartType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_credit_memo_item_parts(self, partid, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo part items  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all items of a credit memo part. A credit memo part item is a single line item in a credit memo part. A credit memo part can consist of several different types of items.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_item_parts(partid, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str partid: The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts). .  (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :return: GETCreditMemoItemPartsCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_credit_memo_item_parts_with_http_info(partid, credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_credit_memo_item_parts_with_http_info(partid, credit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_credit_memo_item_parts_with_http_info(self, partid, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo part items  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all items of a credit memo part. A credit memo part item is a single line item in a credit memo part. A credit memo part can consist of several different types of items.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_item_parts_with_http_info(partid, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str partid: The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts). .  (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :return: GETCreditMemoItemPartsCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['partid', 'credit_memo_id', 'zuora_entity_ids', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_credit_memo_item_parts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'partid' is set
        if ('partid' not in params or
                params['partid'] is None):
            raise ValueError("Missing the required parameter `partid` when calling `g_et_credit_memo_item_parts`")  # noqa: E501
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `g_et_credit_memo_item_parts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'partid' in params:
            path_params['partid'] = params['partid']  # noqa: E501
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/parts/{partid}/itemparts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoItemPartsCollectionType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_credit_memo_items(self, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo items  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all items of a credit memo. A credit memo item is a single line item in a credit memo.   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:        - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100      - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100&sort=createdDate        # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_items(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * creditTaxItems * taxationItems 
        :param float amount: This parameter filters the response based on the `amount` field.  
        :param float applied_amount: This parameter filters the response based on the `appliedAmount` field.  
        :param str created_by_id: This parameter filters the response based on the `createdById` field.  
        :param datetime created_date: This parameter filters the response based on the `createdDate` field.  
        :param str id: This parameter filters the response based on the `id` field.  
        :param float refund_amount: This parameter filters the response based on the `refundAmount` field.  
        :param date service_end_date: This parameter filters the response based on the `serviceEndDate` field.  
        :param date service_start_date: This parameter filters the response based on the `serviceStartDate` field.  
        :param str sku: This parameter filters the response based on the `sku` field.  
        :param str sku_name: This parameter filters the response based on the `skuName` field.  
        :param str source_item_id: This parameter filters the response based on the `sourceItemId` field.  
        :param str subscription_id: This parameter filters the response based on the `subscriptionId` field. 
        :param str updated_by_id: This parameter filters the response based on the `updatedById` field.  
        :param datetime updated_date: This parameter filters the response based on the `updatedDate` field. 
        :param str sort: This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by updated date.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - amount   - appliedAmount   - createdById   - createdDate   - id   - refundAmount   - serviceEndDate   - serviceStartDate   - sku   - skuName   - sourceItemId   - subscriptionId   - updatedById   - updatedDate    Examples:  - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?sort=createdDate  - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100&sort=createdDate 
        :return: GETCreditMemoItemsListType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_credit_memo_items_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_credit_memo_items_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_credit_memo_items_with_http_info(self, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo items  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all items of a credit memo. A credit memo item is a single line item in a credit memo.   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:        - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100      - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100&sort=createdDate        # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_items_with_http_info(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * creditTaxItems * taxationItems 
        :param float amount: This parameter filters the response based on the `amount` field.  
        :param float applied_amount: This parameter filters the response based on the `appliedAmount` field.  
        :param str created_by_id: This parameter filters the response based on the `createdById` field.  
        :param datetime created_date: This parameter filters the response based on the `createdDate` field.  
        :param str id: This parameter filters the response based on the `id` field.  
        :param float refund_amount: This parameter filters the response based on the `refundAmount` field.  
        :param date service_end_date: This parameter filters the response based on the `serviceEndDate` field.  
        :param date service_start_date: This parameter filters the response based on the `serviceStartDate` field.  
        :param str sku: This parameter filters the response based on the `sku` field.  
        :param str sku_name: This parameter filters the response based on the `skuName` field.  
        :param str source_item_id: This parameter filters the response based on the `sourceItemId` field.  
        :param str subscription_id: This parameter filters the response based on the `subscriptionId` field. 
        :param str updated_by_id: This parameter filters the response based on the `updatedById` field.  
        :param datetime updated_date: This parameter filters the response based on the `updatedDate` field. 
        :param str sort: This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by updated date.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - amount   - appliedAmount   - createdById   - createdDate   - id   - refundAmount   - serviceEndDate   - serviceStartDate   - sku   - skuName   - sourceItemId   - subscriptionId   - updatedById   - updatedDate    Examples:  - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?sort=createdDate  - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100&sort=createdDate 
        :return: GETCreditMemoItemsListType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_memo_id', 'zuora_entity_ids', 'page_size', 'zuora_version', 'amount', 'applied_amount', 'created_by_id', 'created_date', 'id', 'refund_amount', 'service_end_date', 'service_start_date', 'sku', 'sku_name', 'source_item_id', 'subscription_id', 'updated_by_id', 'updated_date', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_credit_memo_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `g_et_credit_memo_items`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501
        if 'applied_amount' in params:
            query_params.append(('appliedAmount', params['applied_amount']))  # noqa: E501
        if 'created_by_id' in params:
            query_params.append(('createdById', params['created_by_id']))  # noqa: E501
        if 'created_date' in params:
            query_params.append(('createdDate', params['created_date']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'refund_amount' in params:
            query_params.append(('refundAmount', params['refund_amount']))  # noqa: E501
        if 'service_end_date' in params:
            query_params.append(('serviceEndDate', params['service_end_date']))  # noqa: E501
        if 'service_start_date' in params:
            query_params.append(('serviceStartDate', params['service_start_date']))  # noqa: E501
        if 'sku' in params:
            query_params.append(('sku', params['sku']))  # noqa: E501
        if 'sku_name' in params:
            query_params.append(('skuName', params['sku_name']))  # noqa: E501
        if 'source_item_id' in params:
            query_params.append(('sourceItemId', params['source_item_id']))  # noqa: E501
        if 'subscription_id' in params:
            query_params.append(('subscriptionId', params['subscription_id']))  # noqa: E501
        if 'updated_by_id' in params:
            query_params.append(('updatedById', params['updated_by_id']))  # noqa: E501
        if 'updated_date' in params:
            query_params.append(('updatedDate', params['updated_date']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501
        if 'zuora_version' in params:
            header_params['zuora-version'] = params['zuora_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/items', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoItemsListType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_credit_memo_part(self, partid, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo part  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific credit memo part. A credit memo can consist of an unapplied part, and several parts applied to invoices and debit memos.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_part(partid, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str partid: The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts).  (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoPartType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_credit_memo_part_with_http_info(partid, credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_credit_memo_part_with_http_info(partid, credit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_credit_memo_part_with_http_info(self, partid, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo part  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific credit memo part. A credit memo can consist of an unapplied part, and several parts applied to invoices and debit memos.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_part_with_http_info(partid, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str partid: The unique ID of a specific credit memo part. You can get the credit memo part ID from the response of [Get credit memo parts](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoParts).  (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoPartType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['partid', 'credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_credit_memo_part" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'partid' is set
        if ('partid' not in params or
                params['partid'] is None):
            raise ValueError("Missing the required parameter `partid` when calling `g_et_credit_memo_part`")  # noqa: E501
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `g_et_credit_memo_part`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'partid' in params:
            path_params['partid'] = params['partid']  # noqa: E501
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/parts/{partid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoPartType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_credit_memo_parts(self, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo parts  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all parts of a credit memo. A credit memo can consist of an unapplied part, and several parts applied to invoices and debit memos. You can use this operation to get all the applied and unapplied portions of a credit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_parts(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :return: GETCreditMemoPartsCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_credit_memo_parts_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_credit_memo_parts_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_credit_memo_parts_with_http_info(self, credit_memo_id, **kwargs):  # noqa: E501
        """Get credit memo parts  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all parts of a credit memo. A credit memo can consist of an unapplied part, and several parts applied to invoices and debit memos. You can use this operation to get all the applied and unapplied portions of a credit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memo_parts_with_http_info(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :return: GETCreditMemoPartsCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_memo_id', 'zuora_entity_ids', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_credit_memo_parts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `g_et_credit_memo_parts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/parts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoPartsCollectionType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_credit_memos(self, **kwargs):  # noqa: E501
        """Get credit memos  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all credit memos.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.     Examples:  - /v1/creditmemos?status=Processed  - /v1/creditmemos?referredInvoiceId=null&status=Draft  - /v1/creditmemos?status=Processed&type=External&sort=+number   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memos(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param str account_id: This parameter filters the response based on the `accountId` field.  
        :param float amount: This parameter filters the response based on the `amount` field.  
        :param float applied_amount: This parameter filters the response based on the `appliedAmount` field.  
        :param bool auto_apply_upon_posting: This parameter filters the response based on the `autoApplyUponPosting` field.  
        :param str created_by_id: This parameter filters the response based on the `createdById` field.  
        :param datetime created_date: This parameter filters the response based on the `createdDate` field.  
        :param date credit_memo_date: This parameter filters the response based on the `creditMemoDate` field.  
        :param str currency: This parameter filters the response based on the `currency` field.  
        :param bool exclude_from_auto_apply_rules: This parameter filters the response based on the `excludeFromAutoApplyRules` field.  
        :param str number: This parameter filters the response based on the `number` field.  
        :param str referred_invoice_id: This parameter filters the response based on the `referredInvoiceId` field.  
        :param float refund_amount: This parameter filters the response based on the `refundAmount` field.  
        :param str status: This parameter filters the response based on the `status` field.  
        :param date target_date: This parameter filters the response based on the `targetDate` field.  
        :param float tax_amount: This parameter filters the response based on the `taxAmount` field.  
        :param float total_tax_exempt_amount: This parameter filters the response based on the `totalTaxExemptAmount` field. 
        :param str transferred_to_accounting: This parameter filters the response based on the `transferredToAccounting` field.  
        :param float unapplied_amount: This parameter filters the response based on the `unappliedAmount` field.  
        :param str updated_by_id: This parameter filters the response based on the `updatedById` field.  
        :param datetime updated_date: This parameter filters the response based on the `updatedDate` field. 
        :param str sort: This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by credit memo number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - accountId   - amount   - appliedAmount   - createdById   - createdDate   - creditMemoDate   - number   - referredInvoiceId   - refundAmount   - status   - targetDate   - taxAmount   - totalTaxExemptAmount   - transferredToAccounting   - unappliedAmount   - updatedDate     Examples:  - /v1/creditmemos?sort=+number  - /v1/creditmemos?status=Processed&sort=-number,+amount 
        :return: GETCreditMemoCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_credit_memos_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.g_et_credit_memos_with_http_info(**kwargs)  # noqa: E501
            return data

    def g_et_credit_memos_with_http_info(self, **kwargs):  # noqa: E501
        """Get credit memos  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all credit memos.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.     Examples:  - /v1/creditmemos?status=Processed  - /v1/creditmemos?referredInvoiceId=null&status=Draft  - /v1/creditmemos?status=Processed&type=External&sort=+number   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_credit_memos_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param str account_id: This parameter filters the response based on the `accountId` field.  
        :param float amount: This parameter filters the response based on the `amount` field.  
        :param float applied_amount: This parameter filters the response based on the `appliedAmount` field.  
        :param bool auto_apply_upon_posting: This parameter filters the response based on the `autoApplyUponPosting` field.  
        :param str created_by_id: This parameter filters the response based on the `createdById` field.  
        :param datetime created_date: This parameter filters the response based on the `createdDate` field.  
        :param date credit_memo_date: This parameter filters the response based on the `creditMemoDate` field.  
        :param str currency: This parameter filters the response based on the `currency` field.  
        :param bool exclude_from_auto_apply_rules: This parameter filters the response based on the `excludeFromAutoApplyRules` field.  
        :param str number: This parameter filters the response based on the `number` field.  
        :param str referred_invoice_id: This parameter filters the response based on the `referredInvoiceId` field.  
        :param float refund_amount: This parameter filters the response based on the `refundAmount` field.  
        :param str status: This parameter filters the response based on the `status` field.  
        :param date target_date: This parameter filters the response based on the `targetDate` field.  
        :param float tax_amount: This parameter filters the response based on the `taxAmount` field.  
        :param float total_tax_exempt_amount: This parameter filters the response based on the `totalTaxExemptAmount` field. 
        :param str transferred_to_accounting: This parameter filters the response based on the `transferredToAccounting` field.  
        :param float unapplied_amount: This parameter filters the response based on the `unappliedAmount` field.  
        :param str updated_by_id: This parameter filters the response based on the `updatedById` field.  
        :param datetime updated_date: This parameter filters the response based on the `updatedDate` field. 
        :param str sort: This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by credit memo number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - accountId   - amount   - appliedAmount   - createdById   - createdDate   - creditMemoDate   - number   - referredInvoiceId   - refundAmount   - status   - targetDate   - taxAmount   - totalTaxExemptAmount   - transferredToAccounting   - unappliedAmount   - updatedDate     Examples:  - /v1/creditmemos?sort=+number  - /v1/creditmemos?status=Processed&sort=-number,+amount 
        :return: GETCreditMemoCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zuora_entity_ids', 'page_size', 'account_id', 'amount', 'applied_amount', 'auto_apply_upon_posting', 'created_by_id', 'created_date', 'credit_memo_date', 'currency', 'exclude_from_auto_apply_rules', 'number', 'referred_invoice_id', 'refund_amount', 'status', 'target_date', 'tax_amount', 'total_tax_exempt_amount', 'transferred_to_accounting', 'unapplied_amount', 'updated_by_id', 'updated_date', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_credit_memos" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501
        if 'applied_amount' in params:
            query_params.append(('appliedAmount', params['applied_amount']))  # noqa: E501
        if 'auto_apply_upon_posting' in params:
            query_params.append(('autoApplyUponPosting', params['auto_apply_upon_posting']))  # noqa: E501
        if 'created_by_id' in params:
            query_params.append(('createdById', params['created_by_id']))  # noqa: E501
        if 'created_date' in params:
            query_params.append(('createdDate', params['created_date']))  # noqa: E501
        if 'credit_memo_date' in params:
            query_params.append(('creditMemoDate', params['credit_memo_date']))  # noqa: E501
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501
        if 'exclude_from_auto_apply_rules' in params:
            query_params.append(('excludeFromAutoApplyRules', params['exclude_from_auto_apply_rules']))  # noqa: E501
        if 'number' in params:
            query_params.append(('number', params['number']))  # noqa: E501
        if 'referred_invoice_id' in params:
            query_params.append(('referredInvoiceId', params['referred_invoice_id']))  # noqa: E501
        if 'refund_amount' in params:
            query_params.append(('refundAmount', params['refund_amount']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'target_date' in params:
            query_params.append(('targetDate', params['target_date']))  # noqa: E501
        if 'tax_amount' in params:
            query_params.append(('taxAmount', params['tax_amount']))  # noqa: E501
        if 'total_tax_exempt_amount' in params:
            query_params.append(('totalTaxExemptAmount', params['total_tax_exempt_amount']))  # noqa: E501
        if 'transferred_to_accounting' in params:
            query_params.append(('transferredToAccounting', params['transferred_to_accounting']))  # noqa: E501
        if 'unapplied_amount' in params:
            query_params.append(('unappliedAmount', params['unapplied_amount']))  # noqa: E501
        if 'updated_by_id' in params:
            query_params.append(('updatedById', params['updated_by_id']))  # noqa: E501
        if 'updated_date' in params:
            query_params.append(('updatedDate', params['updated_date']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoCollectionType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_taxation_items_of_credit_memo_item(self, cmitemid, credit_memo_id, **kwargs):  # noqa: E501
        """Get taxation items of credit memo item  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves information about the taxation items of a specific credit memo item.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_taxation_items_of_credit_memo_item(cmitemid, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cmitemid: The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param int page: Page number. 
        :return: GETTaxationItemsOfCreditMemoItemType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_taxation_items_of_credit_memo_item_with_http_info(cmitemid, credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_taxation_items_of_credit_memo_item_with_http_info(cmitemid, credit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_taxation_items_of_credit_memo_item_with_http_info(self, cmitemid, credit_memo_id, **kwargs):  # noqa: E501
        """Get taxation items of credit memo item  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves information about the taxation items of a specific credit memo item.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_taxation_items_of_credit_memo_item_with_http_info(cmitemid, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cmitemid: The unique ID of a credit memo item. You can get the credit memo item ID from the response of [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems).  (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param int page: Page number. 
        :return: GETTaxationItemsOfCreditMemoItemType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cmitemid', 'credit_memo_id', 'zuora_entity_ids', 'page_size', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_taxation_items_of_credit_memo_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cmitemid' is set
        if ('cmitemid' not in params or
                params['cmitemid'] is None):
            raise ValueError("Missing the required parameter `cmitemid` when calling `g_et_taxation_items_of_credit_memo_item`")  # noqa: E501
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `g_et_taxation_items_of_credit_memo_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cmitemid' in params:
            path_params['cmitemid'] = params['cmitemid']  # noqa: E501
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/items/{cmitemid}/taxation-items', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETTaxationItemsOfCreditMemoItemType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_credit_memo_from_prpc(self, body, **kwargs):  # noqa: E501
        """Create credit memo from charge  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates an ad-hoc credit memo from a product rate plan charge. Zuora supports the creation of credit memos from any type of product rate plan charge. The charges can also have any amount and any charge model, except for discout charge models.   You can create a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_credit_memo_from_prpc(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreditMemoFromChargeType body: (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * amount * memoItemAmount 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ost_credit_memo_from_prpc_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ost_credit_memo_from_prpc_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def p_ost_credit_memo_from_prpc_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create credit memo from charge  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates an ad-hoc credit memo from a product rate plan charge. Zuora supports the creation of credit memos from any type of product rate plan charge. The charges can also have any amount and any charge model, except for discout charge models.   You can create a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_credit_memo_from_prpc_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreditMemoFromChargeType body: (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * amount * memoItemAmount 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'zuora_entity_ids', 'zuora_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_credit_memo_from_prpc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ost_credit_memo_from_prpc`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501
        if 'zuora_version' in params:
            header_params['zuora-version'] = params['zuora_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_credit_memo_pdf(self, credit_memo_id, **kwargs):  # noqa: E501
        """Create credit memo PDF  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates a PDF file for a specified credit memo. To access the generated PDF file, you can download it by clicking **View PDF** on the detailed credit memo page through the Zuora UI.  This REST API operation can be used only if you have the Billing user permission \"Regenerate PDF\" enabled.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_credit_memo_pdf(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of the credit memo that you want to create a PDF file for. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTMemoPdfResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ost_credit_memo_pdf_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ost_credit_memo_pdf_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ost_credit_memo_pdf_with_http_info(self, credit_memo_id, **kwargs):  # noqa: E501
        """Create credit memo PDF  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates a PDF file for a specified credit memo. To access the generated PDF file, you can download it by clicking **View PDF** on the detailed credit memo page through the Zuora UI.  This REST API operation can be used only if you have the Billing user permission \"Regenerate PDF\" enabled.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_credit_memo_pdf_with_http_info(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of the credit memo that you want to create a PDF file for. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTMemoPdfResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_credit_memo_pdf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `p_ost_credit_memo_pdf`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/pdfs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTMemoPdfResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_email_credit_memo(self, body, credit_memo_id, **kwargs):  # noqa: E501
        """Email credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Sends a posted credit memo to the specified email addresses manually.    ## Notes   - You must activate the **Email Credit Memo | Manually email Credit Memo** notification before emailing credit memos. To include the credit memo PDF in the email, select the **Include Credit Memo PDF** check box in the **Edit notification** dialog from the Zuora UI. See [Create and Edit Notifications](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/C_Create_Notifications#section_2) for more information.     - Zuora sends the email messages based on the email template you set. You can set the email template to use in the **Delivery Options** panel of the **Edit notification** dialog from the Zuora UI. By default, the **Manual Email for Credit Memo Default Template** template is used. See [Create and Edit Email Templates](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/Create_Email_Templates) for more information.     - The credit memos are sent only to the work email addresses or personal email addresses of the Bill To contact if the following conditions are all met:      * The `useEmailTemplateSetting` field is set to `false`.     * The email addresses are not specified in the `emailAddresses` field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_email_credit_memo(body, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostCreditMemoEmailRequestType body: (required)
        :param str credit_memo_id: The ID of a posted credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ost_email_credit_memo_with_http_info(body, credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ost_email_credit_memo_with_http_info(body, credit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ost_email_credit_memo_with_http_info(self, body, credit_memo_id, **kwargs):  # noqa: E501
        """Email credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Sends a posted credit memo to the specified email addresses manually.    ## Notes   - You must activate the **Email Credit Memo | Manually email Credit Memo** notification before emailing credit memos. To include the credit memo PDF in the email, select the **Include Credit Memo PDF** check box in the **Edit notification** dialog from the Zuora UI. See [Create and Edit Notifications](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/C_Create_Notifications#section_2) for more information.     - Zuora sends the email messages based on the email template you set. You can set the email template to use in the **Delivery Options** panel of the **Edit notification** dialog from the Zuora UI. By default, the **Manual Email for Credit Memo Default Template** template is used. See [Create and Edit Email Templates](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/Create_Email_Templates) for more information.     - The credit memos are sent only to the work email addresses or personal email addresses of the Bill To contact if the following conditions are all met:      * The `useEmailTemplateSetting` field is set to `false`.     * The email addresses are not specified in the `emailAddresses` field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_email_credit_memo_with_http_info(body, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostCreditMemoEmailRequestType body: (required)
        :param str credit_memo_id: The ID of a posted credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_email_credit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ost_email_credit_memo`")  # noqa: E501
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `p_ost_email_credit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/emails', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonResponseType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_refund_credit_memo(self, body, creditmemo_id, **kwargs):  # noqa: E501
        """Refund credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Refunds a full or partial posted credit memo to your customers. Only the amount of unapplied part could be refunded.   You can refund a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_refund_credit_memo(body, creditmemo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostNonRefRefundType body: (required)
        :param str creditmemo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETRefundCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ost_refund_credit_memo_with_http_info(body, creditmemo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ost_refund_credit_memo_with_http_info(body, creditmemo_id, **kwargs)  # noqa: E501
            return data

    def p_ost_refund_credit_memo_with_http_info(self, body, creditmemo_id, **kwargs):  # noqa: E501
        """Refund credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Refunds a full or partial posted credit memo to your customers. Only the amount of unapplied part could be refunded.   You can refund a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_refund_credit_memo_with_http_info(body, creditmemo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostNonRefRefundType body: (required)
        :param str creditmemo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETRefundCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'creditmemo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_refund_credit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ost_refund_credit_memo`")  # noqa: E501
        # verify the required parameter 'creditmemo_id' is set
        if ('creditmemo_id' not in params or
                params['creditmemo_id'] is None):
            raise ValueError("Missing the required parameter `creditmemo_id` when calling `p_ost_refund_credit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'creditmemo_id' in params:
            path_params['creditmemoId'] = params['creditmemo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditmemoId}/refunds', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETRefundCreditMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_request_breakdown_credit_memo_items_by_order(self, body, **kwargs):  # noqa: E501
        """Request breakdown of credit memo items by order  # noqa: E501

        **Note:** This feature is in Limited Availability.   Retrieve specified credit memo items which are broken down by orders. One credit memo item might be broken down into a list of order related items.  You can only use this operation to retrieve breakdowns of credit memos whose source value is `BillRun` or `API`.  The maximum number of credit memo items to retrieve is 1000.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_request_breakdown_credit_memo_items_by_order(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param POSTCreditMemoItemsForOrderBreakdown body: (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GetCreditMemoAmountBreakdownByOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ost_request_breakdown_credit_memo_items_by_order_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ost_request_breakdown_credit_memo_items_by_order_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def p_ost_request_breakdown_credit_memo_items_by_order_with_http_info(self, body, **kwargs):  # noqa: E501
        """Request breakdown of credit memo items by order  # noqa: E501

        **Note:** This feature is in Limited Availability.   Retrieve specified credit memo items which are broken down by orders. One credit memo item might be broken down into a list of order related items.  You can only use this operation to retrieve breakdowns of credit memos whose source value is `BillRun` or `API`.  The maximum number of credit memo items to retrieve is 1000.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_request_breakdown_credit_memo_items_by_order_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param POSTCreditMemoItemsForOrderBreakdown body: (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GetCreditMemoAmountBreakdownByOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_request_breakdown_credit_memo_items_by_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ost_request_breakdown_credit_memo_items_by_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/items/amountBreakdownByOrder', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetCreditMemoAmountBreakdownByOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_upload_file_for_credit_memo(self, credit_memo_id, **kwargs):  # noqa: E501
        """Upload file for credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Uploads an externally generated PDF file for a credit memo that is in Draft or Posted status.  This operation has the following restrictions: - Only the PDF file format is supported. - The maximum size of the PDF file to upload is 4 MB. - A maximum of 50 PDF files can be uploaded for one credit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_upload_file_for_credit_memo(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The ID of the credit memo that you want to upload a PDF file for. For example, 402890555a7e9791015a879f064a0054.  (required)
        :param file file:
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :return: POSTUploadFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ost_upload_file_for_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ost_upload_file_for_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ost_upload_file_for_credit_memo_with_http_info(self, credit_memo_id, **kwargs):  # noqa: E501
        """Upload file for credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Uploads an externally generated PDF file for a credit memo that is in Draft or Posted status.  This operation has the following restrictions: - Only the PDF file format is supported. - The maximum size of the PDF file to upload is 4 MB. - A maximum of 50 PDF files can be uploaded for one credit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_upload_file_for_credit_memo_with_http_info(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The ID of the credit memo that you want to upload a PDF file for. For example, 402890555a7e9791015a879f064a0054.  (required)
        :param file file:
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :return: POSTUploadFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_memo_id', 'file', 'zuora_entity_ids', 'zuora_track_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_upload_file_for_credit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `p_ost_upload_file_for_credit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501
        if 'zuora_track_id' in params:
            header_params['Zuora-Track-Id'] = params['zuora_track_id']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/files', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='POSTUploadFileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ostcm_taxation_items(self, body, credit_memo_id, **kwargs):  # noqa: E501
        """Create taxation items for credit memo  # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates taxation items for a credit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ostcm_taxation_items(body, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param POSTTaxationItemListForCMType body: (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETTaxationItemListType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ostcm_taxation_items_with_http_info(body, credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ostcm_taxation_items_with_http_info(body, credit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ostcm_taxation_items_with_http_info(self, body, credit_memo_id, **kwargs):  # noqa: E501
        """Create taxation items for credit memo  # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates taxation items for a credit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ostcm_taxation_items_with_http_info(body, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param POSTTaxationItemListForCMType body: (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETTaxationItemListType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ostcm_taxation_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ostcm_taxation_items`")  # noqa: E501
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `p_ostcm_taxation_items`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/taxationitems', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETTaxationItemListType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_apply_credit_memo(self, body, credit_memo_id, **kwargs):  # noqa: E501
        """Apply credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Applies a posted credit memo to one or more invoices and debit memos.   You can apply a credit memo to an invoice or a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.  When applying a credit memo, the total number of invoices and debit memos that the credit memo will apply to must be less than or equal to 1,000.  If the Proration application rule is used, when applying credit memos, the following quantity must be less than or equal to 10,000:   (number of invoice items + number of debit memo items) * number of credit memo items  Otherwise, the First In First Out rule will be used instead of the Proration rule.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_apply_credit_memo(body, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplyCreditMemoType body: (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ut_apply_credit_memo_with_http_info(body, credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_apply_credit_memo_with_http_info(body, credit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ut_apply_credit_memo_with_http_info(self, body, credit_memo_id, **kwargs):  # noqa: E501
        """Apply credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Applies a posted credit memo to one or more invoices and debit memos.   You can apply a credit memo to an invoice or a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.  When applying a credit memo, the total number of invoices and debit memos that the credit memo will apply to must be less than or equal to 1,000.  If the Proration application rule is used, when applying credit memos, the following quantity must be less than or equal to 10,000:   (number of invoice items + number of debit memo items) * number of credit memo items  Otherwise, the First In First Out rule will be used instead of the Proration rule.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_apply_credit_memo_with_http_info(body, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplyCreditMemoType body: (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_apply_credit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ut_apply_credit_memo`")  # noqa: E501
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `p_ut_apply_credit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/apply', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_cancel_credit_memo(self, credit_memo_id, **kwargs):  # noqa: E501
        """Cancel credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Cancels a credit memo. Only credit memos with the Draft status can be cancelled.   You can cancel a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_cancel_credit_memo(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ut_cancel_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_cancel_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ut_cancel_credit_memo_with_http_info(self, credit_memo_id, **kwargs):  # noqa: E501
        """Cancel credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Cancels a credit memo. Only credit memos with the Draft status can be cancelled.   You can cancel a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_cancel_credit_memo_with_http_info(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_cancel_credit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `p_ut_cancel_credit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/cancel', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_post_credit_memo(self, credit_memo_id, **kwargs):  # noqa: E501
        """Post credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Posts a credit memo to activate it. You can post credit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_post_credit_memo(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ut_post_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_post_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ut_post_credit_memo_with_http_info(self, credit_memo_id, **kwargs):  # noqa: E501
        """Post credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Posts a credit memo to activate it. You can post credit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_post_credit_memo_with_http_info(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_post_credit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `p_ut_post_credit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/post', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_unapply_credit_memo(self, body, credit_memo_id, **kwargs):  # noqa: E501
        """Unapply credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Unapplies an applied credit memo from one or more invoices and debit memos. The full applied amount from invoices and debit memos is transferred into the unapplied amount of the credit memo.   You can unapply a credit memo from an invoice or a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.  When unapplying a credit memo, the total number of invoices and debit memos that the credit memo will be unapplied from must be less than or equal to 1,000.  If the Proration application rule is used, when unapplying credit memos, the following quantity must be less than or equal to 10,000:   (number of invoice items + number of debit memo items) * number of credit memo items  Otherwise, the First In First Out rule will be used instead of the Proration rule.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_unapply_credit_memo(body, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnapplyCreditMemoType body: (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ut_unapply_credit_memo_with_http_info(body, credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_unapply_credit_memo_with_http_info(body, credit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ut_unapply_credit_memo_with_http_info(self, body, credit_memo_id, **kwargs):  # noqa: E501
        """Unapply credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Unapplies an applied credit memo from one or more invoices and debit memos. The full applied amount from invoices and debit memos is transferred into the unapplied amount of the credit memo.   You can unapply a credit memo from an invoice or a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.  When unapplying a credit memo, the total number of invoices and debit memos that the credit memo will be unapplied from must be less than or equal to 1,000.  If the Proration application rule is used, when unapplying credit memos, the following quantity must be less than or equal to 10,000:   (number of invoice items + number of debit memo items) * number of credit memo items  Otherwise, the First In First Out rule will be used instead of the Proration rule.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_unapply_credit_memo_with_http_info(body, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnapplyCreditMemoType body: (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_unapply_credit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ut_unapply_credit_memo`")  # noqa: E501
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `p_ut_unapply_credit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/unapply', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_unpost_credit_memo(self, credit_memo_id, **kwargs):  # noqa: E501
        """Unpost credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Unposts a credit memo that is in Posted status. If a credit memo has been applied or refunded, you are not allowed to unpost it. After a credit memo is unposted, its status becomes Draft.   You can unpost credit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_unpost_credit_memo(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ut_unpost_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_unpost_credit_memo_with_http_info(credit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ut_unpost_credit_memo_with_http_info(self, credit_memo_id, **kwargs):  # noqa: E501
        """Unpost credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Unposts a credit memo that is in Posted status. If a credit memo has been applied or refunded, you are not allowed to unpost it. After a credit memo is unposted, its status becomes Draft.   You can unpost credit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_unpost_credit_memo_with_http_info(credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_unpost_credit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `p_ut_unpost_credit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}/unpost', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_update_credit_memo(self, body, credit_memo_id, **kwargs):  # noqa: E501
        """Update credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Updates the basic and finance information about a credit memo. Currently, Zuora supports updating tax-exclusive memo items, but does not support updating tax-inclusive memo items.   If the amount of a memo item is updated, the tax will be recalculated in the following conditions:   - The memo is created from a product rate plan charge and you use Avalara to calculate the tax.   - The memo is created from an invoice and you use Avalara or Zuora Tax to calculate the tax.  You can update a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_update_credit_memo(body, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PUTCreditMemoType body: (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.   (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ut_update_credit_memo_with_http_info(body, credit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_update_credit_memo_with_http_info(body, credit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ut_update_credit_memo_with_http_info(self, body, credit_memo_id, **kwargs):  # noqa: E501
        """Update credit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Updates the basic and finance information about a credit memo. Currently, Zuora supports updating tax-exclusive memo items, but does not support updating tax-inclusive memo items.   If the amount of a memo item is updated, the tax will be recalculated in the following conditions:   - The memo is created from a product rate plan charge and you use Avalara to calculate the tax.   - The memo is created from an invoice and you use Avalara or Zuora Tax to calculate the tax.  You can update a credit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_update_credit_memo_with_http_info(body, credit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PUTCreditMemoType body: (required)
        :param str credit_memo_id: The unique ID of a credit memo. For example, 8a8082e65b27f6c3015ba45ff82c7172.   (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETCreditMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'credit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_update_credit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ut_update_credit_memo`")  # noqa: E501
        # verify the required parameter 'credit_memo_id' is set
        if ('credit_memo_id' not in params or
                params['credit_memo_id'] is None):
            raise ValueError("Missing the required parameter `credit_memo_id` when calling `p_ut_update_credit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_memo_id' in params:
            path_params['creditMemoId'] = params['credit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/creditmemos/{creditMemoId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCreditMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
