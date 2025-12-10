from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class JupersBase(BaseModel):
    name: str
    reg_nr: str
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    notes: Optional[str] = None

class JupersCreate(JupersBase):
    pass

class JupersUpdate(JupersBase):
    pass

class JupersRead(JupersBase):
    id: int