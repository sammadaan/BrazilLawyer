"""Pydantic schemas for validation and serialization."""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

class LegalPrecedentBase(BaseModel):
    citation: str
    summary: Optional[str] = None

class LegalPrecedentCreate(LegalPrecedentBase): pass

class LegalPrecedent(LegalPrecedentBase):
    id: int
    class Config:
        orm_mode = True

class CourtDecisionBase(BaseModel):
    decision_text: str
    judge: Optional[str]
    date: Optional[datetime]
    metadata: Optional[Dict] = None

class CourtDecisionCreate(CourtDecisionBase):
    precedents: Optional[List[LegalPrecedentCreate]] = []

class CourtDecision(CourtDecisionBase):
    id: int
    precedents: List[LegalPrecedent] = []
    class Config:
        orm_mode = True

class ProcessedDocumentBase(BaseModel):
    filename: str
    content: str
    processed_data: Optional[Dict] = None

class ProcessedDocumentCreate(ProcessedDocumentBase): pass

class ProcessedDocument(ProcessedDocumentBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class SearchQueryBase(BaseModel):
    query_text: str
    filters: Optional[Dict] = None

class SearchQueryCreate(SearchQueryBase): pass

class SearchQuery(SearchQueryBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class CaseBase(BaseModel):
    case_number: str
    court: str
    title: Optional[str]
    summary: Optional[str]
    url: Optional[str]
    filed_date: Optional[datetime]

class CaseCreate(CaseBase):
    search_queries: Optional[List[SearchQueryCreate]] = []
    processed_documents: Optional[List[ProcessedDocumentCreate]] = []
    decisions: Optional[List[CourtDecisionCreate]] = []

class Case(CaseBase):
    id: int
    updated_at: Optional[datetime]
    search_queries: List[SearchQuery] = []
    processed_documents: List[ProcessedDocument] = []
    decisions: List[CourtDecision] = []
    class Config:
        orm_mode = True