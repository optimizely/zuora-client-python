# coding: utf-8

"""
    Zuora API Reference

      # Introduction Welcome to the reference for the Zuora REST API!  <a href=\"http://en.wikipedia.org/wiki/REST_API\" target=\"_blank\">REST</a> is a web-service protocol that lends itself to rapid development by using everyday HTTP and JSON technology.  The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Production | https://rest.zuora.com   | |US API Sandbox    | https://rest.apisandbox.zuora.com| |US Performance Test | https://rest.pt1.zuora.com | |EU Production | https://rest.eu.zuora.com | |EU Sandbox | https://rest.sandbox.eu.zuora.com |  The Production endpoint provides access to your live user data. API Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision an API Sandbox tenant for you, contact your Zuora representative for assistance.  **Note:** If you have a tenant in the Production Copy Environment, submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints.  If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.  # API Changelog You can find the <a href=\"https://community.zuora.com/t5/Developers/API-Changelog/gpm-p/18092\" target=\"_blank\">Changelog</a> of the API Reference in the Zuora Community.  # Authentication  ## OAuth v2.0  Zuora recommends that you use OAuth v2.0 to authenticate to the Zuora REST API. Currently, OAuth is not available in every environment. See [Zuora Testing Environments](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Environments) for more information.  Zuora recommends you to create a dedicated API user with API write access on a tenant when authenticating via OAuth, and then create an OAuth client for this user. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for how to do this. By creating a dedicated API user, you can control permissions of the API user without affecting other non-API users.  If a user is deactivated, all of the user's OAuth clients will be automatically deactivated.  Authenticating via OAuth requires the following steps: 1. Create a Client 2. Generate a Token 3. Make Authenticated Requests  ### Create a Client  You must first [create an OAuth client](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) in the Zuora UI. To do this, you must be an administrator of your Zuora tenant. This is a one-time operation. You will be provided with a Client ID and a Client Secret. Please note this information down, as it will be required for the next step.  **Note:** The OAuth client will be owned by a Zuora user account. If you want to perform PUT, POST, or DELETE operations using the OAuth client, the owner of the OAuth client must have a Platform role that includes the \"API Write Access\" permission.  ### Generate a Token  After creating a client, you must make a call to obtain a bearer token using the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) operation. This operation requires the following parameters: - `client_id` - the Client ID displayed when you created the OAuth client in the previous step - `client_secret` - the Client Secret displayed when you created the OAuth client in the previous step - `grant_type` - must be set to `client_credentials`  **Note**: The Client ID and Client Secret mentioned above were displayed when you created the OAuth Client in the prior step. The [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response specifies how long the bearer token is valid for. Call [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) again to generate a new bearer token.  ### Make Authenticated Requests  To authenticate subsequent API requests, you must provide a valid bearer token in an HTTP header:  `Authorization: Bearer {bearer_token}`  If you have [Zuora Multi-entity](https://www.zuora.com/developer/api-reference/#tag/Entities) enabled, you need to set an additional header to specify the ID of the entity that you want to access. You can use the `scope` field in the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response to determine whether you need to specify an entity ID.  If the `scope` field contains more than one entity ID, you must specify the ID of the entity that you want to access. For example, if the `scope` field contains `entity.1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` and `entity.c92ed977-510c-4c48-9b51-8d5e848671e9`, specify one of the following headers: - `Zuora-Entity-Ids: 1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` - `Zuora-Entity-Ids: c92ed977-510c-4c48-9b51-8d5e848671e9`  **Note**: For a limited period of time, Zuora will accept the `entityId` header as an alternative to the `Zuora-Entity-Ids` header. If you choose to set the `entityId` header, you must remove all \"-\" characters from the entity ID in the `scope` field.  If the `scope` field contains a single entity ID, you do not need to specify an entity ID.  ## Other Supported Authentication Schemes  Zuora continues to support the following additional legacy means of authentication:    * Use username and password. Include authentication with each request in the header:         * `apiAccessKeyId`      * `apiSecretAccessKey`          Zuora recommends that you create an API user specifically for making API calls. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for more information.      * Use an authorization cookie. The cookie authorizes the user to make calls to the REST API for the duration specified in  **Administration > Security Policies > Session timeout**. The cookie expiration time is reset with this duration after every call to the REST API. To obtain a cookie, call the [Connections](https://www.zuora.com/developer/api-reference/#tag/Connections) resource with the following API user information:         *   ID         *   Password        * For CORS-enabled APIs only: Include a 'single-use' token in the request header, which re-authenticates the user with each request. See below for more details.  ### Entity Id and Entity Name  The `entityId` and `entityName` parameters are only used for [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity \"Zuora Multi-entity\"). These are the legacy parameters that Zuora will only continue to support for a period of time. Zuora recommends you to use the `Zuora-Entity-Ids` parameter instead.   The  `entityId` and `entityName` parameters specify the Id and the [name of the entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/B_Introduction_to_Entity_and_Entity_Hierarchy#Name_and_Display_Name \"Introduction to Entity and Entity Hierarchy\") that you want to access, respectively. Note that you must have permission to access the entity.   You can specify either the `entityId` or `entityName` parameter in the authentication to access and view an entity.    * If both `entityId` and `entityName` are specified in the authentication, an error occurs.    * If neither `entityId` nor `entityName` is specified in the authentication, you will log in to the entity in which your user account is created.      To get the entity Id and entity name, you can use the GET Entities REST call. For more information, see [API User Authentication](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/A_Overview_of_Multi-entity#API_User_Authentication \"API User Authentication\").      ### Token Authentication for CORS-Enabled APIs      The CORS mechanism enables REST API calls to Zuora to be made directly from your customer's browser, with all credit card and security information transmitted directly to Zuora. This minimizes your PCI compliance burden, allows you to implement advanced validation on your payment forms, and  makes your payment forms look just like any other part of your website.    For security reasons, instead of using cookies, an API request via CORS uses **tokens** for authentication.  The token method of authentication is only designed for use with requests that must originate from your customer's browser; **it should  not be considered a replacement to the existing cookie authentication** mechanism.  See [Zuora CORS REST](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Zuora_CORS_REST \"Zuora CORS REST\") for details on how CORS works and how you can begin to implement customer calls to the Zuora REST APIs. See  [HMAC Signatures](https://www.zuora.com/developer/api-reference/#operation/POSTHMACSignature \"HMAC Signatures\") for details on the HMAC method that returns the authentication token.  # Requests and Responses  ## Request IDs  As a general rule, when asked to supply a \"key\" for an account or subscription (accountKey, account-key, subscriptionKey, subscription-key), you can provide either the actual ID or  the number of the entity.  ## HTTP Request Body  Most of the parameters and data accompanying your requests will be contained in the body of the HTTP request.   The Zuora REST API accepts JSON in the HTTP request body. No other data format (e.g., XML) is supported.  ### Data Type  ([Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations only) We recommend that you do not specify the decimal values with quotation marks, commas, and spaces. Use characters of `+-0-9.eE`, for example, `5`, `1.9`, `-8.469`, and `7.7e2`. Also, Zuora does not convert currencies for decimal values.  ## Testing a Request  Use a third party client, such as [curl](https://curl.haxx.se \"curl\"), [Postman](https://www.getpostman.com \"Postman\"), or [Advanced REST Client](https://advancedrestclient.com \"Advanced REST Client\"), to test the Zuora REST API.  You can test the Zuora REST API from the Zuora API Sandbox or Production tenants. If connecting to Production, bear in mind that you are working with your live production data, not sample data or test data.  ## Testing with Credit Cards  Sooner or later it will probably be necessary to test some transactions that involve credit cards. For suggestions on how to handle this, see [Going Live With Your Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards \"C_Zuora_User_Guides/A_Billing_and_Payments/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards\" ).  ## Concurrent Request Limits  Zuora enforces tenant-level concurrent request limits. See <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits\" target=\"_blank\">Concurrent Request Limits</a> for more information.  ## Timeout Limit  If a request does not complete within 120 seconds, the request times out and Zuora returns a Gateway Timeout error.  ## Error Handling  Responses and error codes are detailed in [Responses and errors](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Responses_and_Errors \"Responses and errors\").  # Pagination  When retrieving information (using GET methods), the optional `pageSize` query parameter sets the maximum number of rows to return in a response. The maximum is `40`; larger values are treated as `40`. If this value is empty or invalid, `pageSize` typically defaults to `10`.  The default value for the maximum number of rows retrieved can be overridden at the method level.  If more rows are available, the response will include a `nextPage` element, which contains a URL for requesting the next page.  If this value is not provided, no more rows are available. No \"previous page\" element is explicitly provided; to support backward paging, use the previous call.  ## Array Size  For data items that are not paginated, the REST API supports arrays of up to 300 rows.  Thus, for instance, repeated pagination can retrieve thousands of customer accounts, but within any account an array of no more than 300 rate plans is returned.  # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.  ## Major Version  The major version number of the REST API appears in the REST URL. Currently, Zuora only supports the **v1** major version. For example, `POST https://rest.zuora.com/v1/subscriptions`.  ## Minor Version  Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.   Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not serial. This section documents the changes made to each Zuora REST API minor version.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 196.0 and earlier  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. | | creditTaxItems | 238.0 and earlier | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\") | Container for the taxation items of the credit memo item. | | taxItems | 238.0 and earlier | [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the debit memo item. | | taxationItems | 239.0 and later | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the memo item. |   #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") and [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics  # Zuora Object Model  The following diagram presents a high-level view of the key Zuora objects. Click the image to open it in a new tab to resize it.  <a href=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" target=\"_blank\"><img src=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" alt=\"Zuora Object Model Diagram\"></a>  See the following articles for information about other parts of the Zuora business object model:    * <a href=\"https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/D_Invoice_Settlement_Object_Model\" target=\"_blank\">Invoice Settlement Object Model</a>   * <a href=\"https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/BA_Orders_Object_Model\" target=\"_blank\">Orders Object Model</a>  You can use the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun`</p><p>**Note:** The API name of this object is `BillingRun` in the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation, Export ZOQL queries, and Data Query. Otherwise, the API name of this object is `BillRun`.</p> | | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Feature                                       | `Feature`                                  | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                         | `UpdaterDetail`                            | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Feature                               | `ProductFeature`                           | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Subscription Product Feature                  | `SubscriptionProductFeature`               | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    |   # noqa: E501

    OpenAPI spec version: 2019-07-26
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from zuora_client.models.post_tier_type import POSTTierType  # noqa: F401,E501
from zuora_client.models.rate_plan_charge_object_custom_fields import RatePlanChargeObjectCustomFields  # noqa: F401,E501


class POSTScCreateType(object):
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
        'apply_discount_to': 'str',
        'bill_cycle_day': 'str',
        'bill_cycle_type': 'str',
        'billing_period': 'str',
        'billing_period_alignment': 'str',
        'billing_timing': 'str',
        'description': 'str',
        'discount_amount': 'str',
        'discount_level': 'str',
        'discount_percentage': 'str',
        'end_date_condition': 'str',
        'included_units': 'str',
        'list_price_base': 'str',
        'number': 'str',
        'number_of_periods': 'int',
        'overage_price': 'str',
        'overage_unused_units_credit_option': 'str',
        'price': 'str',
        'price_change_option': 'str',
        'price_increase_percentage': 'str',
        'product_rate_plan_charge_id': 'str',
        'quantity': 'str',
        'rating_group': 'str',
        'specific_billing_period': 'int',
        'specific_end_date': 'date',
        'tiers': 'list[POSTTierType]',
        'trigger_date': 'date',
        'trigger_event': 'str',
        'unused_units_credit_rates': 'str',
        'up_to_periods': 'int',
        'up_to_periods_type': 'str',
        'weekly_bill_cycle_day': 'str'
    }

    attribute_map = {
        'apply_discount_to': 'applyDiscountTo',
        'bill_cycle_day': 'billCycleDay',
        'bill_cycle_type': 'billCycleType',
        'billing_period': 'billingPeriod',
        'billing_period_alignment': 'billingPeriodAlignment',
        'billing_timing': 'billingTiming',
        'description': 'description',
        'discount_amount': 'discountAmount',
        'discount_level': 'discountLevel',
        'discount_percentage': 'discountPercentage',
        'end_date_condition': 'endDateCondition',
        'included_units': 'includedUnits',
        'list_price_base': 'listPriceBase',
        'number': 'number',
        'number_of_periods': 'numberOfPeriods',
        'overage_price': 'overagePrice',
        'overage_unused_units_credit_option': 'overageUnusedUnitsCreditOption',
        'price': 'price',
        'price_change_option': 'priceChangeOption',
        'price_increase_percentage': 'priceIncreasePercentage',
        'product_rate_plan_charge_id': 'productRatePlanChargeId',
        'quantity': 'quantity',
        'rating_group': 'ratingGroup',
        'specific_billing_period': 'specificBillingPeriod',
        'specific_end_date': 'specificEndDate',
        'tiers': 'tiers',
        'trigger_date': 'triggerDate',
        'trigger_event': 'triggerEvent',
        'unused_units_credit_rates': 'unusedUnitsCreditRates',
        'up_to_periods': 'upToPeriods',
        'up_to_periods_type': 'upToPeriodsType',
        'weekly_bill_cycle_day': 'weeklyBillCycleDay'
    }

    def __init__(self, apply_discount_to=None, bill_cycle_day=None, bill_cycle_type=None, billing_period=None, billing_period_alignment=None, billing_timing=None, description=None, discount_amount=None, discount_level=None, discount_percentage=None, end_date_condition=None, included_units=None, list_price_base=None, number=None, number_of_periods=None, overage_price=None, overage_unused_units_credit_option=None, price=None, price_change_option=None, price_increase_percentage=None, product_rate_plan_charge_id=None, quantity=None, rating_group=None, specific_billing_period=None, specific_end_date=None, tiers=None, trigger_date=None, trigger_event=None, unused_units_credit_rates=None, up_to_periods=None, up_to_periods_type=None, weekly_bill_cycle_day=None):  # noqa: E501
        """POSTScCreateType - a model defined in Swagger"""  # noqa: E501

        self._apply_discount_to = None
        self._bill_cycle_day = None
        self._bill_cycle_type = None
        self._billing_period = None
        self._billing_period_alignment = None
        self._billing_timing = None
        self._description = None
        self._discount_amount = None
        self._discount_level = None
        self._discount_percentage = None
        self._end_date_condition = None
        self._included_units = None
        self._list_price_base = None
        self._number = None
        self._number_of_periods = None
        self._overage_price = None
        self._overage_unused_units_credit_option = None
        self._price = None
        self._price_change_option = None
        self._price_increase_percentage = None
        self._product_rate_plan_charge_id = None
        self._quantity = None
        self._rating_group = None
        self._specific_billing_period = None
        self._specific_end_date = None
        self._tiers = None
        self._trigger_date = None
        self._trigger_event = None
        self._unused_units_credit_rates = None
        self._up_to_periods = None
        self._up_to_periods_type = None
        self._weekly_bill_cycle_day = None
        self.discriminator = None

        if apply_discount_to is not None:
            self.apply_discount_to = apply_discount_to
        if bill_cycle_day is not None:
            self.bill_cycle_day = bill_cycle_day
        if bill_cycle_type is not None:
            self.bill_cycle_type = bill_cycle_type
        if billing_period is not None:
            self.billing_period = billing_period
        if billing_period_alignment is not None:
            self.billing_period_alignment = billing_period_alignment
        if billing_timing is not None:
            self.billing_timing = billing_timing
        if description is not None:
            self.description = description
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if discount_level is not None:
            self.discount_level = discount_level
        if discount_percentage is not None:
            self.discount_percentage = discount_percentage
        if end_date_condition is not None:
            self.end_date_condition = end_date_condition
        if included_units is not None:
            self.included_units = included_units
        if list_price_base is not None:
            self.list_price_base = list_price_base
        if number is not None:
            self.number = number
        if number_of_periods is not None:
            self.number_of_periods = number_of_periods
        if overage_price is not None:
            self.overage_price = overage_price
        if overage_unused_units_credit_option is not None:
            self.overage_unused_units_credit_option = overage_unused_units_credit_option
        if price is not None:
            self.price = price
        if price_change_option is not None:
            self.price_change_option = price_change_option
        if price_increase_percentage is not None:
            self.price_increase_percentage = price_increase_percentage
        self.product_rate_plan_charge_id = product_rate_plan_charge_id
        if quantity is not None:
            self.quantity = quantity
        if rating_group is not None:
            self.rating_group = rating_group
        if specific_billing_period is not None:
            self.specific_billing_period = specific_billing_period
        if specific_end_date is not None:
            self.specific_end_date = specific_end_date
        if tiers is not None:
            self.tiers = tiers
        if trigger_date is not None:
            self.trigger_date = trigger_date
        if trigger_event is not None:
            self.trigger_event = trigger_event
        if unused_units_credit_rates is not None:
            self.unused_units_credit_rates = unused_units_credit_rates
        if up_to_periods is not None:
            self.up_to_periods = up_to_periods
        if up_to_periods_type is not None:
            self.up_to_periods_type = up_to_periods_type
        if weekly_bill_cycle_day is not None:
            self.weekly_bill_cycle_day = weekly_bill_cycle_day

    @property
    def apply_discount_to(self):
        """Gets the apply_discount_to of this POSTScCreateType.  # noqa: E501

        Specifies the type of charges that you want a specific discount to apply to.  Values:  * `ONETIME` * `RECURRING` * `USAGE` * `ONETIMERECURRING` * `ONETIMEUSAGE` * `RECURRINGUSAGE` * `ONETIMERECURRINGUSAGE`   # noqa: E501

        :return: The apply_discount_to of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._apply_discount_to

    @apply_discount_to.setter
    def apply_discount_to(self, apply_discount_to):
        """Sets the apply_discount_to of this POSTScCreateType.

        Specifies the type of charges that you want a specific discount to apply to.  Values:  * `ONETIME` * `RECURRING` * `USAGE` * `ONETIMERECURRING` * `ONETIMEUSAGE` * `RECURRINGUSAGE` * `ONETIMERECURRINGUSAGE`   # noqa: E501

        :param apply_discount_to: The apply_discount_to of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._apply_discount_to = apply_discount_to

    @property
    def bill_cycle_day(self):
        """Gets the bill_cycle_day of this POSTScCreateType.  # noqa: E501

        Sets the bill cycle day (BCD) for the charge. The BCD determines which day of the month the customer is billed.  Values: `1`-`31`   # noqa: E501

        :return: The bill_cycle_day of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._bill_cycle_day

    @bill_cycle_day.setter
    def bill_cycle_day(self, bill_cycle_day):
        """Sets the bill_cycle_day of this POSTScCreateType.

        Sets the bill cycle day (BCD) for the charge. The BCD determines which day of the month the customer is billed.  Values: `1`-`31`   # noqa: E501

        :param bill_cycle_day: The bill_cycle_day of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._bill_cycle_day = bill_cycle_day

    @property
    def bill_cycle_type(self):
        """Gets the bill_cycle_type of this POSTScCreateType.  # noqa: E501

        Specifies how to determine the billing day for the charge. When this field is set to `SpecificDayofMonth`, set the `BillCycleDay` field. When this field is set to `SpecificDayofWeek`, set the `weeklyBillCycleDay` field.  Values:  * `DefaultFromCustomer` * `SpecificDayofMonth` * `SubscriptionStartDay` * `ChargeTriggerDay` * `SpecificDayofWeek`   # noqa: E501

        :return: The bill_cycle_type of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._bill_cycle_type

    @bill_cycle_type.setter
    def bill_cycle_type(self, bill_cycle_type):
        """Sets the bill_cycle_type of this POSTScCreateType.

        Specifies how to determine the billing day for the charge. When this field is set to `SpecificDayofMonth`, set the `BillCycleDay` field. When this field is set to `SpecificDayofWeek`, set the `weeklyBillCycleDay` field.  Values:  * `DefaultFromCustomer` * `SpecificDayofMonth` * `SubscriptionStartDay` * `ChargeTriggerDay` * `SpecificDayofWeek`   # noqa: E501

        :param bill_cycle_type: The bill_cycle_type of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._bill_cycle_type = bill_cycle_type

    @property
    def billing_period(self):
        """Gets the billing_period of this POSTScCreateType.  # noqa: E501

        Billing period for the charge. The start day of the billing period is also called the bill cycle day (BCD).  Values:  * `Month` * `Quarter` * `Semi_Annual` * `Annual` * `Eighteen_Months` * `Two_Years` * `Three_Years` * `Five_Years` * `Specific_Months` * `Subscription_Term` * `Week` * `Specific_Weeks`   # noqa: E501

        :return: The billing_period of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this POSTScCreateType.

        Billing period for the charge. The start day of the billing period is also called the bill cycle day (BCD).  Values:  * `Month` * `Quarter` * `Semi_Annual` * `Annual` * `Eighteen_Months` * `Two_Years` * `Three_Years` * `Five_Years` * `Specific_Months` * `Subscription_Term` * `Week` * `Specific_Weeks`   # noqa: E501

        :param billing_period: The billing_period of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._billing_period = billing_period

    @property
    def billing_period_alignment(self):
        """Gets the billing_period_alignment of this POSTScCreateType.  # noqa: E501

        Aligns charges within the same subscription if multiple charges begin on different dates.  Values:  * `AlignToCharge` * `AlignToSubscriptionStart` * `AlignToTermStart`   # noqa: E501

        :return: The billing_period_alignment of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._billing_period_alignment

    @billing_period_alignment.setter
    def billing_period_alignment(self, billing_period_alignment):
        """Sets the billing_period_alignment of this POSTScCreateType.

        Aligns charges within the same subscription if multiple charges begin on different dates.  Values:  * `AlignToCharge` * `AlignToSubscriptionStart` * `AlignToTermStart`   # noqa: E501

        :param billing_period_alignment: The billing_period_alignment of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._billing_period_alignment = billing_period_alignment

    @property
    def billing_timing(self):
        """Gets the billing_timing of this POSTScCreateType.  # noqa: E501

        Billing timing for the charge for recurring charge types. Not avaliable for one time, usage, and discount charges.  Values:  * `IN_ADVANCE` (default) * `IN_ARREARS`   # noqa: E501

        :return: The billing_timing of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._billing_timing

    @billing_timing.setter
    def billing_timing(self, billing_timing):
        """Sets the billing_timing of this POSTScCreateType.

        Billing timing for the charge for recurring charge types. Not avaliable for one time, usage, and discount charges.  Values:  * `IN_ADVANCE` (default) * `IN_ARREARS`   # noqa: E501

        :param billing_timing: The billing_timing of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._billing_timing = billing_timing

    @property
    def description(self):
        """Gets the description of this POSTScCreateType.  # noqa: E501

        Description of the charge.   # noqa: E501

        :return: The description of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this POSTScCreateType.

        Description of the charge.   # noqa: E501

        :param description: The description of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def discount_amount(self):
        """Gets the discount_amount of this POSTScCreateType.  # noqa: E501

        Specifies the amount of fixed-amount discount.   # noqa: E501

        :return: The discount_amount of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this POSTScCreateType.

        Specifies the amount of fixed-amount discount.   # noqa: E501

        :param discount_amount: The discount_amount of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._discount_amount = discount_amount

    @property
    def discount_level(self):
        """Gets the discount_level of this POSTScCreateType.  # noqa: E501

        Specifies if the discount applies to the product rate plan only, the entire subscription, or to any activity in the account.  Values:  * `rateplan` * `subscription` * `account`   # noqa: E501

        :return: The discount_level of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._discount_level

    @discount_level.setter
    def discount_level(self, discount_level):
        """Sets the discount_level of this POSTScCreateType.

        Specifies if the discount applies to the product rate plan only, the entire subscription, or to any activity in the account.  Values:  * `rateplan` * `subscription` * `account`   # noqa: E501

        :param discount_level: The discount_level of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._discount_level = discount_level

    @property
    def discount_percentage(self):
        """Gets the discount_percentage of this POSTScCreateType.  # noqa: E501

        Percentage of discount for a percentage discount.    # noqa: E501

        :return: The discount_percentage of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, discount_percentage):
        """Sets the discount_percentage of this POSTScCreateType.

        Percentage of discount for a percentage discount.    # noqa: E501

        :param discount_percentage: The discount_percentage of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._discount_percentage = discount_percentage

    @property
    def end_date_condition(self):
        """Gets the end_date_condition of this POSTScCreateType.  # noqa: E501

        Defines when the charge ends after the charge trigger date. If the subscription ends before the charge end date, the charge ends when the subscription ends. But if the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge will end on the charge end date.  Values:  * `Subscription_End` * `Fixed_Period` * `Specific_End_Date`   # noqa: E501

        :return: The end_date_condition of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._end_date_condition

    @end_date_condition.setter
    def end_date_condition(self, end_date_condition):
        """Sets the end_date_condition of this POSTScCreateType.

        Defines when the charge ends after the charge trigger date. If the subscription ends before the charge end date, the charge ends when the subscription ends. But if the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge will end on the charge end date.  Values:  * `Subscription_End` * `Fixed_Period` * `Specific_End_Date`   # noqa: E501

        :param end_date_condition: The end_date_condition of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._end_date_condition = end_date_condition

    @property
    def included_units(self):
        """Gets the included_units of this POSTScCreateType.  # noqa: E501

        Specifies the number of units in the base set of units for this charge. Must be >=`0`.   # noqa: E501

        :return: The included_units of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._included_units

    @included_units.setter
    def included_units(self, included_units):
        """Sets the included_units of this POSTScCreateType.

        Specifies the number of units in the base set of units for this charge. Must be >=`0`.   # noqa: E501

        :param included_units: The included_units of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._included_units = included_units

    @property
    def list_price_base(self):
        """Gets the list_price_base of this POSTScCreateType.  # noqa: E501

        The list price base for the product rate plan charge.  Values:  * `Per_Billing_Period` * `Per_Month` * `Per_Week`   # noqa: E501

        :return: The list_price_base of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._list_price_base

    @list_price_base.setter
    def list_price_base(self, list_price_base):
        """Sets the list_price_base of this POSTScCreateType.

        The list price base for the product rate plan charge.  Values:  * `Per_Billing_Period` * `Per_Month` * `Per_Week`   # noqa: E501

        :param list_price_base: The list_price_base of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._list_price_base = list_price_base

    @property
    def number(self):
        """Gets the number of this POSTScCreateType.  # noqa: E501

        Unique number that identifies the charge. Max 50 characters. System-generated if not provided.   # noqa: E501

        :return: The number of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this POSTScCreateType.

        Unique number that identifies the charge. Max 50 characters. System-generated if not provided.   # noqa: E501

        :param number: The number of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def number_of_periods(self):
        """Gets the number_of_periods of this POSTScCreateType.  # noqa: E501

        Specifies the number of periods to use when calculating charges in an overage smoothing charge model.   # noqa: E501

        :return: The number_of_periods of this POSTScCreateType.  # noqa: E501
        :rtype: int
        """
        return self._number_of_periods

    @number_of_periods.setter
    def number_of_periods(self, number_of_periods):
        """Sets the number_of_periods of this POSTScCreateType.

        Specifies the number of periods to use when calculating charges in an overage smoothing charge model.   # noqa: E501

        :param number_of_periods: The number_of_periods of this POSTScCreateType.  # noqa: E501
        :type: int
        """

        self._number_of_periods = number_of_periods

    @property
    def overage_price(self):
        """Gets the overage_price of this POSTScCreateType.  # noqa: E501

        Price for units over the allowed amount.   # noqa: E501

        :return: The overage_price of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._overage_price

    @overage_price.setter
    def overage_price(self, overage_price):
        """Sets the overage_price of this POSTScCreateType.

        Price for units over the allowed amount.   # noqa: E501

        :param overage_price: The overage_price of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._overage_price = overage_price

    @property
    def overage_unused_units_credit_option(self):
        """Gets the overage_unused_units_credit_option of this POSTScCreateType.  # noqa: E501

        Determines whether to credit the customer with unused units of usage.  Values:  * `NoCredit` * `CreditBySpecificRate`   # noqa: E501

        :return: The overage_unused_units_credit_option of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._overage_unused_units_credit_option

    @overage_unused_units_credit_option.setter
    def overage_unused_units_credit_option(self, overage_unused_units_credit_option):
        """Sets the overage_unused_units_credit_option of this POSTScCreateType.

        Determines whether to credit the customer with unused units of usage.  Values:  * `NoCredit` * `CreditBySpecificRate`   # noqa: E501

        :param overage_unused_units_credit_option: The overage_unused_units_credit_option of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._overage_unused_units_credit_option = overage_unused_units_credit_option

    @property
    def price(self):
        """Gets the price of this POSTScCreateType.  # noqa: E501

        Price for units in the subscription rate plan.   # noqa: E501

        :return: The price of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this POSTScCreateType.

        Price for units in the subscription rate plan.   # noqa: E501

        :param price: The price of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def price_change_option(self):
        """Gets the price_change_option of this POSTScCreateType.  # noqa: E501

        Applies an automatic price change when a termed subscription is renewed. The Billing Admin setting **Enable Automatic Price Change When Subscriptions are Renewed?** must be set to Yes to use this field. Values:  * `NoChange` (default) * `SpecificPercentageValue` * `UseLatestProductCatalogPricing`   # noqa: E501

        :return: The price_change_option of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._price_change_option

    @price_change_option.setter
    def price_change_option(self, price_change_option):
        """Sets the price_change_option of this POSTScCreateType.

        Applies an automatic price change when a termed subscription is renewed. The Billing Admin setting **Enable Automatic Price Change When Subscriptions are Renewed?** must be set to Yes to use this field. Values:  * `NoChange` (default) * `SpecificPercentageValue` * `UseLatestProductCatalogPricing`   # noqa: E501

        :param price_change_option: The price_change_option of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._price_change_option = price_change_option

    @property
    def price_increase_percentage(self):
        """Gets the price_increase_percentage of this POSTScCreateType.  # noqa: E501

        Specifies the percentage to increase or decrease the price of a termed subscription's renewal. Required if you set the `PriceChangeOption` field to `SpecificPercentageValue`.   Value must be a decimal between `-100` and `100`.   # noqa: E501

        :return: The price_increase_percentage of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._price_increase_percentage

    @price_increase_percentage.setter
    def price_increase_percentage(self, price_increase_percentage):
        """Sets the price_increase_percentage of this POSTScCreateType.

        Specifies the percentage to increase or decrease the price of a termed subscription's renewal. Required if you set the `PriceChangeOption` field to `SpecificPercentageValue`.   Value must be a decimal between `-100` and `100`.   # noqa: E501

        :param price_increase_percentage: The price_increase_percentage of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._price_increase_percentage = price_increase_percentage

    @property
    def product_rate_plan_charge_id(self):
        """Gets the product_rate_plan_charge_id of this POSTScCreateType.  # noqa: E501

        ID of a product rate-plan charge for this subscription.   # noqa: E501

        :return: The product_rate_plan_charge_id of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_charge_id

    @product_rate_plan_charge_id.setter
    def product_rate_plan_charge_id(self, product_rate_plan_charge_id):
        """Sets the product_rate_plan_charge_id of this POSTScCreateType.

        ID of a product rate-plan charge for this subscription.   # noqa: E501

        :param product_rate_plan_charge_id: The product_rate_plan_charge_id of this POSTScCreateType.  # noqa: E501
        :type: str
        """
        if product_rate_plan_charge_id is None:
            raise ValueError("Invalid value for `product_rate_plan_charge_id`, must not be `None`")  # noqa: E501

        self._product_rate_plan_charge_id = product_rate_plan_charge_id

    @property
    def quantity(self):
        """Gets the quantity of this POSTScCreateType.  # noqa: E501

        Number of units. Must be a decimal >=`0`.   When using `chargeOverrides` for creating subscriptions with recurring charge types, the `quantity` field must be populated when the charge model is \"Tiered Pricing\" or \"Volume Pricing\". It is not required for \"Flat Fee Pricing\" charge model.   # noqa: E501

        :return: The quantity of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this POSTScCreateType.

        Number of units. Must be a decimal >=`0`.   When using `chargeOverrides` for creating subscriptions with recurring charge types, the `quantity` field must be populated when the charge model is \"Tiered Pricing\" or \"Volume Pricing\". It is not required for \"Flat Fee Pricing\" charge model.   # noqa: E501

        :param quantity: The quantity of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._quantity = quantity

    @property
    def rating_group(self):
        """Gets the rating_group of this POSTScCreateType.  # noqa: E501

        Specifies a rating group based on which usage records are rated.  **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Possible values:  - `ByBillingPeriod` (default): The rating is based on all the usages in a billing period. - `ByUsageStartDate`: The rating is based on all the usages on the same usage start date.  - `ByUsageRecord`: The rating is based on each usage record. - `ByUsageUpload`: The rating is based on all the  usages in a uploaded usage file (`.xls` or `.csv`). - `ByGroupId`: The rating is based on all the usages in a custom group.  **Note:**  - The `ByBillingPeriod` value can be applied for all charge models.  - The `ByUsageStartDate`, `ByUsageRecord`, and `ByUsageUpload` values can only be applied for per unit, volume pricing, and tiered pricing charge models.  - The `ByGroupId` value is only available if you have [Active Rating](https://knowledgecenter.zuora.com/CB_Billing/J_Billing_Operations/H_Active_Rating) feature enabled. - Use this field only for Usage charges. One-Time Charges and Recurring Charges return `NULL`.   # noqa: E501

        :return: The rating_group of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._rating_group

    @rating_group.setter
    def rating_group(self, rating_group):
        """Sets the rating_group of this POSTScCreateType.

        Specifies a rating group based on which usage records are rated.  **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Possible values:  - `ByBillingPeriod` (default): The rating is based on all the usages in a billing period. - `ByUsageStartDate`: The rating is based on all the usages on the same usage start date.  - `ByUsageRecord`: The rating is based on each usage record. - `ByUsageUpload`: The rating is based on all the  usages in a uploaded usage file (`.xls` or `.csv`). - `ByGroupId`: The rating is based on all the usages in a custom group.  **Note:**  - The `ByBillingPeriod` value can be applied for all charge models.  - The `ByUsageStartDate`, `ByUsageRecord`, and `ByUsageUpload` values can only be applied for per unit, volume pricing, and tiered pricing charge models.  - The `ByGroupId` value is only available if you have [Active Rating](https://knowledgecenter.zuora.com/CB_Billing/J_Billing_Operations/H_Active_Rating) feature enabled. - Use this field only for Usage charges. One-Time Charges and Recurring Charges return `NULL`.   # noqa: E501

        :param rating_group: The rating_group of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._rating_group = rating_group

    @property
    def specific_billing_period(self):
        """Gets the specific_billing_period of this POSTScCreateType.  # noqa: E501

        Specifies the number of month or week for the charges billing period. Required if you set the value of the `billingPeriod` field to `Specific_Months` or `Specific_Weeks`.   # noqa: E501

        :return: The specific_billing_period of this POSTScCreateType.  # noqa: E501
        :rtype: int
        """
        return self._specific_billing_period

    @specific_billing_period.setter
    def specific_billing_period(self, specific_billing_period):
        """Sets the specific_billing_period of this POSTScCreateType.

        Specifies the number of month or week for the charges billing period. Required if you set the value of the `billingPeriod` field to `Specific_Months` or `Specific_Weeks`.   # noqa: E501

        :param specific_billing_period: The specific_billing_period of this POSTScCreateType.  # noqa: E501
        :type: int
        """

        self._specific_billing_period = specific_billing_period

    @property
    def specific_end_date(self):
        """Gets the specific_end_date of this POSTScCreateType.  # noqa: E501

        Defines when the charge ends after the charge trigger date.  **note:**  * This field is only applicable when the `endDateCondition` field is set to `Specific_End_Date`.  * If the subscription ends before the specific end date, the charge ends when the subscription ends. But if the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge will end on the specific end date.   # noqa: E501

        :return: The specific_end_date of this POSTScCreateType.  # noqa: E501
        :rtype: date
        """
        return self._specific_end_date

    @specific_end_date.setter
    def specific_end_date(self, specific_end_date):
        """Sets the specific_end_date of this POSTScCreateType.

        Defines when the charge ends after the charge trigger date.  **note:**  * This field is only applicable when the `endDateCondition` field is set to `Specific_End_Date`.  * If the subscription ends before the specific end date, the charge ends when the subscription ends. But if the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge will end on the specific end date.   # noqa: E501

        :param specific_end_date: The specific_end_date of this POSTScCreateType.  # noqa: E501
        :type: date
        """

        self._specific_end_date = specific_end_date

    @property
    def tiers(self):
        """Gets the tiers of this POSTScCreateType.  # noqa: E501

        Container for Volume, Tiered, or Tiered with Overage charge models. Supports the following charge types:  * One-time * Recurring * Usage-based   # noqa: E501

        :return: The tiers of this POSTScCreateType.  # noqa: E501
        :rtype: list[POSTTierType]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this POSTScCreateType.

        Container for Volume, Tiered, or Tiered with Overage charge models. Supports the following charge types:  * One-time * Recurring * Usage-based   # noqa: E501

        :param tiers: The tiers of this POSTScCreateType.  # noqa: E501
        :type: list[POSTTierType]
        """

        self._tiers = tiers

    @property
    def trigger_date(self):
        """Gets the trigger_date of this POSTScCreateType.  # noqa: E501

        Specifies when to start billing the customer for the charge. Required if the `triggerEvent` field is set to `USD`.   # noqa: E501

        :return: The trigger_date of this POSTScCreateType.  # noqa: E501
        :rtype: date
        """
        return self._trigger_date

    @trigger_date.setter
    def trigger_date(self, trigger_date):
        """Sets the trigger_date of this POSTScCreateType.

        Specifies when to start billing the customer for the charge. Required if the `triggerEvent` field is set to `USD`.   # noqa: E501

        :param trigger_date: The trigger_date of this POSTScCreateType.  # noqa: E501
        :type: date
        """

        self._trigger_date = trigger_date

    @property
    def trigger_event(self):
        """Gets the trigger_event of this POSTScCreateType.  # noqa: E501

        Specifies when to start billing the customer for the charge.  Values:  * `UCE` * `USA` * `UCA` * `USD`   # noqa: E501

        :return: The trigger_event of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._trigger_event

    @trigger_event.setter
    def trigger_event(self, trigger_event):
        """Sets the trigger_event of this POSTScCreateType.

        Specifies when to start billing the customer for the charge.  Values:  * `UCE` * `USA` * `UCA` * `USD`   # noqa: E501

        :param trigger_event: The trigger_event of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._trigger_event = trigger_event

    @property
    def unused_units_credit_rates(self):
        """Gets the unused_units_credit_rates of this POSTScCreateType.  # noqa: E501

        Specifies the rate to credit a customer for unused units of usage. This field applies only for overage charge models when the `OverageUnusedUnitsCreditOption` field is set to `CreditBySpecificRate`.   # noqa: E501

        :return: The unused_units_credit_rates of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._unused_units_credit_rates

    @unused_units_credit_rates.setter
    def unused_units_credit_rates(self, unused_units_credit_rates):
        """Sets the unused_units_credit_rates of this POSTScCreateType.

        Specifies the rate to credit a customer for unused units of usage. This field applies only for overage charge models when the `OverageUnusedUnitsCreditOption` field is set to `CreditBySpecificRate`.   # noqa: E501

        :param unused_units_credit_rates: The unused_units_credit_rates of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._unused_units_credit_rates = unused_units_credit_rates

    @property
    def up_to_periods(self):
        """Gets the up_to_periods of this POSTScCreateType.  # noqa: E501

        Specifies the length of the period during which the charge is active. If this period ends before the subscription ends, the charge ends when this period ends.  **Note:** You must use this field together with the `upToPeriodsType` field to specify the time period.  * This field is applicable only when the `endDateCondition` field is set to `Fixed_Period`.  * If the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge end date will change accordingly up to the original period end.   # noqa: E501

        :return: The up_to_periods of this POSTScCreateType.  # noqa: E501
        :rtype: int
        """
        return self._up_to_periods

    @up_to_periods.setter
    def up_to_periods(self, up_to_periods):
        """Sets the up_to_periods of this POSTScCreateType.

        Specifies the length of the period during which the charge is active. If this period ends before the subscription ends, the charge ends when this period ends.  **Note:** You must use this field together with the `upToPeriodsType` field to specify the time period.  * This field is applicable only when the `endDateCondition` field is set to `Fixed_Period`.  * If the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge end date will change accordingly up to the original period end.   # noqa: E501

        :param up_to_periods: The up_to_periods of this POSTScCreateType.  # noqa: E501
        :type: int
        """

        self._up_to_periods = up_to_periods

    @property
    def up_to_periods_type(self):
        """Gets the up_to_periods_type of this POSTScCreateType.  # noqa: E501

         The period type used to define when the charge ends.   Values:  * `Billing_Periods` * `Days` * `Weeks` * `Months` * `Years`  You must use this field together with the `upToPeriods` field to specify the time period.  This field is applicable only when the `endDateCondition` field is set to `Fixed_Period`.    # noqa: E501

        :return: The up_to_periods_type of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._up_to_periods_type

    @up_to_periods_type.setter
    def up_to_periods_type(self, up_to_periods_type):
        """Sets the up_to_periods_type of this POSTScCreateType.

         The period type used to define when the charge ends.   Values:  * `Billing_Periods` * `Days` * `Weeks` * `Months` * `Years`  You must use this field together with the `upToPeriods` field to specify the time period.  This field is applicable only when the `endDateCondition` field is set to `Fixed_Period`.    # noqa: E501

        :param up_to_periods_type: The up_to_periods_type of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._up_to_periods_type = up_to_periods_type

    @property
    def weekly_bill_cycle_day(self):
        """Gets the weekly_bill_cycle_day of this POSTScCreateType.  # noqa: E501

        Specifies which day of the week is the bill cycle day (BCD) for the charge.   Values:  * `Sunday` * `Monday` * `Tuesday` * `Wednesday` * `Thursday` * `Friday` * `Saturday`   # noqa: E501

        :return: The weekly_bill_cycle_day of this POSTScCreateType.  # noqa: E501
        :rtype: str
        """
        return self._weekly_bill_cycle_day

    @weekly_bill_cycle_day.setter
    def weekly_bill_cycle_day(self, weekly_bill_cycle_day):
        """Sets the weekly_bill_cycle_day of this POSTScCreateType.

        Specifies which day of the week is the bill cycle day (BCD) for the charge.   Values:  * `Sunday` * `Monday` * `Tuesday` * `Wednesday` * `Thursday` * `Friday` * `Saturday`   # noqa: E501

        :param weekly_bill_cycle_day: The weekly_bill_cycle_day of this POSTScCreateType.  # noqa: E501
        :type: str
        """

        self._weekly_bill_cycle_day = weekly_bill_cycle_day

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
        if issubclass(POSTScCreateType, dict):
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
        if not isinstance(other, POSTScCreateType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
