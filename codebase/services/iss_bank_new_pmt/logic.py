from model.logevent import RequestReceivedLogEvent
from services.iss_bank_new_pmt.rqrsp import IssuingBankPaymentExport, IssuingBankNewPaymentRequest, IssuingBankNewPaymentResponse
from services.platform_new_pmt.client import PlatformNewPaymentClient
from util.env import endpoint_from_env


def handle_issuing_bank_new_payment_request(
    client_id: int, 
    rq: IssuingBankNewPaymentRequest
):

    platform_new_pmt_service = PlatformNewPaymentClient(endpoint_from_env('PLATFORM_NEW_PMT', no_path = True))

    return IssuingBankNewPaymentResponse(
        payment=IssuingBankPaymentExport()
    )

def rq_received_logevent(client_id, rq):
    return RequestReceivedLogEvent(text=str(rq))