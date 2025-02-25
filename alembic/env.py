import sqlmodel
import sys
from pathlib import Path
import os
import subprocess
from dotenv import load_dotenv
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from sqlmodel import SQLModel

# Ensure project root is in sys.path
sys.path.append(str(Path(__file__).parent.parent))

# Import models explicitly
from models import (
    Artist, Artwork, Department, Series, Medium, 
    ArtworksMediumsLink, AdditionalImage, Organization, 
    Person, SoldArtwork
)

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)

# Alembic Config object
config = context.config

# Set the database URL dynamically in Alembic config
config.set_main_option('sqlalchemy.url', DATABASE_URL)

# Set up logging
if config.config_file_name:
    fileConfig(config.config_file_name)

# Use SQLModel metadata for autogeneration
target_metadata = SQLModel.metadata

# Exclude views from Alembic migrations
def include_object(object, name, type_, reflected, compare_to):
    if type_ == "table" and name in ("mediums_by_artwork", "art_list"):
        return False
    return True

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    engine = create_engine(DATABASE_URL, poolclass=pool.NullPool)
    
    with engine.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            include_object=include_object
        )
        with context.begin_transaction():
            context.run_migrations()
    
    # Run view_creator.py after migrations
    script_path = os.path.join(Path(__file__).parent.parent, "view_creator.py")
    if os.path.exists(script_path):
        try:
            subprocess.run(["python", script_path], check=True)
            print("✅ Successfully ran view_creator.py after migrations.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running view_creator.py: {e}")

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
