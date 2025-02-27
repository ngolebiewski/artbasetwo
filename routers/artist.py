from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlmodel import Session, select
from database import get_db
from models import Artist, User
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, Field
from sqlalchemy.exc import IntegrityError
from auth_utils import get_current_active_user

router = APIRouter()

class ArtistCreate(BaseModel):
    first_name: str
    last_name: str
    artist_name: Optional[str] = None
    short_bio: str = Field(max_length=200)
    long_bio: Optional[str] = None
    image_url: Optional[str] = None
    birth_country: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None

class ArtistUpdate(BaseModel):
    first_name: str
    last_name: str
    artist_name: Optional[str] = None
    short_bio: str = Field(max_length=200)
    long_bio: Optional[str] = None
    image_url: Optional[str] = None
    birth_country: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None

@router.get("/", response_model=List[Artist])
async def read_artists(session: AsyncSession = Depends(get_db)):
    """Retrieve a list of all artists."""
    result = await session.execute(select(Artist))
    artists = result.scalars().all()
    return artists

@router.post("/", response_model=Artist, status_code=status.HTTP_201_CREATED)
async def create_artist(artist_create: ArtistCreate, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    """Create a new artist (admin only)."""
    artist = Artist(
        first_name=artist_create.first_name,
        last_name=artist_create.last_name,
        artist_name=artist_create.artist_name,
        short_bio=artist_create.short_bio,
        long_bio=artist_create.long_bio,
        image_url=artist_create.image_url,
        birth_country=artist_create.birth_country,
        birth_year=artist_create.birth_year,
        death_year=artist_create.death_year,
    )
    session.add(artist)
    try:
        await session.commit()
        await session.refresh(artist)
        return artist
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Artist name already exists")

@router.get("/{artist_id}", response_model=Artist)
async def read_artist_by_id(artist_id: int, session: AsyncSession = Depends(get_db)):
    """Retrieve an artist by ID."""
    artist = await session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artist not found")
    return artist

@router.put("/{artist_id}", response_model=Artist)
async def update_artist(artist_id: int, artist_update: ArtistUpdate, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    """Update an artist by ID (admin only)."""
    artist = await session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artist not found")

    artist.first_name = artist_update.first_name
    artist.last_name = artist_update.last_name
    artist.artist_name = artist_update.artist_name
    artist.short_bio = artist_update.short_bio
    artist.long_bio = artist_update.long_bio
    artist.image_url = artist_update.image_url
    artist.birth_country = artist_update.birth_country
    artist.birth_year = artist_update.birth_year
    artist.death_year = artist_update.death_year

    session.add(artist)
    try:
        await session.commit()
        await session.refresh(artist)
        return artist
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Artist name already exists")

@router.delete("/{artist_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_artist(artist_id: int, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    """Delete an artist by ID (admin only)."""
    artist = await session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artist not found")

    await session.delete(artist)
    await session.commit()