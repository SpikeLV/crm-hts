from pydantic import BaseModel, ConfigDict, field_validator
from datetime import date
from typing import Optional, Union

class InvoiceBase(BaseModel):

    invoice_number: str
    invoice_date: date
    invoice_amount: float
    invoice_payment_date:  Optional[date] = None
    invoice_payed_amount:  Optional[float] = None
    invoice_payed_date:  Optional[date] = None
    invoice_description:  Optional[str] = None
    project_id: int
    jupers_id: int