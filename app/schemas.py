from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    department: Optional[str] = None
    role: Optional[str] = None

class EmployeeUpdate(BaseModel):
    name: Optional[str]
    department: Optional[str]
    role: Optional[str]

class EmployeeOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: Optional[str]
    role: Optional[str]
    date_joined: date

    class Config:
        orm_mode = True
