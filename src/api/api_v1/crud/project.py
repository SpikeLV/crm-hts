from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models.project import Project as ProjectModel
from core.schemas.project import ProjectCreate, ProjectUpdate

async def get_all(session: AsyncSession) -> Sequence[ProjectModel]:
    stmt = select(ProjectModel).order_by(ProjectModel.project_code.asc())
    result = await session.scalars(stmt)
    return result.all()

async def get_by_id(session: AsyncSession, project_id: int) -> Optional[ProjectModel]:
    stmt = select(ProjectModel).where(ProjectModel.id == project_id)
    result = await session.scalar(stmt)
    return result

async def create(session: AsyncSession, project_create: ProjectCreate) -> ProjectModel:
    try:
        project = ProjectModel(
            project_code=project_create.project_code,
            project_status=project_create.project_status if project_create.project_status else None,
            project_budget=project_create.project_budget if project_create.project_budget else None,
            project_description=project_create.project_description if project_create.project_description else None,
        )
        session.add(project)
        await session.commit()
        await session.refresh(project)
        return project
    except Exception as e:
        await session.rollback()
        raise

async def update(session: AsyncSession, project_id: int, project_update: ProjectUpdate) -> Optional[ProjectModel]:
    project = await get_by_id(session, project_id)
    if not project:
        return None
    
    update_data = project_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(project, key, value)
    
    await session.commit()
    await session.refresh(project)
    return project