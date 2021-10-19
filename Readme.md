## Redis container

- Run: `docker run -p 6379:6379 --name redis-container -d redis`
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
