from services.platform_new_pmt.rqrsp import PlatformNewPaymentRequest
from util.service import request_handler
from services.platform_new_pmt.logic import configure_logic, handle_platform_new_payment_request, rq_received_logevent

from sqlalchemy.engine.base import Engine
from util.events import log_event

from fastapi import FastAPI

from model.logevent import HealthChecked

def configure_api(write_engine: Engine, q_publisher):
    configure_logic(write_engine, q_publisher)

api = FastAPI()

@api.get("/healthcheck")
async def get_root():
    log_event(HealthChecked())

@api.post("/")
def new_platform_payment(rq: PlatformNewPaymentRequest):
    return request_handler(
        'PlatformNewPaymentRequest', 
        rq_received_logevent, 
        handle_platform_new_payment_request
    )(rq)