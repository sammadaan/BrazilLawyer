"""JusBrasil scraper using async httpx and BeautifulSoup."""
import httpx
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Optional
import asyncio
from app.scrapers.base_scraper import BaseScraper
from app.utils.text_processor import clean_text

class JusBrasilScraper(BaseScraper):
    BASE_URL = "https://www.jusbrasil.com.br"
    SEARCH_ENDPOINT = "/jurisprudencia/busca?q={query}&page={page}"

    async def fetch_case_list(self, query: str, max_pages: int = 3) -> List[Dict[str, Any]]:
        cases = []
        async with httpx.AsyncClient(timeout=30) as client:
            for page in range(1, max_pages + 1):
                url = self.BASE_URL + self.SEARCH_ENDPOINT.format(query=query, page=page)
                resp = await self.throttled_request(client, url)
                if resp is None:
                    continue
                soup = BeautifulSoup(resp.text, "html.parser")
                for case in soup.select(".document-card"):
                    case_data = self.parse_case_card(case)
                    if case_data:
                        cases.append(case_data)
                await asyncio.sleep(self.get_delay())
        return cases

    def parse_case_card(self, card) -> Optional[Dict[str, Any]]:
        try:
            case_number = card.select_one(".case-number, .number").text.strip()
            title = card.select_one(".title, h2").text.strip()
            summary = clean_text(card.select_one(".excerpt, .summary").text)
            court = card.select_one(".court, .court-name").text.strip()
            url = self.BASE_URL + card.find("a")["href"]
            return {
                "case_number": case_number,
                "title": title,
                "summary": summary,
                "court": court,
                "url": url
            }
        except Exception:
            return None

    async def fetch_case_details(self, case_url: str) -> Optional[Dict[str, Any]]:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await self.throttled_request(client, case_url)
            if resp is None:
                return None
            soup = BeautifulSoup(resp.text, "html.parser")
            # Extract more details as needed
            return {
                "full_text": clean_text(soup.select_one(".document-content, .full-text").text)
            }