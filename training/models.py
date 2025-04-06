from django.db import models

from main.models import Profile


# Create your models here.

class Stats(models.Model):
    time = models.IntegerField()
    successes = models.IntegerField()
    mistakes = models.IntegerField()
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)


class Atts(models.Model):
    time = models.IntegerField()
    successes = models.IntegerField()
    mistakes = models.IntegerField()
    stat = models.ForeignKey(to=Stats, on_delete=models.CASCADE)
