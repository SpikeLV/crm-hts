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
    try:
        # Convert empty strings to None for optional fields
        ssn = fiper_create.ssn if fiper_create.ssn and fiper_create.ssn.strip() else None
        
        fiper = FipersModel(
            first_name=fiper_create.first_name,
            last_name=fiper_create.last_name,
            ssn=ssn,
            gender=fiper_create.gender if fiper_create.gender else None,
            birth_date=fiper_create.birth_date,
            phone=fiper_create.phone if fiper_create.phone else None,
            email=fiper_create.email if fiper_create.email else None,
            address=fiper_create.address if fiper_create.address else None,
        )
        session.add(fiper)
        await session.commit()
        await session.refresh(fiper)
        return fiper
    except Exception as e:
        await session.rollback()
        raise

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