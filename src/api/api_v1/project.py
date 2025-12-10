from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper

from .crud import project as project_crood
from core.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate

router = APIRouter(tags=["Project"])

@router.get("/", response_model=list[ProjectRead])
async def get_all(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> list[ProjectRead]:
    projects = await project_crood.get_all(session=session)
    return projects

@router.get("/{project_id}", response_model=ProjectRead)
async def get_by_id(
    project_id: int,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> ProjectRead:
    project = await project_crood.get_by_id(session=session, project_id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("/", response_model=ProjectRead)
async def create(
    project_create: ProjectCreate, 
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
        ) -> ProjectRead:
    project = await project_crood.create(
        session=session, 
        project_create=project_create
    )
    return project

@router.put("/{project_id}", response_model=ProjectRead)
async def update(
    project_id: int,
    project_update: ProjectUpdate,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
    ],
) -> ProjectRead:
    project = await project_crood.update(
        session=session, 
        project_id=project_id,
        project_update=project_update
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project