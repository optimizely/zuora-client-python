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

from zuora_client.models.product_rate_plan_object_custom_fields import ProductRatePlanObjectCustomFields  # noqa: F401,E501
from zuora_client.models.product_rate_plan_object_ns_fields import ProductRatePlanObjectNSFields  # noqa: F401,E501


class ProxyCreateProductRatePlan(object):
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
        'billing_period__ns': 'str',
        'class__ns': 'str',
        'department__ns': 'str',
        'include_children__ns': 'str',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'item_type__ns': 'str',
        'location__ns': 'str',
        'multi_currency_price__ns': 'str',
        'price__ns': 'str',
        'subsidiary__ns': 'str',
        'sync_date__ns': 'str',
        'description': 'str',
        'effective_end_date': 'date',
        'effective_start_date': 'date',
        'name': 'str',
        'product_id': 'str'
    }

    attribute_map = {
        'billing_period__ns': 'BillingPeriod__NS',
        'class__ns': 'Class__NS',
        'department__ns': 'Department__NS',
        'include_children__ns': 'IncludeChildren__NS',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'item_type__ns': 'ItemType__NS',
        'location__ns': 'Location__NS',
        'multi_currency_price__ns': 'MultiCurrencyPrice__NS',
        'price__ns': 'Price__NS',
        'subsidiary__ns': 'Subsidiary__NS',
        'sync_date__ns': 'SyncDate__NS',
        'description': 'Description',
        'effective_end_date': 'EffectiveEndDate',
        'effective_start_date': 'EffectiveStartDate',
        'name': 'Name',
        'product_id': 'ProductId'
    }

    def __init__(self, billing_period__ns=None, class__ns=None, department__ns=None, include_children__ns=None, integration_id__ns=None, integration_status__ns=None, item_type__ns=None, location__ns=None, multi_currency_price__ns=None, price__ns=None, subsidiary__ns=None, sync_date__ns=None, description=None, effective_end_date=None, effective_start_date=None, name=None, product_id=None):  # noqa: E501
        """ProxyCreateProductRatePlan - a model defined in Swagger"""  # noqa: E501

        self._billing_period__ns = None
        self._class__ns = None
        self._department__ns = None
        self._include_children__ns = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._item_type__ns = None
        self._location__ns = None
        self._multi_currency_price__ns = None
        self._price__ns = None
        self._subsidiary__ns = None
        self._sync_date__ns = None
        self._description = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._name = None
        self._product_id = None
        self.discriminator = None

        if billing_period__ns is not None:
            self.billing_period__ns = billing_period__ns
        if class__ns is not None:
            self.class__ns = class__ns
        if department__ns is not None:
            self.department__ns = department__ns
        if include_children__ns is not None:
            self.include_children__ns = include_children__ns
        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if item_type__ns is not None:
            self.item_type__ns = item_type__ns
        if location__ns is not None:
            self.location__ns = location__ns
        if multi_currency_price__ns is not None:
            self.multi_currency_price__ns = multi_currency_price__ns
        if price__ns is not None:
            self.price__ns = price__ns
        if subsidiary__ns is not None:
            self.subsidiary__ns = subsidiary__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if description is not None:
            self.description = description
        if effective_end_date is not None:
            self.effective_end_date = effective_end_date
        if effective_start_date is not None:
            self.effective_start_date = effective_start_date
        self.name = name
        self.product_id = product_id

    @property
    def billing_period__ns(self):
        """Gets the billing_period__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        Billing period associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The billing_period__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._billing_period__ns

    @billing_period__ns.setter
    def billing_period__ns(self, billing_period__ns):
        """Sets the billing_period__ns of this ProxyCreateProductRatePlan.

        Billing period associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param billing_period__ns: The billing_period__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        allowed_values = ["Monthly", "Quarterly", "Annual", "Semi-Annual"]  # noqa: E501
        if billing_period__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_period__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_period__ns, allowed_values)
            )

        self._billing_period__ns = billing_period__ns

    @property
    def class__ns(self):
        """Gets the class__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        Class associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The class__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._class__ns

    @class__ns.setter
    def class__ns(self, class__ns):
        """Sets the class__ns of this ProxyCreateProductRatePlan.

        Class associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param class__ns: The class__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        if class__ns is not None and len(class__ns) > 255:
            raise ValueError("Invalid value for `class__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._class__ns = class__ns

    @property
    def department__ns(self):
        """Gets the department__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        Department associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The department__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._department__ns

    @department__ns.setter
    def department__ns(self, department__ns):
        """Sets the department__ns of this ProxyCreateProductRatePlan.

        Department associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param department__ns: The department__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        if department__ns is not None and len(department__ns) > 255:
            raise ValueError("Invalid value for `department__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._department__ns = department__ns

    @property
    def include_children__ns(self):
        """Gets the include_children__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        Specifies whether the corresponding item in NetSuite is visible under child subsidiaries. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The include_children__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._include_children__ns

    @include_children__ns.setter
    def include_children__ns(self, include_children__ns):
        """Sets the include_children__ns of this ProxyCreateProductRatePlan.

        Specifies whether the corresponding item in NetSuite is visible under child subsidiaries. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param include_children__ns: The include_children__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        allowed_values = ["Yes", "No"]  # noqa: E501
        if include_children__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `include_children__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(include_children__ns, allowed_values)
            )

        self._include_children__ns = include_children__ns

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this ProxyCreateProductRatePlan.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        Status of the product rate plan's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this ProxyCreateProductRatePlan.

        Status of the product rate plan's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def item_type__ns(self):
        """Gets the item_type__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        Type of item that is created in NetSuite for the product rate plan. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The item_type__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._item_type__ns

    @item_type__ns.setter
    def item_type__ns(self, item_type__ns):
        """Sets the item_type__ns of this ProxyCreateProductRatePlan.

        Type of item that is created in NetSuite for the product rate plan. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param item_type__ns: The item_type__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        allowed_values = ["Inventory", "Non Inventory", "Service"]  # noqa: E501
        if item_type__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `item_type__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(item_type__ns, allowed_values)
            )

        self._item_type__ns = item_type__ns

    @property
    def location__ns(self):
        """Gets the location__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        Location associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The location__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._location__ns

    @location__ns.setter
    def location__ns(self, location__ns):
        """Sets the location__ns of this ProxyCreateProductRatePlan.

        Location associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param location__ns: The location__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        if location__ns is not None and len(location__ns) > 255:
            raise ValueError("Invalid value for `location__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._location__ns = location__ns

    @property
    def multi_currency_price__ns(self):
        """Gets the multi_currency_price__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        Multi-currency price associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The multi_currency_price__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._multi_currency_price__ns

    @multi_currency_price__ns.setter
    def multi_currency_price__ns(self, multi_currency_price__ns):
        """Sets the multi_currency_price__ns of this ProxyCreateProductRatePlan.

        Multi-currency price associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param multi_currency_price__ns: The multi_currency_price__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        if multi_currency_price__ns is not None and len(multi_currency_price__ns) > 255:
            raise ValueError("Invalid value for `multi_currency_price__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._multi_currency_price__ns = multi_currency_price__ns

    @property
    def price__ns(self):
        """Gets the price__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        Price associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The price__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._price__ns

    @price__ns.setter
    def price__ns(self, price__ns):
        """Sets the price__ns of this ProxyCreateProductRatePlan.

        Price associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param price__ns: The price__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        if price__ns is not None and len(price__ns) > 255:
            raise ValueError("Invalid value for `price__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._price__ns = price__ns

    @property
    def subsidiary__ns(self):
        """Gets the subsidiary__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        Subsidiary associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The subsidiary__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._subsidiary__ns

    @subsidiary__ns.setter
    def subsidiary__ns(self, subsidiary__ns):
        """Sets the subsidiary__ns of this ProxyCreateProductRatePlan.

        Subsidiary associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param subsidiary__ns: The subsidiary__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        if subsidiary__ns is not None and len(subsidiary__ns) > 255:
            raise ValueError("Invalid value for `subsidiary__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._subsidiary__ns = subsidiary__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this ProxyCreateProductRatePlan.  # noqa: E501

        Date when the product rate plan was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this ProxyCreateProductRatePlan.

        Date when the product rate plan was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def description(self):
        """Gets the description of this ProxyCreateProductRatePlan.  # noqa: E501

        A description of the product rate plan. **Character limit**: 500 **Values**: a string of 500 characters or fewer   # noqa: E501

        :return: The description of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProxyCreateProductRatePlan.

        A description of the product rate plan. **Character limit**: 500 **Values**: a string of 500 characters or fewer   # noqa: E501

        :param description: The description of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def effective_end_date(self):
        """Gets the effective_end_date of this ProxyCreateProductRatePlan.  # noqa: E501

         The date when the product rate plan expires and can't be subscribed to, in `yyyy-mm-dd` format. **Character limit**: 29   # noqa: E501

        :return: The effective_end_date of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: date
        """
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, effective_end_date):
        """Sets the effective_end_date of this ProxyCreateProductRatePlan.

         The date when the product rate plan expires and can't be subscribed to, in `yyyy-mm-dd` format. **Character limit**: 29   # noqa: E501

        :param effective_end_date: The effective_end_date of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: date
        """

        self._effective_end_date = effective_end_date

    @property
    def effective_start_date(self):
        """Gets the effective_start_date of this ProxyCreateProductRatePlan.  # noqa: E501

         The date when the product rate plan becomes available and can be subscribed to, in `yyyy-mm-dd` format. **Character limit**: 29   # noqa: E501

        :return: The effective_start_date of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: date
        """
        return self._effective_start_date

    @effective_start_date.setter
    def effective_start_date(self, effective_start_date):
        """Sets the effective_start_date of this ProxyCreateProductRatePlan.

         The date when the product rate plan becomes available and can be subscribed to, in `yyyy-mm-dd` format. **Character limit**: 29   # noqa: E501

        :param effective_start_date: The effective_start_date of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: date
        """

        self._effective_start_date = effective_start_date

    @property
    def name(self):
        """Gets the name of this ProxyCreateProductRatePlan.  # noqa: E501

        The name of the product rate plan. The name doesn't have to be unique in a Product Catalog, but the name has to be unique within a product. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :return: The name of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProxyCreateProductRatePlan.

        The name of the product rate plan. The name doesn't have to be unique in a Product Catalog, but the name has to be unique within a product. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :param name: The name of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def product_id(self):
        """Gets the product_id of this ProxyCreateProductRatePlan.  # noqa: E501

        The ID of the product that contains the product rate plan. **Character limit**: 32 **Values**: a string of 32 characters or fewer   # noqa: E501

        :return: The product_id of this ProxyCreateProductRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProxyCreateProductRatePlan.

        The ID of the product that contains the product rate plan. **Character limit**: 32 **Values**: a string of 32 characters or fewer   # noqa: E501

        :param product_id: The product_id of this ProxyCreateProductRatePlan.  # noqa: E501
        :type: str
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

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
        if issubclass(ProxyCreateProductRatePlan, dict):
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
        if not isinstance(other, ProxyCreateProductRatePlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
