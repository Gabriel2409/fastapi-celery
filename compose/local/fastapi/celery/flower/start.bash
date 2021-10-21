#!/bin/bash

set -o errexit
set -o nounset

worker_ready() {
    celery -A app.main.celery inspect ping
}

until worker_ready; do
  >&2 echo 'Celery workers not available'
  sleep 1
done
>&2 echo 'Celery workers is available'

celery -A app.main.celery --broker="${broker_url}" flower flower --port=5555
