from __future__ import annotations

from django.views.generic import TemplateView


class StartupView(TemplateView):
    template_name = "startup.html"
