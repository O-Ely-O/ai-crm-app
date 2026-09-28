from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str = "member"
    company: str = ""
    avatar: str = ""


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    password: str = Field(..., min_length=6)
    company: str = ""


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    company: Optional[str] = None
    avatar: Optional[str] = None
    password: Optional[str] = Field(None, min_length=6)


class UserOut(BaseModel):
    id: str
    name: str
    email: str
    role: str
    company: str = ""
    avatar: str = ""
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    success: bool = True
    token: str
    user: UserOut
