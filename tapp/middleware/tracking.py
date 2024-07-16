from __future__ import annotations

from ..apps.dashboard.tasks import track_visitor


class TrackingMiddleware:
    """Track how many times a user visits a url."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith("/explore/"):
            track_visitor.run(request.path)
        return response
