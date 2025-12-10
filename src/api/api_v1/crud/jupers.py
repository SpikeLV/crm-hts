from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models.jupers import Jupers as JupersModel
from core.schemas.jupers import JupersCreate, JupersUpdate

async def get_all(session: AsyncSession) -> Sequence[JupersModel]:
    stmt = select(JupersModel).order_by(JupersModel.name.asc())
    result = await session.scalars(stmt)
    return result.all()

async def get_by_id(session: AsyncSession, jupers_id: int) -> Optional[JupersModel]:
    stmt = select(JupersModel).where(JupersModel.id == jupers_id)
    result = await session.scalar(stmt)
    return result

async def create(session: AsyncSession, jupers_create: JupersCreate) -> JupersModel:
    try:
        jupers = JupersModel(
            name=jupers_create.name,
            reg_nr=jupers_create.reg_nr,
            address=jupers_create.address if jupers_create.address else None,
            phone=jupers_create.phone if jupers_create.phone else None,
            email=jupers_create.email if jupers_create.email else None,
            notes=jupers_create.notes if jupers_create.notes else None,
        )
        session.add(jupers)
        await session.commit()
        await session.refresh(jupers)
        return jupers
    except Exception as e:
        await session.rollback()
        raise

async def update(session: AsyncSession, jupers_id: int, jupers_update: JupersUpdate) -> Optional[JupersModel]:
    jupers = await get_by_id(session, jupers_id)
    if not jupers:
        return None
    
    update_data = jupers_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(jupers, key, value)
    
    await session.commit()
    await session.refresh(jupers)
    return jupers