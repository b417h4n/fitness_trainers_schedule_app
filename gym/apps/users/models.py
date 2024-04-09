from django.db import models
from django.contrib.auth.models import AbstractUser

from gym.apps.users import Roles


class User(AbstractUser):
    role = models.CharField(max_length=15, choices=Roles.choices, default=Roles.CLIENT)

