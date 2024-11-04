from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    point = models.IntegerField(default=0)
