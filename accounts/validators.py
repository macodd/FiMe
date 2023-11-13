from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def valid_ruc(value: str):
    _check_length(value, 13)


def valid_phone(value: str):
    _check_length(value, 10)


def _check_length(value: str, length: int) -> None:
    if not value.isdigit():
        raise ValidationError(
            _(f"{value} must be only digits"), params={"value": value}
        )
    if len(value) != length:
        raise ValidationError(
            _(f"{value} must be {length} digits long"), params={"value": value}
        )
