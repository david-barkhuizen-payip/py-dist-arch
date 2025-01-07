from typing import Optional
from pydantic import BaseModel

class MerchantPosNewCheckoutRequestLine(BaseModel):

    sku_id: int
    sku_count: int
    currency_amount: int

class MerchantPosNewCheckoutRequest(BaseModel):

    client_id: Optional[int] = None    

    lines: list[MerchantPosNewCheckoutRequestLine]

    currency: str

    total_amount_before_tax: int
    sales_tax_amount: int
    total_amount_after_tax: int

class MerchantPosNewCheckoutResponse(BaseModel):
    rq: MerchantPosNewCheckoutRequest
