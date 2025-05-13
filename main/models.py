from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

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

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
