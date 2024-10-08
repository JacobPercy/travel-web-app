from __future__ import annotations

from django.contrib.auth import views as auth_views
from django.urls import path

from .views import SignupView

app_name = "auth"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
]
