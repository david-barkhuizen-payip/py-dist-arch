from services.iss_bank_new_pmt.client import IssuingBankNewCustomerPaymentClient
from services.pmt_proc_new_pmt.rqrsp import PaymentProcessorNewCustomerPaymentRequest
from sqlalchemy.engine.base import Engine
from util.events import log_event
from fastapi import FastAPI

from util.service import request_handler
from services.pmt_proc_new_pmt.logic import configure_logic, handle_payment_processor_new_customer_payment_request, rq_received_logevent
from model.logevent import HealthChecked

def configure_api(
    write_engine: Engine, 
    iss_bank_new_pmt_service: IssuingBankNewCustomerPaymentClient, 
):
    
    configure_logic(write_engine, iss_bank_new_pmt_service)

api = FastAPI()

@api.get("/healthcheck")
async def get_root():
    log_event(HealthChecked())

@api.post("/")
def new_payment(rq: PaymentProcessorNewCustomerPaymentRequest):
    return request_handler(
        'PaymentProcessorNewCustomerPaymentRequestReceived', 
        rq_received_logevent, 
        handle_payment_processor_new_customer_payment_request
    )(rq)