import time
from typing import Optional
from util.env import env_float
import os, traceback
from fluent import sender
from model.logevent import LoggingTag
from model.common import Service
from pydantic.main import BaseModel
import inflection

LOGGING_HOST: str = os.environ['LOGGING_HOST']
LOGGING_PORT: int = int(os.environ['LOGGING_PORT'])
SERVICE: Service = None

class ExceptionOccurred(BaseModel):
    _tag = 'exception_occurred'
    msg: str
    stack_trace: Optional[str] = ...

class ConnectedToLogging(BaseModel):
    _tag = 'logging_connected'

class FailedToConnectToLogging(BaseModel):
    _tag = 'failed_to_connect_to_logging'
    host: str
    port: int
    info: str

def log_event(event_model: BaseModel):

    tag = inflection.underscore(type(event_model).__name__)

    print(f'log_event: {LoggingTag.Root.value} - {SERVICE.value}')

    fsender = sender.FluentSender(
        f'{LoggingTag.Root.value}.{SERVICE.value}', 
        host=LOGGING_HOST, 
        port=LOGGING_PORT
    )

    try:
        fsender.emit(tag, event_model.dict())
    finally:
        fsender.close()


def log_exception(msg):
    log_event(ExceptionOccurred(msg=msg, stack_trace=traceback.format_exc()))

def configure_and_test_logging(service_: Service):

    retry_s = env_float('LOGGING_RETRY_S')
    
    global SERVICE
    SERVICE = service_
    
    while True:
        try:
            log_event(ConnectedToLogging())
            print(f'{SERVICE.value} connected to logging')
            break
        except:
            log_event(FailedToConnectToLogging(host=LOGGING_HOST, port=LOGGING_PORT, info=traceback.format_exc()))
            time.sleep(retry_s)
