from __future__ import annotations

from django.urls import path

from .views import StartupView

app_name = "dashboard"

urlpatterns = [
    path("", StartupView.as_view(), name="startup"),
]
