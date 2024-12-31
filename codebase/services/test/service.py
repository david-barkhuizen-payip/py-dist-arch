from model.common import Service
from services.test.rqrsp import TestRequest
from util.service_base import register_healthcheck_endpoint
from util.structured_logging import configure_structured_logging, log_event
from fastapi import FastAPI
from util.service import request_handler
from model.logevent import HealthChecked
from services.test.logic import handle_test_request


def api():

    api = FastAPI()
    configure_structured_logging(Service.TEST)

    register_healthcheck_endpoint(api)

    @api.post("/")
    def checkout(rq: TestRequest):
        return request_handler(
            TestRequest, 
            handle_test_request
        )(rq)
    
    return api