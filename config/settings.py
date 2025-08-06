"""Application settings using environment variables."""
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str = "redis://redis:6379/0"
    GEMINI_API_KEY: str
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "brazillawyer"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: str = "5432"
    SPACY_MODEL: str = "pt_core_news_md"
    LANGUAGETOOL_URL: str = "https://api.languagetoolplus.com/v2/check"
    SECRET_KEY: str = "CHANGE_ME"
    class Config:
        env_file = ".env"

settings = Settings()