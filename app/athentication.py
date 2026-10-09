from datetime import datetime,timedelta
from jose import jwt
from passlib.context import CryptContext
from fastapi import HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

load_dotenv()
SECURITY_KEY=os.environ.get("SECURITY_KEY")
ALGORITHM=os.environ.get("ALGORITHM")
EXPIRE_MINUTES=int(os.environ.get("EXPIRE_MINUTES"))

oauth2=OAuth2PasswordBearer(tokenUrl="/login")
password_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str):
    return password_context.hash(password)

def verify_password(password:str,hash_pwd:str):
    return password_context.verify(password,hash_pwd)

def create_token(username:str):
    expire=datetime.utcnow()+timedelta(minutes=EXPIRE_MINUTES)
    plaload={
        "sub":username,
        "exp":expire
    }
    token=jwt.encode(plaload,SECURITY_KEY,ALGORITHM)
    return token

def get_current_user(token:str=Depends(oauth2)):
    try:
        plaload=jwt.decode(token,SECURITY_KEY,ALGORITHM)
        username=plaload.get("sub")

        if username is None:
            raise HTTPException(status_code=401,detail="Invalid token")

        return username
    except Exception:
        raise HTTPException(status_code=401,detail="Invalid or expired token")
    