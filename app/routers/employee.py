from fastapi import APIRouter,Depends,HTTPException
from app.schemas import EmployeeAdd,EmployeeUpdate
from sqlalchemy.orm import Session
from app.models import EmployeeModel
from app.database import get_database
from app.athentication import get_current_user
router=APIRouter(tags=["Employees"])

@router.get("/employees")
def all_employees(limit:int=None,database:Session=Depends(get_database),username:str=Depends(get_current_user)):
    query=database.query(EmployeeModel)
    if limit:
        query=query.limit(limit)
    return query.all()

@router.get("/employee/{employee_id}")
def get_employee(employee_id:int,database:Session=Depends(get_database),username:str=Depends(get_current_user)):
    query=database.query(EmployeeModel).filter(EmployeeModel.Employee_ID==employee_id).first()
    if not query:
        raise HTTPException(status_code=401,detail="Employee not found")
    return query

@router.post("/add")
def add_employee(user:EmployeeAdd,database:Session=Depends(get_database),username:str=Depends(get_current_user)):
    new_employee=EmployeeModel(
        Employee_Name=user.Employee_Name,
        Employee_Age=user.Employee_Age,
        Employee_Gender=user.Employee_Gender,
        Employee_Email=user.Employee_Email,
        Employee_Phone=user.Employee_Phone
    )
    database.add(new_employee)
    database.commit()
    database.refresh(new_employee)
    return {"Message":"Employee Add successfully","Employee":new_employee}

@router.put("/update/{employee_id}")
def employee_update(emp_update:EmployeeUpdate,employee_id:int,database:Session=Depends(get_database),username:str=Depends(get_current_user)):
    existing_employee=database.query(EmployeeModel).filter(EmployeeModel.Employee_ID==employee_id).first()
    if not existing_employee:
        raise HTTPException(status_code=401,detail="Employee not found")
    if emp_update.Employee_Name is not None:
        existing_employee.Employee_Name=emp_update.Employee_Name
    if emp_update.Employee_Age is not None:
        existing_employee.Employee_Age=emp_update.Employee_Age
    if emp_update.Employee_Gender is not None:
        existing_employee.Employee_Gender=emp_update.Employee_Gender
    if emp_update.Employee_Email is not None:
        existing_employee.Employee_Email=emp_update.Employee_Email
    if emp_update.Employee_Phone is not None:
        existing_employee.Employee_Phone=emp_update.Employee_Phone

    database.commit()
    database.refresh(existing_employee)

    return {"Message":"Update successfully","Employee":existing_employee}

@router.delete("/delete/{employee_id}")
def employee_delete(employee_id:int,database:Session=Depends(get_database),username:str=Depends(get_current_user)):
    query=database.query(EmployeeModel).filter(EmployeeModel.Employee_ID==employee_id).first()
    if not query:
        raise HTTPException(status_code=401,detail="Employee not found")
    database.delete(query)
    database.commit()

    return {"Message":"Employee delete successfully","Employee":query}