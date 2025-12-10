from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper

from .crud import jupers as jupers_crood
from core.schemas.jupers import JupersCreate, JupersRead, JupersUpdate

router = APIRouter(tags=["Jupers"])

@router.get("/", response_model=list[JupersRead])
async def get_all(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> list[JupersRead]:
    jupers = await jupers_crood.get_all(session=session)
    return jupers

@router.get("/{jupers_id}", response_model=JupersRead)
async def get_by_id(
    jupers_id: int,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> JupersRead:
    jupers = await jupers_crood.get_by_id(session=session, jupers_id=jupers_id)
    if not jupers:
        raise HTTPException(status_code=404, detail="Jupers not found")
    return jupers

@router.post("/", response_model=JupersRead)
async def create(
    jupers_create: JupersCreate, 
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
        ) -> JupersRead:
    jupers = await jupers_crood.create(
        session=session, 
        jupers_create=jupers_create
    )
    return jupers

@router.put("/{jupers_id}", response_model=JupersRead)
async def update(
    jupers_id: int,
    jupers_update: JupersUpdate,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> JupersRead:
    jupers = await jupers_crood.update(
        session=session, 
        jupers_id=jupers_id,
        jupers_update=jupers_update
    )
    if not jupers:
        raise HTTPException(status_code=404, detail="Person not found")
    return jupers