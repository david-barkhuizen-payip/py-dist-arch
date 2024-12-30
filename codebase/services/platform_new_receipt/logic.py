from model.logevent import RequestReceivedLogEvent
from services.platform_new_receipt.rqrsp import PlatformNewReceiptRequest, PlatformNewReceiptResponse

def handle_platform_new_receipt_request(client_id: int, rq: PlatformNewReceiptRequest):
    return PlatformNewReceiptResponse()

def rq_received_logevent(client_id, rq):
    return RequestReceivedLogEvent(text=str(rq))