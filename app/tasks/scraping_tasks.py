"""Async scraping tasks and batch processing."""
from app.tasks.celery_app import celery_app
from app.services.dje_scraper import DJEScraper

@celery_app.task
def scrape_dje(tribunal: str, date_from: str, date_to: str, query: str):
    import asyncio
    asyncio.run(_scrape_dje(tribunal, date_from, date_to, query))

async def _scrape_dje(tribunal, date_from, date_to, query):
    scraper = DJEScraper()
    results = await scraper.search(tribunal, date_from, date_to, query)
    # Add results to database...
    return results