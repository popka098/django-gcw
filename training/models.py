from django.db import models

from main.models import Profile
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    """
    Абстрактная модель для задания
    :param Word: Слово
    :param Context_Before: Контекст перед словом
    :param Pass: Слово с пропуском
    :param Context_After: Контекст после слова
    """
    Word = models.CharField(
        max_length=256, 
        blank=False,
    )
    Context_Before = models.CharField(
        max_length=256, 
        blank=True, 
        default="",
    )
    Pass = models.CharField(
        max_length=256, 
        blank=False,
    )
    Context_After = models.CharField(
        max_length=256, 
        blank=True, default="",
    )

    class Meta:
        abstract = True

class Task_9(Task):
    pass
class Task_10(Task):
    pass

class Task_11(Task):
    pass

class Task_12(Task):
    pass

class Task_15(Task):
    pass

class Stats(models.Model):
    time = models.IntegerField(default=0)
    successes = models.IntegerField(default=0)
    mistakes = models.IntegerField(default=0)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class Atts(models.Model):
    time = models.IntegerField()
    successes = models.IntegerField()
    mistakes = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class MistakesAnswers(models.Model):
    input_answer = models.TextField()
    correct_answer = models.TextField()
    att = models.ForeignKey(to=Atts, on_delete=models.CASCADE)
