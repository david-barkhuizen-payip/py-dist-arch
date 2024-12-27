from services.merchant_pos_new_checkout.client import MerchantPosNewCheckoutClient
from services.test_service.rqrsp import TestRequest
from sqlalchemy.engine.base import Engine
from util.events import log_event
from fastapi import FastAPI

from util.service import request_handler
from model.logevent import HealthChecked
from services.test_service.logic import configure_logic, handle_test_request, rq_received_logevent

def configure_api(
    write_engine: Engine, 
    merchant_pos_new_checkout_service: MerchantPosNewCheckoutClient, 
):
    
    configure_logic(write_engine, merchant_pos_new_checkout_service)

api = FastAPI()

@api.get("/healthcheck")
async def get_root():
    log_event(HealthChecked())

@api.post("/test")
def checkout(rq: TestRequest):
    return request_handler(
        'TestRequestReceived', 
        rq_received_logevent, 
        handle_test_request
    )(rq)