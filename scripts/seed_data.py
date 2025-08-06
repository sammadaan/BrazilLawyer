"""Seed sample legal data into the database."""
import asyncio
from app.database.connection import AsyncSessionLocal
from app.database.models import Case

async def seed():
    async with AsyncSessionLocal() as session:
        sample_case = Case(
            case_number="0000000-00.0000.0.00.0000",
            court="STF",
            title="Caso Exemplo",
            summary="Resumo do caso exemplo.",
            url="https://www.stf.jus.br",
        )
        session.add(sample_case)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(seed())