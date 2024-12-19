import datetime
import uuid
from model.common import SUPPORTED_CURRENCIES
from pydantic import BaseModel, validator

class PlatformNewPaymentRequest(BaseModel):
    pass

class PlatformPaymentExport(BaseModel):
    id: uuid.UUID
    created_at: datetime.datetime
    pass

class PlatformNewPaymentResponse(BaseModel):
    payment: PlatformPaymentExport