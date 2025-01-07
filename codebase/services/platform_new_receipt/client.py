from services.platform_new_receipt.rqrsp import PlatformNewReceiptRequest, PlatformNewReceiptResponse
from util.service_client_base import ServiceClientBase
from model.common import Endpoint

class PlatformNewReceiptClient(ServiceClientBase):

    def __init__(self, endpoint: Endpoint):
        super().__init__(endpoint, PlatformNewReceiptRequest, PlatformNewReceiptResponse)
