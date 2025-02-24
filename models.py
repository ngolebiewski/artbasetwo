from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship, Column, Integer, ForeignKey
from sqlalchemy import Table, CheckConstraint

'''
Database Schema from Nick Golebiewski's Harvard CS50SQL FINAL PROJECT, art database in SQLITE3
https://github.com/ngolebiewski/CS50SQL-final-project-ng/tree/main/studio_artist
'''

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    password: str
    email: str
    admin: Optional[bool] = Field(default=False)

class Artist(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    artist_name: Optional[str] = None
    short_bio: str = Field(max_length=200)
    long_bio: Optional[str] = None
    image_url: Optional[str] = None
    birth_country: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None

    artworks: List["Artwork"] = Relationship(back_populates="artist")
    series: List["Series"] = Relationship(back_populates="artist")

class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    description: Optional[str] = Field(default=None, max_length=300)
    web: Optional[bool] = Field(default=False)
    order: Optional[int] = None

    artworks: List["Artwork"] = Relationship(back_populates="department")

class Series(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    artist_id: int = Field(foreign_key="artist.id")
    name: str = Field(unique=True)
    description: Optional[str] = Field(default=None, max_length=300)
    web: Optional[bool] = Field(default=False)
    order: Optional[int] = None

    artist: "Artist" = Relationship(back_populates="series")
    artworks: List["Artwork"] = Relationship(back_populates="series")

class ArtworksMediumsLink(SQLModel, table=True):
    artwork_id: int = Field(foreign_key="artwork.id", primary_key=True)
    medium_id: int = Field(foreign_key="medium.id", primary_key=True)

artworks_mediums_table = Table(
    "artworks_mediums",
    SQLModel.metadata,
    Column("artwork_id", Integer, ForeignKey("artwork.id"), primary_key=True),
    Column("medium_id", Integer, ForeignKey("medium.id"), primary_key=True),
)

class Medium(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)

    artworks: List["Artwork"] = Relationship(back_populates="mediums", link_model=ArtworksMediumsLink)

class Artwork(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    artist_id: int = Field(foreign_key="artist.id")
    title: str
    size: str
    year: Optional[int] = None
    end_year: Optional[int] = None
    image_url: Optional[str] = None
    hi_res_url: Optional[str] = None
    description: Optional[str] = None
    keywords: Optional[str] = None
    department_id: Optional[int] = Field(default=None, foreign_key="department.id")
    series_id: Optional[int] = Field(default=None, foreign_key="series.id")
    date_added: Optional[str] = None
    price: Optional[float] = None
    sold: bool = Field(default=False)

    artist: "Artist" = Relationship(back_populates="artworks")
    department: Optional["Department"] = Relationship(back_populates="artworks")
    series: Optional["Series"] = Relationship(back_populates="artworks")
    mediums: List["Medium"] = Relationship(back_populates="artworks", link_model=ArtworksMediumsLink)
    additional_images: List["AdditionalImage"] = Relationship(back_populates="artwork")

class AdditionalImage(SQLModel, table=True):
    artwork_id: int = Field(foreign_key="artwork.id", primary_key=True)
    image_url: str = Field(primary_key=True)

    artwork: "Artwork" = Relationship(back_populates="additional_images")

class Organization(SQLModel, table=True):
    __table_args__ = (
        CheckConstraint("type IN ('museum', 'gallery', 'non-profit', 'restaurant', 'business', 'other')", name="check_type"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    city: str
    state: str
    country: Optional[str] = Field(default="United States")
    phone: Optional[str] = None
    email: Optional[str] = None
    type: str

    persons: List["Person"] = Relationship(back_populates="organization")
    sold_artworks: List["SoldArtwork"] = Relationship(back_populates="organization")

class Person(SQLModel, table=True):
    __table_args__ = (
        CheckConstraint("type IN ('collector', 'friend', 'artist', 'client', 'curator', 'other')", name="check_type"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: Optional[str] = Field(default=None, unique=True)
    phone: Optional[int] = None
    org_id: Optional[int] = Field(default=None, foreign_key="organization.id")
    note: Optional[str] = None
    type: str = Field(default="contact")

    organization: Optional["Organization"] = Relationship(back_populates="persons")
    # sold_artworks: List["SoldArtwork"] = Relationship(back_populates="sold_artworks")
    sold_artworks: List["SoldArtwork"] = Relationship(back_populates="person") # Corrected Line

class SoldArtwork(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    artwork_id: int = Field(foreign_key="artwork.id")
    person_id: int = Field(foreign_key="person.id")
    org_id: Optional[int] = Field(default=None, foreign_key="organization.id")
    price: Optional[float] = None
    date_sold: Optional[str] = None
    timestamp: Optional[str] = None

    artwork: "Artwork" = Relationship()
    person: "Person" = Relationship(back_populates="sold_artworks")
    organization: Optional["Organization"] = Relationship(back_populates="sold_artworks")

# Need to ensure view_creator.py script is run to create views after each migration

class MediumsByArtwork(SQLModel, table=True):
    __tablename__ = "mediums_by_artwork"

    id: int = Field(primary_key=True)
    title: str
    mediums: Optional[str]  # Comma-separated string of mediums


class ArtList(SQLModel, table=True):
    __tablename__ = "art_list"

    id: int = Field(primary_key=True)
    name: str
    title: str
    size: Optional[str]
    year: Optional[int]
    mediums: Optional[str]  # From mediums_by_artwork
    image_url: Optional[str]
    description: Optional[str]
    series: Optional[str]
    department: Optional[str]
    price: Optional[float]
    sold: Optional[bool]