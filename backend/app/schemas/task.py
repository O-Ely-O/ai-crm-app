from datetime import datetime
from typing import List, Optional, Any
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = ""
    due_date: Optional[datetime] = None
    status: str = "Pending"
    priority: str = "Medium"
    related_lead_id: Optional[str] = None
    related_contact_id: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    related_lead_id: Optional[str] = None
    related_contact_id: Optional[str] = None
    completed_at: Optional[datetime] = None


class TaskOut(TaskBase):
    id: str
    owner_id: str
    completed_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    related_lead: Optional[Any] = None
    related_contact: Optional[Any] = None

    class Config:
        from_attributes = True


class TasksResponse(BaseModel):
    success: bool = True
    count: int
    tasks: List[TaskOut]


class TaskResponse(BaseModel):
    success: bool = True
    task: TaskOut