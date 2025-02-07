from typing import Optional

from fastapi import FastAPI
from routers import artists

app = FastAPI()

app.include_router(artists.router, prefix="/artists", tags=["artists"])

@app.get("/")
async def root():
    return {"message": "Welcome to Golebiewski Artworks Database API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}