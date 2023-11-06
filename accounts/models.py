from django.db import models
from django.contrib.auth.models import AbstractUser


class FimeUser(AbstractUser):
    phone = models.CharField(max_length=16, null=True)

    def __str__(self):
        return self.email
