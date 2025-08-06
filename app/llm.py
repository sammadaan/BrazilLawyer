import requests
from app import config

def _call_gemini(prompt: str) -> str:
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": config.GEMINI_API_KEY}
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    resp = requests.post(url, headers=headers, params=params, json=data)
    if resp.status_code == 200:
        try:
            return resp.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            return "Error: Unexpected Gemini API response structure"
    return f"Error: {resp.text}"

def rewrite_text(text: str) -> str:
    prompt = f"Reescreva este texto jurídico de maneira clara, correta e coesa:\n\n{text}"
    return _call_gemini(prompt)

def strengthen_argument(text: str) -> str:
    prompt = f"Você é um advogado experiente. Melhore e reforce o argumento jurídico a seguir para torná-lo mais convincente e fundamentado:\n\n{text}"
    return _call_gemini(prompt)