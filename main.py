from typing import Optional
from fastapi import FastAPI, Depends
from .routers import artists
# from . import models  # Import your models 
# from .database import create_db_and_tables, get_session # Import from database.py
# from sqlmodel import Session

app = FastAPI(
    title="Art Base One",
    description="An API for managing artworks, artists and clients.",
    contact={
        "name": "Nick Golebiewski",
        "url": "https://github.com/ngolebiewski/",
    },
    version="0.0.2",
)

# @app.on_event("startup")
# async def startup_event():
#     create_db_and_tables() # Call the setup function

# # Dependency Injection for database session
# @app.get("/items/")
# def read_items(session: Session = Depends(get_session)):
#     # use the session here
#     pass

app.include_router(artists.router, prefix="/artists", tags=["artists"])

@app.get("/")
async def root():
    return {"message": "Welcome to Golebiewski Artworks Database API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}