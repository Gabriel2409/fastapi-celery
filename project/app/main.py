from app.config import settings
from app.routers import hello, math, users
from celery import current_app as current_celery_app
from fastapi import FastAPI


def create_celery():
    celery_app = current_celery_app
    celery_app.config_from_object(settings.CELERY_CONFIG)

    celery_app.autodiscover_tasks(["app.tasks.math"])

    return celery_app


def create_app() -> FastAPI:
    """Creates application"""
    app = FastAPI()
    app.celery_app = create_celery()
    app.include_router(users.router)
    app.include_router(math.router)

    app.include_router(hello.router)

    return app


app = create_app()
celery = app.celery_app
