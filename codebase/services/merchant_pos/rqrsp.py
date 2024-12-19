import datetime
import uuid
from model.common import SUPPORTED_CURRENCIES
from pydantic import BaseModel, validator

class MerchantNewCheckoutRequest(BaseModel):
    pass

class MerchantCheckoutExport(BaseModel):
    id: uuid.UUID
    created_at: datetime.datetime

class MerchantNewCheckoutResponse(BaseModel):
    checkout: MerchantCheckoutExport