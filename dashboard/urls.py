from django.urls import path

from dashboard.views import (
    HomePageView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)

app_name = "dashboard"


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete-confirm"),

]