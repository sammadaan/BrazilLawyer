"""AI-powered case analyzer using Gemini API."""
from google.generativeai import GenerativeModel
from config.settings import settings

class CaseAnalyzer:
    def __init__(self):
        self.model = GenerativeModel(api_key=settings.GEMINI_API_KEY)

    async def analyze_case(self, case_text: str) -> dict:
        """Analyze a case using Gemini API."""
        prompt = (
            "Analise este caso jurídico brasileiro. "
            "Identifique os pontos principais, precedentes relevantes e possíveis argumentos."
            f"\n\n{case_text}"
        )
        result = self.model.generate_content(prompt)
        return {"analysis": result.text}