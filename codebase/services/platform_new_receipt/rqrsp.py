import datetime
import uuid
from model.common import SUPPORTED_CURRENCIES
from pydantic import BaseModel, validator

class PlatformNewReceiptRequest(BaseModel):
    pass

class PlatformReceiptExport(BaseModel):
    id: uuid.UUID
    created_at: datetime.datetime
    pass

class PlatformNewReceiptResponse(BaseModel):
    receipt: PlatformReceiptExport