from sqlalchemy.engine.base import Engine
from util.events import log_event
from fastapi import FastAPI

from services.merchant_pos_new_checkout.rqrsp import MerchantNewCheckoutRequest
from services.platform_new_receipt.client import PlatformNewReceiptClient
from services.pmt_proc_new_pmt.client import PaymentProcessorNewPaymentClient
from util.service import request_handler
from services.merchant_pos_new_checkout.logic import configure_logic, handle_merchant_new_checkout_request, rq_received_logevent
from model.logevent import HealthChecked

def configure_api(
    write_engine: Engine, 
    pmt_proc_new_pmt_service: PaymentProcessorNewPaymentClient, 
    platform_new_receipt_service: PlatformNewReceiptClient
):
    
    configure_logic(write_engine, pmt_proc_new_pmt_service, platform_new_receipt_service)

api = FastAPI()

@api.get("/healthcheck")
def get_root():
    log_event(HealthChecked())

@api.post("/")
def checkout(rq: MerchantNewCheckoutRequest):
    return request_handler(
        'MerchantNewCheckoutRequestReceived', 
        rq_received_logevent, 
        handle_merchant_new_checkout_request
    )(rq)