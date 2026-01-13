from fastapi import FastAPI
from .database import Base, engine
from .routers import employees
from .auth import create_access_token

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management API")

@app.post("/api/token")
def login():
    return {"access_token": create_access_token(), "token_type": "bearer"}

app.include_router(employees.router)
