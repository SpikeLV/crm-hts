from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int