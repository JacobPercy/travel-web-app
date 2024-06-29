from __future__ import annotations

from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import SignupUserForm


class SignupView(FormView):
    success_url = reverse_lazy("dashboard:startup")
    form_class = SignupUserForm
    template_name = "registration/signup.html"

    def form_valid(self, form: SignupUserForm):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
