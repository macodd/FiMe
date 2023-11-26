from django import forms
from datetime import date

from .models import Patient
from .validators import valid_id
from .choices import BloodType


class PatientCreateForm(forms.ModelForm):
    id = forms.CharField(max_length=10, validators=[valid_id])
    dob = forms.DateField(
        widget=forms.SelectDateWidget(
            years=[x for x in range(date.today().year, date.today().year - 100, -1)],
        )
    )
    blood_type = forms.ChoiceField(choices=BloodType.choices)

    class Meta:
        model = Patient
        fields = ["id", "first_name", "last_name", "dob", "blood_type"]
