from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database import get_db
from models import User
from pydantic import BaseModel
from auth_utils import get_password_hash, verify_password, create_access_token, Token, TokenData
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    admin: bool = False

@router.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: Session = Depends(get_db)):
    db_user = await session.execute(select(User).where(User.username == user.username))
    if db_user.first():
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, password=hashed_password, email=user.email, admin=user.admin)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    user = await session.execute(select(User).where(User.username == form_data.username))
    user = user.scalars().first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = None #Use default expiration
    access_token = create_access_token(
        data={"sub": user.username, "admin": user.admin}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}