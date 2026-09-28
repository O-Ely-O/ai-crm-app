from datetime import datetime
from typing import List, Optional, Any
from pydantic import BaseModel, Field


class NoteBase(BaseModel):
    content: str = Field(..., min_length=1)
    lead_id: Optional[str] = None
    contact_id: Optional[str] = None
    pinned: bool = False


class NoteCreate(NoteBase):
    pass


class NoteUpdate(BaseModel):
    content: Optional[str] = None
    lead_id: Optional[str] = None
    contact_id: Optional[str] = None
    pinned: Optional[bool] = None


class NoteOut(NoteBase):
    id: str
    owner_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    lead: Optional[Any] = None
    contact: Optional[Any] = None

    class Config:
        from_attributes = True


class NotesResponse(BaseModel):
    success: bool = True
    count: int
    notes: List[NoteOut]


class NoteResponse(BaseModel):
    success: bool = True
    note: NoteOut