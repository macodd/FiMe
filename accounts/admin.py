from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import FimeUserCreationForm, FimeUserChangeForm
from .models import FimeUser


class CustomUserAdmin(UserAdmin):
    add_form = FimeUserCreationForm
    form = FimeUserChangeForm
    model = FimeUser
    list_display = [
        "email",
        "username",
    ]


admin.site.register(FimeUser, CustomUserAdmin)
