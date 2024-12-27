from typing import List, Optional
from model.logevent import RequestReceivedLogEvent
from services.merchant_pos_new_checkout.client import MerchantPosNewCheckoutClient
from services.test_service.rqrsp import TestExport, TestRequest, TestResponse
from sqlalchemy.sql.expression import select
from sqlalchemy.engine.base import Engine

from sqlalchemy.orm import Session

from model.orm.write_model import Currency

write_engine: Optional[Engine] = None
currencies: List[Currency] = None
merchant_pos_new_checkout_service: MerchantPosNewCheckoutClient = None 

def configure_logic(
    write_engine_: Engine, 
    merchant_pos_new_checkout_service_: MerchantPosNewCheckoutClient, 
):
    global write_engine, merchant_pos_new_checkout_service
    
    write_engine = write_engine_

    with Session(write_engine) as db_session:
        stmt = select(Currency)
        _ = db_session.execute(stmt).scalars().all()

    merchant_pos_new_checkout_service = merchant_pos_new_checkout_service_

def handle_new_test_request(client_id: int, rq: TestRequest):

    return TestResponse(
        test=TestExport(    
        )
    )

def rq_received_logevent(client_id, rq):
    return RequestReceivedLogEvent()