from services.platform_new_pmt.rqrsp import PlatformNewPaymentRequest, PlatformNewPaymentResponse
from util.web import http_post, url_for_endpoint
from model.common import Endpoint
import requests

class PlatformNewPaymentClient:

    def __init__(self, endpoint: Endpoint):
        self.endpoint = endpoint

    def new_payment(self):

        http_rsp = http_post(f'{url_for_endpoint(self.endpoint)}', json=PlatformNewPaymentRequest())

        if http_rsp.status_code != 200:
            raise f'platform new customer payment error: {http_rsp.text}'

        return PlatformNewPaymentResponse.parse_raw(http_rsp.text).payment
    