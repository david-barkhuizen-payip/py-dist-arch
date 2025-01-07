
import math
import random
from model.common import Service
from services.merchant_pos_new_checkout.client import MerchantPosNewCheckoutClient
from services.merchant_pos_new_checkout.rqrsp import MerchantPosNewCheckoutRequest, MerchantPosNewCheckoutRequestLine
from services.trigger.rqrsp import TriggerRequest
from util.db import get_tested_database_engine
from util.env import database_endpoint_from_env, endpoint_from_env

from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select


from model.orm.write_model.merchant_write_model import SKU, Currency
from util.service_config_base import ServiceConfig

def random_merchant_pos_new_checkout_request(
    write_model_db_engine: Engine,
    max_count_per_sku = 3,
    sales_tax_percent = 14.0
) -> MerchantPosNewCheckoutRequest:
    
    currencies = None
    skus = None

    # Example query
    #user = session.query(User).filter(User.email == "john.doe@example.com").first()

    with Session(write_model_db_engine) as session:

        currencies = session.query(Currency).all()
        print(currencies)

        skus = session.query(SKU).all()
        print(skus)

    lines = []

    for sku in random.sample(skus, random.randint(1, len(skus))):

        sku_count = random.randint(1, max_count_per_sku)

        lines.append(
            MerchantPosNewCheckoutRequestLine(
                sku_id = sku.id,
                sku_count = sku_count,
                currency_amount = sku.price * sku_count
            )
        )

    currency = random.sample(currencies, 1)[0] 

    total_amount_before_tax = sum([x.currency_amount for x in lines])
    sales_tax_amount = round(total_amount_before_tax * sales_tax_percent / 100.0)
    total_amount_after_tax = total_amount_before_tax + sales_tax_amount 

    return MerchantPosNewCheckoutRequest(
        client_id = None,    
        lines = lines,
        currency = currency.iso3,
        total_amount_before_tax = total_amount_before_tax,
        sales_tax_amount = sales_tax_amount,
        total_amount_after_tax = total_amount_after_tax,
    )

def handle_trigger_merchant_pos_new_checkout_request(config: ServiceConfig, rq: TriggerRequest):

    merchant_pos_checkout_rq =  random_merchant_pos_new_checkout_request(
        write_model_db_engine=config.write_model_db_engine()
    )

    return MerchantPosNewCheckoutClient(
        endpoint_from_env(Service.MERCHANT_POS_NEW_CHECKOUT)
    ).post(merchant_pos_checkout_rq)
