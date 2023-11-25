from django.contrib import admin

from .models import Medic
from .models import Membership

# Register your models here.
admin.site.register(Medic)
admin.site.register(Membership)
