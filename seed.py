from sqlmodel import Session, create_engine
from models import User, Artist, Medium, Department, Series
from datetime import datetime
from dotenv import load_dotenv
import os

# Initialize the database connection
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

def seed_medium(session: Session):
    mediums = [
        'watercolor', 
        'oil paint', 
        'canvas', 
        'paper', 
        'pencil', 
        'gouache', 
        'super 8 film', 
        'posca marker', 
        'pen & ink',
    ]
    
    # Creating Medium instances and adding to the session
    medium_objects = [Medium(name=medium) for medium in mediums]
    
    session.add_all(medium_objects)
    session.commit()
    
# Function to add seed data
def create_seed_data(session: Session):
    # Seed Users
    user1 = User(
        username="Nick",
        password="hashed_password_123",  # Store hashed passwords
        email="x@nickgolebiewski.com",
        admin=True
    )
    
    user2 = User(
        username="user1",
        password="hashed_password_456",
        email="user1@example.com",
        admin=False
    )
    
    session.add_all([user1, user2])
    session.commit()

    # Seed Mediums
    medium1 = Medium(name="Oil Paint")
    medium2 = Medium(name="Watercolor")
    medium3 = Medium(name="Acrylic")
    
    session.add_all([medium1, medium2, medium3])
    session.commit()

    # Seed Departments
    department1 = Department(name="Painting", description="Fine art painting")
    department2 = Department(name="Sculpture", description="Sculptures and installations")
    
    session.add_all([department1, department2])
    session.commit()

    # Seed Artists
    artist1 = Artist(
        first_name="Pablo",
        last_name="Picasso",
        artist_name="Picasso",
        short_bio="Spanish painter and sculptor.",
        birth_year=1881,
        death_year=1973
    )
    
    artist2 = Artist(
        first_name="Frida",
        last_name="Kahlo",
        artist_name="Kahlo",
        short_bio="Mexican painter known for self-portraits.",
        birth_year=1907,
        death_year=1954
    )
    
    session.add_all([artist1, artist2])
    session.commit()

    # Seed Series
    series1 = Series(
        artist_id=artist1.id,
        name="Blue Period",
        description="A series of works painted in shades of blue.",
    )
    
    series2 = Series(
        artist_id=artist2.id,
        name="Self-Portraits",
        description="A series of self-portraits exploring identity and pain.",
    )
    
    session.add_all([series1, series2])
    session.commit()

# Running the seed function
if __name__ == "__main__":
    with Session(engine) as session:
        seed_medium(session)
