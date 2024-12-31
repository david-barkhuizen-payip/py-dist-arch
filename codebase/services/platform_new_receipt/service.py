from model.common import Service
from services.platform_new_receipt.rqrsp import PlatformNewReceiptRequest
from util.service import request_handler
from services.platform_new_receipt.logic import handle_platform_new_receipt_request
from util.structured_logging import configure_structured_logging, log_event
from fastapi import FastAPI
from model.logevent import HealthChecked


def api():

    api = FastAPI()
    configure_structured_logging(Service.PLATFORM_NEW_RECEIPT)

    @api.get("/healthcheck")
    def get_root():
        log_event(HealthChecked())

    @api.post("/")
    def new_platform_receipt(rq: PlatformNewReceiptRequest):
        return request_handler(
            PlatformNewReceiptRequest, 
            handle_platform_new_receipt_request
        )(rq)
    
    return api