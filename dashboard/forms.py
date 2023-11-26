from django import forms

from .validators import valid_search
from .enums import SearchFormType


class SearchForm(forms.Form):
    patient_search = forms.CharField(
        min_length=2,
        max_length=300,
        validators=[valid_search],
        widget=forms.TextInput(
            attrs={
                "class": "form-control me-2",
                "placeholder": "Search by last name..",
                "onkeyup": "searchFunction()",
            }
        ),
    )

    def clean_patient_search(self):
        data = {}
        search: str = self.cleaned_data.get("patient_search")
        if search.isdigit():
            data = {"id": search, "form_type": SearchFormType.DIGIT}
        else:
            search_data = search.split(",")
            if len(search_data) == 1:
                data = {
                    "last_name": search_data[0],
                    "form_type": SearchFormType.ONE_VALUE,
                }
            elif len(search_data) == 2:
                data = {
                    "first_name": search_data[1],
                    "last_name": search_data[0],
                    "form_type": SearchFormType.TWO_VALUE,
                }
        return data
