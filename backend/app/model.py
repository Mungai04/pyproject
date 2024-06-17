from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str = None
    password: str

class Ticket(BaseModel):
    event_id: int
    username: str