from django.db import models
from django.conf import settings

from patient.models import Patient
from specialty.models import Specialty


class Medic(models.Model):
    ruc = models.BigIntegerField(primary_key=True)  # must have RUC
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )
    specialties = models.ManyToManyField(to=Specialty, through="Education")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    patients = models.ManyToManyField(to=Patient, through="Membership")

    def __str__(self):
        return f"{self.ruc:013}"


class Membership(models.Model):
    patient = models.ForeignKey(to=Patient, on_delete=models.PROTECT)
    medic = models.ForeignKey(to=Medic, on_delete=models.PROTECT)
    date_linked = models.DateField(auto_now_add=True)
    date_unlinked = models.DateField(null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return "patient_id: %s, medic_id: %s" % (self.patient_id, self.medic_id)


class Education(models.Model):
    medic = models.ForeignKey(to=Medic, on_delete=models.PROTECT)
    specialty = models.ForeignKey(to=Specialty, on_delete=models.PROTECT)
    date_linked = models.DateField(auto_now_add=True)

    def __str__(self):
        return "specialty_id: %s, medic_id: %s" % (self.specialty_id, self.medic_id)
