from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator

import PIL
import os
import uuid

class Profile(models.Model):
    """
    Доп. таблица к пользователю
    """
    def path_file(instance, filename):
        """
        Функция, которая переименовываает файл на уникальный индентификатор
        :param instance: модель
        :param filename: имя получаемого файла
        """
        uniqe_id = uuid.uuid4()
        ext = filename.split('.')[-1]

        new_filename = f"{uniqe_id}.{ext}"
        return os.path.join("avatars/", new_filename)


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    icon = models.ImageField(null=True,
                             blank=True, 
                             upload_to=path_file
                            )

    telegram = models.CharField(null=True, 
                                blank=True, 
                                unique=True
                               )
    
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phoneNumberRegex], 
                             max_length=16, 
                             unique=True, 
                             null=True, 
                             blank=True, 
                            )
