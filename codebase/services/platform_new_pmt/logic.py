from typing import Callable, List, Optional
from services.platform_new_pmt.rqrsp import PlatformNewPaymentRequest, PlatformNewPaymentResponse
from sqlalchemy.sql.expression import select
from services.btc_price.client import BtcPriceServiceClient
from sqlalchemy.engine.base import Engine

from sqlalchemy.orm import Session
from model.orm.write_model import Currency
from model.logevent import RequestReceivedLogEvent

write_engine: Optional[Engine] = None
q_publisher: Optional[Callable] = None
btc_price_service: Optional[BtcPriceServiceClient] = None
currencies: List[Currency] = None

def configure_logic(write_engine_: Engine, q_publisher_):
    global write_engine, q_publisher, currencies
    
    write_engine = write_engine_

    with Session(write_engine) as db_session:
        stmt = select(Currency)
        currencies = db_session.execute(stmt).scalars().all()

    q_publisher = q_publisher_

def handle_platform_new_payment_request(client_id: int, rq: PlatformNewPaymentRequest):
    return PlatformNewPaymentResponse()

def rq_received_logevent(client_id, rq):
    return RequestReceivedLogEvent()