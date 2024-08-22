from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index_view(request):
    return render(request, "learn/index.html")
