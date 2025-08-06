"""Database initialization for FastAPI app."""
from .connection import engine, get_db
from .models import Base

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)