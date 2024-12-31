from services.iss_bank_new_pmt.rqrsp import IssuingBankNewPaymentRequest, IssuingBankNewPaymentResponse
from model.common import Endpoint
from util.service_client_base import ServiceClientBase

class IssuingBankNewCustomerPaymentClient(ServiceClientBase):

    def __init__(self, endpoint: Endpoint):
        super().__init__(endpoint, IssuingBankNewPaymentRequest, IssuingBankNewPaymentResponse)
