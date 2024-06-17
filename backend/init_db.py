from fastapi import FastAPI
from app.routers import auth, tickets, events

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(tickets.router, prefix="/tickets", tags=["tickets"])
app.include_router(events.router, prefix="/events", tags=["events"])

@app.get("/")
def read_root():
    return {"Hello": "World"}