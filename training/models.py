from django.db import models
from rest_framework import serializers

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


class TaskSerializer(serializers.Serializer):
    Word = serializers.CharField()
    Context_Before = serializers.CharField()
    Pass = serializers.CharField()
    Context_After = serializers.CharField()
    class Meta:
        fields = [
            "Word",
            "Context_Before",
            "Pass",
            "Context_After"
        ]
        


class WordsSerializer(serializers.ListSerializer):
    child = TaskSerializer()


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

