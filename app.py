from celery import Celery

from api import create_app

app = create_app()


celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0",
)


@app.route("/")
def index():
    return "Hello, World"


@celery.task
def divide(x, y):
    import time

    time.sleep(5)
    return x / y
