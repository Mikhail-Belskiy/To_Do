from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Task(BaseModel):
    id: Optional[int]
    title: str
    description: Optional[str] = None
    created_date: datetime
    deadline: datetime
    completed: bool

