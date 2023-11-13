from django.db import models


class Specialty(models.Model):
    specialty = models.CharField(max_length=256)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.specialty
