from services.merchant_pos_callback.rqrsp import MerchantPosCallbackRequest, MerchantPosCallbackResponse

def handle_merchant_pos_callback_request(
    client_id: int, 
    rq: MerchantPosCallbackRequest
):
    return MerchantPosCallbackResponse()