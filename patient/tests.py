from django.test import TestCase

from .choices import BloodType
from .forms import PatientCreateForm


class PatientCreateFormTest(TestCase):
    def setUp(self):
        self.data = {
            "id": "1111111111",
            "first_name": "test-first-name",
            "last_name": "test-last-name",
            "dob": "2023-01-01",
            "blood_type": BloodType.UNKNOWN,
        }

    def test_valid_form(self):
        form = PatientCreateForm(data=self.data)
        self.assertTrue(form.is_valid())
        patient = form.save()
        self.assertEquals(BloodType.UNKNOWN, patient.blood_type)

    def test_invalid_form(self):
        data = self.data
        data["id"] = "1"
        form = PatientCreateForm(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertFormError(form, "id", ["ID must be 10 digits long"])
        data["id"] = "a"
        form = PatientCreateForm(data=self.data)
        self.assertFalse(form.is_valid())
        self.assertFormError(form, "id", ["ID must be only digits"])
