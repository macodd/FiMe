from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import FimeUser


class FimeUserCreationForm(UserCreationForm):
    class Meta:
        model = FimeUser
        fields = ("username", "email")


class FimeUserChangeForm(UserChangeForm):
    class Meta:
        model = FimeUser
        fields = ("username", "email")
