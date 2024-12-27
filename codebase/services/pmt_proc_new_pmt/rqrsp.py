import datetime
import uuid
from pydantic import BaseModel

from model.common import Currency

class PaymentProcessorNewCustomerPaymentRequest(BaseModel):
    currency: Currency
    currency_amt: int

class PaymentProcessorCustomerPaymentExport(BaseModel):
    currency: Currency
    currency_amt: int

class PaymentProcessorNewCustomerPaymentResponse(BaseModel):
    payment: PaymentProcessorCustomerPaymentExport