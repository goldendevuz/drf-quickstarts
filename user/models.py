from django.contrib.auth.models import AbstractUser
from anchor.models.fields import SingleAttachmentField

class User(AbstractUser):
    image = SingleAttachmentField()
