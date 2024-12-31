import datetime
from fastapi import FastAPI

from model.common import Service
from model.logevent import HealthChecked
from util.service_base import register_healthcheck_endpoint
from util.structured_logging import configure_structured_logging, log_event
from util.rqrsp import HealthCheckResponse


def api():

    api = FastAPI()
    configure_structured_logging(Service.MIGRATION)

    register_healthcheck_endpoint(api)
    
    return api