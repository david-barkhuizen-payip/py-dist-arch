import datetime
import uuid
from model.common import SUPPORTED_CURRENCIES, Currency
from pydantic import BaseModel, validator

class MerchantNewCheckoutRequest(BaseModel):
    currency_amt: int
    currency: Currency

class MerchantPosCheckoutExport(BaseModel):
    id: uuid.UUID
    client_id: int
    created_at: datetime.datetime

class MerchantNewCheckoutResponse(BaseModel):
    checkout: MerchantPosCheckoutExport