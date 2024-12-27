import sys, traceback
from typing import Callable, Optional
from dataclasses import dataclass

import uvicorn

from util.events import configure_and_test_logging
from model.logevent import ServiceConfigurationExceptionOccurred, ServiceRunLogicExceptionOccurred, ServiceShutDown, ServiceWebServeExceptionOccurred
from model.common import Service
from util.events import log_event
from util.env import env_int, env_str

from dataclasses import dataclass

def launch_uvicorn_server(
    service: Service, 
    before_launching_server: Callable = None
):

    configure_and_test_logging(service)

    host: str
    port: int

    try:
        host=env_str('SERVICE_HOST')
        port=env_int('SERVICE_PORT')
    except:
        log_event(ServiceConfigurationExceptionOccurred(info=traceback.format_exc()))
        raise

    if before_launching_server:
        try:
            before_launching_server()
        except:
            log_event(ServiceRunLogicExceptionOccurred(info=traceback.format_exc()))
            raise

    try:
        uvicorn.run(
            app=f'services.{service.value}.service:api',
            factory=True, 

            host=host, 
            port=port, 
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