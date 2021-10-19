from app.routers import hello
from celery import Celery
from fastapi import FastAPI


def create_app() -> FastAPI:
    """Creates application"""
    app = FastAPI()
    app.include_router(hello.router)

    return app


app = create_app()

celery = Celery(
    __name__, broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0"
)


@celery.task
def divide(x, y):
    """divide task celery"""
    import time

    time.sleep(5)
    return x / y
