from typing import Optional
from services.btc_price.logic import configure_logic, handle_request, rq_received_logevent
from fastapi import FastAPI

from model.logevent import HealthChecked
from util.coinbase import CoinBaseClient
from util.service_base import register_healthcheck_endpoint
from util.structured_logging import log_event
from util.service import request_handler

api = FastAPI()

def configureApi(coinbase_client: CoinBaseClient):
    configure_logic(coinbase_client)

register_healthcheck_endpoint(api)

@api.get("/buy")
def get_btc_buy_price_quote(currency: str):
    return request_handler(
        'get_btc_buy_price_quote',
        rq_received_logevent,
        handle_request
    )(currency)