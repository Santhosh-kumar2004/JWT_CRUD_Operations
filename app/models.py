from sqlalchemy import Column,String,Integer
from app.database import Base

class EmployeeModel(Base):
    __tablename__="Employee"
    Employee_ID=Column(Integer,primary_key=True,index=True,autoincrement=True)
    Employee_Name=Column(String,index=True)
    Employee_Age=Column(Integer,index=True)
    Employee_Gender=Column(String,index=True)
    Employee_Email=Column(String,index=True)
    Employee_Phone=Column(String,index=True)


class UserModel(Base):
    __tablename__="Users"
    User_ID=Column(Integer,primary_key=True,index=True,autoincrement=True)
    User_Name=Column(String,index=True,unique=True)
    User_Password=Column(String,index=True)