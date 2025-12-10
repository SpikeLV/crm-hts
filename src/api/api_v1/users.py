from typing import Annotated
from fastapi import APIRouter, Depends
from core.schemas.users import UserCreate, UserRead
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from .crud import users as users_crood

router = APIRouter(tags=["Users"])

@router.get("/", response_model=list[UserRead])
async def get_all(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> list[UserRead]:
    users = await users_crood.get_all(session=session)
    return users

@router.post("/", response_model=UserRead)
async def create(
    user_create: UserCreate, 
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> UserRead:
    user = await users_crood.create(
        session=session, 
        user_create=user_create
    )
    return user