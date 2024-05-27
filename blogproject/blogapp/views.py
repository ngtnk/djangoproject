from django.views.generic.base import TemplateView
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = "index.html"


def index_view(request):
    return render(request, "index.html")
