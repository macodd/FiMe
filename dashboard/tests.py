from django.test import TestCase

from .forms import SearchForm
from .enums import SearchFormType


class SearchFormTypeTest(TestCase):
    def test_form_type(self):
        form_type = SearchFormType.DIGIT
        self.assertTrue(form_type.is_digit())
        self.assertFalse(form_type.is_one_value())
        form_type = SearchFormType.ONE_VALUE
        self.assertTrue(form_type.is_one_value())
        self.assertFalse(form_type.is_digit())
        form_type = SearchFormType.TWO_VALUE
        self.assertFalse(form_type.is_one_value())
        self.assertFalse(form_type.is_digit())


class SearchFormTest(TestCase):
    def test_valid_form(self):
        data = {"patient_search": "last_name, first_name"}
        form = SearchForm(data=data)
        self.assertTrue(form.is_valid())
        data = {"patient_search": "last_name"}
        form = SearchForm(data=data)
        self.assertTrue(form.is_valid())
        data = {"patient_search": "1111111111"}
        form = SearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        data = {"patient_search": "last_name, first_name, another_name"}
        form = SearchForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertFormError(
            form, "patient_search", ["Search must be: last name, first name"]
        )
