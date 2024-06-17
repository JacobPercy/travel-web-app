from __future__ import annotations

import pytest

USERNAME = "jasongrace2282"
PASSWORD = "Made with <3"

# flake8: noqa


@pytest.fixture
def user(django_user_model):
    user, _ = django_user_model().objects.get_or_create(username=USERNAME)
    user.set_password(PASSWORD)


@pytest.fixture
def client_login(client, user):
    client.login(username=USERNAME, password=PASSWORD)
