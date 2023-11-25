from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from dashboard.enums import PatientFormType


class PatientSearchForm(forms.Form):
    patient_search = forms.CharField(
        min_length=2,
        max_length=300,
        widget=forms.TextInput(
            attrs={
                "class": "form-control me-2",
                "placeholder": "Search by last name..",
                "onkeyup": "searchFunction()",
            }
        ),
    )

    def clean(self):
        data = {}
        search: str = self.cleaned_data.get("patient_search")
        if search.isdigit():
            if len(search) != 10:
                raise ValidationError(
                    _(f"ID must be 10 digits long", params={"ID": search})
                )
            data = {"id": search, "form_type": PatientFormType.DIGIT}
        else:
            search_data = search.split(",")
            if len(search_data) > 2:
                raise ValidationError(
                    _(
                        f"Search must be: last name, first name",
                        params={"search": search},
                    )
                )
            elif len(search_data) == 1:
                if len(search_data[0]) < 2:
                    raise ValidationError(
                        _(
                            f"Last name must be 2 digits long",
                            params={"last_name": search_data[0]},
                        )
                    )
                data = {
                    "last_name": search_data[0],
                    "form_type": PatientFormType.ONE_VALUE,
                }
            elif len(search_data) == 2:
                if len(search_data[0]) < 2 or len(search_data[1]) < 2:
                    raise ValidationError(
                        _(
                            f"Last name and First name must be 2 letters long",
                            params={
                                "last_name": search_data[0],
                                "first_name": search_data[1],
                            },
                        )
                    )
                data = {
                    "first_name": search_data[1],
                    "last_name": search_data[0],
                    "form_type": PatientFormType.ONE_VALUE,
                }
        return data
