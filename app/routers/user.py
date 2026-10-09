from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_database
from app.schemas import UserCreate
from app.models import UserModel
from app.athentication import hash_password,verify_password,create_token,get_current_user
router=APIRouter(tags=["User"])

@router.post("/register")
def register(user:UserCreate,database:Session=Depends(get_database)):
    hash_pwd=hash_password(user.User_Password)
    existing_user=database.query(UserModel).filter(UserModel.User_Name==user.User_Name).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="User already exists")
    new_user=UserModel(User_Name=user.User_Name,User_Password=hash_pwd)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)

    return {"Message":"Register successfully","User":new_user}

@router.post("/login")
def login(user:OAuth2PasswordRequestForm=Depends(),database:Session=Depends(get_database)):
    existing_user=database.query(UserModel).filter(UserModel.User_Name==user.username).first()
    if not existing_user:
        raise HTTPException(status_code=401,detail="Invalid user and password")
    if not verify_password(user.password,existing_user.User_Password):
        raise HTTPException(status_code=401,detail="Invalid user and password")
    token=create_token(existing_user.User_Name)
    return {
        "access_token":token,
        "token_type":"Bearer"
    }
