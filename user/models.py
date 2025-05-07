from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']
