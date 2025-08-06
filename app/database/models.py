"""SQLAlchemy ORM models for the legal AI backend."""
from sqlalchemy import (
    Column, Integer, String, Text, DateTime, ForeignKey, JSON, Table
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Case(Base):
    __tablename__ = "cases"
    id = Column(Integer, primary_key=True, index=True)
    case_number = Column(String(64), unique=True, nullable=False, index=True)
    court = Column(String(64), nullable=False)
    title = Column(String(255))
    summary = Column(Text)
    url = Column(String(255))
    filed_date = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    decisions = relationship("CourtDecision", back_populates="case", cascade="all, delete")
    processed_documents = relationship("ProcessedDocument", back_populates="case", cascade="all, delete")
    search_queries = relationship("SearchQuery", back_populates="case", cascade="all, delete")

class SearchQuery(Base):
    __tablename__ = "search_queries"
    id = Column(Integer, primary_key=True)
    query_text = Column(String(255), nullable=False)
    filters = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    case_id = Column(Integer, ForeignKey("cases.id"))
    case = relationship("Case", back_populates="search_queries")

class ProcessedDocument(Base):
    __tablename__ = "processed_documents"
    id = Column(Integer, primary_key=True)
    filename = Column(String(255))
    content = Column(Text)
    processed_data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    case_id = Column(Integer, ForeignKey("cases.id"))
    case = relationship("Case", back_populates="processed_documents")

class CourtDecision(Base):
    __tablename__ = "court_decisions"
    id = Column(Integer, primary_key=True)
    decision_text = Column(Text)
    judge = Column(String(128))
    date = Column(DateTime)
    metadata = Column(JSON)
    case_id = Column(Integer, ForeignKey("cases.id"))
    case = relationship("Case", back_populates="decisions")
    precedents = relationship("LegalPrecedent", back_populates="decision", cascade="all, delete")

class LegalPrecedent(Base):
    __tablename__ = "legal_precedents"
    id = Column(Integer, primary_key=True)
    citation = Column(String(255))
    summary = Column(Text)
    decision_id = Column(Integer, ForeignKey("court_decisions.id"))
    decision = relationship("CourtDecision", back_populates="precedents")