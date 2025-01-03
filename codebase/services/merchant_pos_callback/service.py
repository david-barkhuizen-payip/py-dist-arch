from model.common import Service
from services.merchant_pos_callback.rqrsp import MerchantPosCallbackRequest
from util.service_base import register_healthcheck_endpoint
from util.structured_logging import configure_structured_logging
from fastapi import FastAPI
from util.service import request_handler
from services.merchant_pos_callback.logic import handle_merchant_pos_callback_request

def api():
    api = FastAPI()
    configure_structured_logging(Service.MERCHANT_POS_CALLBACK)

    register_healthcheck_endpoint(api)

    @api.post("/")
    def callback(rq: MerchantPosCallbackRequest):
        return request_handler(
            MerchantPosCallbackRequest,
            handle_merchant_pos_callback_request
        )(rq)

    return api