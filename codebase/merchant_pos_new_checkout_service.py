from model.common import Service
from util.service_base import launch_uvicorn_server

if __name__ == '__main__':
    launch_uvicorn_server(
        service=Service.MERCHANT_POS_NEW_CHECKOUT,
    )