from __future__ import annotations

from django import forms
from django.contrib.auth import get_user_model


class SignupUserForm(forms.ModelForm):
    template_name = "registration/signup.html"

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "password",
        ]
