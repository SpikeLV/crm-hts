from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper

from .crud import invoice as invoice_crood
from core.schemas.invoice import InvoiceCreate, InvoiceRead, InvoiceUpdate

router = APIRouter(tags=["Invoice"])

@router.get("/", response_model=list[InvoiceRead])
async def get_all(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> list[InvoiceRead]:
    invoices = await invoice_crood.get_all(session=session)
    return invoices

@router.get("/{invoice_id}", response_model=InvoiceRead)
async def get_by_id(
    invoice_id: int,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> InvoiceRead:
    invoice = await invoice_crood.get_by_id(session=session, invoice_id=invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@router.post("/", response_model=InvoiceRead)
async def create(
    invoice_create: InvoiceCreate, 
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
        ) -> InvoiceRead:
    invoice = await invoice_crood.create(
        session=session, 
        invoice_create=invoice_create
    )
    return invoice

@router.put("/{invoice_id}", response_model=InvoiceRead)
async def update(
    invoice_id: int,
    invoice_update: InvoiceUpdate,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> InvoiceRead:
    invoice = await invoice_crood.update(
        session=session, 
        invoice_id=invoice_id,
        invoice_update=invoice_update
    )
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice