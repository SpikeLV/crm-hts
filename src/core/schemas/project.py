from pydantic import BaseModel, ConfigDict
from typing import Optional

class Project(BaseModel):
    id: int
    project_code: str
    project_status:  Optional[str] = None
    project_budget: Optional[float] = None
    project_description: Optional[str] = None