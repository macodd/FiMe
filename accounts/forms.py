from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import FimeUser
from .validators import valid_ruc, valid_phone
from medic.models import Medic


class FimeUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=16, validators=[valid_phone])

    class Meta:
        model = FimeUser
        fields = ["first_name", "last_name", "email", "phone", "username"]


class FimeUserChangeForm(UserChangeForm):
    phone = forms.CharField(max_length=16, validators=[valid_phone])

    class Meta:
        model = FimeUser
        fields = ["first_name", "last_name", "email", "phone", "username"]


class MedicRegister(forms.ModelForm):
    ruc = forms.CharField(max_length=13, validators=[valid_ruc])

    class Meta:
        model = Medic
        fields = ["ruc"]
