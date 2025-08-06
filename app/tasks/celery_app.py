"""Celery app configuration with Redis broker/beat."""
from celery import Celery
from config.settings import settings

celery_app = Celery(
    "brazillawyer",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["app.tasks.scraping_tasks", "app.tasks.data_updater"]
)

celery_app.conf.beat_schedule = {
    "weekly-case-law-update": {
        "task": "app.tasks.data_updater.weekly_update",
        "schedule": 604800.0,  # one week in seconds
    },
}
celery_app.conf.timezone = "America/Sao_Paulo"