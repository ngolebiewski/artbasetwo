# routers/medium.py
from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session, select
from database import get_db 
from models import Medium
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/", response_model=List[Medium])
async def read_mediums(session: AsyncSession = Depends(get_db)):
    """
    Retrieve a list of all mediums.
    """
    result = await session.execute(select(Medium))
    mediums = result.scalars().all()
    return mediums