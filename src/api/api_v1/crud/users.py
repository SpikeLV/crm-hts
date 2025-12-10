from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
from sqlalchemy import select

from core.schemas.users import UserCreate

async def get_all(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.email.asc())
    result = await session.scalars(stmt)
    return result.all()

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