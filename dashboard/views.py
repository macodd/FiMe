from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from medic.models import Medic


class DashboardPageView(LoginRequiredMixin, ListView):
    login_url = "accounts/login"
    template_name = "dashboard/home.html"

    def get_queryset(self):
        medic_obj = Medic.objects.get(user=self.request.user)
        return medic_obj.patients.values_list("first_name", "last_name", "dob").values()
