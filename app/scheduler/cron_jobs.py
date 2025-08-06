"""Scheduled job definitions for FastAPI startup."""
from fastapi import FastAPI
from app.tasks.data_updater import weekly_update

def register_cron_jobs(app: FastAPI):
    @app.on_event("startup")
    async def schedule_weekly_update():
        from celery import current_app
        current_app.send_task("app.tasks.data_updater.weekly_update")