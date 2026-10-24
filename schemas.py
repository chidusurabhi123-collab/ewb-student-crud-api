from pydantic import BaseModel
from datetime import date
from typing import Optional

class StudentBase(BaseModel):
    student_id: str
    name: str
    dob: Optional[date] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    course: Optional[str] = None
    address: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    dob: Optional[date] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    course: Optional[str] = None
    address: Optional[str] = None

class StudentOut(StudentBase):
    id: int
    class Config:
        from_attributes = True