import datetime
import uuid
from services.merchant_pos_new_checkout.rqrsp import MerchantPosNewCheckoutRequest, MerchantPosNewCheckoutResponse
from services.platform_new_receipt.client import PlatformNewReceiptClient
from services.pmt_proc_new_pmt.client import PaymentProcessorNewPaymentClient
from services.pmt_proc_new_pmt.rqrsp import PaymentProcessorNewCustomerPaymentRequest
from util.env import endpoint_from_env

def handle_merchant_pos_new_checkout_request(client_id: int, rq: MerchantPosNewCheckoutRequest):

    pmt_proc_new_pmt_service = PaymentProcessorNewPaymentClient(endpoint_from_env('PMT_PROC_NEW_PMT', no_path = True))
    
    payment = pmt_proc_new_pmt_service.post(
        PaymentProcessorNewCustomerPaymentRequest(
            currency=rq.currency,
            currency_amt=rq.currency_amt
    ))

    # platform new receipt
    platform_new_receipt_service = PlatformNewReceiptClient(endpoint_from_env('PLATFORM_NEW_RECEIPT', no_path = True))

    return MerchantPosNewCheckoutResponse(
        id = uuid.uuid4(),
        created_at=datetime.datetime.now(),
        client_id=client_id
    )
