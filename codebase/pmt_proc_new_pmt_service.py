from util.service_base import launch_uvicorn_server
from model.common import Service

if __name__ == '__main__':
    launch_uvicorn_server(
        service=Service.PMT_PROC_NEW_PMT
    )