import datetime
from fastapi import FastAPI

from model.common import Service
from model.logevent import HealthChecked
from util.structured_logging import configure_structured_logging, log_event
from util.rqrsp import HealthCheckResponse


def api():

    api = FastAPI()
    configure_structured_logging(Service.MIGRATION)

    @api.get("/healthcheck")
    async def get_healthcheck():
        timestamp = datetime.datetime.now().isoformat()
        log_event(HealthChecked(timestamp=timestamp))
        return HealthCheckResponse(timestamp=timestamp)
    
    return api