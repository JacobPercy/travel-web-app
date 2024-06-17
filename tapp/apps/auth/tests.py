from __future__ import annotations

from django.urls import reverse


def test_homepage_not_404(client):
    response = client.get(reverse("dashboard:startup"))
    assert response.status_code == 200
