"""DJE (Diário da Justiça Eletrônico) scraper for multiple courts."""
from app.scrapers.tribunal_scrapers.stf_scraper import STFScraper
from app.scrapers.tribunal_scrapers.stj_scraper import STJScraper
from app.scrapers.tribunal_scrapers.tjsp_scraper import TJSPscraper

class DJEScraper:
    def __init__(self):
        self.tribunal_scrapers = {
            "STF": STFScraper(),
            "STJ": STJScraper(),
            "TJ-SP": TJSPscraper(),
            # Add more courts as needed
        }

    async def search(self, tribunal: str, date_from: str, date_to: str, query: str):
        scraper = self.tribunal_scrapers.get(tribunal)
        if not scraper:
            raise ValueError(f"Tribunal '{tribunal}' not supported.")
        return await scraper.search(date_from, date_to, query)