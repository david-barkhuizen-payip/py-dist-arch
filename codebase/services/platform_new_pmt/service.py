from model.common import Service
from services.platform_new_pmt.rqrsp import PlatformNewPaymentRequest
from util.service import request_handler
from services.platform_new_pmt.logic import handle_platform_new_payment_request
from util.structured_logging import configure_structured_logging, log_event
from fastapi import FastAPI
from model.logevent import HealthChecked

def api():

    api = FastAPI()
    configure_structured_logging(Service.PLATFORM_NEW_PMT)

    @api.get("/healthcheck")
    def get_root():
        log_event(HealthChecked())

    @api.post("/")
    def new_platform_payment(rq: PlatformNewPaymentRequest):
        return request_handler(
            PlatformNewPaymentRequest, 
            handle_platform_new_payment_request
        )(rq)

    return api
