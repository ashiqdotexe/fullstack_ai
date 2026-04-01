from celery import Celery

celery_app = Celery(
    "task",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["myqueue.worker"]
)