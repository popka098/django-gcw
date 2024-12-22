from django.db import models

# Модель User не создавать

class Profile(models.Model):
    """
    Доп. таблица к пользователю
    """
    pass


class Vote(models.Model):
    pass
