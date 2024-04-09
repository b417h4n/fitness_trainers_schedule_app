from django.db import models

from gym.apps.schedule.models import Schedule
from gym.apps.users.models import User


class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"{self.client.name and self.schedule.name}"
