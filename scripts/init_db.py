"""Initialize the database (run migrations)."""
import asyncio
from app.database import init_db

if __name__ == "__main__":
    asyncio.run(init_db())