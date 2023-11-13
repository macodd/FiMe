from django.db import models
from django.contrib.auth.models import AbstractUser


class FimeUser(AbstractUser):
    phone = models.CharField(max_length=16, null=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        super().save(*args, **kwargs)
