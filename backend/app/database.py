import sqlite3

DATABASE_URL = "database.db"

def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn