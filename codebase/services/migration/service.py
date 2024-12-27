import datetime
from fastapi import FastAPI

from model.common import Service
from model.logevent import HealthChecked
from util.events import configure_and_test_logging, log_event
from util.rqrsp import HealthCheckResponse


def api():

    app = FastAPI()

    configure_and_test_logging(Service.MIGRATION)

    @app.get("/healthcheck")
    async def get_healthcheck():
        timestamp = datetime.datetime.now().isoformat()
        log_event(HealthChecked(timestamp=timestamp))
        return HealthCheckResponse(timestamp=timestamp)
    
    return app