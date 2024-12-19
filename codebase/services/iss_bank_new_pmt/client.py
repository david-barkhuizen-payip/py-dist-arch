from services.iss_bank_new_pmt.rqrsp import IssuingBankNewCustomerPaymentRequest, IssuingBankNewCustomerPaymentResponse
from util.web import url_for_endpoint
from model.common import Currency, Endpoint
import requests

class IssuingBankNewCustomerPaymentClient:

    def __init__(self, endpoint: Endpoint):
        self.endpoint = endpoint

    def new_customer_payment(self, currency: Currency, amount: int):

        url = f'{url_for_endpoint(self.endpoint)}'
        http_rsp = requests.post(url, IssuingBankNewCustomerPaymentRequest(currency=currency, amount=amount))

        if http_rsp.status_code != 200:
            raise f'new customer payment error: {http_rsp.text}'

        return IssuingBankNewCustomerPaymentResponse.parse_raw(http_rsp.text).payment
    