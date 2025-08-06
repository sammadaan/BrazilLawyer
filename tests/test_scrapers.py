import pytest
from app.services.jusbrasil_scraper import JusBrasilScraper

@pytest.mark.asyncio
async def test_jusbrasil_scraper():
    scraper = JusBrasilScraper()
    results = await scraper.fetch_case_list("direito civil", max_pages=1)
    assert isinstance(results, list)