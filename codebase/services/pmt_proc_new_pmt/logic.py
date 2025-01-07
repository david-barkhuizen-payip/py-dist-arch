from model.common import Service
from model.logevent import RequestReceivedLogEvent
from services.iss_bank_new_pmt.client import IssuingBankNewCustomerPaymentClient
from services.pmt_proc_new_pmt.rqrsp import PaymentProcessorCustomerPaymentExport, PaymentProcessorNewCustomerPaymentRequest, PaymentProcessorNewCustomerPaymentResponse
from util.env import endpoint_from_env


def handle_payment_processor_new_customer_payment_request(
    client_id: int, 
    rq: PaymentProcessorNewCustomerPaymentRequest
):

    iss_bank_new_pmt_service = IssuingBankNewCustomerPaymentClient(
        endpoint_from_env(Service.ISS_BANK_NEW_PMT)
    )

    return PaymentProcessorNewCustomerPaymentResponse(
        payment=PaymentProcessorCustomerPaymentExport(
            currency=rq.currency,
            currency_amt=rq.currency_amt
        )
    )