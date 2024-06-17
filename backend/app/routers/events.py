from fastapi import APIRouter, Depends
from app.database import get_db
from app.crud import create_event, get_events
import sqlite3

router = APIRouter()

@router.post("/events/")
def create_event_route(name: str, location: str, date: str, db: sqlite3.Connection = Depends(get_db)):
    event_id = create_event(db, name, location, date)
    return {"id": event_id, "name": name, "location": location, "date": date}

@router.get("/events/")
def read_events(skip: int = 0, limit: int = 10, db: sqlite3.Connection = Depends(get_db)):
    events = get_events(db)
    return events