from django.urls import path

from dashboard.views import HomePageView

app_name = "dashboard"


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
]