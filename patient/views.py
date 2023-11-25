from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PatientCreateForm

from medic.models import Medic
from medic.models import Membership


class PatientCreateView(LoginRequiredMixin, CreateView):
    template_name = "patient/patient_create.html"
    form_class = PatientCreateForm
    success_url = "dashboard/home"

    def form_valid(self, form):
        patient_obj = form.save(commit=False)
        medic_obj = Medic.objects.get(user=self.request.user)
        qs = Membership.objects.filter(medic=medic_obj, patient=patient_obj)
        if qs.exists():
            raise ValueError("Relationship already exists")
        patient_obj.save()
        membership_obj = Membership(medic=medic_obj, patient=patient_obj, active=True)
        membership_obj.save()
        return redirect("dashboard:home")
