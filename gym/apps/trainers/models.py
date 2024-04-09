from django.db import models

from gym.apps.gyms.models import Gym
from gym.apps.users.models import User


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    gender = models.CharField(max_length=200, )
    gyms = models.ManyToManyField(Gym)

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

    def __str__(self):
        return self.user