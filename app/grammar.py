import requests
from app import config

def correct_text(text: str) -> str:
    payload = {
        "text": text,
        "language": "pt-BR"
    }
    response = requests.post(config.LANGUAGETOOL_URL, data=payload)
    if response.status_code != 200:
        return f"LanguageTool Error: {response.text}"

    data = response.json()
    corrected = text
    matches = data.get("matches", [])
    for match in sorted(matches, key=lambda m: m["offset"], reverse=True):
        if match.get("replacements"):
            replacement = match["replacements"][0]["value"]
            start = match["offset"]
            end = start + match["length"]
            corrected = corrected[:start] + replacement + corrected[end:]
    return corrected
