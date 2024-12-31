from model.common import Service
from services.test.rqrsp import TestRequest
from util.structured_logging import configure_structured_logging, log_event
from fastapi import FastAPI
from util.service import request_handler
from model.logevent import HealthChecked
from services.test.logic import handle_test_request


def api():

    api = FastAPI()
    configure_structured_logging(Service.TEST)

    @api.get("/healthcheck")
    async def get_root():
        log_event(HealthChecked())

    @api.post("/checkout")
    def checkout(rq: TestRequest):
        return request_handler(
            TestRequest, 
            handle_test_request
        )(rq)
    
    return api