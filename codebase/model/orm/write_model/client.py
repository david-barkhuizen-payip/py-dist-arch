from sqlalchemy import Column, Integer, String

from model.orm.write_model.write_model_base import WriteModelBase

class Client(WriteModelBase):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    email = Column(String(254), unique=True, nullable=False)