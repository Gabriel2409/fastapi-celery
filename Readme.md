## Redis container

- Run: `docker container run -p 6379:6379 --name redis-container -d redis`
- Test : `docker exec -it redis-container redis-cli ping`

## celery

```python
celery = Celery(
    __name__, broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0"
)
...

@celery.task
def divide(x, y):
    import time

    time.sleep(5)
    return x / y
```

- launch celery : `celery -A app.main.celery worker --loglevel=info`

- launch celery so that it auto reloads on code change : `python watch_celery.py`
```python
# watch_celery.py

from watchgod import run_process
import subprocess

def celery_worker():
    def run_worker():
        subprocess.call(
            ["celery", "-A", "app.main.celery", "worker", "--loglevel=info"]
        )

    run_process("./", run_worker)


if __name__ == "__main__":
    celery_worker()
```


```python
from main import app, divide

# send a task
task = divide.delay(1,2)

# see status
print(task.state, task.result)
```

```python
# get specific task
from celery.result import AsyncResult
task = AsyncResult('c4ecac49-d364-4593-a3c0-d06ca7d3949f')

```

## flower

Monitor celery

- launch flower: `celery -A app.main.celery flower --port=5555`

## sql alchemy

```python

# database/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-sqlalchemy-engine
engine = create_engine(
    settings.DATABASE_URL, connect_args=settings.DATABASE_CONNECT_DICT
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

## alembic

- `alembic init alembic`

In the created env.py add :

```python

from app.main import create_app
from app.config import settings
from app.database.models import Base
...

config.set_main_option("sqlalchemy.url", str(settings.DATABASE_URL))
fastapi_app = create_app()
target_metadata = Base.metadata
```

- create empty sqlite3 :

```python
>>> from main import app
>>> from project.database import Base, engine
>>> Base.metadata.create_all(bind=engine)
>>> exit()
```

- migrate db :
  - `alembic revision --autogenerate`
  - `alembic upgrade head`
