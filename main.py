import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String(100))
    employee_salary = Column(Integer)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class EmployeeCreate(BaseModel):
    employee_name: str
    employee_salary: int

class EmployeeUpdate(BaseModel):
    id: int
    employee_name: str
    employee_salary: int

class EmployeeResponse(BaseModel):
    id: int
    employee_name: str
    employee_salary: int

@app.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate):
    db = SessionLocal()
    db_employee = Employee(employee_name=employee.employee_name, employee_salary=employee.employee_salary)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    db.close()
    return db_employee

@app.put("/employees/", response_model=EmployeeResponse)
def update_employee(employee: EmployeeUpdate):
    db = SessionLocal()
    db_employee = db.query(Employee).filter(Employee.id == employee.id).first()
    if not db_employee:
        db.close()
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db_employee.employee_name = employee.employee_name
    db_employee.employee_salary = employee.employee_salary
    db.commit()
    db.refresh(db_employee)
    db.close()
    return db_employee

@app.delete("/employees/{employee_id}", response_model=dict)
def delete_employee(employee_id: int):
    db = SessionLocal()
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        db.close()
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db.delete(db_employee)
    db.commit()
    db.close()
    return {"detail": "Employee deleted"}