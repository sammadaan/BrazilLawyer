"""Document upload, PDF processing, and analysis."""
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.pdf_handler import extract_text_from_pdf
from app.utils.text_processor import clean_text
from app.services.case_analyzer import CaseAnalyzer

router = APIRouter(prefix="/documents", tags=["documents"])

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")
    content = await file.read()
    text = extract_text_from_pdf(content)
    cleaned = clean_text(text)
    return {"text": cleaned}

@router.post("/analyze")
async def analyze_document(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_pdf(content)
    cleaned = clean_text(text)
    analyzer = CaseAnalyzer()
    analysis = await analyzer.analyze_case(cleaned)
    return analysis