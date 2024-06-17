from __future__ import annotations

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupUserForm


class SignupView(CreateView):
    success_url = reverse_lazy("auth:login")
    form_class = SignupUserForm
