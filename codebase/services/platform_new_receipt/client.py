from services.platform_new_receipt.rqrsp import PlatformNewReceiptRequest, PlatformNewReceiptResponse
from util.web import url_for_endpoint
from model.common import Currency, Endpoint
import requests

class PlatformNewReceiptClient:

    def __init__(self, endpoint: Endpoint):
        self.endpoint = endpoint

    def new_receipt(self, currency: Currency, amount: int):

        url = f'{url_for_endpoint(self.endpoint)}'
        http_rsp = requests.post(url, PlatformNewReceiptRequest(currency=currency, amount=amount))

        if http_rsp.status_code != 200:
            raise f'new customer payment error: {http_rsp.text}'

        return PlatformNewReceiptResponse.parse_raw(http_rsp.text).receipt
    