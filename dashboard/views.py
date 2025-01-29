from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from dashboard.forms import TaskCreateForm, TaskUpdateForm
from dashboard.models import Task


class HomePageView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").order_by("-is_done")
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm

    def form_valid(self, form):
        response = super().form_valid(form)
        if "tags" in form.cleaned_data:
            self.object.tags.set(form.cleaned_data["tags"])
        return response

    success_url = reverse_lazy("dashboard:index")



class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm

    def form_valid(self, form):
        response = super().form_valid(form)
        if "tags" in form.cleaned_data:
            self.object.tags.set(form.cleaned_data["tags"])
        return response

    success_url = reverse_lazy("dashboard:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("dashboard:index")
