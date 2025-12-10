from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class JupersBase(BaseModel):
    name:str
    reg_nr:str
    type:Optional[str] = None
    address:Optional[str] = None
    city:Optional[str] = None
    state:Optional[str] = None
    zip:Optional[str] = None
    country:Optional[str] = None
    phone:Optional[str] = None
    email:Optional[str] = None
    website:Optional[str] = None
    notes:Optional[str] = None

class JupersCreate(JupersBase):
    pass

class JupersUpdate(JupersBase):
    pass

class JupersRead(JupersBase):
    id: int