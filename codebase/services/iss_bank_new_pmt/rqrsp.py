import datetime
import uuid
from model.common import SUPPORTED_CURRENCIES
from pydantic import BaseModel, validator

class IssuingBankNewCustomerPaymentRequest(BaseModel):
    currency: str
    amount: int

    @validator('currency')
    def currency_must_be_valid(cls, v):
        if v not in SUPPORTED_CURRENCIES:
            raise ValueError(f'invalid currency. valid currencies: {", ".join(SUPPORTED_CURRENCIES)}')
        return v

    @validator('amount')
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('invalid amount. amount must be positive.')
        return v


class IssuingBankCustomerPaymentExport(BaseModel):
    id: uuid.UUID
    created_at: datetime.datetime
    currency: str
    currency_amount: int
    successful: bool

class IssuingBankNewCustomerPaymentResponse(BaseModel):
    payment: IssuingBankCustomerPaymentExport