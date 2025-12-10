from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    email: str
    password: str
    is_active: bool
    is_superuser: bool

class UserCreate(User):
    pass

class UserUpdate(User):
    email: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

class UserRead(User):
    id: int
    email: str
    is_active: bool
    is_superuser: bool