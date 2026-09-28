from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class ContactBase(BaseModel):
    name: str = Field(..., min_length=1)
    email: str = ""
    phone: str = ""
    company: str = ""
    title: str = ""
    tags: List[str] = []
    notes: str = ""
    favorite: bool = False


class ContactCreate(ContactBase):
    pass


class ContactUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    title: Optional[str] = None
    tags: Optional[List[str]] = None
    notes: Optional[str] = None
    favorite: Optional[bool] = None


class ContactOut(ContactBase):
    id: str
    owner_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ContactsResponse(BaseModel):
    success: bool = True
    count: int
    contacts: List[ContactOut]


class ContactResponse(BaseModel):
    success: bool = True
    contact: ContactOut
