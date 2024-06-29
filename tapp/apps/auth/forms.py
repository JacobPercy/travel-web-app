from __future__ import annotations

from django.contrib.auth.forms import UserCreationForm


class SignupUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        fields = ("username", "password1", "password2")
        for field in fields:
            self.fields[field].widget.attrs.update({"class": "form-control w-25"})
