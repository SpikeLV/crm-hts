from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from core.schemas.users import UserCreate, UserRead, UserUpdate
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

@router.get("/{user_id}", response_model=UserRead)
async def get_by_id(
    user_id: int,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> UserRead:
    user = await users_crood.get_by_id(session=session, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

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

@router.put("/{user_id}", response_model=UserRead)
async def update(
    user_id: int,
    user_update: UserUpdate,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> UserRead:
    try:
        user = await users_crood.update(
            session=session,
            user_id=user_id,
            user_update=user_update
        )
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))