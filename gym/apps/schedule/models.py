from django.db import models

from gym.apps.gyms.models import Gym
from gym.apps.trainers.models import Trainer


class Schedule(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Настройка: Расписание"

    def __str__(self):
        return f"{self.trainer and self.start_time}"
