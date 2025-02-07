# database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
import os
from dotenv import load_dotenv
from . import models


# Load environment variables from .env file
load_dotenv()

# Access environment variables (standard postgresql:// format in .env)
database_url = os.getenv("DATABASE_URL")

# Modify the URL for asyncpg
DATABASE_URL = database_url.replace("postgresql://", "postgresql+asyncpg://")

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with SessionLocal() as session:
        yield session

async def create_db_and_tables():  # Make this function async
    async with engine.begin() as conn:  # Use async context manager
        await conn.run_sync(SQLModel.metadata.create_all) # Run sync operation in async context
        #or
        #await SQLModel.metadata.create_all(engine) # this should work for sqlmodel 0.0.12 or newer