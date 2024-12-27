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

def handle_test_request(client_id: int, rq: TestRequest):

    rsp = merchant_pos_new_checkout_service.invoke(
        currency_amt=rq.currency_amt,
        currency=rq.currency,    
    )


    print('-'*20)
    print(rsp)
    print('-'*20)

    return TestResponse(
        test=TestExport(
            merchant_pos_checkout=rsp.checkout
        )
    )

def rq_received_logevent(client_id, rq):
    return RequestReceivedLogEvent(text=str(rq))