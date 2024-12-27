
from services.pmt_proc_new_pmt.rqrsp import PaymentProcessorNewCustomerPaymentRequest, PaymentProcessorNewCustomerPaymentResponse
from util.service_client_base import ServiceClientBase
from util.web import url_for_endpoint
from model.common import Endpoint


class PaymentProcessorNewPaymentClient(ServiceClientBase):

    def __init__(self, endpoint: Endpoint):
        super().__init__(endpoint, PaymentProcessorNewCustomerPaymentRequest, PaymentProcessorNewCustomerPaymentResponse)