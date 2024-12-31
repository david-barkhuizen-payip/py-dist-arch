import datetime
import uuid
from model.common import Currency
from pydantic import BaseModel

class MerchantNewCheckoutRequest(BaseModel):
    currency_amt: int
    currency: Currency

class MerchantPosCheckoutExport(BaseModel):
    id: uuid.UUID
    client_id: int
    created_at: datetime.datetime

class MerchantNewCheckoutResponse(BaseModel):
    checkout: MerchantPosCheckoutExport