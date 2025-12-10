from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models.invoice import Invoice as InvoiceModel
from core.schemas.invoice import InvoiceCreate, InvoiceUpdate

async def get_all(session: AsyncSession) -> Sequence[InvoiceModel]:
    stmt = select(InvoiceModel).order_by(InvoiceModel.invoice_number.asc())
    result = await session.scalars(stmt)
    return result.all()

async def get_by_id(session: AsyncSession, invoice_id: int) -> Optional[InvoiceModel]:
    stmt = select(InvoiceModel).where(InvoiceModel.id == invoice_id)
    result = await session.scalar(stmt)
    return result

async def create(session: AsyncSession, invoice_create: InvoiceCreate) -> InvoiceModel:
    try:
        invoice = InvoiceModel(
            invoice_number=invoice_create.invoice_number,
            invoice_date=invoice_create.invoice_date,
            invoice_amount=invoice_create.invoice_amount,
            invoice_payment_date=invoice_create.invoice_payment_date,
            invoice_payed_amount=invoice_create.invoice_payed_amount,
            invoice_payed_date=invoice_create.invoice_payed_date,
            invoice_description=invoice_create.invoice_description,
            project_id=invoice_create.project_id,
            jupers_id=invoice_create.jupers_id,
        )
        session.add(invoice)
        await session.commit()
        await session.refresh(invoice)
        return invoice
    except Exception as e:
        await session.rollback()
        raise

async def update(session: AsyncSession, invoice_id: int, invoice_update: InvoiceUpdate) -> Optional[InvoiceModel]:
    invoice = await get_by_id(session, invoice_id)
    if not invoice:
        return None
    
    update_data = invoice_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(invoice, key, value)
    
    await session.commit()
    await session.refresh(invoice)
    return invoice