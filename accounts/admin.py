from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from .forms import FimeUserCreationForm, FimeUserChangeForm
from .models import FimeUser


class FimeUserAdmin(UserAdmin):
    add_form = FimeUserCreationForm
    form = FimeUserChangeForm
    model = FimeUser
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "phone")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = [
        "email",
        "username",
    ]


admin.site.register(FimeUser, FimeUserAdmin)
