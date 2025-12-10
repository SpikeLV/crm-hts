from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    password: str
    is_active: bool
    is_superuser: bool

class UserCreate(User):
    pass

class UserRead(User):
    id: int