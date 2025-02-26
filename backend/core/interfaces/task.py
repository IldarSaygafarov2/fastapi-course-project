from datetime import datetime
from enum import StrEnum
from typing import Optional
from pydantic import BaseModel


class TaskStatus(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class TaskDTO(BaseModel):
    id: int
    name: str
    description: Optional[str]
    status: str
    user_id: int
    finish_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime


class TaskCreateDTO(BaseModel):
    name: str
    description: Optional[str]
    status: TaskStatus
    user_id: int
    finish_date: Optional[datetime] = None


class TaskUpdateDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    finish_date: Optional[datetime] = None
