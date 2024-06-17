from __future__ import annotations

from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tapp.apps.auth"
    label = "tapp_auth"
