from __future__ import annotations

from datetime import datetime

from celery import shared_task

from .models import VisitorLog


@shared_task
def track_visitor(url: str):
    # Create a visitor log entry
    VisitorLog.objects.create(
        timestamp=datetime.now(),
        url=url.removeprefix("/explore/"),
    )
