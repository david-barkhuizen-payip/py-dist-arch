
from model.common import Service
from services.merchant_pos_new_checkout.client import MerchantPosNewCheckoutClient
from services.merchant_pos_new_checkout.rqrsp import MerchantPosNewCheckoutRequest
from services.trigger.rqrsp import TriggerRequest
from util.env import endpoint_from_env

def random_merchant_pos_new_checkout_request() -> MerchantPosNewCheckoutRequest:
    return MerchantPosNewCheckoutRequest(
        currency='ZAR',
        currency_amt=100
    )

def trigger_merchant_pos_new_checkout(client_id: int, rq: TriggerRequest):

    return MerchantPosNewCheckoutClient(
        endpoint_from_env(Service.MERCHANT_POS_NEW_CHECKOUT)
    ).post(
        random_merchant_pos_new_checkout_request()
    )
