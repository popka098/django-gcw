from django.db import models
from django.contrib.auth.models import User


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
class Profile(models.Model):
    """
    Доп. таблица к пользователю
    """
    pass
