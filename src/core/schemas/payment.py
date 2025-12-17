from datetime import date
from typing import Optional

from pydantic import BaseModel


class PaymentBase(BaseModel):
    amount: float
    date: date
    description: str
    invoice_id: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(PaymentBase):
    amount: Optional[float] = None
    date: Optional[date] = None
    description: Optional[str] = None
    invoice_id: Optional[int] = None


class PaymentRead(PaymentBase):
    id: int

