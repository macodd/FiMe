from django.urls import path

from .views import PatientCreateView

app_name = "patient"

urlpatterns = [
    path("create/", PatientCreateView.as_view(), name="create"),
]
