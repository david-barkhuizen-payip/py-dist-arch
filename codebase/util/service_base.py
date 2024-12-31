import datetime
import traceback
from typing import Callable
from services.migration.client import MigrationServiceClient
import uvicorn
from util.structured_logging import configure_structured_logging, configure_structured_logging
from model.logevent import HealthChecked, ServiceStartupLogicExceptionOccurred, ServiceWebServeExceptionOccurred
from model.common import Service
from util.structured_logging import log_event
from util.env import env_int, env_str


def register_healthcheck_endpoint(api):

    @api.get("/healthcheck")
    def get_root():
        log_event(HealthChecked(timestamp=datetime.datetime.now().isoformat()))


def launch_uvicorn_server(
    service: Service, 
    before_launching_server: Callable = None,
    wait_for_migrations: bool = True
):

    configure_structured_logging(service)

    if wait_for_migrations:
        MigrationServiceClient.wait_until_ready()

    if before_launching_server:
        try:
            before_launching_server()
        except:
            log_event(ServiceStartupLogicExceptionOccurred(info=traceback.format_exc()))
            raise

    try:
        uvicorn.run(
            app=f'services.{service.value}.service:api',
            factory=True, 

            host=env_str('SERVICE_HOST'), 
            port=env_int('SERVICE_PORT'), 
            log_level="info",

            reload=True,
            reload_dirs=["/application"],
            reload_includes=["*.py"],
            reload_excludes=["*.log"],
            reload_delay=1,
        )
    except:
        log_event(ServiceWebServeExceptionOccurred(info=traceback.format_exc()))
        raise