"""Text processing utilities for Portuguese legal text."""
import re
import unicodedata

def clean_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s.,;:()\-]", "", text, flags=re.UNICODE)
    return text.strip()