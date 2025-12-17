from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper

from .crud import payment as payment_crood
from core.schemas.payment import PaymentCreate, PaymentRead, PaymentUpdate

router = APIRouter(tags=["Payment"])

@router.get("/", response_model=list[PaymentRead])
async def get_all(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> list[PaymentRead]:
    payments = await payment_crood.get_all(session=session)
    return payments

@router.get("/{payment_id}", response_model=PaymentRead)
async def get_by_id(
    payment_id: int,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> PaymentRead:
    payment = await payment_crood.get_by_id(session=session, payment_id=payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.post("/", response_model=PaymentRead)
async def create(
    payment_create: PaymentCreate, 
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> PaymentRead:
    payment = await payment_crood.create(
        session=session, 
        payment_create=payment_create
    )
    return payment

@router.put("/{payment_id}", response_model=PaymentRead)
async def update(
    payment_id: int,
    payment_update: PaymentUpdate,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> PaymentRead:
    payment = await payment_crood.update(
        session=session, 
        payment_id=payment_id,
        payment_update=payment_update
    )
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.delete("/{payment_id}", response_model=PaymentRead)
async def delete(
    payment_id: int,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> PaymentRead:
    payment = await payment_crood.delete(
        session=session, 
        payment_id=payment_id
    )
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

