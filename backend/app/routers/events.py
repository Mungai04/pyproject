from fastapi import APIRouter

router = APIRouter(prefix="/events")

events_db = [
    {"id": 1, "name": "Event 1"},
    {"id": 2, "name": "Event 2"},
]

@router.get("/")
async def get_events():
    return events_db