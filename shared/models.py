from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords

class HistoricalRecordsModel(models.Model):
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

class User(AbstractUser, HistoricalRecordsModel):
    pass