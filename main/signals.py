from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from main.models import Profile
from training.models import Stats


@receiver(post_save, sender=User)
def create_links(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Stats.objects.create(user=instance)
