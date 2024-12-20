import datetime
from typing import Callable, List, Optional
import uuid
from model.logevent import RequestReceivedLogEvent
from services.iss_bank_new_pmt.rqrsp import IssuingBankPaymentExport, IssuingBankNewPaymentRequest, IssuingBankNewPaymentResponse
from services.platform_new_pmt.client import PlatformNewPaymentClient
from sqlalchemy.sql.expression import select


from sqlalchemy.engine.base import Engine

from sqlalchemy.orm import Session

from model.orm.write_model import Currency

write_engine: Optional[Engine] = None
q_publisher: Optional[Callable] = None
platform_new_pmt_service: Optional[PlatformNewPaymentClient] = None
currencies: List[Currency] = None

def configure_logic(write_engine_: Engine, platform_new_pmt_service_: PlatformNewPaymentClient):
    global write_engine, platform_new_pmt_service, currencies
    
    write_engine = write_engine_

    with Session(write_engine) as db_session:
        stmt = select(Currency)
        currencies = db_session.execute(stmt).scalars().all()

    platform_new_pmt_service = platform_new_pmt_service_

def handle_issuing_bank_new_payment_request(client_id: int, rq: IssuingBankNewPaymentRequest):

    return IssuingBankNewPaymentResponse(
        payment=IssuingBankPaymentExport()
    )

def rq_received_logevent(client_id, rq):
    return RequestReceivedLogEvent()