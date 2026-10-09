from fastapi import FastAPI
from app.routers import employee,user
from app.models import Base
from app.database import engine


Base.metadata.create_all(bind=engine)
app=FastAPI()

app.include_router(user.router)
app.include_router(employee.router)

@app.get("/")
def root():
    return {"Message":"API run Successfully"}


