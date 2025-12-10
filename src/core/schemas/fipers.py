from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class FipersBase(BaseModel):
    
    first_name: str
    last_name: str
    ssn: Optional[str] = None
    
    # Non-encrypted fields (less sensitive or required for indexing)
    middle_name: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[date] = None

    height: Optional[int] = None
    weight: Optional[int] = None
    
    phone: Optional[str] = None
    email: Optional[str] = None

    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None

class FipersCreate(FipersBase):
    pass

class FipersUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    ssn: Optional[str] = None
    middle_name: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    
    height: Optional[int] = None
    weight: Optional[int] = None

    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None

class FipersRead(FipersBase):
    id: int