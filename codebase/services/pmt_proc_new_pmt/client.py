
from services.pmt_proc_new_pmt.rqrsp import PaymentProcessorNewCustomerPaymentRequest, PaymentProcessorNewCustomerPaymentResponse
from util.web import url_for_endpoint
from model.common import Endpoint
import requests

class PaymentProcessorNewCustomerPaymentClient:

    def __init__(self, endpoint: Endpoint):
        self.endpoint = endpoint

    def new_customer_payment(self):

        url = f'{url_for_endpoint(self.endpoint)}'
        http_rsp = requests.post(url, PaymentProcessorNewCustomerPaymentRequest())

        if http_rsp.status_code != 200:
            raise f'new customer payment error: {http_rsp.text}'

        return PaymentProcessorNewCustomerPaymentResponse.parse_raw(http_rsp.text).payment

