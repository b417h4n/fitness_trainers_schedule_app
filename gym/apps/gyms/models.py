from django.db import models


class Gym(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    equipment = models.TextField()

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"

    def __str__(self):
        return self.name
