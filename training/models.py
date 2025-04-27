from django.db import models

from main.models import Profile
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    """Абстрактная модель слова для задания

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
    """слова задания 9

    """
    pass
class Task_10(Task):
    """слова задания 10

    """
    pass

class Task_11(Task):
    """слова задания 11

    """
    pass

class Task_12(Task):
    """слова задания 12

    """
    pass

class Task_15(Task):
    """слова задания 15

    """
    pass

class Stats(models.Model):
    """статистика тренировок пользователя

    :param time: все проведенное время (в секундах)
    :param successes: количество правильных ответов
    :param mistakes: количество ошибок
    :param user: пользователь
    """
    time = models.IntegerField(default=0)
    successes = models.IntegerField(default=0)
    mistakes = models.IntegerField(default=0)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class Atts(models.Model):
    """попытка

    :param time: затраченное проведенное время (в секундах)
    :param successes: количество правильных ответов
    :param mistakes: количество ошибок
    :param user: пользователь
    """
    time = models.IntegerField()
    successes = models.IntegerField()
    mistakes = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class MistakesAnswers(models.Model):
    """ошибки

    :param input_answer: введенный ответ
    :param correct_answer: правильный ответ
    :param att: попытка
    """
    input_answer = models.TextField()
    correct_answer = models.TextField()
    att = models.ForeignKey(to=Atts, on_delete=models.CASCADE)
