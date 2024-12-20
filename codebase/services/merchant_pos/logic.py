import datetime
from typing import Callable, List, Optional
import uuid
from model.logevent import RequestReceivedLogEvent
from services.merchant_pos.rqrsp import MerchantCheckoutExport, MerchantNewCheckoutRequest, MerchantNewCheckoutResponse
from sqlalchemy.sql.expression import select
from services.btc_price.client import BtcPriceServiceClient
from decimal import Decimal
import traceback
from sqlalchemy.engine.base import Engine

from sqlalchemy.orm import Session

from model.orm.write_model import Currency

write_engine: Optional[Engine] = None
q_publisher: Optional[Callable] = None
btc_price_service: Optional[BtcPriceServiceClient] = None
currencies: List[Currency] = None

def configure_logic(write_engine_: Engine, q_publisher_, btc_price_service_: BtcPriceServiceClient):
    global write_engine, q_publisher, btc_price_service, currencies
    
    write_engine = write_engine_

    with Session(write_engine) as db_session:
        stmt = select(Currency)
        currencies = db_session.execute(stmt).scalars().all()

    q_publisher = q_publisher_
    btc_price_service = btc_price_service_

def handle_merchant_new_checkout_request(client_id: int, rq: MerchantNewCheckoutRequest):

    return MerchantNewCheckoutResponse(
        checkout=MerchantCheckoutExport(
            id = uuid.UUID4(),
            created_at=datetime.datetime.now(),
            client_id=client_id
        )
    )

def rq_received_logevent(client_id, rq):
    return RequestReceivedLogEvent()