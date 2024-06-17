import sqlite3
from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db, username: str, email: str, password: str):
    hashed_password = pwd_context.hash(password)
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO users (username, email, hashed_password, is_active)
        VALUES (?, ?, ?, ?)
    """, (username, email, hashed_password, True))
    db.commit()
    return cursor.lastrowid

def get_user_by_username(db, username: str):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()

def create_ticket(db, title: str, description: str, user_id: int, event_id: int):
    created_at = datetime.utcnow()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO tickets (title, description, owner_id, event_id, created_at, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (title, description, user_id, event_id, created_at, "open"))
    db.commit()
    return cursor.lastrowid

def get_tickets(db, user_id: int):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tickets WHERE owner_id = ?", (user_id,))
    return cursor.fetchall()

def create_event(db, name: str, location: str, date: str):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO events (name, location, date)
        VALUES (?, ?, ?)
    """, (name, location, date))
    db.commit()
    return cursor.lastrowid

def get_events(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM events")
    return cursor.fetchall()