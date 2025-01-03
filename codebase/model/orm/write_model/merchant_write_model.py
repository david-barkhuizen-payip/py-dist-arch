from model.common import BTC_RATE_PRECISION, BTC_RATE_SCALE
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from model.orm.write_model.write_model_base import WriteModelBase

class Client(WriteModelBase):
    __tablename__ = 'merchant_client'

    id = Column(Integer, primary_key=True)
    platform_id = Column(UUID(as_uuid=True), nullable=False)
    

class PaymentProcessor(WriteModelBase):
    __tablename__ = 'merchant_payment_processor'

    id = Column(Integer, primary_key=True)
    name = Column(String(254), unique=True, nullable=False)
    vostro_id =Column(UUID(as_uuid=True), nullable=False)

class SKU(WriteModelBase):
    __tablename__ = 'merchant_sku'

    id = Column(Integer, primary_key=True)
    name = Column(String(254), nullable=False)
    price = Column(Integer, nullable=False)


class Transaction(WriteModelBase):
    __tablename__ = 'merchant_transaction'
    
    id = Column(Integer, primary_key=True)
    client = Column(ForeignKey('merchant_client.id'), nullable=True)

    timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now()) 
    
    total_before_tax = Column(Integer())
    sales_tax = Column(Integer())
    total_after_tax = Column(Integer())

class TransactionLine(WriteModelBase):
    __tablename__ = 'merchant_transaction_line'

    id = Column(Integer, primary_key=True)
    transaction = Column(ForeignKey('merchant_transaction.id'), nullable=False)

    sku = Column(ForeignKey('merchant_sku.id'), nullable=False)
    unit_count = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)

class TransactionPayment(WriteModelBase):
    __tablename__ = 'merchant_transaction_payment'

    id = Column(Integer, primary_key=True)
    transaction = Column(ForeignKey('merchant_transaction.id'), nullable=False)
    
    currency = Column(String(3), nullable=False)
    currency_amount = Column(Integer, nullable=False)

    payment_processor = Column(ForeignKey('merchant_payment_processor.id'), nullable=False)
    payment_processor_reference = Column(String(254), nullable=False)

class TransactionReceipt(WriteModelBase):
    __tablename__ = 'merchant_transaction_receipt'

    id = Column(Integer, primary_key=True)
    transaction = Column(ForeignKey('merchant_transaction.id'), nullable=False)
    