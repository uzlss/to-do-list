from django.urls import path

from dashboard.views import (
    HomePageView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleDoneView,
    TagListView,
    TagCreateView,
    TagUpdateView, TagDeleteView
)

app_name = "dashboard"


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete-confirm"
    ),
    path(
        "tasks/<int:pk>/toggle_done/",
        TaskToggleDoneView.as_view(),
        name="task-toggle-done"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete-confirm"
    ),
]
