from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    email: str
    password: str
    is_active: bool
    is_superuser: bool

class UserCreate(BaseModel):
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False

class UserUpdate(UserBase):
    email: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int