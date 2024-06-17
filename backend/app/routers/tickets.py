from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.database import get_db
from app.crud import create_ticket, get_tickets, get_user_by_username
import sqlite3

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/tickets/")
def create_ticket_route(title: str, description: str, event_id: int, db: sqlite3.Connection = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = get_user_by_username(db, token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    ticket_id = create_ticket(db, title, description, user["id"], event_id)
    return {"id": ticket_id, "title": title, "description": description, "owner_id": user["id"], "event_id": event_id}

@router.get("/tickets/")
def read_tickets(skip: int = 0, limit: int = 10, db: sqlite3.Connection = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = get_user_by_username(db, token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    tickets = get_tickets(db, user["id"])
    return tickets