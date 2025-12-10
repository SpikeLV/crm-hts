from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from core.schemas.fipers import FipersCreate, FipersRead, FipersUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from .crud import fipers as fipers_crood

router = APIRouter(tags=["Fipers"])

@router.get("/", response_model=list[FipersRead])
async def get_all(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> list[FipersRead]:
    fipers = await fipers_crood.get_all(session=session)
    return fipers

@router.get("/{fiper_id}", response_model=FipersRead)
async def get_by_id(
    fiper_id: int,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> FipersRead:
    fiper = await fipers_crood.get_by_id(session=session, fiper_id=fiper_id)
    if not fiper:
        raise HTTPException(status_code=404, detail="Person not found")
    return fiper

@router.post("/", response_model=FipersRead)
async def create(
    fiper_create: FipersCreate, 
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> FipersRead:
    fiper = await fipers_crood.create(
        session=session, 
        fiper_create=fiper_create
    )
    return fiper

@router.put("/{fiper_id}", response_model=FipersRead)
async def update(
    fiper_id: int,
    fiper_update: FipersUpdate,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> FipersRead:
    fiper = await fipers_crood.update(
        session=session, 
        fiper_id=fiper_id,
        fiper_update=fiper_update
    )
    if not fiper:
        raise HTTPException(status_code=404, detail="Person not found")
    return fiper