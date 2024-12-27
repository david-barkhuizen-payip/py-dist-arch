from pydantic import BaseModel, validator

from services.merchant_pos_new_checkout.rqrsp import MerchantPosCheckoutExport

class TestRequest(BaseModel):
    currency_amt: int

class TestExport(BaseModel):
    merchant_pos_checkout: MerchantPosCheckoutExport    

class TestResponse(BaseModel):
    test: TestExport