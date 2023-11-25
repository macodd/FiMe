from django import forms

from .models import Medic
from .validators import valid_ruc


class MedicRegister(forms.ModelForm):
    ruc = forms.CharField(max_length=13, validators=[valid_ruc])

    class Meta:
        model = Medic
        fields = ["ruc"]
