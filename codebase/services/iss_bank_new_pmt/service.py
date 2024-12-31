from model.common import Service
from services.iss_bank_new_pmt.rqrsp import IssuingBankNewPaymentRequest
from util.service_base import register_healthcheck_endpoint
from util.structured_logging import configure_structured_logging
from fastapi import FastAPI
from util.service import request_handler
from services.iss_bank_new_pmt.logic import handle_issuing_bank_new_payment_request

def api():

    api = FastAPI()
    configure_structured_logging(Service.ISS_BANK_NEW_PMT)

    register_healthcheck_endpoint(api)

    @api.post("/")
    def new_payment(rq: IssuingBankNewPaymentRequest):
        return request_handler(
            IssuingBankNewPaymentRequest,
            handle_issuing_bank_new_payment_request
        )(rq)

    return api