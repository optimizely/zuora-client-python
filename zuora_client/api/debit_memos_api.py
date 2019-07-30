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


class DebitMemosApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def d_elete_debit_memo(self, debit_memo_id, **kwargs):  # noqa: E501
        """Delete debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Deletes a debit memo. Only debit memos with the Cancelled status can be deleted.   You can delete a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.d_elete_debit_memo(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.d_elete_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.d_elete_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
            return data

    def d_elete_debit_memo_with_http_info(self, debit_memo_id, **kwargs):  # noqa: E501
        """Delete debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Deletes a debit memo. Only debit memos with the Cancelled status can be deleted.   You can delete a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.d_elete_debit_memo_with_http_info(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['debit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method d_elete_debit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `d_elete_debit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}', 'DELETE',
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

    def g_et_debit_memo(self, debit_memo_id, **kwargs):  # noqa: E501
        """Get debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific debit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_debit_memo(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETDebitMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_debit_memo_with_http_info(self, debit_memo_id, **kwargs):  # noqa: E501
        """Get debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about a specific debit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_debit_memo_with_http_info(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETDebitMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['debit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_debit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `g_et_debit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETDebitMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_debit_memo_application_parts(self, debit_memo_id, **kwargs):  # noqa: E501
        """Get debit memo application parts  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves information about the payments or credit memos that are applied to a specified debit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_debit_memo_application_parts(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GetDebitMemoApplicationPartCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_debit_memo_application_parts_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_debit_memo_application_parts_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_debit_memo_application_parts_with_http_info(self, debit_memo_id, **kwargs):  # noqa: E501
        """Get debit memo application parts  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves information about the payments or credit memos that are applied to a specified debit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_debit_memo_application_parts_with_http_info(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GetDebitMemoApplicationPartCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['debit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_debit_memo_application_parts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `g_et_debit_memo_application_parts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}/application-parts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetDebitMemoApplicationPartCollectionType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_debit_memo_item(self, dmitemid, debit_memo_id, **kwargs):  # noqa: E501
        """Get debit memo item  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves information about a specific item of a debit memo. A debit memo item is a single line item in a debit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_debit_memo_item(dmitemid, debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dmitemid: The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  (required)
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * taxItems * taxationItems 
        :return: GETDebitMemoItemType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_debit_memo_item_with_http_info(dmitemid, debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_debit_memo_item_with_http_info(dmitemid, debit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_debit_memo_item_with_http_info(self, dmitemid, debit_memo_id, **kwargs):  # noqa: E501
        """Get debit memo item  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves information about a specific item of a debit memo. A debit memo item is a single line item in a debit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_debit_memo_item_with_http_info(dmitemid, debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dmitemid: The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  (required)
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * taxItems * taxationItems 
        :return: GETDebitMemoItemType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dmitemid', 'debit_memo_id', 'zuora_entity_ids', 'zuora_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_debit_memo_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dmitemid' is set
        if ('dmitemid' not in params or
                params['dmitemid'] is None):
            raise ValueError("Missing the required parameter `dmitemid` when calling `g_et_debit_memo_item`")  # noqa: E501
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `g_et_debit_memo_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dmitemid' in params:
            path_params['dmitemid'] = params['dmitemid']  # noqa: E501
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

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
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}/items/{dmitemid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETDebitMemoItemType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_debit_memo_items(self, debit_memo_id, **kwargs):  # noqa: E501
        """Get debit memo items  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all items of a debit memo. A debit memo item is a single line item in a debit memo.   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100&sort=createdDate   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_debit_memo_items(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * taxItems * taxationItems 
        :param float amount: This parameter filters the response based on the `amount` field. 
        :param float be_applied_amount: This parameter filters the response based on the `beAppliedAmount` field. 
        :param str created_by_id: This parameter filters the response based on the `createdById` field. 
        :param datetime created_date: This parameter filters the response based on the `createdDate` field. 
        :param str id: This parameter filters the response based on the `id` field. 
        :param date service_end_date: This parameter filters the response based on the `serviceEndDate` field. 
        :param date service_start_date: This parameter filters the response based on the `serviceStartDate` field. 
        :param str sku: This parameter filters the response based on the `sku` field. 
        :param str sku_name: This parameter filters the response based on the `skuName` field. 
        :param str source_item_id: This parameter filters the response based on the `sourceItemId` field. 
        :param str subscription_id: This parameter filters the response based on the `subscriptionId` field. 
        :param str updated_by_id: This parameter filters the response based on the `updatedById` field. 
        :param datetime updated_date: This parameter filters the response based on the `updatedDate` field. 
        :param str sort: This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by updated date.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - id   - amount   - beAppliedAmount   - sku   - skuName   - serviceStartDate   - serviceEndDate   - sourceItemId   - createdDate   - createdById   - updatedDate   - updatedById   - subscriptionId    Examples:  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?sort=createdDate  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100&sort=createdDate 
        :return: GETDebitMemoItemCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_debit_memo_items_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_debit_memo_items_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_debit_memo_items_with_http_info(self, debit_memo_id, **kwargs):  # noqa: E501
        """Get debit memo items  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves the information about all items of a debit memo. A debit memo item is a single line item in a debit memo.   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100&sort=createdDate   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_debit_memo_items_with_http_info(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * taxItems * taxationItems 
        :param float amount: This parameter filters the response based on the `amount` field. 
        :param float be_applied_amount: This parameter filters the response based on the `beAppliedAmount` field. 
        :param str created_by_id: This parameter filters the response based on the `createdById` field. 
        :param datetime created_date: This parameter filters the response based on the `createdDate` field. 
        :param str id: This parameter filters the response based on the `id` field. 
        :param date service_end_date: This parameter filters the response based on the `serviceEndDate` field. 
        :param date service_start_date: This parameter filters the response based on the `serviceStartDate` field. 
        :param str sku: This parameter filters the response based on the `sku` field. 
        :param str sku_name: This parameter filters the response based on the `skuName` field. 
        :param str source_item_id: This parameter filters the response based on the `sourceItemId` field. 
        :param str subscription_id: This parameter filters the response based on the `subscriptionId` field. 
        :param str updated_by_id: This parameter filters the response based on the `updatedById` field. 
        :param datetime updated_date: This parameter filters the response based on the `updatedDate` field. 
        :param str sort: This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by updated date.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - id   - amount   - beAppliedAmount   - sku   - skuName   - serviceStartDate   - serviceEndDate   - sourceItemId   - createdDate   - createdById   - updatedDate   - updatedById   - subscriptionId    Examples:  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?sort=createdDate  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100&sort=createdDate 
        :return: GETDebitMemoItemCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['debit_memo_id', 'zuora_entity_ids', 'page_size', 'zuora_version', 'amount', 'be_applied_amount', 'created_by_id', 'created_date', 'id', 'service_end_date', 'service_start_date', 'sku', 'sku_name', 'source_item_id', 'subscription_id', 'updated_by_id', 'updated_date', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_debit_memo_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `g_et_debit_memo_items`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 40:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `g_et_debit_memo_items`, must be a value less than or equal to `40`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501
        if 'be_applied_amount' in params:
            query_params.append(('beAppliedAmount', params['be_applied_amount']))  # noqa: E501
        if 'created_by_id' in params:
            query_params.append(('createdById', params['created_by_id']))  # noqa: E501
        if 'created_date' in params:
            query_params.append(('createdDate', params['created_date']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
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
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}/items', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETDebitMemoItemCollectionType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_debit_memos(self, **kwargs):  # noqa: E501
        """Get debit memos  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the information about all debit memos associated with all customer accounts.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/debitmemos?status=Processed  - /v1/debitmemos?referredInvoiceId=null&status=Draft  - /v1/debitmemos?status=Processed&type=External&sort=+number   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_debit_memos(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param str account_id: This parameter filters the response based on the `accountId` field. 
        :param float amount: This parameter filters the response based on the `amount` field. 
        :param float balance: This parameter filters the response based on the `balance` field. 
        :param float be_applied_amount: This parameter filters the response based on the `beAppliedAmount` field. 
        :param str created_by_id: This parameter filters the response based on the `createdById` field. 
        :param datetime created_date: This parameter filters the response based on the `createdDate` field. 
        :param str currency: This parameter filters the response based on the `currency` field. 
        :param date debit_memo_date: This parameter filters the response based on the `debitMemoDate` field. 
        :param date due_date: This parameter filters the response based on the `dueDate` field. 
        :param str number: This parameter filters the response based on the `number` field. 
        :param str referred_invoice_id: This parameter filters the response based on the `referredInvoiceId` field. 
        :param str status: This parameter filters the response based on the `status` field. 
        :param date target_date: This parameter filters the response based on the `targetDate` field. 
        :param float tax_amount: This parameter filters the response based on the `taxAmount` field. 
        :param float total_tax_exempt_amount: This parameter filters the response based on the `totalTaxExemptAmount` field. 
        :param str updated_by_id: This parameter filters the response based on the `updatedById` field. 
        :param datetime updated_date: This parameter filters the response based on the `updatedDate` field. 
        :param str sort: This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by debit memo number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - number   - accountId   - debitMemoDate   - targetDate   - dueDate   - amount   - taxAmount   - totalTaxExemptAmount   - balance   - beAppliedAmount   - referredInvoiceId   - createdDate   - createdById   - updatedDate   - updatedById    Examples:  - /v1/debitmemos?sort=+number  - /v1/debitmemos?status=Processed&sort=-number,+amount 
        :return: GETDebitMemoCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_debit_memos_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.g_et_debit_memos_with_http_info(**kwargs)  # noqa: E501
            return data

    def g_et_debit_memos_with_http_info(self, **kwargs):  # noqa: E501
        """Get debit memos  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves the information about all debit memos associated with all customer accounts.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/debitmemos?status=Processed  - /v1/debitmemos?referredInvoiceId=null&status=Draft  - /v1/debitmemos?status=Processed&type=External&sort=+number   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_debit_memos_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param str account_id: This parameter filters the response based on the `accountId` field. 
        :param float amount: This parameter filters the response based on the `amount` field. 
        :param float balance: This parameter filters the response based on the `balance` field. 
        :param float be_applied_amount: This parameter filters the response based on the `beAppliedAmount` field. 
        :param str created_by_id: This parameter filters the response based on the `createdById` field. 
        :param datetime created_date: This parameter filters the response based on the `createdDate` field. 
        :param str currency: This parameter filters the response based on the `currency` field. 
        :param date debit_memo_date: This parameter filters the response based on the `debitMemoDate` field. 
        :param date due_date: This parameter filters the response based on the `dueDate` field. 
        :param str number: This parameter filters the response based on the `number` field. 
        :param str referred_invoice_id: This parameter filters the response based on the `referredInvoiceId` field. 
        :param str status: This parameter filters the response based on the `status` field. 
        :param date target_date: This parameter filters the response based on the `targetDate` field. 
        :param float tax_amount: This parameter filters the response based on the `taxAmount` field. 
        :param float total_tax_exempt_amount: This parameter filters the response based on the `totalTaxExemptAmount` field. 
        :param str updated_by_id: This parameter filters the response based on the `updatedById` field. 
        :param datetime updated_date: This parameter filters the response based on the `updatedDate` field. 
        :param str sort: This parameter restricts the order of the data returned in the response. You can use this parameter to supply a dimension you want to sort on.  A sortable field uses the following form:   *operator* *field_name*  You can use at most two sortable fields in one URL path. Use a comma to separate sortable fields. For example:  *operator* *field_name*, *operator* *field_name*    *operator* is used to mark the order of sequencing. The operator is optional. If you only specify the sortable field without any operator, the response data is sorted in descending order by this field.    - The `-` operator indicates an ascending order.   - The `+` operator indicates a descending order.  By default, the response data is displayed in descending order by debit memo number.  *field_name* indicates the name of a sortable field. The supported sortable fields of this operation are as below:    - number   - accountId   - debitMemoDate   - targetDate   - dueDate   - amount   - taxAmount   - totalTaxExemptAmount   - balance   - beAppliedAmount   - referredInvoiceId   - createdDate   - createdById   - updatedDate   - updatedById    Examples:  - /v1/debitmemos?sort=+number  - /v1/debitmemos?status=Processed&sort=-number,+amount 
        :return: GETDebitMemoCollectionType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zuora_entity_ids', 'page_size', 'account_id', 'amount', 'balance', 'be_applied_amount', 'created_by_id', 'created_date', 'currency', 'debit_memo_date', 'due_date', 'number', 'referred_invoice_id', 'status', 'target_date', 'tax_amount', 'total_tax_exempt_amount', 'updated_by_id', 'updated_date', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_debit_memos" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] > 40:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `g_et_debit_memos`, must be a value less than or equal to `40`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501
        if 'balance' in params:
            query_params.append(('balance', params['balance']))  # noqa: E501
        if 'be_applied_amount' in params:
            query_params.append(('beAppliedAmount', params['be_applied_amount']))  # noqa: E501
        if 'created_by_id' in params:
            query_params.append(('createdById', params['created_by_id']))  # noqa: E501
        if 'created_date' in params:
            query_params.append(('createdDate', params['created_date']))  # noqa: E501
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501
        if 'debit_memo_date' in params:
            query_params.append(('debitMemoDate', params['debit_memo_date']))  # noqa: E501
        if 'due_date' in params:
            query_params.append(('dueDate', params['due_date']))  # noqa: E501
        if 'number' in params:
            query_params.append(('number', params['number']))  # noqa: E501
        if 'referred_invoice_id' in params:
            query_params.append(('referredInvoiceId', params['referred_invoice_id']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'target_date' in params:
            query_params.append(('targetDate', params['target_date']))  # noqa: E501
        if 'tax_amount' in params:
            query_params.append(('taxAmount', params['tax_amount']))  # noqa: E501
        if 'total_tax_exempt_amount' in params:
            query_params.append(('totalTaxExemptAmount', params['total_tax_exempt_amount']))  # noqa: E501
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
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETDebitMemoCollectionType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def g_et_taxation_items_of_debit_memo_item(self, dmitemid, debit_memo_id, **kwargs):  # noqa: E501
        """Get taxation items of debit memo item  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves information about the taxation items of a specific debit memo item.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_taxation_items_of_debit_memo_item(dmitemid, debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dmitemid: The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  (required)
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param int page: Page number. 
        :return: GETTaxationItemsOfDebitMemoItemType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.g_et_taxation_items_of_debit_memo_item_with_http_info(dmitemid, debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.g_et_taxation_items_of_debit_memo_item_with_http_info(dmitemid, debit_memo_id, **kwargs)  # noqa: E501
            return data

    def g_et_taxation_items_of_debit_memo_item_with_http_info(self, dmitemid, debit_memo_id, **kwargs):  # noqa: E501
        """Get taxation items of debit memo item  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves information about the taxation items of a specific debit memo item.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.g_et_taxation_items_of_debit_memo_item_with_http_info(dmitemid, debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dmitemid: The unique ID of a debit memo item. You can get the debit memo item ID from the response of [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems).  (required)
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param int page_size: Number of rows returned per page. 
        :param int page: Page number. 
        :return: GETTaxationItemsOfDebitMemoItemType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dmitemid', 'debit_memo_id', 'zuora_entity_ids', 'page_size', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method g_et_taxation_items_of_debit_memo_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dmitemid' is set
        if ('dmitemid' not in params or
                params['dmitemid'] is None):
            raise ValueError("Missing the required parameter `dmitemid` when calling `g_et_taxation_items_of_debit_memo_item`")  # noqa: E501
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `g_et_taxation_items_of_debit_memo_item`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 40:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `g_et_taxation_items_of_debit_memo_item`, must be a value less than or equal to `40`")  # noqa: E501
        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `g_et_taxation_items_of_debit_memo_item`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'dmitemid' in params:
            path_params['dmitemid'] = params['dmitemid']  # noqa: E501
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

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
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}/items/{dmitemid}/taxation-items', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETTaxationItemsOfDebitMemoItemType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_debit_memo_from_prpc(self, body, **kwargs):  # noqa: E501
        """Create debit memo from charge  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates an ad-hoc debit memo from a product rate plan charge. Zuora supports the creation of debit memos from any type of product rate plan charge. The charges can also have any amount and any charge model, except for discout charge models.   You can create a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_debit_memo_from_prpc(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DebitMemoFromChargeType body:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * amount * memoItemAmount 
        :return: GETDebitMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ost_debit_memo_from_prpc_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ost_debit_memo_from_prpc_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def p_ost_debit_memo_from_prpc_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create debit memo from charge  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Creates an ad-hoc debit memo from a product rate plan charge. Zuora supports the creation of debit memos from any type of product rate plan charge. The charges can also have any amount and any charge model, except for discout charge models.   You can create a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_debit_memo_from_prpc_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DebitMemoFromChargeType body:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_version:  The minor version of the Zuora REST API. See [Minor Version](https://www.zuora.com/developer/api-reference/#section/API-Versions/Minor-Version) for information about REST API version control.   This header affects the availability of the following fields: * amount * memoItemAmount 
        :return: GETDebitMemoType
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
                    " to method p_ost_debit_memo_from_prpc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ost_debit_memo_from_prpc`")  # noqa: E501

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
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETDebitMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ost_debit_memo_pdf(self, debit_memo_id, **kwargs):  # noqa: E501
        """Create debit memo PDF  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a PDF file for a specified debit memo. To access the generated PDF file, you can download it by clicking **View PDF** on the detailed debit memo page through the Zuora UI.  This REST API operation can be used only if you have the Billing user permission \"Regenerate PDF\" enabled.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_debit_memo_pdf(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of the debit memo that you want to create a PDF file for. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTMemoPdfResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ost_debit_memo_pdf_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ost_debit_memo_pdf_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ost_debit_memo_pdf_with_http_info(self, debit_memo_id, **kwargs):  # noqa: E501
        """Create debit memo PDF  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates a PDF file for a specified debit memo. To access the generated PDF file, you can download it by clicking **View PDF** on the detailed debit memo page through the Zuora UI.  This REST API operation can be used only if you have the Billing user permission \"Regenerate PDF\" enabled.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_debit_memo_pdf_with_http_info(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of the debit memo that you want to create a PDF file for. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: POSTMemoPdfResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['debit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_debit_memo_pdf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `p_ost_debit_memo_pdf`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}/pdfs', 'POST',
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

    def p_ost_email_debit_memo(self, request, debit_memo_id, **kwargs):  # noqa: E501
        """Email debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Sends a posted debit memo to the specified email addresses manually.    ## Notes   - You must activate the **Email Debit Memo | Manually email Debit Memo** notification before emailing debit memos. To include the debit memo PDF in the email, select the **Include Debit Memo PDF** check box in the **Edit notification** dialog from the Zuora UI. See [Create and Edit Notifications](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/C_Create_Notifications#section_2) for more information.     - Zuora sends the email messages based on the email template you set. You can set the email template to use in the **Delivery Options** panel of the **Edit notification** dialog from the Zuora UI. By default, the **Manual Email for Debit Memo Default Template** template is used. See [Create and Edit Email Templates](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/Create_Email_Templates) for more information.     - The debit memos are sent only to the work email addresses or personal email addresses of the Bill To contact if the following conditions are all met:      * The `useEmailTemplateSetting` field is set to `false`.     * The email addresses are not specified in the `emailAddresses` field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_email_debit_memo(request, debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostDebitMemoEmailType request:  (required)
        :param str debit_memo_id: The ID of a posted debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ost_email_debit_memo_with_http_info(request, debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ost_email_debit_memo_with_http_info(request, debit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ost_email_debit_memo_with_http_info(self, request, debit_memo_id, **kwargs):  # noqa: E501
        """Email debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Sends a posted debit memo to the specified email addresses manually.    ## Notes   - You must activate the **Email Debit Memo | Manually email Debit Memo** notification before emailing debit memos. To include the debit memo PDF in the email, select the **Include Debit Memo PDF** check box in the **Edit notification** dialog from the Zuora UI. See [Create and Edit Notifications](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/C_Create_Notifications#section_2) for more information.     - Zuora sends the email messages based on the email template you set. You can set the email template to use in the **Delivery Options** panel of the **Edit notification** dialog from the Zuora UI. By default, the **Manual Email for Debit Memo Default Template** template is used. See [Create and Edit Email Templates](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/Notifications/Create_Email_Templates) for more information.     - The debit memos are sent only to the work email addresses or personal email addresses of the Bill To contact if the following conditions are all met:      * The `useEmailTemplateSetting` field is set to `false`.     * The email addresses are not specified in the `emailAddresses` field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_email_debit_memo_with_http_info(request, debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostDebitMemoEmailType request:  (required)
        :param str debit_memo_id: The ID of a posted debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'debit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_email_debit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `p_ost_email_debit_memo`")  # noqa: E501
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `p_ost_email_debit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}/emails', 'POST',
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

    def p_ost_upload_file_for_debit_memo(self, debit_memo_id, **kwargs):  # noqa: E501
        """Upload file for debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Uploads an externally generated PDF file for a debit memo that is in Draft or Posted status.  This operation has the following restrictions: - Only the PDF file format is supported. - The maximum size of the PDF file to upload is 4 MB. - A maximum of 50 PDF files can be uploaded for one debit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_upload_file_for_debit_memo(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The ID of the debit memo that you want to upload a PDF file for. For example, 402890555a87d7f5015a8919e4fe002e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param file file: The PDF file to upload for the debit memo. 
        :return: POSTUploadFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ost_upload_file_for_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ost_upload_file_for_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ost_upload_file_for_debit_memo_with_http_info(self, debit_memo_id, **kwargs):  # noqa: E501
        """Upload file for debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Uploads an externally generated PDF file for a debit memo that is in Draft or Posted status.  This operation has the following restrictions: - Only the PDF file format is supported. - The maximum size of the PDF file to upload is 4 MB. - A maximum of 50 PDF files can be uploaded for one debit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ost_upload_file_for_debit_memo_with_http_info(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The ID of the debit memo that you want to upload a PDF file for. For example, 402890555a87d7f5015a8919e4fe002e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :param str zuora_track_id: A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`). 
        :param file file: The PDF file to upload for the debit memo. 
        :return: POSTUploadFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['debit_memo_id', 'zuora_entity_ids', 'zuora_track_id', 'file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ost_upload_file_for_debit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `p_ost_upload_file_for_debit_memo`")  # noqa: E501

        if ('zuora_track_id' in params and
                len(params['zuora_track_id']) > 64):
            raise ValueError("Invalid value for parameter `zuora_track_id` when calling `p_ost_upload_file_for_debit_memo`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

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
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}/files', 'POST',
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

    def p_ostdm_taxation_items(self, debit_memo_id, body, **kwargs):  # noqa: E501
        """Create taxation items for debit memo  # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates taxation items for a debit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ostdm_taxation_items(debit_memo_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param POSTTaxationItemListForDMType body:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETTaxationItemListType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ostdm_taxation_items_with_http_info(debit_memo_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ostdm_taxation_items_with_http_info(debit_memo_id, body, **kwargs)  # noqa: E501
            return data

    def p_ostdm_taxation_items_with_http_info(self, debit_memo_id, body, **kwargs):  # noqa: E501
        """Create taxation items for debit memo  # noqa: E501

        **Note:** This feature is only available if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Creates taxation items for a debit memo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ostdm_taxation_items_with_http_info(debit_memo_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param POSTTaxationItemListForDMType body:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETTaxationItemListType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['debit_memo_id', 'body', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ostdm_taxation_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `p_ostdm_taxation_items`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ostdm_taxation_items`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

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
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}/taxationitems', 'POST',
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

    def p_ut_batch_update_debit_memos(self, body, **kwargs):  # noqa: E501
        """Update debit memos  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Updates the due date for multiple debit memos in batches with one call.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_batch_update_debit_memos(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PUTBatchDebitMemosRequest body:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ut_batch_update_debit_memos_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_batch_update_debit_memos_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def p_ut_batch_update_debit_memos_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update debit memos  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Updates the due date for multiple debit memos in batches with one call.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_batch_update_debit_memos_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PUTBatchDebitMemosRequest body:  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: CommonResponseType
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
                    " to method p_ut_batch_update_debit_memos" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ut_batch_update_debit_memos`")  # noqa: E501

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
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos', 'PUT',
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

    def p_ut_cancel_debit_memo(self, debit_memo_id, **kwargs):  # noqa: E501
        """Cancel debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Cancels a debit memo. Only debit memos with the Draft status can be cancelled.   You can cancel a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_cancel_debit_memo(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETDebitMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ut_cancel_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_cancel_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ut_cancel_debit_memo_with_http_info(self, debit_memo_id, **kwargs):  # noqa: E501
        """Cancel debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Cancels a debit memo. Only debit memos with the Draft status can be cancelled.   You can cancel a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_cancel_debit_memo_with_http_info(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETDebitMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['debit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_cancel_debit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `p_ut_cancel_debit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}/cancel', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETDebitMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_debit_memo(self, body, debit_memo_id, **kwargs):  # noqa: E501
        """Update debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Updates the basic and finance information about a debit memo. Currently, Zuora supports updating tax-exclusive memo items, but does not support updating tax-inclusive memo items.   If the amount of a memo item is updated, the tax will be recalculated in the following conditions:   - The memo is created from a product rate plan charge and you use Avalara to calculate the tax.   - The memo is created from an invoice and you use Avalara or Zuora Tax to calculate the tax.  You can update a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_debit_memo(body, debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PUTDebitMemoType body: (required)
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETDebitMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ut_debit_memo_with_http_info(body, debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_debit_memo_with_http_info(body, debit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ut_debit_memo_with_http_info(self, body, debit_memo_id, **kwargs):  # noqa: E501
        """Update debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Updates the basic and finance information about a debit memo. Currently, Zuora supports updating tax-exclusive memo items, but does not support updating tax-inclusive memo items.   If the amount of a memo item is updated, the tax will be recalculated in the following conditions:   - The memo is created from a product rate plan charge and you use Avalara to calculate the tax.   - The memo is created from an invoice and you use Avalara or Zuora Tax to calculate the tax.  You can update a debit memo only if you have the user permission. See [Billing Roles](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles) for more information.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_debit_memo_with_http_info(body, debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PUTDebitMemoType body: (required)
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETDebitMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'debit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_debit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `p_ut_debit_memo`")  # noqa: E501
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `p_ut_debit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

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
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETDebitMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_post_debit_memo(self, debit_memo_id, **kwargs):  # noqa: E501
        """Post debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Posts a debit memo to activate it. You can post debit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_post_debit_memo(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETDebitMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ut_post_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_post_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ut_post_debit_memo_with_http_info(self, debit_memo_id, **kwargs):  # noqa: E501
        """Post debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Posts a debit memo to activate it. You can post debit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_post_debit_memo_with_http_info(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETDebitMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['debit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_post_debit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `p_ut_post_debit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}/post', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETDebitMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def p_ut_unpost_debit_memo(self, debit_memo_id, **kwargs):  # noqa: E501
        """Unpost debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Unposts a debit memo that is in Posted status. If any credit memo or payment has been applied to a debit memo, you are not allowed to unpost the debit memo. After a debit memo is unposted, its status becomes Draft.  You can unpost debit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_unpost_debit_memo(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETDebitMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.p_ut_unpost_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.p_ut_unpost_debit_memo_with_http_info(debit_memo_id, **kwargs)  # noqa: E501
            return data

    def p_ut_unpost_debit_memo_with_http_info(self, debit_memo_id, **kwargs):  # noqa: E501
        """Unpost debit memo  # noqa: E501

        **Note:** The Invoice Settlement feature is in **Limited Availability**. This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Unposts a debit memo that is in Posted status. If any credit memo or payment has been applied to a debit memo, you are not allowed to unpost the debit memo. After a debit memo is unposted, its status becomes Draft.  You can unpost debit memos only if you have the [Billing permissions](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/User_Roles/d_Billing_Roles#Billing_Permissions).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.p_ut_unpost_debit_memo_with_http_info(debit_memo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str debit_memo_id: The unique ID of a debit memo. For example, 8a8082e65b27f6c3015ba419f3c2644e.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header. 
        :return: GETDebitMemoType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['debit_memo_id', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method p_ut_unpost_debit_memo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'debit_memo_id' is set
        if ('debit_memo_id' not in params or
                params['debit_memo_id'] is None):
            raise ValueError("Missing the required parameter `debit_memo_id` when calling `p_ut_unpost_debit_memo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'debit_memo_id' in params:
            path_params['debitMemoId'] = params['debit_memo_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/debitmemos/{debitMemoId}/unpost', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETDebitMemoType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
