from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    email: str
    is_active: bool
    is_superuser: bool