from django.shortcuts import render
from django.views import generic

from dashboard.models import Task


class HomePageView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "base.html"