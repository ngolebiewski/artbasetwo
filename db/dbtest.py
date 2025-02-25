from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
postgres_url = os.getenv("DATABASE_URL")

try:
    engine = create_engine(postgres_url)
    with engine.connect() as conn:  # Try to establish a connection
        print("SQLAlchemy engine connection successful!")
        print(postgres_url)
        # You can execute a simple query here to further verify:
        result = conn.execute(text("SELECT 1"))  # A very basic query
        print(result.fetchone()) # Should print (1,)

except Exception as e: # Catch any SQLAlchemy or underlying DBAPI exceptions
    print(f"SQLAlchemy engine connection failed: {e}")