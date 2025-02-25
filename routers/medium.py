from fastapi import APIRouter, Depends, HTTPException, status, Form, Request
from typing import List, Optional
from sqlmodel import Session, select
from database import get_db
from models import Medium
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError

router = APIRouter()

class MediumCreate(BaseModel):
    name: str

class MediumUpdate(BaseModel):
    name: str

@router.get("/", response_model=List[Medium])
async def read_mediums(session: AsyncSession = Depends(get_db)):
    """Retrieve a list of all mediums."""
    result = await session.execute(select(Medium))
    mediums = result.scalars().all()
    return mediums

@router.post("/", response_model=Medium, status_code=status.HTTP_201_CREATED)
async def create_medium(medium_create: MediumCreate, session: AsyncSession = Depends(get_db)):
    """Create a new medium."""
    medium = Medium(name=medium_create.name.lower())
    session.add(medium)
    try:
        await session.commit()
        await session.refresh(medium)
        return medium
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Medium name already exists")

@router.put("/{medium_id}", response_model=Medium)
async def update_medium(medium_id: int, medium_update: MediumUpdate, session: AsyncSession = Depends(get_db)):
    """Update a medium by ID."""
    medium = await session.get(Medium, medium_id)
    if not medium:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medium not found")

    medium.name = medium_update.name.lower()
    session.add(medium)
    try:
        await session.commit()
        await session.refresh(medium)
        return medium
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Medium name already exists")

@router.delete("/{medium_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_medium(medium_id: int, session: AsyncSession = Depends(get_db)):
    """Delete a medium by ID."""
    medium = await session.get(Medium, medium_id)
    if not medium:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medium not found")

    await session.delete(medium)
    await session.commit()