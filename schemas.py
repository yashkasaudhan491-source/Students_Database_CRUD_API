from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class StudentBase(BaseModel):
    name: str
    dob: date
    email: EmailStr
    phone: str
    course: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    dob: Optional[date] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    course: Optional[str] = None

class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True