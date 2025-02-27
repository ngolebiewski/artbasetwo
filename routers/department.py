from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlmodel import Session, select
from database import get_db
from models import Department, User
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from auth_utils import get_current_active_user

router = APIRouter()

class DepartmentCreate(BaseModel):
    name: str
    description: Optional[str] = None
    web: bool
    order: Optional[int] = None

class DepartmentUpdate(BaseModel):
    name: str
    description: Optional[str] = None
    web: bool
    order: Optional[int] = None

@router.get("/", response_model=List[Department])
async def read_departments(session: AsyncSession = Depends(get_db)):
    """Retrieve a list of all departments."""
    result = await session.execute(select(Department))
    departments = result.scalars().all()
    return departments

@router.post("/", response_model=Department, status_code=status.HTTP_201_CREATED)
async def create_department(department_create: DepartmentCreate, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    """Create a new department (admin only)."""
    department = Department(
        name=department_create.name.lower(),
        description=department_create.description,
        web=department_create.web,
        order = department_create.order
    )
    session.add(department)
    try:
        await session.commit()
        await session.refresh(department)
        return department
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Department name already exists")

@router.get("/{department_id}", response_model=Department)
async def read_department_by_id(department_id: int, session: AsyncSession = Depends(get_db)):
    """Retrieve a department by ID."""
    department = await session.get(Department, department_id)
    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
    return department

@router.put("/{department_id}", response_model=Department)
async def update_department(department_id: int, department_update: DepartmentUpdate, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    """Update a department by ID (admin only)."""
    department = await session.get(Department, department_id)
    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")

    department.name = department_update.name.lower()
    department.description = department_update.description
    department.web = department_update.web
    department.order = department_update.order
    session.add(department)
    try:
        await session.commit()
        await session.refresh(department)
        return department
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Department name already exists")

@router.delete("/{department_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_department(department_id: int, session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    """Delete a department by ID (admin only)."""
    department = await session.get(Department, department_id)
    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")

    await session.delete(department)
    await session.commit()