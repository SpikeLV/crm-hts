from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
from sqlalchemy import select

from core.schemas.users import UserCreate, UserUpdate

async def get_all(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.email.asc())
    result = await session.scalars(stmt)
    return result.all()

async def get_by_id(session: AsyncSession, user_id: int) -> Optional[User]:
    stmt = select(User).where(User.id == user_id)
    result = await session.scalars(stmt)
    return result.first()

async def create(session: AsyncSession, user_create: UserCreate) -> User:
    user = User(
        email=user_create.email,
        password=user_create.password,
        is_active=user_create.is_active,
        is_superuser=user_create.is_superuser
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def update(session: AsyncSession, user_id: int, user_update: UserUpdate) -> User:
    user = await get_by_id(session, user_id)
    if not user:
        raise ValueError("User not found")
    
    if user_update.email is not None:
        user.email = user_update.email
    if user_update.password is not None:
        user.password = user_update.password
    if user_update.is_active is not None:
        user.is_active = user_update.is_active
    if user_update.is_superuser is not None:
        user.is_superuser = user_update.is_superuser
    
    await session.commit()
    await session.refresh(user)
    return user