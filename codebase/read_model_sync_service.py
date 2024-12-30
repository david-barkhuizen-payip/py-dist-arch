from services.read_model_sync.logic import before_launching_rest_server
from util.service_base import launch_uvicorn_server
from model.common import Service

if __name__ == '__main__':

    launch_uvicorn_server(
        service=Service.READ_MODEL_SYNC,
        before_launching_rest_server=before_launching_rest_server
    )