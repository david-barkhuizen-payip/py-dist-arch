from model.common import Service
from services.trigger.rqrsp import TriggerRequest
from util.service_base import register_healthcheck_endpoint
from util.structured_logging import configure_structured_logging
from fastapi import FastAPI
from util.service import request_handler
from services.trigger.logic import handle_trigger_merchant_pos_new_checkout_request

def api():
        
    api = FastAPI()
    configure_structured_logging(Service.TRIGGER)

    register_healthcheck_endpoint(api)

    @api.post("/merchant_pos_new_checkout")
    def merchant_pos_new_checkout(rq: TriggerRequest):
        return request_handler(
            TriggerRequest, 
            handle_trigger_merchant_pos_new_checkout_request
        )(rq)
    
    return api