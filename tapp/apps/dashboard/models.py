from __future__ import annotations

from django.db import models


class VisitorLog(models.Model):
    """A model to store information about the url accessed by a visitor."""

    timestamp = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return f"{self.timestamp} - {self.url}"
