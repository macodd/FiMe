from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import FimeUser
from .validators import valid_phone


class FimeUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=16, validators=[valid_phone])
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        model = FimeUser
        fields = ["first_name", "last_name", "email", "phone", "username"]


class FimeUserChangeForm(UserChangeForm):
    phone = forms.CharField(max_length=16, validators=[valid_phone])
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        model = FimeUser
        fields = ["first_name", "last_name", "email", "phone", "username"]
