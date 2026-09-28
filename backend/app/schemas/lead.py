from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class LeadBase(BaseModel):
    name: str = Field(..., min_length=1)
    email: str = ""
    phone: str = ""
    company: str = ""
    status: str = "New"
    priority: str = "Medium"
    source: str = ""
    value: float = 0
    notes: str = ""
    tags: List[str] = []
    ai_summary: str = ""
    ai_risk_score: Optional[float] = None
    order: int = 0


class LeadCreate(LeadBase):
    pass


class LeadUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    source: Optional[str] = None
    value: Optional[float] = None
    notes: Optional[str] = None
    tags: Optional[List[str]] = None
    ai_summary: Optional[str] = None
    ai_risk_score: Optional[float] = None
    order: Optional[int] = None


class LeadOut(LeadBase):
    id: str
    owner_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class LeadReorderItem(BaseModel):
    id: str
    status: str
    order: int


class LeadReorderRequest(BaseModel):
    updates: List[LeadReorderItem]


class LeadsResponse(BaseModel):
    success: bool = True
    leads: List[LeadOut]


class LeadResponse(BaseModel):
    success: bool = True
    lead: LeadOut
