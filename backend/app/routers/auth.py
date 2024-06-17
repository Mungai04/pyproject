from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.database import get_db
from app.crud import create_user, get_user_by_username
import sqlite3

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/signup")
def signup(username: str, email: str, password: str, db: sqlite3.Connection = Depends(get_db)):
    if get_user_by_username(db, username):
        raise HTTPException(status_code=400, detail="Username already registered")
    user_id = create_user(db, username, email, password)
    return {"id": user_id, "username": username, "email": email}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: sqlite3.Connection = Depends(get_db)):
    user = get_user_by_username(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user["username"], "token_type": "bearer"}