from typing import Callable, List, Optional
from model.logevent import RequestReceivedLogEvent
from services.iss_bank_new_pmt.client import IssuingBankNewCustomerPaymentClient
from services.pmt_proc_new_pmt.rqrsp import PaymentProcessorCustomerPaymentExport, PaymentProcessorNewCustomerPaymentRequest, PaymentProcessorNewCustomerPaymentResponse
from sqlalchemy.sql.expression import select


from sqlalchemy.engine.base import Engine

from sqlalchemy.orm import Session

from model.orm.write_model import Currency

write_engine: Optional[Engine] = None
q_publisher: Optional[Callable] = None
iss_bank_new_pmt_service: Optional[IssuingBankNewCustomerPaymentClient] = None
currencies: List[Currency] = None

def configure_logic(write_engine_: Engine, iss_bank_new_pmt_service_: IssuingBankNewCustomerPaymentClient):
    global write_engine, iss_bank_new_pmt_service, currencies
    
    write_engine = write_engine_

    with Session(write_engine) as db_session:
        stmt = select(Currency)
        currencies = db_session.execute(stmt).scalars().all()

    iss_bank_new_pmt_service = iss_bank_new_pmt_service_

def handle_payment_processor_new_customer_payment_request(
    client_id: int, 
    rq: PaymentProcessorNewCustomerPaymentRequest
):

    return PaymentProcessorNewCustomerPaymentResponse(
        payment=PaymentProcessorCustomerPaymentExport(
            currency=rq.currency,
            currency_amt=rq.currency_amt
        )
    )

def rq_received_logevent(client_id, rq):
    return RequestReceivedLogEvent(text=str(rq))