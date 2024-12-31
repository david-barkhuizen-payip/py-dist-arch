from model.common import Service
from model.logevent import RequestReceivedLogEvent
from services.merchant_pos_new_checkout.client import MerchantPosNewCheckoutClient
from services.merchant_pos_new_checkout.rqrsp import MerchantNewCheckoutRequest
from services.test.rqrsp import TestExport, TestRequest, TestResponse
from util.env import endpoint_from_env


def handle_test_request(client_id: int, rq: TestRequest):

    merchant_pos_new_checkout_service = MerchantPosNewCheckoutClient(        
        endpoint_from_env(Service.MERCHANT_POS_NEW_CHECKOUT)
    )

    rsp = merchant_pos_new_checkout_service.post(
        MerchantNewCheckoutRequest(
            currency_amt=rq.currency_amt,
            currency=rq.currency.value,
        )
    )

    return TestResponse(
        test=TestExport(
            merchant_pos_checkout=rsp.checkout
        )
    )

def rq_received_logevent(client_id, rq):
    return RequestReceivedLogEvent(rq=str(rq))