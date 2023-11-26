from django.shortcuts import render
from django.contrib import messages

from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from medic.models import Medic
from patient.models import Patient
from .forms import SearchForm


class DashboardPageView(LoginRequiredMixin, FormMixin, ListView):
    login_url = "accounts/login"
    template_name = "dashboard/home.html"
    form_class = SearchForm

    def get_queryset(self):
        medic_obj = Medic.objects.get(user=self.request.user)
        return medic_obj.patients.values_list("first_name", "last_name", "dob").values()

    def post(self, request, *args, **kwargs):
        form: SearchForm = self.get_form()
        context = {"form": SearchForm}
        if form.is_valid():
            data = form.cleaned_data
            form_type = data["form_type"]
            if form_type.is_digit():
                qs = Patient.objects.values_list(
                    "first_name", "last_name", "dob"
                ).filter(id__exact=data["id"])
            elif form_type.is_one_value():
                qs = Patient.objects.values_list(
                    "first_name", "last_name", "dob"
                ).filter(last_name__startswith=data["last_name"])
            else:
                qs = Patient.objects.values_list(
                    "first_name", "last_name", "dob"
                ).filter(
                    last_name__startswith=data["last_name"],
                    first_name__startswith=data["first_name"],
                )
            if not qs.exists():
                messages.warning(request, "No patient found.")
            else:
                context.update({"patient_list": qs.values()})
        return render(request, self.template_name, context)
