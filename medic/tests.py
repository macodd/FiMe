from django.test import TestCase

from .forms import MedicRegister


class MedicRegisterTest(TestCase):
    def test_valid_form(self):
        data = {"ruc": "1111111111111"}
        form = MedicRegister(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_ruc_length(self):
        data = {"ruc": "111111111111"}
        form = MedicRegister(data=data)
        self.assertFormError(form, "ruc", ["RUC must be 13 digits long"])

    def test_invalid_ruc_digits(self):
        data = {"ruc": "abcdefghijkl"}
        form = MedicRegister(data=data)
        self.assertFormError(form, "ruc", ["RUC must be only digits"])
