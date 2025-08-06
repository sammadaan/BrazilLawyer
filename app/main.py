"""Main FastAPI application with all routers and DB init."""
from fastapi import FastAPI
from app.database import init_db
from config.logging import setup_logging

from app.routers import cases, search, documents, reports, admin

setup_logging()

app = FastAPI(title="BrazilLawyer AI Backend")

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(cases.router)
app.include_router(search.router)
app.include_router(documents.router)
app.include_router(reports.router)
app.include_router(admin.router)