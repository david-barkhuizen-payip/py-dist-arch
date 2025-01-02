from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DECIMAL

from model.orm.write_model.write_model_base import WriteModelBase

# Merchant
# - id
# - name
# - URL

# IssuingBank
# - id
# - name
# - URL

# Transaction
# - id
# - timestamp
# - merchant_id
# - issuing_bank_id
# - total
# - currency
# - reference