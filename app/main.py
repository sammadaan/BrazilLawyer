from fastapi import FastAPI
from app import nlp, llm, grammar, schemas

app = FastAPI()

@app.post("/grammar-correct", response_model=schemas.TextResponse)
def grammar_correction(req: schemas.TextRequest):
    corrected = grammar.correct_text(req.text)
    return schemas.TextResponse(text=corrected)

@app.post("/ai-rewrite", response_model=schemas.TextResponse)
def ai_rewrite(req: schemas.TextRequest):
    result = llm.rewrite_text(req.text)
    return schemas.TextResponse(text=result)

@app.post("/strengthen-argument", response_model=schemas.TextResponse)
def strengthen_argument(req: schemas.TextRequest):
    result = llm.strengthen_argument(req.text)
    return schemas.TextResponse(text=result)

@app.post("/nlp/analyze", response_model=schemas.NLPResponse)
def nlp_analyze(req: schemas.TextRequest):
    analysis = nlp.analyze_text(req.text)
    return schemas.NLPResponse(**analysis)