from django.db import models

from main.models import Profile
from django.contrib.auth.models import User

# Create your models here.

class Stats(models.Model):
    time = models.IntegerField()
    successes = models.IntegerField()
    mistakes = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class Atts(models.Model):
    time = models.IntegerField()
    successes = models.IntegerField()
    mistakes = models.IntegerField()
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

 class MistakesAnswers(models.Model):
     input_answer = models.TextField()
     correct_answer = models.TextField()
     att = models.ForeignKey(to=Atts, on_delete=models.CASCADE)