from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def valid_ruc(value: str):
    if not value.isdigit():
        raise ValidationError(_(f"RUC must be only digits"), params={"value": value})
    if len(value) != 13:
        raise ValidationError(_(f"RUC must be 13 digits long"), params={"value": value})
