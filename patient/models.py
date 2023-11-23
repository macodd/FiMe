from django.db import models

from .choices import BloodType


class Patient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null=False)
    dob = models.DateField(null=False)
    blood_type = models.PositiveSmallIntegerField(
        default=BloodType.UNKNOWN.value, choices=BloodType.choices
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        super().save(*args, **kwargs)

    def get_blood_type(self):
        return BloodType(self.blood_type).name

    def set_blood_type(self, blood_type: BloodType, commit: bool = False):
        self.blood_type = blood_type.value
        if commit:
            self.save()
