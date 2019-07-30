# PostNonRefRefundType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id__ns** | **str** | ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**integration_status__ns** | **str** | Status of the refund&#39;s synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**origin__ns** | **str** | Origin of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**sync_date__ns** | **str** | Date when the refund was synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**syncto_net_suite__ns** | **str** | Specifies whether the refund should be synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId&#x3D;265).  | [optional] 
**comment** | **str** | Comments about the refund.  | [optional] 
**finance_information** | [**PostNonRefRefundTypeFinanceInformation**](PostNonRefRefundTypeFinanceInformation.md) |  | [optional] 
**gateway_id** | **str** | The ID of the gateway instance that processes the refund. This field can be specified only for electronic refunds. The ID must be a valid gateway instance ID, and this gateway must support the specific payment method.   If no gateway ID is specified, the default gateway in the billing account configuration will be used. If no gateway is specified in the billing account, the default gateway of the corresponding tenant will be used.  | [optional] 
**items** | [**list[RefundCreditMemoItemType]**](RefundCreditMemoItemType.md) | Container for credit memo items.  **Note:** The Invoice Item Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  | [optional] 
**method_type** | **str** | How an external refund was issued to a customer. This field is required for an external refund and must be left empty for an electronic refund. You can issue an external refund on a credit memo.  | [optional] 
**payment_method_id** | **str** | The ID of the payment method used for the refund. This field is required for an electronic refund, and the value must be an electronic payment method ID. This field must be left empty for an external refund.   | [optional] 
**reason_code** | **str** | A code identifying the reason for the transaction. The value must be an existing reason code or empty. If you do not specify a value, Zuora uses the default reason code.  | [optional] 
**reference_id** | **str** | The transaction ID returned by the payment gateway for an electronic refund. Use this field to reconcile refunds between your gateway and Zuora Payments.  | [optional] 
**refund_date** | **date** | The date when the refund takes effect, in &#x60;yyyy-mm-dd&#x60; format. The date of the refund cannot be before the credit memo date. Specify this field only for external refunds. Zuora automatically generates this field for electronic refunds.  | [optional] 
**second_refund_reference_id** | **str** | The transaction ID returned by the payment gateway if there is an additional transaction for the refund. Use this field to reconcile payments between your gateway and Zuora Payments.  | [optional] 
**total_amount** | **float** | The total amount of the refund. The amount cannot exceed the unapplied amount of the associated credit memo. If the original credit memo was applied to one or more invoices or debit memos, you have to unapply a full or partial credit memo from the invoices or debit memos, and then refund the full or partial unapplied credit memo to your customers.  | 
**type** | **str** | The type of the refund.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


