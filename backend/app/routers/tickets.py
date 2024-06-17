from fastapi import APIRouter, HTTPException
from models import Ticket

router = APIRouter(prefix="/tickets")

tickets_db = []

@router.post("/book")
async def book_ticket(ticket: Ticket):
    tickets_db.append(ticket.dict())
    return {"msg": "Ticket booked successfully"}