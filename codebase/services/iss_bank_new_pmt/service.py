from services.iss_bank_new_pmt.rqrsp import IssuingBankNewPaymentRequest
from services.platform_new_pmt.client import PlatformNewPaymentClient

from sqlalchemy.engine.base import Engine
from util.structured_logging import log_event
from fastapi import FastAPI

from util.service import request_handler
from services.iss_bank_new_pmt.logic import configure_logic, handle_issuing_bank_new_payment_request, rq_received_logevent
from model.logevent import HealthChecked

def configure_api(
    write_engine: Engine, 
    platform_new_pmt_service: PlatformNewPaymentClient, 
):
    
    configure_logic(write_engine, platform_new_pmt_service)

api = FastAPI()

@api.get("/healthcheck")
def get_root():
    log_event(HealthChecked())

@api.post("/")
def checkout(rq: IssuingBankNewPaymentRequest):
    return request_handler(
        'IssuingBankNewPaymentRequest', 
        rq_received_logevent, 
        handle_issuing_bank_new_payment_request
    )(rq)