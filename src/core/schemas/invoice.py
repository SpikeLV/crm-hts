from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime
from typing import Optional, Union

class InvoiceBase(BaseModel):
    invoice_number: str
    invoice_date: datetime
    invoice_amount: Optional[float] = None
    invoice_payment_date: Optional[datetime] = None
    invoice_description: Optional[str] = None
    project_id: int
    jupers_id: int


class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(InvoiceBase):
    invoice_number: Optional[str] = None
    invoice_date: Optional[datetime] = None
    invoice_amount: Optional[float] = None
    invoice_payment_date: Optional[datetime] = None
    invoice_description: Optional[str] = None
    project_id: Optional[int] = None
    jupers_id: Optional[int] = None

class InvoiceRead(InvoiceBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
