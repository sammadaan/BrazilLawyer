"""Background tasks for updating and maintaining case law data."""
from app.tasks.celery_app import celery_app
from app.services.jusbrasil_scraper import JusBrasilScraper
from app.database.connection import AsyncSessionLocal
from app.database.models import Case
from sqlalchemy.ext.asyncio import AsyncSession

@celery_app.task
def weekly_update():
    """Weekly fetch of new case law from JusBrasil."""
    import asyncio
    asyncio.run(update_cases())

async def update_cases():
    scraper = JusBrasilScraper()
    cases = await scraper.fetch_case_list(query="direito civil", max_pages=2)
    async with AsyncSessionLocal() as session:
        for case in cases:
            exists = await session.execute(
                Case.__table__.select().where(Case.case_number == case["case_number"])
            )
            if not exists.scalar():
                new_case = Case(**case)
                session.add(new_case)
        await session.commit()