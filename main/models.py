from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.validators import RegexValidator

import PIL
import os
import uuid

class Profile(models.Model):
    """
    Доп. таблица к пользователю
    :param user: Пользователь 
    :param icon: Аватрка
    :param telegram: Телеграм (без @)
    :param phone: Номер телефона
    """
    def path_file(instance, filename):
        """
        Функция, которая переименовывает файл на уникальный идентификатор
        :param instance: модель
        :param filename: имя получаемого файла
        """
        unique_id = uuid.uuid4()
        ext = filename.split('.')[-1]

        new_filename = f"{unique_id}.{ext}"
        return os.path.join("avatars/", new_filename)


    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        default="",
    )
    
    icon = models.ImageField(
        null=True,
        blank=True, 
        upload_to=path_file,
    )

    telegram = models.CharField(
        null=True, 
        blank=True,
        default="", 
        #unique=True,
        max_length=64
    )
    
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(
        validators=[phoneNumberRegex], 
        max_length=16, 
        #unique=True, 
        null=True, 
        blank=True, 
        default="",
    )

    subscribe = models.BooleanField(default=False)
