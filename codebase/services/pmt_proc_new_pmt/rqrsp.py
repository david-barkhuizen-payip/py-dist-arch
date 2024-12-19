import datetime
import uuid
from pydantic import BaseModel

class PaymentProcessorNewCustomerPaymentRequest(BaseModel):
    pass

class PaymentProcessorCustomerPaymentExport(BaseModel):
    id: uuid.UUID
    created_at: datetime.datetime

class PaymentProcessorNewCustomerPaymentResponse(BaseModel):
    payment: PaymentProcessorCustomerPaymentExport
    successful: bool