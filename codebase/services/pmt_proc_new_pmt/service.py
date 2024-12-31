from model.common import Service
from services.pmt_proc_new_pmt.rqrsp import PaymentProcessorNewCustomerPaymentRequest
from util.structured_logging import configure_structured_logging, log_event
from fastapi import FastAPI
from util.service import request_handler
from services.pmt_proc_new_pmt.logic import handle_payment_processor_new_customer_payment_request
from model.logevent import HealthChecked

def api():

    api = FastAPI()
    configure_structured_logging(Service.PMT_PROC_NEW_PMT)

    @api.get("/healthcheck")
    def get_root():
        log_event(HealthChecked())

    @api.post("/")
    def new_payment(rq: PaymentProcessorNewCustomerPaymentRequest):
        return request_handler(
            PaymentProcessorNewCustomerPaymentRequest,
            handle_payment_processor_new_customer_payment_request
        )(rq)

    return api