from django.db import models

# Create your models here.

class Task(models.Model):
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

