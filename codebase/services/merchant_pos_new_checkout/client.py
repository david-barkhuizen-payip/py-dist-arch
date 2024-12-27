


from model.common import Endpoint
from services.merchant_pos_new_checkout.rqrsp import MerchantNewCheckoutRequest, MerchantNewCheckoutResponse
from util.service_client_base import ServiceClientBase


class MerchantPosNewCheckoutClient(ServiceClientBase):

    def __init__(self, endpoint: Endpoint):
        super().__init__(endpoint, MerchantNewCheckoutRequest, MerchantNewCheckoutResponse)