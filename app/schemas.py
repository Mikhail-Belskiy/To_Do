from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: datetime

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None