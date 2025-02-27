from typing import Optional
from fastapi import FastAPI, Depends
from routers import artist, auth, medium, department, series
from database import create_db_and_tables, get_db
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(
    title="Art Base One",
    description="An API for managing artworks, artists and clients.",
    contact={
        "name": "Nick Golebiewski",
        "url": "https://github.com/ngolebiewski/",
    },
    version="0.0.2",
)

@app.on_event("startup")
async def startup_event():
    await create_db_and_tables() # Call the setup function

app.include_router(artist.router, prefix="/artist", tags=["artist"])
app.include_router(medium.router, prefix="/medium", tags=["medium"])
app.include_router(department.router, prefix="/department", tags=["department"])
app.include_router(series.router, prefix="/series", tags=["series"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to Golebiewski Artworks Database API. See the docs at /docs"}