import datetime
import uuid
from model.common import Currency
from pydantic import BaseModel

class MerchantPosNewCheckoutRequest(BaseModel):
    currency_amt: int
    currency: Currency

class MerchantPosNewCheckoutResponse(BaseModel):
    id: uuid.UUID
    client_id: int
    created_at: datetime.datetime
