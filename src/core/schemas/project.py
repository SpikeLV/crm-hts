from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProjectBase(BaseModel):
    project_code: str
    project_status:  Optional[str] = None
    project_budget: Optional[float] = None
    project_description: Optional[str] = None

class ProjectRead(ProjectBase):
    pass

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    project_code: Optional[str] = None
    project_status: Optional[str] = None
    project_budget: Optional[float] = None
    project_description: Optional[str] = None
