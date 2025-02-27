from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlmodel import Session, select
from database import get_db
from models import Series, User
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from auth_utils import get_current_active_user

router = APIRouter()

class SeriesCreate(BaseModel):
    artist_id: int
    name: str
    description: Optional[str] = None
    web: bool
    order: Optional[int] = None

class SeriesUpdate(BaseModel):
    artist_id: int
    name: str
    description: Optional[str] = None
    web: bool
    order: Optional[int] = None

@router.get("/", response_model=List[Series])
async def read_series(session: AsyncSession = Depends(get_db)):
    """Retrieve a list of all series."""
    result = await session.execute(select(Series))
    series = result.scalars().all()
    return series

@router.post("/", response_model=Series, status_code=status.HTTP_201_CREATED)
async def create_series(series_create: SeriesCreate, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    """Create a new series (admin only)."""
    series = Series(
        artist_id=series_create.artist_id,
        name=series_create.name.lower(),
        description=series_create.description,
        web=series_create.web,
        order=series_create.order,
    )
    session.add(series)
    try:
        await session.commit()
        await session.refresh(series)
        return series
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Series name already exists")

@router.get("/{series_id}", response_model=Series)
async def read_series_by_id(series_id: int, session: AsyncSession = Depends(get_db)):
    """Retrieve a series by ID."""
    series = await session.get(Series, series_id)
    if not series:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Series not found")
    return series

@router.put("/{series_id}", response_model=Series)
async def update_series(series_id: int, series_update: SeriesUpdate, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    """Update a series by ID (admin only)."""
    series = await session.get(Series, series_id)
    if not series:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Series not found")

    series.artist_id = series_update.artist_id
    series.name = series_update.name.lower()
    series.description = series_update.description
    series.web = series_update.web
    series.order = series_update.order

    session.add(series)
    try:
        await session.commit()
        await session.refresh(series)
        return series
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Series name already exists")

@router.delete("/{series_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_series(series_id: int, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    """Delete a series by ID (admin only)."""
    series = await session.get(Series, series_id)
    if not series:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Series not found")

    await session.delete(series)
    await session.commit()