FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev \
    # Additional dependencies
    && apt-get install -y telnet netcat \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./compose/local/fastapi/entrypoint.bash /entrypoint.bash
# sed is used to process the line endings of the shell scripts, 
# which converts Windows line endings to UNIX line endings
RUN sed -i 's/\r$//g' /entrypoint.bash
RUN chmod +x /entrypoint.bash

COPY ./compose/local/fastapi/start.bash /start.bash
RUN sed -i 's/\r$//g' /start.bash
RUN chmod +x /start.bash

COPY ./compose/local/fastapi/celery/worker/start.bash /start-celeryworker.bash
RUN sed -i 's/\r$//g' /start-celeryworker.bash
RUN chmod +x /start-celeryworker.bash

COPY ./compose/local/fastapi/celery/beat/start.bash /start-celerybeat.bash
RUN sed -i 's/\r$//g' /start-celerybeat.bash
RUN chmod +x /start-celerybeat.bash

COPY ./compose/local/fastapi/celery/flower/start.bash /start-flower.bash
RUN sed -i 's/\r$//g' /start-flower.bash
RUN chmod +x /start-flower.bash

WORKDIR /project

ENTRYPOINT ["/entrypoint.bash"]
