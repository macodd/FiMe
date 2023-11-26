from django import forms
from .models import Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = [
            "blood_pressure",
            "body_temperature",
            "pulse_rate",
            "respiration_rate",
            "oxygen_level",
            "visit_reason",
        ]
