import subprocess

from watchgod import run_process


def celery_worker():
    def run_worker():
        subprocess.call(
            ["celery", "-A", "app.main.celery", "worker", "--loglevel=info"]
        )

    run_process("./", run_worker)


if __name__ == "__main__":
    celery_worker()
