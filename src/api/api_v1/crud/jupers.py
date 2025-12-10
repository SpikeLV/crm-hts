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
    jupers = JupersModel(
        name=jupers_create.name,
        reg_nr=jupers_create.reg_nr,
        type=jupers_create.type,
        address=jupers_create.address,
        phone=jupers_create.phone,
        email=jupers_create.email,
        notes=jupers_create.notes,
    )
    session.add(jupers)
    await session.commit()
    await session.refresh(jupers)
    return jupers

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