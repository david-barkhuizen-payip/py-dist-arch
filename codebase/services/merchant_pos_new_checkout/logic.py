import datetime
from typing import Callable, List, Optional
import uuid
from model.logevent import RequestReceivedLogEvent
from services.merchant_pos_new_checkout.rqrsp import MerchantCheckoutExport, MerchantNewCheckoutRequest, MerchantNewCheckoutResponse
from services.platform_new_receipt.client import PlatformNewReceiptClient
from services.pmt_proc_new_pmt.client import PaymentProcessorNewPaymentClient
from sqlalchemy.sql.expression import select
from sqlalchemy.engine.base import Engine

from sqlalchemy.orm import Session

from model.orm.write_model import Currency

write_engine: Optional[Engine] = None
currencies: List[Currency] = None
pmt_proc_new_pmt_service: PaymentProcessorNewPaymentClient = None 
platform_new_receipt_service: PlatformNewReceiptClient = None

def configure_logic(
    write_engine_: Engine, 
    pmt_proc_new_pmt_service_: PaymentProcessorNewPaymentClient, 
    platform_new_receipt_service_: PlatformNewReceiptClient
):
    global write_engine, pmt_proc_new_pmt_service, platform_new_receipt_service, currencies
    
    write_engine = write_engine_

    with Session(write_engine) as db_session:
        stmt = select(Currency)
        currencies = db_session.execute(stmt).scalars().all()

    pmt_proc_new_pmt_service = pmt_proc_new_pmt_service_
    platform_new_receipt_service = platform_new_receipt_service_

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