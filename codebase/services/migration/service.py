from fastapi import FastAPI
from model.common import Service
from util.service_base import register_healthcheck_endpoint
from util.structured_logging import configure_structured_logging


def api():

    api = FastAPI()
    configure_structured_logging(Service.MIGRATION)

    register_healthcheck_endpoint(api)
    
    return api