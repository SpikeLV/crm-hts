from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str
    password: str
    is_active: bool
    is_superuser: bool


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None


class UserRead(BaseModel):
    id: int
    email: str
    is_active: bool
    is_superuser: bool