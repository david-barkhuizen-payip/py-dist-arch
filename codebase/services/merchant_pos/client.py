from services.merchant_pos.rqrsp import MerchantNewCheckoutRequest, MerchantNewCheckoutResponse
from util.web import url_for_endpoint
from model.common import Endpoint
import requests

class MerchantCheckoutClient:

    def __init__(self, endpoint: Endpoint):
        self.endpoint = endpoint

    def new_checkout(self):

        url = f'{url_for_endpoint(self.endpoint)}'
        http_rsp = requests.post(url, MerchantNewCheckoutRequest())

        if http_rsp.status_code != 200:
            raise f'platform new customer payment error: {http_rsp.text}'

        return MerchantNewCheckoutResponse.parse_raw(http_rsp.text).payment
    