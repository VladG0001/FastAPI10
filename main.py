from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List

app = FastAPI()

security = HTTPBasic()

VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != VALID_USERNAME or credentials.password != VALID_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app. Use /secure to access the secure route."}

@app.get("/secure")
def read_secure(username: str = Depends(authenticate_user)):
    return {"message": f"Hello, {username}! You have accessed a secure route."}
