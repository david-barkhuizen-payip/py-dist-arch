from services.merchant_pos_new_checkout.rqrsp import MerchantNewCheckoutRequest, MerchantNewCheckoutResponse
from util.web import url_for_endpoint
from model.common import Endpoint
import requests

class MerchantPosNewCheckoutClient:

    def __init__(self, endpoint: Endpoint):
        self.endpoint = endpoint

    def new_checkout(self, currency_amt: int) -> MerchantNewCheckoutResponse:

        url = f'{url_for_endpoint(self.endpoint)}'

        rq = MerchantNewCheckoutRequest(
            currency_amt=currency_amt
        )

        http_rsp = requests.post(url, json=rq.dict())

        if http_rsp.status_code != 200:
            raise Exception(f'platform new customer payment error: {http_rsp}')

        return MerchantNewCheckoutResponse.parse_raw(http_rsp.text)
    