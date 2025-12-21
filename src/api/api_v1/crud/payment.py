from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models.payment import Payment as PaymentModel
from core.schemas.payment import PaymentCreate, PaymentUpdate

async def get_all(session: AsyncSession) -> Sequence[PaymentModel]:
    stmt = select(PaymentModel).order_by(PaymentModel.date.asc())
    result = await session.scalars(stmt)
    return result.all()

async def get_by_id(session: AsyncSession, payment_id: int) -> Optional[PaymentModel]:
    stmt = select(PaymentModel).where(PaymentModel.id == payment_id)
    result = await session.scalar(stmt)
    return result

async def create(session: AsyncSession, payment_create: PaymentCreate) -> PaymentModel:
    try:
        payment = PaymentModel(
            amount=payment_create.amount,
            date=payment_create.date,
            description=payment_create.description,
            invoice_id=payment_create.invoice_id,
        )
        session.add(payment)
        await session.commit()
        await session.refresh(payment)
        return payment

    except Exception as e:
        await session.rollback()
        raise

async def update(session: AsyncSession, payment_id: int, payment_update: PaymentUpdate) -> Optional[PaymentModel]:
    payment = await get_by_id(session, payment_id)
    if not payment:
        return None
    
    update_data = payment_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(payment, key, value)
    
    await session.commit()
    await session.refresh(payment)
    return payment

async def delete(session: AsyncSession, payment_id: int) -> Optional[PaymentModel]:
    payment = await get_by_id(session, payment_id)
    if not payment:
        return None
    
    await session.delete(payment)
    await session.commit()
    return payment