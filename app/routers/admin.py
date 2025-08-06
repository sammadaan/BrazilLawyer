"""Admin endpoints for stats, refresh, health."""
from fastapi import APIRouter
from app.database.connection import engine
from sqlalchemy import text

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/db-stats")
async def db_stats():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT COUNT(*) FROM cases"))
        count = result.scalar()
        return {"cases_count": count}

@router.post("/refresh")
async def refresh_data():
    # Trigger background update task
    from app.tasks.data_updater import weekly_update
    weekly_update.delay()
    return {"status": "refresh triggered"}