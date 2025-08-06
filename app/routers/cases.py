"""Case law endpoints for search, retrieve, analyze, compare."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.database.models import Case
from app.database.schemas import Case, CaseCreate
from typing import List

router = APIRouter(prefix="/cases", tags=["cases"])

@router.get("/", response_model=List[Case])
async def list_cases(db: AsyncSession = Depends(get_db)):
    result = await db.execute(Case.__table__.select())
    return result.scalars().all()

@router.get("/{case_id}", response_model=Case)
async def get_case(case_id: int, db: AsyncSession = Depends(get_db)):
    case = await db.get(Case, case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case

@router.post("/", response_model=Case)
async def create_case(case: CaseCreate, db: AsyncSession = Depends(get_db)):
    db_case = Case(**case.dict())
    db.add(db_case)
    await db.commit()
    await db.refresh(db_case)
    return db_case