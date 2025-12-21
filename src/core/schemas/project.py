from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional
from datetime import datetime

class ProjectBase(BaseModel):
    project_code: str
    project_status:  Optional[str] = None
    project_budget: Optional[float] = None
    project_description: Optional[str] = None
    
    @field_validator('project_status', 'project_description', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == '':
            return None
        return v
    
    @field_validator('project_budget', mode='before')
    @classmethod
    def null_or_float(cls, v):
        if v is None or v == '':
            return None
        return float(v) if v is not None else None


class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    project_code: Optional[str] = None
    project_status: Optional[str] = None
    project_budget: Optional[float] = None
    project_description: Optional[str] = None

class ProjectRead(ProjectBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int