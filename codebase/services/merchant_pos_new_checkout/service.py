from model.common import Service
from util.service_base import register_healthcheck_endpoint
from util.structured_logging import configure_structured_logging, log_event
from fastapi import FastAPI
from services.merchant_pos_new_checkout.rqrsp import MerchantNewCheckoutRequest
from util.service import request_handler
from services.merchant_pos_new_checkout.logic import handle_merchant_new_checkout_request
from model.logevent import HealthChecked


def api():

    api = FastAPI()
    configure_structured_logging(Service.MERCHANT_POS_NEW_CHECKOUT)

    register_healthcheck_endpoint(api)

    @api.post("/")
    def checkout(rq: MerchantNewCheckoutRequest):
        return request_handler(
            MerchantNewCheckoutRequest, 
            handle_merchant_new_checkout_request
        )(rq)
    
    return api