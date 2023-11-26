from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def valid_search(value):
    if value.isdigit():
        if len(value) != 10:
            raise ValidationError(_(f"ID must be 10 digits long", params={"ID": value}))
    else:
        search_data = value.split(",")
        if len(search_data) > 2:
            raise ValidationError(
                _("Search must be: last name, first name"),
                params={"patient_search": value},
            )
        elif len(search_data) == 1:
            if len(search_data[0]) < 2:
                raise ValidationError(
                    _("Last name must be 2 digits long"),
                    params={"last_name": search_data[0]},
                )
        elif len(search_data) == 2:
            if len(search_data[0]) < 2 or len(search_data[1]) < 2:
                raise ValidationError(
                    _("Last name and First name must be 2 letters long"),
                    params={
                        "last_name": search_data[0],
                        "first_name": search_data[1],
                    },
                )
