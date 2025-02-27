# run as: python3 -m db.seed

from sqlmodel import Session, create_engine
from models import User, Artist, Medium, Department, Series
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from auth_utils import get_password_hash
from dotenv import load_dotenv
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize the database connection
load_dotenv()
ADMIN_PWD = os.getenv("ADMIN_PWD")
ART_LOVER_PWD = os.getenv("ADMIN_PWD")
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)

# Seed Art Mediums into the database
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
        'graphite',
        'carbon paper'
    ]
    
    for medium_name in mediums:
        try:
            medium = Medium(name=medium_name)
            session.add(medium)
            session.commit()
            logging.info(f"Added medium: {medium_name}")
        except IntegrityError as e:
            session.rollback()  # Rollback the transaction
            logging.warning(f"IntegrityError: Medium '{medium_name}' already exists. Error: {e}")
        except Exception as e:
            session.rollback()
            logging.error(f"An unexpected error occurred while adding medium '{medium_name}': {e}")

# Seed an admin user
def seed_admin_user(session: Session):
    username = "nick"  # Set the desired admin username
    password = ADMIN_PWD  # Set the desired admin password in the .env file
    email = "x@nickgolebiewski.com"  # Set the desired admin email

    try:
        hashed_password = get_password_hash(password) #hash the password
        admin_user = User(username=username, password=hashed_password, email=email, admin=True)
        session.add(admin_user)
        session.commit()
        logging.info(f"Added admin user: {username}")
        return admin_user
    except IntegrityError as e:
        session.rollback()
        logging.warning(f"IntegrityError: Admin user '{username}' already exists. Error: {e}")
    except Exception as e:
        session.rollback()
        logging.error(f"An unexpected error occurred while adding admin user '{username}': {e}")
    
def seed_regular_user(session: Session):
    username = "art_lover"  # Set the desired admin username
    password = ART_LOVER_PWD  # Set the regular user password in the .env file, should remain SECRET
    email = "info@nickgolebiewski.com"  
    
    try:
        hashed_password = get_password_hash(password) #hash the password
        regular_user = User(username=username, password=hashed_password, email=email, admin=False)
        session.add(regular_user)
        session.commit()
        logging.info(f"Added regular user: {username}")
    except IntegrityError as e:
        session.rollback()
        logging.warning(f"IntegrityError: Admin user '{username}' already exists. Error: {e}")
    except Exception as e:
        session.rollback()
        logging.error(f"An unexpected error occurred while adding admin user '{username}': {e}")
        
        
# Seed 'Departments', overarching organizational umbrellas for artworks into the database
def seed_departmnets(session: Session):
    departments = [
        ("Painting", "All forms of painting, including oil, gouache, watercolor, etc."),
        ("Film", "Video, super 8 film, 16mm, 35mm, and all other moving images."),
        ("Drawing-a-Day", "A daily drawing project."),
        ("Studio", "Artworks made in a studio setting."),
        ("Computer Art", "Artowrks with code as their prime medium.")
    ]

    for dept_info in departments:
        try:
            dept = Department(name=dept_info[0], description=dept_info[1], web=True)
            session.add(dept)
            session.commit()
            logging.info(f"Added Department: {dept_info[0]}")
        except IntegrityError as e:
            session.rollback()  # Rollback the transaction
            logging.warning(f"IntegrityError: Department'{dept_info[0]}' already exists. Error: {e}")
        except Exception as e:
            session.rollback()
            logging.error(f"An unexpected error occurred while adding department '{dept_info[0]}': {e}")

# Function to add seed data
# def create_seed_data(session: Session):
#     # Seed Users
#     user1 = User(
#         username="Nick",
#         password="hashed_password_123",  # Store hashed passwords
#         email="x@nickgolebiewski.com",
#         admin=True
#     )
    
#     user2 = User(
#         username="user1",
#         password="hashed_password_456",
#         email="user1@example.com",
#         admin=False
#     )
    
#     session.add_all([user1, user2])
#     session.commit()

#     # Seed Mediums
#     medium1 = Medium(name="Oil Paint")
#     medium2 = Medium(name="Watercolor")
#     medium3 = Medium(name="Acrylic")
    
#     session.add_all([medium1, medium2, medium3])
#     session.commit()

#     # Seed Departments
#     department1 = Department(name="Painting", description="Fine art painting")
#     department2 = Department(name="Sculpture", description="Sculptures and installations")
    
#     session.add_all([department1, department2])
#     session.commit()

#     # Seed Artists
#     artist1 = Artist(
#         first_name="Pablo",
#         last_name="Picasso",
#         artist_name="Picasso",
#         short_bio="Spanish painter and sculptor.",
#         birth_year=1881,
#         death_year=1973
#     )
    
#     artist2 = Artist(
#         first_name="Frida",
#         last_name="Kahlo",
#         artist_name="Kahlo",
#         short_bio="Mexican painter known for self-portraits.",
#         birth_year=1907,
#         death_year=1954
#     )
    
#     session.add_all([artist1, artist2])
#     session.commit()

#     # Seed Series
#     series1 = Series(
#         artist_id=artist1.id,
#         name="Blue Period",
#         description="A series of works painted in shades of blue.",
#     )
    
#     series2 = Series(
#         artist_id=artist2.id,
#         name="Self-Portraits",
#         description="A series of self-portraits exploring identity and pain.",
#     )
    
#     session.add_all([series1, series2])
#     session.commit()

# Running the seed function
if __name__ == "__main__":
    with Session(engine) as session:
        # seed_medium(session)
        # logging.info("Art mediums seeded.")
        admin_user = seed_admin_user(session) #seed admin user
        # logging.info("Admin Users seeded.")
        # seed_regular_user(session) #seed regular user
        # logging.info("Regular Users seeded.")
        seed_departmnets(session) #seed regular user
        logging.info("Departments seeded.")
        logging.info("Database seeding complete.")
