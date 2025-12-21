from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PaymentBase(BaseModel):
    amount: float
    date: datetime
    description: Optional[str] = None
    invoice_id: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(PaymentBase):
    amount: Optional[float] = None
    date: Optional[datetime] = None
    description: Optional[str] = None
    invoice_id: Optional[int] = None


class PaymentRead(PaymentBase):
    model_config = ConfigDict(from_attributes=True)
    
    created_at: datetime
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

