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

from zuora_client.models.product_rate_plan_charge_object_custom_fields import ProductRatePlanChargeObjectCustomFields  # noqa: F401,E501
from zuora_client.models.product_rate_plan_charge_object_ns_fields import ProductRatePlanChargeObjectNSFields  # noqa: F401,E501


class ProxyModifyProductRatePlanCharge(object):
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
        'class__ns': 'str',
        'deferred_rev_account__ns': 'str',
        'department__ns': 'str',
        'include_children__ns': 'str',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'item_type__ns': 'str',
        'location__ns': 'str',
        'recognized_rev_account__ns': 'str',
        'rev_rec_end__ns': 'str',
        'rev_rec_start__ns': 'str',
        'rev_rec_template_type__ns': 'str',
        'subsidiary__ns': 'str',
        'sync_date__ns': 'str',
        'accounting_code': 'str',
        'apply_discount_to': 'str',
        'bill_cycle_day': 'int',
        'bill_cycle_type': 'str',
        'billing_period': 'str',
        'billing_period_alignment': 'str',
        'billing_timing': 'str',
        'charge_model': 'str',
        'default_quantity': 'float',
        'deferred_revenue_account': 'str',
        'description': 'str',
        'discount_level': 'str',
        'end_date_condition': 'str',
        'included_units': 'float',
        'legacy_revenue_reporting': 'bool',
        'list_price_base': 'str',
        'max_quantity': 'float',
        'min_quantity': 'float',
        'name': 'str',
        'number_of_period': 'int',
        'overage_calculation_option': 'str',
        'overage_unused_units_credit_option': 'str',
        'price_change_option': 'str',
        'price_increase_option': 'str',
        'price_increase_percentage': 'float',
        'product_rate_plan_id': 'str',
        'rating_group': 'str',
        'recognized_revenue_account': 'str',
        'rev_rec_code': 'str',
        'rev_rec_trigger_condition': 'str',
        'revenue_recognition_rule_name': 'str',
        'smoothing_model': 'str',
        'specific_billing_period': 'int',
        'tax_code': 'str',
        'tax_mode': 'str',
        'taxable': 'bool',
        'trigger_event': 'str',
        'uom': 'str',
        'up_to_periods': 'int',
        'up_to_periods_type': 'str',
        'usage_record_rating_option': 'str',
        'use_discount_specific_accounting_code': 'bool',
        'use_tenant_default_for_price_change': 'bool',
        'weekly_bill_cycle_day': 'str'
    }

    attribute_map = {
        'class__ns': 'Class__NS',
        'deferred_rev_account__ns': 'DeferredRevAccount__NS',
        'department__ns': 'Department__NS',
        'include_children__ns': 'IncludeChildren__NS',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'item_type__ns': 'ItemType__NS',
        'location__ns': 'Location__NS',
        'recognized_rev_account__ns': 'RecognizedRevAccount__NS',
        'rev_rec_end__ns': 'RevRecEnd__NS',
        'rev_rec_start__ns': 'RevRecStart__NS',
        'rev_rec_template_type__ns': 'RevRecTemplateType__NS',
        'subsidiary__ns': 'Subsidiary__NS',
        'sync_date__ns': 'SyncDate__NS',
        'accounting_code': 'AccountingCode',
        'apply_discount_to': 'ApplyDiscountTo',
        'bill_cycle_day': 'BillCycleDay',
        'bill_cycle_type': 'BillCycleType',
        'billing_period': 'BillingPeriod',
        'billing_period_alignment': 'BillingPeriodAlignment',
        'billing_timing': 'BillingTiming',
        'charge_model': 'ChargeModel',
        'default_quantity': 'DefaultQuantity',
        'deferred_revenue_account': 'DeferredRevenueAccount',
        'description': 'Description',
        'discount_level': 'DiscountLevel',
        'end_date_condition': 'EndDateCondition',
        'included_units': 'IncludedUnits',
        'legacy_revenue_reporting': 'LegacyRevenueReporting',
        'list_price_base': 'ListPriceBase',
        'max_quantity': 'MaxQuantity',
        'min_quantity': 'MinQuantity',
        'name': 'Name',
        'number_of_period': 'NumberOfPeriod',
        'overage_calculation_option': 'OverageCalculationOption',
        'overage_unused_units_credit_option': 'OverageUnusedUnitsCreditOption',
        'price_change_option': 'PriceChangeOption',
        'price_increase_option': 'PriceIncreaseOption',
        'price_increase_percentage': 'PriceIncreasePercentage',
        'product_rate_plan_id': 'ProductRatePlanId',
        'rating_group': 'RatingGroup',
        'recognized_revenue_account': 'RecognizedRevenueAccount',
        'rev_rec_code': 'RevRecCode',
        'rev_rec_trigger_condition': 'RevRecTriggerCondition',
        'revenue_recognition_rule_name': 'RevenueRecognitionRuleName',
        'smoothing_model': 'SmoothingModel',
        'specific_billing_period': 'SpecificBillingPeriod',
        'tax_code': 'TaxCode',
        'tax_mode': 'TaxMode',
        'taxable': 'Taxable',
        'trigger_event': 'TriggerEvent',
        'uom': 'UOM',
        'up_to_periods': 'UpToPeriods',
        'up_to_periods_type': 'UpToPeriodsType',
        'usage_record_rating_option': 'UsageRecordRatingOption',
        'use_discount_specific_accounting_code': 'UseDiscountSpecificAccountingCode',
        'use_tenant_default_for_price_change': 'UseTenantDefaultForPriceChange',
        'weekly_bill_cycle_day': 'WeeklyBillCycleDay'
    }

    def __init__(self, class__ns=None, deferred_rev_account__ns=None, department__ns=None, include_children__ns=None, integration_id__ns=None, integration_status__ns=None, item_type__ns=None, location__ns=None, recognized_rev_account__ns=None, rev_rec_end__ns=None, rev_rec_start__ns=None, rev_rec_template_type__ns=None, subsidiary__ns=None, sync_date__ns=None, accounting_code=None, apply_discount_to=None, bill_cycle_day=None, bill_cycle_type=None, billing_period=None, billing_period_alignment=None, billing_timing=None, charge_model=None, default_quantity=None, deferred_revenue_account=None, description=None, discount_level=None, end_date_condition=None, included_units=None, legacy_revenue_reporting=None, list_price_base=None, max_quantity=None, min_quantity=None, name=None, number_of_period=None, overage_calculation_option=None, overage_unused_units_credit_option=None, price_change_option=None, price_increase_option=None, price_increase_percentage=None, product_rate_plan_id=None, rating_group=None, recognized_revenue_account=None, rev_rec_code=None, rev_rec_trigger_condition=None, revenue_recognition_rule_name=None, smoothing_model=None, specific_billing_period=None, tax_code=None, tax_mode=None, taxable=None, trigger_event=None, uom=None, up_to_periods=None, up_to_periods_type=None, usage_record_rating_option='EndOfBillingPeriod', use_discount_specific_accounting_code=None, use_tenant_default_for_price_change=None, weekly_bill_cycle_day=None):  # noqa: E501
        """ProxyModifyProductRatePlanCharge - a model defined in Swagger"""  # noqa: E501

        self._class__ns = None
        self._deferred_rev_account__ns = None
        self._department__ns = None
        self._include_children__ns = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._item_type__ns = None
        self._location__ns = None
        self._recognized_rev_account__ns = None
        self._rev_rec_end__ns = None
        self._rev_rec_start__ns = None
        self._rev_rec_template_type__ns = None
        self._subsidiary__ns = None
        self._sync_date__ns = None
        self._accounting_code = None
        self._apply_discount_to = None
        self._bill_cycle_day = None
        self._bill_cycle_type = None
        self._billing_period = None
        self._billing_period_alignment = None
        self._billing_timing = None
        self._charge_model = None
        self._default_quantity = None
        self._deferred_revenue_account = None
        self._description = None
        self._discount_level = None
        self._end_date_condition = None
        self._included_units = None
        self._legacy_revenue_reporting = None
        self._list_price_base = None
        self._max_quantity = None
        self._min_quantity = None
        self._name = None
        self._number_of_period = None
        self._overage_calculation_option = None
        self._overage_unused_units_credit_option = None
        self._price_change_option = None
        self._price_increase_option = None
        self._price_increase_percentage = None
        self._product_rate_plan_id = None
        self._rating_group = None
        self._recognized_revenue_account = None
        self._rev_rec_code = None
        self._rev_rec_trigger_condition = None
        self._revenue_recognition_rule_name = None
        self._smoothing_model = None
        self._specific_billing_period = None
        self._tax_code = None
        self._tax_mode = None
        self._taxable = None
        self._trigger_event = None
        self._uom = None
        self._up_to_periods = None
        self._up_to_periods_type = None
        self._usage_record_rating_option = None
        self._use_discount_specific_accounting_code = None
        self._use_tenant_default_for_price_change = None
        self._weekly_bill_cycle_day = None
        self.discriminator = None

        if class__ns is not None:
            self.class__ns = class__ns
        if deferred_rev_account__ns is not None:
            self.deferred_rev_account__ns = deferred_rev_account__ns
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
        if recognized_rev_account__ns is not None:
            self.recognized_rev_account__ns = recognized_rev_account__ns
        if rev_rec_end__ns is not None:
            self.rev_rec_end__ns = rev_rec_end__ns
        if rev_rec_start__ns is not None:
            self.rev_rec_start__ns = rev_rec_start__ns
        if rev_rec_template_type__ns is not None:
            self.rev_rec_template_type__ns = rev_rec_template_type__ns
        if subsidiary__ns is not None:
            self.subsidiary__ns = subsidiary__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if accounting_code is not None:
            self.accounting_code = accounting_code
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
        if charge_model is not None:
            self.charge_model = charge_model
        if default_quantity is not None:
            self.default_quantity = default_quantity
        if deferred_revenue_account is not None:
            self.deferred_revenue_account = deferred_revenue_account
        if description is not None:
            self.description = description
        if discount_level is not None:
            self.discount_level = discount_level
        if end_date_condition is not None:
            self.end_date_condition = end_date_condition
        if included_units is not None:
            self.included_units = included_units
        if legacy_revenue_reporting is not None:
            self.legacy_revenue_reporting = legacy_revenue_reporting
        if list_price_base is not None:
            self.list_price_base = list_price_base
        if max_quantity is not None:
            self.max_quantity = max_quantity
        if min_quantity is not None:
            self.min_quantity = min_quantity
        if name is not None:
            self.name = name
        if number_of_period is not None:
            self.number_of_period = number_of_period
        if overage_calculation_option is not None:
            self.overage_calculation_option = overage_calculation_option
        if overage_unused_units_credit_option is not None:
            self.overage_unused_units_credit_option = overage_unused_units_credit_option
        if price_change_option is not None:
            self.price_change_option = price_change_option
        if price_increase_option is not None:
            self.price_increase_option = price_increase_option
        if price_increase_percentage is not None:
            self.price_increase_percentage = price_increase_percentage
        if product_rate_plan_id is not None:
            self.product_rate_plan_id = product_rate_plan_id
        if rating_group is not None:
            self.rating_group = rating_group
        if recognized_revenue_account is not None:
            self.recognized_revenue_account = recognized_revenue_account
        if rev_rec_code is not None:
            self.rev_rec_code = rev_rec_code
        if rev_rec_trigger_condition is not None:
            self.rev_rec_trigger_condition = rev_rec_trigger_condition
        if revenue_recognition_rule_name is not None:
            self.revenue_recognition_rule_name = revenue_recognition_rule_name
        if smoothing_model is not None:
            self.smoothing_model = smoothing_model
        if specific_billing_period is not None:
            self.specific_billing_period = specific_billing_period
        if tax_code is not None:
            self.tax_code = tax_code
        if tax_mode is not None:
            self.tax_mode = tax_mode
        if taxable is not None:
            self.taxable = taxable
        if trigger_event is not None:
            self.trigger_event = trigger_event
        if uom is not None:
            self.uom = uom
        if up_to_periods is not None:
            self.up_to_periods = up_to_periods
        if up_to_periods_type is not None:
            self.up_to_periods_type = up_to_periods_type
        if usage_record_rating_option is not None:
            self.usage_record_rating_option = usage_record_rating_option
        if use_discount_specific_accounting_code is not None:
            self.use_discount_specific_accounting_code = use_discount_specific_accounting_code
        if use_tenant_default_for_price_change is not None:
            self.use_tenant_default_for_price_change = use_tenant_default_for_price_change
        if weekly_bill_cycle_day is not None:
            self.weekly_bill_cycle_day = weekly_bill_cycle_day

    @property
    def class__ns(self):
        """Gets the class__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Class associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The class__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._class__ns

    @class__ns.setter
    def class__ns(self, class__ns):
        """Sets the class__ns of this ProxyModifyProductRatePlanCharge.

        Class associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param class__ns: The class__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        if class__ns is not None and len(class__ns) > 255:
            raise ValueError("Invalid value for `class__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._class__ns = class__ns

    @property
    def deferred_rev_account__ns(self):
        """Gets the deferred_rev_account__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Deferrred revenue account associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The deferred_rev_account__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._deferred_rev_account__ns

    @deferred_rev_account__ns.setter
    def deferred_rev_account__ns(self, deferred_rev_account__ns):
        """Sets the deferred_rev_account__ns of this ProxyModifyProductRatePlanCharge.

        Deferrred revenue account associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param deferred_rev_account__ns: The deferred_rev_account__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        if deferred_rev_account__ns is not None and len(deferred_rev_account__ns) > 255:
            raise ValueError("Invalid value for `deferred_rev_account__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._deferred_rev_account__ns = deferred_rev_account__ns

    @property
    def department__ns(self):
        """Gets the department__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Department associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The department__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._department__ns

    @department__ns.setter
    def department__ns(self, department__ns):
        """Sets the department__ns of this ProxyModifyProductRatePlanCharge.

        Department associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param department__ns: The department__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        if department__ns is not None and len(department__ns) > 255:
            raise ValueError("Invalid value for `department__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._department__ns = department__ns

    @property
    def include_children__ns(self):
        """Gets the include_children__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Specifies whether the corresponding item in NetSuite is visible under child subsidiaries. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The include_children__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._include_children__ns

    @include_children__ns.setter
    def include_children__ns(self, include_children__ns):
        """Sets the include_children__ns of this ProxyModifyProductRatePlanCharge.

        Specifies whether the corresponding item in NetSuite is visible under child subsidiaries. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param include_children__ns: The include_children__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
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
        """Gets the integration_id__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this ProxyModifyProductRatePlanCharge.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Status of the product rate plan charge's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this ProxyModifyProductRatePlanCharge.

        Status of the product rate plan charge's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def item_type__ns(self):
        """Gets the item_type__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Type of item that is created in NetSuite for the product rate plan charge. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The item_type__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._item_type__ns

    @item_type__ns.setter
    def item_type__ns(self, item_type__ns):
        """Sets the item_type__ns of this ProxyModifyProductRatePlanCharge.

        Type of item that is created in NetSuite for the product rate plan charge. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param item_type__ns: The item_type__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
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
        """Gets the location__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Location associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The location__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._location__ns

    @location__ns.setter
    def location__ns(self, location__ns):
        """Sets the location__ns of this ProxyModifyProductRatePlanCharge.

        Location associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param location__ns: The location__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        if location__ns is not None and len(location__ns) > 255:
            raise ValueError("Invalid value for `location__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._location__ns = location__ns

    @property
    def recognized_rev_account__ns(self):
        """Gets the recognized_rev_account__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Recognized revenue account associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The recognized_rev_account__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._recognized_rev_account__ns

    @recognized_rev_account__ns.setter
    def recognized_rev_account__ns(self, recognized_rev_account__ns):
        """Sets the recognized_rev_account__ns of this ProxyModifyProductRatePlanCharge.

        Recognized revenue account associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param recognized_rev_account__ns: The recognized_rev_account__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        if recognized_rev_account__ns is not None and len(recognized_rev_account__ns) > 255:
            raise ValueError("Invalid value for `recognized_rev_account__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._recognized_rev_account__ns = recognized_rev_account__ns

    @property
    def rev_rec_end__ns(self):
        """Gets the rev_rec_end__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        End date condition of the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The rev_rec_end__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._rev_rec_end__ns

    @rev_rec_end__ns.setter
    def rev_rec_end__ns(self, rev_rec_end__ns):
        """Sets the rev_rec_end__ns of this ProxyModifyProductRatePlanCharge.

        End date condition of the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param rev_rec_end__ns: The rev_rec_end__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        allowed_values = ["Charge Period Start", "Rev Rec Trigger Date", "Use NetSuite Rev Rec Template"]  # noqa: E501
        if rev_rec_end__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `rev_rec_end__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(rev_rec_end__ns, allowed_values)
            )

        self._rev_rec_end__ns = rev_rec_end__ns

    @property
    def rev_rec_start__ns(self):
        """Gets the rev_rec_start__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Start date condition of the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The rev_rec_start__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._rev_rec_start__ns

    @rev_rec_start__ns.setter
    def rev_rec_start__ns(self, rev_rec_start__ns):
        """Sets the rev_rec_start__ns of this ProxyModifyProductRatePlanCharge.

        Start date condition of the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param rev_rec_start__ns: The rev_rec_start__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        allowed_values = ["Charge Period Start", "Rev Rec Trigger Date", "Use NetSuite Rev Rec Template"]  # noqa: E501
        if rev_rec_start__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `rev_rec_start__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(rev_rec_start__ns, allowed_values)
            )

        self._rev_rec_start__ns = rev_rec_start__ns

    @property
    def rev_rec_template_type__ns(self):
        """Gets the rev_rec_template_type__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The rev_rec_template_type__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._rev_rec_template_type__ns

    @rev_rec_template_type__ns.setter
    def rev_rec_template_type__ns(self, rev_rec_template_type__ns):
        """Sets the rev_rec_template_type__ns of this ProxyModifyProductRatePlanCharge.

        Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param rev_rec_template_type__ns: The rev_rec_template_type__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        if rev_rec_template_type__ns is not None and len(rev_rec_template_type__ns) > 255:
            raise ValueError("Invalid value for `rev_rec_template_type__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._rev_rec_template_type__ns = rev_rec_template_type__ns

    @property
    def subsidiary__ns(self):
        """Gets the subsidiary__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Subsidiary associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The subsidiary__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._subsidiary__ns

    @subsidiary__ns.setter
    def subsidiary__ns(self, subsidiary__ns):
        """Sets the subsidiary__ns of this ProxyModifyProductRatePlanCharge.

        Subsidiary associated with the corresponding item in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param subsidiary__ns: The subsidiary__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        if subsidiary__ns is not None and len(subsidiary__ns) > 255:
            raise ValueError("Invalid value for `subsidiary__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._subsidiary__ns = subsidiary__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Date when the product rate plan charge was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this ProxyModifyProductRatePlanCharge.

        Date when the product rate plan charge was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def accounting_code(self):
        """Gets the accounting_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        The accounting code for the charge. Accounting codes group transactions that contain similar accounting attributes. **Character limit**: 100 **Values**: an active accounting code in your Zuora Chart of Accounts   # noqa: E501

        :return: The accounting_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._accounting_code

    @accounting_code.setter
    def accounting_code(self, accounting_code):
        """Sets the accounting_code of this ProxyModifyProductRatePlanCharge.

        The accounting code for the charge. Accounting codes group transactions that contain similar accounting attributes. **Character limit**: 100 **Values**: an active accounting code in your Zuora Chart of Accounts   # noqa: E501

        :param accounting_code: The accounting_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._accounting_code = accounting_code

    @property
    def apply_discount_to(self):
        """Gets the apply_discount_to of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Specifies the type of charges that you want a specific discount to apply to. All field values are case sensitive: note that these values are in all-caps. **Character limit**: 21 **Values**: one of the following:  - `ONETIME (1)` - `RECURRING (2)` - `USAGE (4)` - `ONETIMERECURRING (3)` - `ONETIMEUSAGE (5)` - `RECURRINGUSAGE (6)` - `ONETIMERECURRINGUSAGE (7)`   # noqa: E501

        :return: The apply_discount_to of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._apply_discount_to

    @apply_discount_to.setter
    def apply_discount_to(self, apply_discount_to):
        """Sets the apply_discount_to of this ProxyModifyProductRatePlanCharge.

        Specifies the type of charges that you want a specific discount to apply to. All field values are case sensitive: note that these values are in all-caps. **Character limit**: 21 **Values**: one of the following:  - `ONETIME (1)` - `RECURRING (2)` - `USAGE (4)` - `ONETIMERECURRING (3)` - `ONETIMEUSAGE (5)` - `RECURRINGUSAGE (6)` - `ONETIMERECURRINGUSAGE (7)`   # noqa: E501

        :param apply_discount_to: The apply_discount_to of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._apply_discount_to = apply_discount_to

    @property
    def bill_cycle_day(self):
        """Gets the bill_cycle_day of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Sets the bill cycle day (BCD) for the charge. The BCD determines which day of the month customer is billed. The BCD value in the account can override the BCD in this object. **Character limit**: 2 **Values**: a valid BCD integer, 1 - 31   # noqa: E501

        :return: The bill_cycle_day of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: int
        """
        return self._bill_cycle_day

    @bill_cycle_day.setter
    def bill_cycle_day(self, bill_cycle_day):
        """Sets the bill_cycle_day of this ProxyModifyProductRatePlanCharge.

         Sets the bill cycle day (BCD) for the charge. The BCD determines which day of the month customer is billed. The BCD value in the account can override the BCD in this object. **Character limit**: 2 **Values**: a valid BCD integer, 1 - 31   # noqa: E501

        :param bill_cycle_day: The bill_cycle_day of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: int
        """

        self._bill_cycle_day = bill_cycle_day

    @property
    def bill_cycle_type(self):
        """Gets the bill_cycle_type of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Specifies how to determine the billing day for the charge. **Character limit**: 20 **Values**: one of the following:  - `DefaultFromCustomer` - `SpecificDayofMonth:` - `SubscriptionStartDay` - `ChargeTriggerDay` - `SpecificDayofWeek` **Note**:  - If you set this field to `SpecificDayofMonth`, you must specify which day of the month as the billing day for the charge in the BillCycleDay field. - If you set this field to `SpecificDayofWeek`, you must specify which day of the week as the billing day for the charge in the WeeklyBillCycleDay field.   # noqa: E501

        :return: The bill_cycle_type of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._bill_cycle_type

    @bill_cycle_type.setter
    def bill_cycle_type(self, bill_cycle_type):
        """Sets the bill_cycle_type of this ProxyModifyProductRatePlanCharge.

         Specifies how to determine the billing day for the charge. **Character limit**: 20 **Values**: one of the following:  - `DefaultFromCustomer` - `SpecificDayofMonth:` - `SubscriptionStartDay` - `ChargeTriggerDay` - `SpecificDayofWeek` **Note**:  - If you set this field to `SpecificDayofMonth`, you must specify which day of the month as the billing day for the charge in the BillCycleDay field. - If you set this field to `SpecificDayofWeek`, you must specify which day of the week as the billing day for the charge in the WeeklyBillCycleDay field.   # noqa: E501

        :param bill_cycle_type: The bill_cycle_type of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._bill_cycle_type = bill_cycle_type

    @property
    def billing_period(self):
        """Gets the billing_period of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         The billing period for the charge. The start day of the billing period is also called the bill cycle day (BCD). **Character limit**: 15 **Values**: one of the following  - `Month` - `Quarter` - `Annual` - `Semi-Annual` - `Specific Months` - `Subscription Term` (This value is in **Limited Availability**.) - `Week` - `Specific Weeks` **Note**: Specify the number of months or weeks in the SpecificBillingPeriod field if you set this field to `Specific Months` or `Specific Weeks`.   # noqa: E501

        :return: The billing_period of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this ProxyModifyProductRatePlanCharge.

         The billing period for the charge. The start day of the billing period is also called the bill cycle day (BCD). **Character limit**: 15 **Values**: one of the following  - `Month` - `Quarter` - `Annual` - `Semi-Annual` - `Specific Months` - `Subscription Term` (This value is in **Limited Availability**.) - `Week` - `Specific Weeks` **Note**: Specify the number of months or weeks in the SpecificBillingPeriod field if you set this field to `Specific Months` or `Specific Weeks`.   # noqa: E501

        :param billing_period: The billing_period of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._billing_period = billing_period

    @property
    def billing_period_alignment(self):
        """Gets the billing_period_alignment of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Aligns charges within the same subscription if multiple charges begin on different dates. **Character limit**: 24 **Values**: one of the following:  - `AlignToCharge` - `AlignToSubscriptionStart` - `AlignToTermStart`   # noqa: E501

        :return: The billing_period_alignment of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._billing_period_alignment

    @billing_period_alignment.setter
    def billing_period_alignment(self, billing_period_alignment):
        """Sets the billing_period_alignment of this ProxyModifyProductRatePlanCharge.

         Aligns charges within the same subscription if multiple charges begin on different dates. **Character limit**: 24 **Values**: one of the following:  - `AlignToCharge` - `AlignToSubscriptionStart` - `AlignToTermStart`   # noqa: E501

        :param billing_period_alignment: The billing_period_alignment of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._billing_period_alignment = billing_period_alignment

    @property
    def billing_timing(self):
        """Gets the billing_timing of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         The billing timing for the charge. You can choose to bill in advance or in arrears for recurring charge types. This field is not used in one-time or usage based charge types. **Character limit**: **Values**: one of the following:  - `In Advance` - `In Arrears`  This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    # noqa: E501

        :return: The billing_timing of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._billing_timing

    @billing_timing.setter
    def billing_timing(self, billing_timing):
        """Sets the billing_timing of this ProxyModifyProductRatePlanCharge.

         The billing timing for the charge. You can choose to bill in advance or in arrears for recurring charge types. This field is not used in one-time or usage based charge types. **Character limit**: **Values**: one of the following:  - `In Advance` - `In Arrears`  This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    # noqa: E501

        :param billing_timing: The billing_timing of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._billing_timing = billing_timing

    @property
    def charge_model(self):
        """Gets the charge_model of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Determines how to calculate charges. Charge models must be individually activated in Zuora Billing administration. **Character limit**: 27 **Values**: one of the following:  - `Discount-Fixed Amount` - `Discount-Percentage` - `Flat Fee Pricing` - `Per Unit Pricing` - `Overage Pricing` - `Tiered Pricing` - `Tiered with Overage Pricing` - `Volume Pricing`   # noqa: E501

        :return: The charge_model of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._charge_model

    @charge_model.setter
    def charge_model(self, charge_model):
        """Sets the charge_model of this ProxyModifyProductRatePlanCharge.

         Determines how to calculate charges. Charge models must be individually activated in Zuora Billing administration. **Character limit**: 27 **Values**: one of the following:  - `Discount-Fixed Amount` - `Discount-Percentage` - `Flat Fee Pricing` - `Per Unit Pricing` - `Overage Pricing` - `Tiered Pricing` - `Tiered with Overage Pricing` - `Volume Pricing`   # noqa: E501

        :param charge_model: The charge_model of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._charge_model = charge_model

    @property
    def default_quantity(self):
        """Gets the default_quantity of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         The default quantity of units, such as the number of authors in a hosted wiki service. This field is required if you use a per-unit pricing model. **Character limit**: 16 **Values**: a valid quantity value   # noqa: E501

        :return: The default_quantity of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: float
        """
        return self._default_quantity

    @default_quantity.setter
    def default_quantity(self, default_quantity):
        """Sets the default_quantity of this ProxyModifyProductRatePlanCharge.

         The default quantity of units, such as the number of authors in a hosted wiki service. This field is required if you use a per-unit pricing model. **Character limit**: 16 **Values**: a valid quantity value   # noqa: E501

        :param default_quantity: The default_quantity of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: float
        """

        self._default_quantity = default_quantity

    @property
    def deferred_revenue_account(self):
        """Gets the deferred_revenue_account of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         The name of the deferred revenue account for this charge. **Character limit**: 100 **Values**: an active accounting code in your Zuora Chart of Accounts This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    # noqa: E501

        :return: The deferred_revenue_account of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._deferred_revenue_account

    @deferred_revenue_account.setter
    def deferred_revenue_account(self, deferred_revenue_account):
        """Sets the deferred_revenue_account of this ProxyModifyProductRatePlanCharge.

         The name of the deferred revenue account for this charge. **Character limit**: 100 **Values**: an active accounting code in your Zuora Chart of Accounts This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    # noqa: E501

        :param deferred_revenue_account: The deferred_revenue_account of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._deferred_revenue_account = deferred_revenue_account

    @property
    def description(self):
        """Gets the description of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        A description of the charge. **Character limit**: 500 **Values**: a string of 500 characters or fewer   # noqa: E501

        :return: The description of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProxyModifyProductRatePlanCharge.

        A description of the charge. **Character limit**: 500 **Values**: a string of 500 characters or fewer   # noqa: E501

        :param description: The description of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def discount_level(self):
        """Gets the discount_level of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Specifies if the discount applies to just the product rate plan, the entire subscription, or to any activity in the account. **Character limit**: 12 **Values**: one of the following:  - `rateplan` - `subscription`, `account`   # noqa: E501

        :return: The discount_level of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._discount_level

    @discount_level.setter
    def discount_level(self, discount_level):
        """Sets the discount_level of this ProxyModifyProductRatePlanCharge.

         Specifies if the discount applies to just the product rate plan, the entire subscription, or to any activity in the account. **Character limit**: 12 **Values**: one of the following:  - `rateplan` - `subscription`, `account`   # noqa: E501

        :param discount_level: The discount_level of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._discount_level = discount_level

    @property
    def end_date_condition(self):
        """Gets the end_date_condition of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Defines when the charge ends after the charge trigger date. **Values**: one of the following:  - `SubscriptionEnd`: The charge ends on the subscription end date after a specified period based on the trigger date of the charge. This is the default value. - `FixedPeriod`: The charge ends after a specified period based on the trigger date of the charge. If you set this field to `FixedPeriod`, you must specify the length of the period and a period type by defining the `UpToPeriods` and `UpToPeriodsType` fields. **Note**: If the subscription ends before the charge end date, the charge ends when the subscription ends. But if the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge will end on the charge end date.   # noqa: E501

        :return: The end_date_condition of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._end_date_condition

    @end_date_condition.setter
    def end_date_condition(self, end_date_condition):
        """Sets the end_date_condition of this ProxyModifyProductRatePlanCharge.

         Defines when the charge ends after the charge trigger date. **Values**: one of the following:  - `SubscriptionEnd`: The charge ends on the subscription end date after a specified period based on the trigger date of the charge. This is the default value. - `FixedPeriod`: The charge ends after a specified period based on the trigger date of the charge. If you set this field to `FixedPeriod`, you must specify the length of the period and a period type by defining the `UpToPeriods` and `UpToPeriodsType` fields. **Note**: If the subscription ends before the charge end date, the charge ends when the subscription ends. But if the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge will end on the charge end date.   # noqa: E501

        :param end_date_condition: The end_date_condition of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._end_date_condition = end_date_condition

    @property
    def included_units(self):
        """Gets the included_units of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Specifies the number of units in the base set of units. **Character limit**: 16 **Values**: a positive decimal value   # noqa: E501

        :return: The included_units of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: float
        """
        return self._included_units

    @included_units.setter
    def included_units(self, included_units):
        """Sets the included_units of this ProxyModifyProductRatePlanCharge.

        Specifies the number of units in the base set of units. **Character limit**: 16 **Values**: a positive decimal value   # noqa: E501

        :param included_units: The included_units of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: float
        """

        self._included_units = included_units

    @property
    def legacy_revenue_reporting(self):
        """Gets the legacy_revenue_reporting of this ProxyModifyProductRatePlanCharge.  # noqa: E501

          # noqa: E501

        :return: The legacy_revenue_reporting of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: bool
        """
        return self._legacy_revenue_reporting

    @legacy_revenue_reporting.setter
    def legacy_revenue_reporting(self, legacy_revenue_reporting):
        """Sets the legacy_revenue_reporting of this ProxyModifyProductRatePlanCharge.

          # noqa: E501

        :param legacy_revenue_reporting: The legacy_revenue_reporting of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: bool
        """

        self._legacy_revenue_reporting = legacy_revenue_reporting

    @property
    def list_price_base(self):
        """Gets the list_price_base of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        The list price base for the product rate plan charge. **Values**: one of the following:  - `Per Month` - `Per Billing Period` - `Per Week`   # noqa: E501

        :return: The list_price_base of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._list_price_base

    @list_price_base.setter
    def list_price_base(self, list_price_base):
        """Sets the list_price_base of this ProxyModifyProductRatePlanCharge.

        The list price base for the product rate plan charge. **Values**: one of the following:  - `Per Month` - `Per Billing Period` - `Per Week`   # noqa: E501

        :param list_price_base: The list_price_base of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._list_price_base = list_price_base

    @property
    def max_quantity(self):
        """Gets the max_quantity of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Specifies the maximum number of units for this charge. Use this field and the `MinQuantity` field to create a range of units allowed in a product rate plan charge. **Character limit**: 16 **Values**: a positive decimal value   # noqa: E501

        :return: The max_quantity of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: float
        """
        return self._max_quantity

    @max_quantity.setter
    def max_quantity(self, max_quantity):
        """Sets the max_quantity of this ProxyModifyProductRatePlanCharge.

         Specifies the maximum number of units for this charge. Use this field and the `MinQuantity` field to create a range of units allowed in a product rate plan charge. **Character limit**: 16 **Values**: a positive decimal value   # noqa: E501

        :param max_quantity: The max_quantity of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: float
        """

        self._max_quantity = max_quantity

    @property
    def min_quantity(self):
        """Gets the min_quantity of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Specifies the minimum number of units for this charge. Use this field and the `MaxQuantity` field to create a range of units allowed in a product rate plan charge. **Character limit**: 16 **Values**: a positive decimal value   # noqa: E501

        :return: The min_quantity of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: float
        """
        return self._min_quantity

    @min_quantity.setter
    def min_quantity(self, min_quantity):
        """Sets the min_quantity of this ProxyModifyProductRatePlanCharge.

        Specifies the minimum number of units for this charge. Use this field and the `MaxQuantity` field to create a range of units allowed in a product rate plan charge. **Character limit**: 16 **Values**: a positive decimal value   # noqa: E501

        :param min_quantity: The min_quantity of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: float
        """

        self._min_quantity = min_quantity

    @property
    def name(self):
        """Gets the name of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        The name of the product rate plan charge. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :return: The name of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProxyModifyProductRatePlanCharge.

        The name of the product rate plan charge. **Character limit**: 100 **Values**: a string of 100 characters or fewer   # noqa: E501

        :param name: The name of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number_of_period(self):
        """Gets the number_of_period of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Specifies the number of periods to use when calculating charges in an overage smoothing charge model. **Character limit**: **Values**: a positive whole number   # noqa: E501

        :return: The number_of_period of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: int
        """
        return self._number_of_period

    @number_of_period.setter
    def number_of_period(self, number_of_period):
        """Sets the number_of_period of this ProxyModifyProductRatePlanCharge.

        Specifies the number of periods to use when calculating charges in an overage smoothing charge model. **Character limit**: **Values**: a positive whole number   # noqa: E501

        :param number_of_period: The number_of_period of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: int
        """

        self._number_of_period = number_of_period

    @property
    def overage_calculation_option(self):
        """Gets the overage_calculation_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Determines when to calculate overage charges. If the value of the SmoothingMode field is not specified, the value of this field is ignored. **Character limit**: 20 **Values**: one of the following:  - `EndOfSmoothingPeriod`: This option is used by default. The overage is charged at the end of the smoothing period. - `PerBillingPeriod`: The overage is charged on-demand rather than waiting until the end of the smoothing period.   # noqa: E501

        :return: The overage_calculation_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._overage_calculation_option

    @overage_calculation_option.setter
    def overage_calculation_option(self, overage_calculation_option):
        """Sets the overage_calculation_option of this ProxyModifyProductRatePlanCharge.

        Determines when to calculate overage charges. If the value of the SmoothingMode field is not specified, the value of this field is ignored. **Character limit**: 20 **Values**: one of the following:  - `EndOfSmoothingPeriod`: This option is used by default. The overage is charged at the end of the smoothing period. - `PerBillingPeriod`: The overage is charged on-demand rather than waiting until the end of the smoothing period.   # noqa: E501

        :param overage_calculation_option: The overage_calculation_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._overage_calculation_option = overage_calculation_option

    @property
    def overage_unused_units_credit_option(self):
        """Gets the overage_unused_units_credit_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Determines whether to credit the customer with unused units of usage. **Character limit**: 20 **Values**: one of the following:  - `NoCredit` - `CreditBySpecificRate`   # noqa: E501

        :return: The overage_unused_units_credit_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._overage_unused_units_credit_option

    @overage_unused_units_credit_option.setter
    def overage_unused_units_credit_option(self, overage_unused_units_credit_option):
        """Sets the overage_unused_units_credit_option of this ProxyModifyProductRatePlanCharge.

         Determines whether to credit the customer with unused units of usage. **Character limit**: 20 **Values**: one of the following:  - `NoCredit` - `CreditBySpecificRate`   # noqa: E501

        :param overage_unused_units_credit_option: The overage_unused_units_credit_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._overage_unused_units_credit_option = overage_unused_units_credit_option

    @property
    def price_change_option(self):
        """Gets the price_change_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Applies an automatic price change when a termed subscription is renewed. **Character limit**: **Values**: one of the following:  - `NoChange` (default) - `SpecificPercentageValue` - `UseLatestProductCatalogPricing`   # noqa: E501

        :return: The price_change_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._price_change_option

    @price_change_option.setter
    def price_change_option(self, price_change_option):
        """Sets the price_change_option of this ProxyModifyProductRatePlanCharge.

         Applies an automatic price change when a termed subscription is renewed. **Character limit**: **Values**: one of the following:  - `NoChange` (default) - `SpecificPercentageValue` - `UseLatestProductCatalogPricing`   # noqa: E501

        :param price_change_option: The price_change_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._price_change_option = price_change_option

    @property
    def price_increase_option(self):
        """Gets the price_increase_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Applies an automatic price change when a termed subscription is renewed.   # noqa: E501

        :return: The price_increase_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._price_increase_option

    @price_increase_option.setter
    def price_increase_option(self, price_increase_option):
        """Sets the price_increase_option of this ProxyModifyProductRatePlanCharge.

        Applies an automatic price change when a termed subscription is renewed.   # noqa: E501

        :param price_increase_option: The price_increase_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        allowed_values = ["FromTenantPercentageValue", "SpecificPercentageValue"]  # noqa: E501
        if price_increase_option not in allowed_values:
            raise ValueError(
                "Invalid value for `price_increase_option` ({0}), must be one of {1}"  # noqa: E501
                .format(price_increase_option, allowed_values)
            )

        self._price_increase_option = price_increase_option

    @property
    def price_increase_percentage(self):
        """Gets the price_increase_percentage of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Specifies the percentage to increase or decrease the price of a termed subscription's renewal. Use this field if you set the value to `SpecificPercentageValue`. **Character limit**: 16 **Values**: a decimal value between -100 and 100   # noqa: E501

        :return: The price_increase_percentage of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: float
        """
        return self._price_increase_percentage

    @price_increase_percentage.setter
    def price_increase_percentage(self, price_increase_percentage):
        """Sets the price_increase_percentage of this ProxyModifyProductRatePlanCharge.

         Specifies the percentage to increase or decrease the price of a termed subscription's renewal. Use this field if you set the value to `SpecificPercentageValue`. **Character limit**: 16 **Values**: a decimal value between -100 and 100   # noqa: E501

        :param price_increase_percentage: The price_increase_percentage of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: float
        """

        self._price_increase_percentage = price_increase_percentage

    @property
    def product_rate_plan_id(self):
        """Gets the product_rate_plan_id of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         The ID of the product rate plan associated with this product rate plan charge. **Character limit**: 32 **Values**: a valid product rate plan ID   # noqa: E501

        :return: The product_rate_plan_id of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_id

    @product_rate_plan_id.setter
    def product_rate_plan_id(self, product_rate_plan_id):
        """Sets the product_rate_plan_id of this ProxyModifyProductRatePlanCharge.

         The ID of the product rate plan associated with this product rate plan charge. **Character limit**: 32 **Values**: a valid product rate plan ID   # noqa: E501

        :param product_rate_plan_id: The product_rate_plan_id of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._product_rate_plan_id = product_rate_plan_id

    @property
    def rating_group(self):
        """Gets the rating_group of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Specifies a rating group based on which usage records are rated.  **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Possible values:  - `ByBillingPeriod` (default): The rating is based on all the usages in a billing period. - `ByUsageStartDate`: The rating is based on all the usages on the same usage start date.  - `ByUsageRecord`: The rating is based on each usage record. - `ByUsageUpload`: The rating is based on all the  usages in a uploaded usage file (`.xls` or `.csv`). - `ByGroupId`: The rating is based on all the usages in a custom group.  **Note:**  - The `ByBillingPeriod` value can be applied for all charge models.  - The `ByUsageStartDate`, `ByUsageRecord`, and `ByUsageUpload` values can only be applied for per unit, volume pricing, and tiered pricing charge models.  - The `ByGroupId` value is only available if you have [Active Rating](https://knowledgecenter.zuora.com/CB_Billing/J_Billing_Operations/H_Active_Rating) feature enabled. - Use this field only for Usage charges. One-Time Charges and Recurring Charges return `NULL`.   # noqa: E501

        :return: The rating_group of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._rating_group

    @rating_group.setter
    def rating_group(self, rating_group):
        """Sets the rating_group of this ProxyModifyProductRatePlanCharge.

        Specifies a rating group based on which usage records are rated.  **Note:** This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Possible values:  - `ByBillingPeriod` (default): The rating is based on all the usages in a billing period. - `ByUsageStartDate`: The rating is based on all the usages on the same usage start date.  - `ByUsageRecord`: The rating is based on each usage record. - `ByUsageUpload`: The rating is based on all the  usages in a uploaded usage file (`.xls` or `.csv`). - `ByGroupId`: The rating is based on all the usages in a custom group.  **Note:**  - The `ByBillingPeriod` value can be applied for all charge models.  - The `ByUsageStartDate`, `ByUsageRecord`, and `ByUsageUpload` values can only be applied for per unit, volume pricing, and tiered pricing charge models.  - The `ByGroupId` value is only available if you have [Active Rating](https://knowledgecenter.zuora.com/CB_Billing/J_Billing_Operations/H_Active_Rating) feature enabled. - Use this field only for Usage charges. One-Time Charges and Recurring Charges return `NULL`.   # noqa: E501

        :param rating_group: The rating_group of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._rating_group = rating_group

    @property
    def recognized_revenue_account(self):
        """Gets the recognized_revenue_account of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         The name of the recognized revenue account for this charge.  - Required when the Allow Blank Accounting Code setting is No. - Optional when the Allow Blank Accounting Code setting is Yes.  **Character limit**: 100 **Values**: an active accounting code in your Zuora Chart of Accounts This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    # noqa: E501

        :return: The recognized_revenue_account of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._recognized_revenue_account

    @recognized_revenue_account.setter
    def recognized_revenue_account(self, recognized_revenue_account):
        """Sets the recognized_revenue_account of this ProxyModifyProductRatePlanCharge.

         The name of the recognized revenue account for this charge.  - Required when the Allow Blank Accounting Code setting is No. - Optional when the Allow Blank Accounting Code setting is Yes.  **Character limit**: 100 **Values**: an active accounting code in your Zuora Chart of Accounts This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    # noqa: E501

        :param recognized_revenue_account: The recognized_revenue_account of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._recognized_revenue_account = recognized_revenue_account

    @property
    def rev_rec_code(self):
        """Gets the rev_rec_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Associates this product rate plan charge with a specific revenue recognition code. **Character limit**: 70 **Values**: a valid revenue recognition code   # noqa: E501

        :return: The rev_rec_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._rev_rec_code

    @rev_rec_code.setter
    def rev_rec_code(self, rev_rec_code):
        """Sets the rev_rec_code of this ProxyModifyProductRatePlanCharge.

        Associates this product rate plan charge with a specific revenue recognition code. **Character limit**: 70 **Values**: a valid revenue recognition code   # noqa: E501

        :param rev_rec_code: The rev_rec_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._rev_rec_code = rev_rec_code

    @property
    def rev_rec_trigger_condition(self):
        """Gets the rev_rec_trigger_condition of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Specifies when revenue recognition begins. **Character limit**: 22 **Values**: one of the following:  - `ContractEffectiveDate` - `ServiceActivationDate` - `CustomerAcceptanceDate`   # noqa: E501

        :return: The rev_rec_trigger_condition of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._rev_rec_trigger_condition

    @rev_rec_trigger_condition.setter
    def rev_rec_trigger_condition(self, rev_rec_trigger_condition):
        """Sets the rev_rec_trigger_condition of this ProxyModifyProductRatePlanCharge.

         Specifies when revenue recognition begins. **Character limit**: 22 **Values**: one of the following:  - `ContractEffectiveDate` - `ServiceActivationDate` - `CustomerAcceptanceDate`   # noqa: E501

        :param rev_rec_trigger_condition: The rev_rec_trigger_condition of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._rev_rec_trigger_condition = rev_rec_trigger_condition

    @property
    def revenue_recognition_rule_name(self):
        """Gets the revenue_recognition_rule_name of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Determines when to recognize the revenue for this charge. **Character limit**: 25 **Values**: one of the following:  - `Recognize upon invoicing` - `Recognize daily over time`   # noqa: E501

        :return: The revenue_recognition_rule_name of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._revenue_recognition_rule_name

    @revenue_recognition_rule_name.setter
    def revenue_recognition_rule_name(self, revenue_recognition_rule_name):
        """Sets the revenue_recognition_rule_name of this ProxyModifyProductRatePlanCharge.

        Determines when to recognize the revenue for this charge. **Character limit**: 25 **Values**: one of the following:  - `Recognize upon invoicing` - `Recognize daily over time`   # noqa: E501

        :param revenue_recognition_rule_name: The revenue_recognition_rule_name of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._revenue_recognition_rule_name = revenue_recognition_rule_name

    @property
    def smoothing_model(self):
        """Gets the smoothing_model of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Specifies the smoothing model for an overage smoothing charge model. **Character limit**: 22 **Values**: one of the following:  - `RollingWindow` - `Rollover`   # noqa: E501

        :return: The smoothing_model of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._smoothing_model

    @smoothing_model.setter
    def smoothing_model(self, smoothing_model):
        """Sets the smoothing_model of this ProxyModifyProductRatePlanCharge.

         Specifies the smoothing model for an overage smoothing charge model. **Character limit**: 22 **Values**: one of the following:  - `RollingWindow` - `Rollover`   # noqa: E501

        :param smoothing_model: The smoothing_model of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._smoothing_model = smoothing_model

    @property
    def specific_billing_period(self):
        """Gets the specific_billing_period of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Customizes the number of months or weeks for the charges billing period. This field is required if you set the value of the BillingPeriod field to `Specific Months` or `Specific Weeks`. **Values**: a positive integer   # noqa: E501

        :return: The specific_billing_period of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: int
        """
        return self._specific_billing_period

    @specific_billing_period.setter
    def specific_billing_period(self, specific_billing_period):
        """Sets the specific_billing_period of this ProxyModifyProductRatePlanCharge.

         Customizes the number of months or weeks for the charges billing period. This field is required if you set the value of the BillingPeriod field to `Specific Months` or `Specific Weeks`. **Values**: a positive integer   # noqa: E501

        :param specific_billing_period: The specific_billing_period of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: int
        """

        self._specific_billing_period = specific_billing_period

    @property
    def tax_code(self):
        """Gets the tax_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Specifies the tax code for taxation rules. Required when the Taxable field is set to `True`.  **Character limit**: 64  **Values**: a valid tax code  **Note**: This value affects the tax calculation of rate plan charges that come from the `ProductRatePlanCharge`.   # noqa: E501

        :return: The tax_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._tax_code

    @tax_code.setter
    def tax_code(self, tax_code):
        """Sets the tax_code of this ProxyModifyProductRatePlanCharge.

         Specifies the tax code for taxation rules. Required when the Taxable field is set to `True`.  **Character limit**: 64  **Values**: a valid tax code  **Note**: This value affects the tax calculation of rate plan charges that come from the `ProductRatePlanCharge`.   # noqa: E501

        :param tax_code: The tax_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._tax_code = tax_code

    @property
    def tax_mode(self):
        """Gets the tax_mode of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Determines how to define taxation for the charge. Required when the Taxable field is set to `True`.  **Character limit**: 12  **Values**: one of the following:  - `TaxExclusive` - `TaxInclusive`  **Note**: This value affects the tax calculation of rate plan charges that come from the `ProductRatePlanCharge`.   # noqa: E501

        :return: The tax_mode of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._tax_mode

    @tax_mode.setter
    def tax_mode(self, tax_mode):
        """Sets the tax_mode of this ProxyModifyProductRatePlanCharge.

         Determines how to define taxation for the charge. Required when the Taxable field is set to `True`.  **Character limit**: 12  **Values**: one of the following:  - `TaxExclusive` - `TaxInclusive`  **Note**: This value affects the tax calculation of rate plan charges that come from the `ProductRatePlanCharge`.   # noqa: E501

        :param tax_mode: The tax_mode of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._tax_mode = tax_mode

    @property
    def taxable(self):
        """Gets the taxable of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Determines whether the charge is taxable. When set to `True`, the TaxMode and TaxCode fields are required when creating or updating th ProductRatePlanCharge object.  **Character limit**: 5  **Values**: `True`, `False`  **Note**: This value affects the tax calculation of rate plan charges that come from the `ProductRatePlanCharge`.   # noqa: E501

        :return: The taxable of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: bool
        """
        return self._taxable

    @taxable.setter
    def taxable(self, taxable):
        """Sets the taxable of this ProxyModifyProductRatePlanCharge.

         Determines whether the charge is taxable. When set to `True`, the TaxMode and TaxCode fields are required when creating or updating th ProductRatePlanCharge object.  **Character limit**: 5  **Values**: `True`, `False`  **Note**: This value affects the tax calculation of rate plan charges that come from the `ProductRatePlanCharge`.   # noqa: E501

        :param taxable: The taxable of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: bool
        """

        self._taxable = taxable

    @property
    def trigger_event(self):
        """Gets the trigger_event of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Specifies when to start billing the customer for the charge. **Character limit**: 18 **Values**: one of the following:  - `ContractEffective` is the date when the subscription's contract goes into effect and the charge is ready to be billed. - `ServiceActivation` is the date when the services or products for a subscription have been activated and the customers have access. - `CustomerAcceptance` is when the customer accepts the services or products for a subscription.   # noqa: E501

        :return: The trigger_event of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._trigger_event

    @trigger_event.setter
    def trigger_event(self, trigger_event):
        """Sets the trigger_event of this ProxyModifyProductRatePlanCharge.

         Specifies when to start billing the customer for the charge. **Character limit**: 18 **Values**: one of the following:  - `ContractEffective` is the date when the subscription's contract goes into effect and the charge is ready to be billed. - `ServiceActivation` is the date when the services or products for a subscription have been activated and the customers have access. - `CustomerAcceptance` is when the customer accepts the services or products for a subscription.   # noqa: E501

        :param trigger_event: The trigger_event of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._trigger_event = trigger_event

    @property
    def uom(self):
        """Gets the uom of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Specifies the units to measure usage. **Character limit**: 25 **Values**: a configured unit of measure **Note**: You must specify this field when creating the following charge models:  - Per Unit Pricing - Volume Pricing - Overage Pricing - Tiered Pricing - Tiered with Overage Pricing   # noqa: E501

        :return: The uom of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._uom

    @uom.setter
    def uom(self, uom):
        """Sets the uom of this ProxyModifyProductRatePlanCharge.

         Specifies the units to measure usage. **Character limit**: 25 **Values**: a configured unit of measure **Note**: You must specify this field when creating the following charge models:  - Per Unit Pricing - Volume Pricing - Overage Pricing - Tiered Pricing - Tiered with Overage Pricing   # noqa: E501

        :param uom: The uom of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._uom = uom

    @property
    def up_to_periods(self):
        """Gets the up_to_periods of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Specifies the length of the period during which the charge is active. If this period ends before the subscription ends, the charge ends when this period ends. **Character limit**: 5 **Values**: a whole number between 0 and 65535, exclusive **Note**:  - You must use this field together with the `UpToPeriodsType` field to specify the time period. This field is applicable only when the `EndDateCondition` field is set to `FixedPeriod`. - If the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge end date will change accordingly up to the original period end.   # noqa: E501

        :return: The up_to_periods of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: int
        """
        return self._up_to_periods

    @up_to_periods.setter
    def up_to_periods(self, up_to_periods):
        """Sets the up_to_periods of this ProxyModifyProductRatePlanCharge.

         Specifies the length of the period during which the charge is active. If this period ends before the subscription ends, the charge ends when this period ends. **Character limit**: 5 **Values**: a whole number between 0 and 65535, exclusive **Note**:  - You must use this field together with the `UpToPeriodsType` field to specify the time period. This field is applicable only when the `EndDateCondition` field is set to `FixedPeriod`. - If the subscription end date is subsequently changed through a Renewal, or Terms and Conditions amendment, the charge end date will change accordingly up to the original period end.   # noqa: E501

        :param up_to_periods: The up_to_periods of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: int
        """

        self._up_to_periods = up_to_periods

    @property
    def up_to_periods_type(self):
        """Gets the up_to_periods_type of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         The period type used to define when the charge ends. **Character limit**: -- **Values**: one of the following:  - `Billing Periods` (default) - `Days` - `Weeks` - `Months` - Years **Note**:  - You must use this field together with the `UpToPeriods` field to specify the time period. - This field is applicable only when the `EndDateCondition` field is set to `FixedPeriod`.   # noqa: E501

        :return: The up_to_periods_type of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._up_to_periods_type

    @up_to_periods_type.setter
    def up_to_periods_type(self, up_to_periods_type):
        """Sets the up_to_periods_type of this ProxyModifyProductRatePlanCharge.

         The period type used to define when the charge ends. **Character limit**: -- **Values**: one of the following:  - `Billing Periods` (default) - `Days` - `Weeks` - `Months` - Years **Note**:  - You must use this field together with the `UpToPeriods` field to specify the time period. - This field is applicable only when the `EndDateCondition` field is set to `FixedPeriod`.   # noqa: E501

        :param up_to_periods_type: The up_to_periods_type of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """

        self._up_to_periods_type = up_to_periods_type

    @property
    def usage_record_rating_option(self):
        """Gets the usage_record_rating_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Determines how Zuora processes usage records for per-unit usage charges.    # noqa: E501

        :return: The usage_record_rating_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._usage_record_rating_option

    @usage_record_rating_option.setter
    def usage_record_rating_option(self, usage_record_rating_option):
        """Sets the usage_record_rating_option of this ProxyModifyProductRatePlanCharge.

        Determines how Zuora processes usage records for per-unit usage charges.    # noqa: E501

        :param usage_record_rating_option: The usage_record_rating_option of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: str
        """
        allowed_values = ["EndOfBillingPeriod", "OnDemand"]  # noqa: E501
        if usage_record_rating_option not in allowed_values:
            raise ValueError(
                "Invalid value for `usage_record_rating_option` ({0}), must be one of {1}"  # noqa: E501
                .format(usage_record_rating_option, allowed_values)
            )

        self._usage_record_rating_option = usage_record_rating_option

    @property
    def use_discount_specific_accounting_code(self):
        """Gets the use_discount_specific_accounting_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501

        Determines whether to define a new accounting code for the new discount charge. **Character limit**: 5 **Values**: `True`, `False`   # noqa: E501

        :return: The use_discount_specific_accounting_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: bool
        """
        return self._use_discount_specific_accounting_code

    @use_discount_specific_accounting_code.setter
    def use_discount_specific_accounting_code(self, use_discount_specific_accounting_code):
        """Sets the use_discount_specific_accounting_code of this ProxyModifyProductRatePlanCharge.

        Determines whether to define a new accounting code for the new discount charge. **Character limit**: 5 **Values**: `True`, `False`   # noqa: E501

        :param use_discount_specific_accounting_code: The use_discount_specific_accounting_code of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: bool
        """

        self._use_discount_specific_accounting_code = use_discount_specific_accounting_code

    @property
    def use_tenant_default_for_price_change(self):
        """Gets the use_tenant_default_for_price_change of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Applies the tenant-level percentage uplift value for an automatic price change to a termed subscription's renewal. **Character limit**: 5 **Values**: `true`, `false`   # noqa: E501

        :return: The use_tenant_default_for_price_change of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: bool
        """
        return self._use_tenant_default_for_price_change

    @use_tenant_default_for_price_change.setter
    def use_tenant_default_for_price_change(self, use_tenant_default_for_price_change):
        """Sets the use_tenant_default_for_price_change of this ProxyModifyProductRatePlanCharge.

         Applies the tenant-level percentage uplift value for an automatic price change to a termed subscription's renewal. **Character limit**: 5 **Values**: `true`, `false`   # noqa: E501

        :param use_tenant_default_for_price_change: The use_tenant_default_for_price_change of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :type: bool
        """

        self._use_tenant_default_for_price_change = use_tenant_default_for_price_change

    @property
    def weekly_bill_cycle_day(self):
        """Gets the weekly_bill_cycle_day of this ProxyModifyProductRatePlanCharge.  # noqa: E501

         Specifies which day of the week as the bill cycle day (BCD) for the charge. This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  **Values**: one of the following:  - `Sunday` - `Monday` - `Tuesday` - `Wednesday` - `Thursday` - `Friday` - `Saturday`   # noqa: E501

        :return: The weekly_bill_cycle_day of this ProxyModifyProductRatePlanCharge.  # noqa: E501
        :rtype: str
        """
        return self._weekly_bill_cycle_day

    @weekly_bill_cycle_day.setter
    def weekly_bill_cycle_day(self, weekly_bill_cycle_day):
        """Sets the weekly_bill_cycle_day of this ProxyModifyProductRatePlanCharge.

         Specifies which day of the week as the bill cycle day (BCD) for the charge. This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  **Values**: one of the following:  - `Sunday` - `Monday` - `Tuesday` - `Wednesday` - `Thursday` - `Friday` - `Saturday`   # noqa: E501

        :param weekly_bill_cycle_day: The weekly_bill_cycle_day of this ProxyModifyProductRatePlanCharge.  # noqa: E501
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
        if issubclass(ProxyModifyProductRatePlanCharge, dict):
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
        if not isinstance(other, ProxyModifyProductRatePlanCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
