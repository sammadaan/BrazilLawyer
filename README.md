# AI Backend MVP

This backend uses FastAPI and integrates with:
- Google Gemini API (for LLM)
- spaCy (for NLP)
- LanguageTool (for grammar correction)

## Setup

1. Copy `.env.example` to `.env` and fill in your API keys.
2. Build and run with Docker Compose:
   ```
   docker-compose up --build
   ```
3. Access docs at `http://localhost:8000/docs`

## Endpoints

- `/grammar-correct`: Grammar correction (LanguageTool)
- `/ai-rewrite`: Rewrite legal text (Gemini)
- `/strengthen-argument`: Enhance legal arguments (Gemini)
- `/nlp/analyze`: Extract entities & lemmas (spaCy)

## Environment Variables

- `GEMINI_API_KEY`: Required. Get from Google AI Studio.
- `LANGUAGETOOL_URL`: Default provided.
- `SPACY_MODEL`: Default `pt_core_news_md`.

---

**Security Note:**  
Never commit `.env` files with real secrets!
