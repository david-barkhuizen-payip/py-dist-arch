from services.platform_new_pmt.rqrsp import PlatformNewPaymentRequest, PlatformNewPaymentResponse
from util.service_client_base import ServiceClientBase
from model.common import Endpoint

class PlatformNewPaymentClient(ServiceClientBase):

    def __init__(self, endpoint: Endpoint):
        super().__init__(endpoint, PlatformNewPaymentRequest, PlatformNewPaymentResponse)
