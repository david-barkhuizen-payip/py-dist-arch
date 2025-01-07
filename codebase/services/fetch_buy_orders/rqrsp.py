from services.create_buy_order.rqrsp import BuyOrderExport
import datetime
from typing import List, Optional

from pydantic import BaseModel
from pydantic.types import uuid4

class BuyOrderPage(BaseModel):
    rows: List[BuyOrderExport]
    last_reference: Optional[str]