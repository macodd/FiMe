from django.urls import path

from .views import (
    MedicRegisterView,
    RegistrationSuccessView,
    UserLoginView,
    UserLogoutView,
)


app_name = "accounts"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", MedicRegisterView.as_view(), name="register"),
    path("success/", RegistrationSuccessView.as_view(), name="success"),
]
