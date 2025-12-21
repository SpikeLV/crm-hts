from pydantic import BaseModel, ConfigDict, field_validator
from datetime import date
from typing import Optional, Union

class FipersBase(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    first_name: str
    last_name: str
    ssn: Optional[str] = None
    
    # Non-encrypted fields (less sensitive or required for indexing)
    gender: Optional[str] = None
    birth_date: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    
    @field_validator('birth_date', mode='before')
    @classmethod
    def parse_birth_date(cls, v):
        if v is None or v == '':
            return None
        return v

class FipersCreate(FipersBase):
    pass

class FipersUpdate(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    ssn: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    
    @field_validator('birth_date', mode='before')
    @classmethod
    def parse_birth_date(cls, v):
        if v is None or v == '':
            return None
        return v

class FipersRead(FipersBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int