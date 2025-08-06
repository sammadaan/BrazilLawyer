"""Abstract base class for scrapers, with error handling, rate limiting."""
import asyncio
from abc import ABC, abstractmethod
from time import time
import httpx

class BaseScraper(ABC):
    RATE_LIMIT = 1.0  # seconds between requests

    def __init__(self):
        self._last_request = 0.0

    @abstractmethod
    async def fetch_case_list(self, query: str, max_pages: int = 1):
        pass

    async def throttled_request(self, client: httpx.AsyncClient, url: str):
        now = time()
        if now - self._last_request < self.RATE_LIMIT:
            await asyncio.sleep(self.RATE_LIMIT - (now - self._last_request))
        self._last_request = time()
        try:
            resp = await client.get(url)
            resp.raise_for_status()
            return resp
        except Exception as e:
            print(f"Scraper error on {url}: {e}")
            return None

    def get_delay(self):
        return self.RATE_LIMIT