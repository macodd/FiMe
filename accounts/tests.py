from django.test import TestCase
from django.core.exceptions import ValidationError

from uuid import uuid4

from .forms import FimeUserCreationForm
from .models import FimeUser
from .validators import valid_phone


class FimeUserCreationFormTest(TestCase):
    def setUp(self):
        pw = uuid4()
        self.test_data = {
            "first_name": "test",
            "last_name": "test",
            "email": "test@test.com",
            "phone": "1111111111",
            "username": "test-user",
            "password1": pw,
            "password2": pw,
        }

    def test_valid_create_form(self):
        form = FimeUserCreationForm(data=self.test_data)
        self.assertTrue(form.is_valid())
        user: FimeUser = form.save()
        self.assertTrue(user.first_name.istitle())
        self.assertTrue(user.last_name.istitle())

    def test_invalid_phone_create_form(self):
        data = self.test_data
        data["phone"] = "1"
        form = FimeUserCreationForm(data=self.test_data)
        self.assertFormError(form, "phone", ["Phone must be 10 digits long"])

    def test_invalid_email_create_form(self):
        data = self.test_data
        data["email"] = "first name"
        form = FimeUserCreationForm(data=data)
        self.assertFormError(form, "email", ["Enter a valid email address."])


class FimeUserValidatorTest(TestCase):
    def test_valid_phone_only_digits(self):
        try:
            valid_phone("abc")
            self.assertTrue(False)
        except ValidationError as e:
            self.assertEquals("Phone must be only digits", e.message)

    def test_valid_phone_length(self):
        try:
            valid_phone("123456")
            self.assertTrue(False)
        except ValidationError as e:
            self.assertEquals("Phone must be 10 digits long", e.message)
