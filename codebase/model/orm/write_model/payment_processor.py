from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DECIMAL

from model.orm.write_model.write_model_base import WriteModelBase

class PaymentProcessorNewPayment(WriteModelBase):
    __tablename__ = 'payment_processor_new_payment'

    id = Column(Integer, primary_key=True)
    currency = Column(String(3), nullable=False)
    currency_amt = Column(DECIMAL(precision=12, scale=2), nullable=False)