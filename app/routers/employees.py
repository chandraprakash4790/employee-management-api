from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from ..database import SessionLocal
from ..models import Employee
from ..schemas import EmployeeCreate, EmployeeUpdate, EmployeeOut
from ..deps import get_current_user

router = APIRouter(prefix="/api/employees", tags=["Employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=201, response_model=EmployeeOut)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not emp.name.strip():
        raise HTTPException(400, "Name cannot be empty")
    if db.query(Employee).filter(Employee.email == emp.email).first():
        raise HTTPException(400, "Email already exists")
    employee = Employee(**emp.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

@router.get("/", response_model=List[EmployeeOut])
def list_employees(department: str = None, role: str = None, page: int = Query(1, ge=1),
                   db: Session = Depends(get_db), user=Depends(get_current_user)):
    query = db.query(Employee)
    if department:
        query = query.filter(Employee.department == department)
    if role:
        query = query.filter(Employee.role == role)
    return query.offset((page - 1) * 10).limit(10).all()

@router.get("/{id}", response_model=EmployeeOut)
def get_employee(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    emp = db.query(Employee).get(id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    return emp

@router.put("/{id}", response_model=EmployeeOut)
def update_employee(id: int, data: EmployeeUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    emp = db.query(Employee).get(id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    for k, v in data.dict(exclude_unset=True).items():
        setattr(emp, k, v)
    db.commit()
    db.refresh(emp)
    return emp

@router.delete("/{id}", status_code=204)
def delete_employee(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    emp = db.query(Employee).get(id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    db.delete(emp)
    db.commit()
