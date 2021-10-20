import os
import pathlib
from functools import lru_cache

# I do not recommend pydantic BaseSettings here because
# it might cause Celery to raise [ERROR/MainProcess]
# pidbox command error: KeyError('__signature__') error when we
# launch Flower


class BaseConfig:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parents[1]

    DATABASE_URL: str = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3"
    )
    DATABASE_CONNECT_DICT: dict = {}
    CELERY_CONFIG: dict = {
        "broker_url": os.environ.get("broker_url", "redis://127.0.0.1:6379/0"),
        "result_backend": os.environ.get("result_backend", "redis://127.0.0.1:6379/0"),
    }


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig,
    }

    config_name = os.environ.get("FASTAPI_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()
