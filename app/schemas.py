from pydantic import BaseModel,Field
from typing import Optional

class EmployeeAdd(BaseModel):
    Employee_Name:str
    Employee_Age:int
    Employee_Gender:str
    Employee_Email:str
    Employee_Phone:str
    
class EmployeeUpdate(BaseModel):
    Employee_Name:Optional[str]=None
    Employee_Age:Optional[int]=None
    Employee_Gender:Optional[str]=None
    Employee_Email:Optional[str]=None
    Employee_Phone:Optional[str]=None
    
class UserCreate(BaseModel):
    User_Name:str
    User_Password:str=Field(min_length=5,max_length=72)

class UserLogin(BaseModel):
    User_Name:str
    User_Password:str=Field(min_length=5,max_length=72)