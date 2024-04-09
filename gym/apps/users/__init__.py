from django.db.models import TextChoices


class Roles(TextChoices):
    CLIENT = "CLIENT", "Клиент"
    TRAINER = "TRAINER", "Тренер"
    ADMIN = "ADMIN", "Админ"
