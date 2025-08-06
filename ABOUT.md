# About

This repository contains the AI Backend MVP for a legal tech platform. It is built using FastAPI and Docker, and integrates several powerful AI and NLP tools:

- **Google Gemini API** for advanced language model capabilities (LLM).
- **spaCy** for natural language processing, specifically using the Portuguese `pt_core_news_md` model.
- **LanguageTool** for grammar and spelling correction.

**Main Features:**
- Grammar and language correction for legal documents.
- Automated rewriting and enhancement of legal arguments using AI.
- Entity and lemma extraction from legal texts for better analytics.

**Quick Start:**
1. Copy `.env.example` to `.env` and fill in API keys.
2. Build and start the stack with Docker Compose.
3. Access interactive API docs at `http://localhost:8000/docs`.

This backend is designed for rapid prototyping and integration into larger legal tech systems.  
**Note:** Never commit real secrets or API keys to the repository.