from django.urls import path, include

from .views import DashboardPageView

app_name = "dashboard"

urlpatterns = [
    path("", DashboardPageView.as_view(), name="home"),
    path("patient/", include("patient.urls", namespace="patient")),
]
