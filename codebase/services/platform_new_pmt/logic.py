from model.logevent import RequestReceivedLogEvent
from services.iss_bank_new_pmt.client import IssuingBankNewCustomerPaymentClient
from services.platform_new_pmt.rqrsp import PlatformNewPaymentRequest, PlatformNewPaymentResponse
from util.env import endpoint_from_env


def handle_platform_new_payment_request(
    client_id: int, 
    rq: PlatformNewPaymentRequest
):
    
    iss_bank_new_pmt_service = IssuingBankNewCustomerPaymentClient(
        endpoint_from_env('ISS_BANK_NEW_PMT', no_path = True)
    )

    return PlatformNewPaymentResponse()