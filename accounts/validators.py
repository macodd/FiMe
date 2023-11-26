from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def valid_phone(value: str):
    if not value.isdigit():
        raise ValidationError(_(f"Phone must be only digits"), params={"value": value})
    if len(value) != 10:
        raise ValidationError(
            _(f"Phone must be 10 digits long"), params={"value": value}
        )
