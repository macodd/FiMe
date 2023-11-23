from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(min_length=1, max_length=300)
