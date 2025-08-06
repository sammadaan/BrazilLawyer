import spacy
from app import config

nlp_model = spacy.load(config.SPACY_MODEL)

def analyze_text(text: str):
    doc = nlp_model(text)
    entities = [ent.text for ent in doc.ents]
    lemmas = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return {
        "entities": entities,
        "lemmas": lemmas
    }