from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models.fipers import Fipers as FipersModel
from core.schemas.fipers import FipersCreate, FipersUpdate

async def get_all(session: AsyncSession) -> Sequence[FipersModel]:
    stmt = select(FipersModel).order_by(FipersModel.first_name.asc(), FipersModel.last_name.asc())
    result = await session.scalars(stmt)
    return result.all()

async def get_by_id(session: AsyncSession, fiper_id: int) -> Optional[FipersModel]:
    stmt = select(FipersModel).where(FipersModel.id == fiper_id)
    result = await session.scalar(stmt)
    return result

async def create(session: AsyncSession, fiper_create: FipersCreate) -> FipersModel:
    fiper = FipersModel(
        first_name=fiper_create.first_name,
        last_name=fiper_create.last_name,
        ssn=fiper_create.ssn,
        middle_name=fiper_create.middle_name,
        gender=fiper_create.gender,
        birth_date=fiper_create.birth_date,
        phone=fiper_create.phone,
        email=fiper_create.email,
        height=fiper_create.height,
        weight=fiper_create.weight,
        address=fiper_create.address,
        city=fiper_create.city,
        state=fiper_create.state,
        zip=fiper_create.zip,
        country=fiper_create.country,
    )
    session.add(fiper)
    await session.commit()
    await session.refresh(fiper)
    return fiper

async def update(session: AsyncSession, fiper_id: int, fiper_update: FipersUpdate) -> Optional[FipersModel]:
    fiper = await get_by_id(session, fiper_id)
    if not fiper:
        return None
    
    update_data = fiper_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(fiper, key, value)
    
    await session.commit()
    await session.refresh(fiper)
    return fiper