from django.db import models

from patient.models import Patient


class Visit(models.Model):
    patient: Patient = models.OneToOneField(to=Patient, on_delete=models.CASCADE)
    blood_pressure = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    body_temperature = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    pulse_rate = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    respiration_rate = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    oxygen_level = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    visit_reason = models.CharField(null=True, max_length=256)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.pk
