from model.common import Endpoint
from services.merchant_pos_new_checkout.rqrsp import MerchantPosNewCheckoutRequest, MerchantPosNewCheckoutResponse
from util.service_client_base import ServiceClientBase

class MerchantPosNewCheckoutClient(ServiceClientBase):

    def __init__(self, endpoint: Endpoint = None):
        super().__init__(endpoint, MerchantPosNewCheckoutRequest, MerchantPosNewCheckoutResponse)