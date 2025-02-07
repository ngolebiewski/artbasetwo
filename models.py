from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

'''
Database Schema from Nick Golebiewski's Harvard CS50SQL FINAL PROJECT, art database in SQLITE3
https://github.com/ngolebiewski/CS50SQL-final-project-ng/tree/main/studio_artist
'''

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    password: str  # In real application, hash this!
    email: str
    admin: Optional[bool] = Field(default=False)  # More Pythonic

class Artist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    artist_name: Optional[str] = Field(default=None)
    short_bio: str = Field(max_length=200)
    long_bio: Optional[str] = Field(default=None)
    image_url: Optional[str] = Field(default=None)
    birth_country: Optional[str] = Field(default=None)
    birth_year: Optional[int] = Field(default=None)
    death_year: Optional[int] = Field(default=None)

    artworks: List["Artwork"] = Relationship(back_populates="artist")
    series: List["Series"] = Relationship(back_populates="artist")

class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    description: Optional[str] = Field(max_length=300)
    web: Optional[bool] = Field(default=False)  # More Pythonic
    order: Optional[int] = Field(default=None)

    artworks: List["Artwork"] = Relationship(back_populates="department")

class Series(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    artist_id: int = Field(foreign_key="artist.id")
    name: str = Field(unique=True)
    description: Optional[str] = Field(max_length=300)
    web: Optional[bool] = Field(default=False)
    order: Optional[int] = Field(default=None)

    artist: Artist = Relationship(back_populates="series")
    artworks: List["Artwork"] = Relationship(back_populates="series")

class Medium(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = Field(default=None, unique=True)

    artworks: List["Artwork"] = Relationship(back_populates="mediums", secondary="artworks_mediums")

class ArtworksMediums(SQLModel, table=True):
    artwork_id: int = Field(foreign_key="artwork.id", primary_key=True)
    medium_id: int = Field(foreign_key="medium.id", primary_key=True)

class Artwork(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    artist_id: int = Field(foreign_key="artist.id")
    title: str
    size: str
    year: Optional[int] = Field(default=None)
    end_year: Optional[int] = Field(default=None)
    image_url: Optional[str] = Field(default=None)
    hi_res_url: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    keywords: Optional[str] = Field(default=None)
    department_id: Optional[int] = Field(default=None, foreign_key="department.id") # Changed to department_id
    series_id: Optional[int] = Field(default=None, foreign_key="series.id") # Changed to series_id
    date_added: Optional[str] = Field(default=None) # Timestamp is handled by db
    price: Optional[float] = Field(default=None)
    sold: bool = Field(default=False)  # More Pythonic

    artist: Artist = Relationship(back_populates="artworks")
    department: Optional[Department] = Relationship(back_populates="artworks")
    series: Optional[Series] = Relationship(back_populates="artworks")
    mediums: List[Medium] = Relationship(back_populates="artworks", secondary="artworks_mediums")
    additional_images: List["AdditionalImage"] = Relationship(back_populates="artwork")

class AdditionalImage(SQLModel, table=True):
    artwork_id: int = Field(foreign_key="artwork.id", primary_key=True)  # Composite key with image_url
    image_url: str = Field(primary_key=True) # Composite key with artwork_id

    artwork: Artwork = Relationship(back_populates="additional_images")

class Organization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address_1: Optional[str] = Field(default=None)
    address_2: Optional[str] = Field(default=None)
    city: str
    state: str
    country: Optional[str] = Field(default="United States")
    phone: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    type: str = Field(
        sa_column_kwargs={"check_constraint": "type IN ('museum', 'gallery', 'non-profit', 'restaurant', 'business', 'other')"}
    )

    persons: List["Person"] = Relationship(back_populates="organization")
    sold_artworks: List["SoldArtwork"] = Relationship(back_populates="organization")

class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: Optional[str] = Field(default=None, unique=True)
    phone: Optional[int] = Field(default=None)
    org_id: Optional[int] = Field(default=None, foreign_key="organization.id")
    note: Optional[str] = Field(default=None)
    type: str = Field(default="contact", sa_column_kwargs={"check_constraint": "type IN ('collector', 'friend', 'artist', 'client', 'curator', 'other')"})

    organization: Optional[Organization] = Relationship(back_populates="persons")
    sold_artworks: List["SoldArtwork"] = Relationship(back_populates="person")

class SoldArtwork(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    artwork_id: int = Field(foreign_key="artwork.id")
    person_id: int = Field(foreign_key="person.id")
    org_id: Optional[int] = Field(default=None, foreign_key="organization.id")
    price: Optional[float] = Field(default=None)
    date_sold: Optional[str] = Field(default=None) # Date is handled by db
    timestamp: Optional[str] = Field(default=None) # Timestamp is handled by db

    artwork: Artwork = Relationship()
    person: Person = Relationship(back_populates="sold_artworks")
    organization: Optional[Organization] = Relationship(back_populates="sold_artworks")



# Views (Define these outside the model definitions, in your main application logic or migration scripts)
# Triggers (Define these using SQLAlchemy Core in your migration scripts)