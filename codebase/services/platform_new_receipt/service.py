from services.platform_new_receipt.rqrsp import PlatformNewReceiptRequest
from util.service import request_handler
from services.platform_new_receipt.logic import configure_logic, handle_platform_new_receipt_request, rq_received_logevent

from sqlalchemy.engine.base import Engine
from util.structured_logging import log_event

from fastapi import FastAPI

from model.logevent import HealthChecked

def configure_api(write_engine: Engine, q_publisher):
    configure_logic(write_engine, q_publisher)

api = FastAPI()

@api.get("/healthcheck")
def get_root():
    log_event(HealthChecked())

@api.post("/")
def new_platform_receipt(rq: PlatformNewReceiptRequest):
    return request_handler(
        'PlatformNewReceiptRequest', 
        rq_received_logevent, 
        handle_platform_new_receipt_request
    )(rq)