import datetime
import uuid
from model.logevent import RequestReceivedLogEvent
from services.merchant_pos_new_checkout.rqrsp import MerchantPosCheckoutExport, MerchantNewCheckoutRequest, MerchantNewCheckoutResponse
from services.platform_new_receipt.client import PlatformNewReceiptClient
from services.pmt_proc_new_pmt.client import PaymentProcessorNewPaymentClient
from util.env import endpoint_from_env

def handle_merchant_new_checkout_request(client_id: int, rq: MerchantNewCheckoutRequest):

    pmt_proc_new_pmt_service = PaymentProcessorNewPaymentClient(endpoint_from_env('PMT_PROC_NEW_PMT', no_path = True))
    payment = pmt_proc_new_pmt_service.invoke(currency_amt=rq.currency_amt, currency=rq.currency)

    # platform new receipt
    platform_new_receipt_service = PlatformNewReceiptClient(endpoint_from_env('PLATFORM_NEW_RECEIPT', no_path = True))

    return MerchantNewCheckoutResponse(
        checkout=MerchantPosCheckoutExport(
            id = uuid.uuid4(),
            created_at=datetime.datetime.now(),
            client_id=client_id
        )
    )

def rq_received_logevent(client_id, rq):
    return RequestReceivedLogEvent(text=str(rq))