import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
LANGUAGETOOL_URL = os.getenv("LANGUAGETOOL_URL", "https://api.languagetoolplus.com/v2/check")
SPACY_MODEL = os.getenv("SPACY_MODEL", "pt_core_news_md")