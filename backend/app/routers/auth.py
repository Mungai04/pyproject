from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from models import User

router = APIRouter(prefix="/auth")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_db = {
    "users": []
}

@router.post("/signup")
async def signup(user: User):
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password
    fake_db["users"].append(user.dict())
    return {"msg": "User signed up successfully"}

@router.post("/login")
async def login(user: User):
    user_in_db = next((u for u in fake_db["users"] if u["username"] == user.username), None)
    if not user_in_db:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    if not pwd_context.verify(user.password, user_in_db["password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"msg": "Login successful"}