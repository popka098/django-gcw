import random

from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

from training.models import Task_9, Task_10, Task_11, Task_12
from training.models import TaskSerializer, WordsSerializer



def get_all_words(request: WSGIRequest, limit=0):
    words = (
        WordsSerializer(Task_9.objects.all()).data +
        WordsSerializer(Task_10.objects.all()).data +
        WordsSerializer(Task_11.objects.all()).data +
        WordsSerializer(Task_12.objects.all()).data
    )

    if limit == 0:
        limit = len(words)
    
    words_shuffeled = words.copy()
    random.shuffle(words_shuffeled)
    return JsonResponse({"words": words_shuffeled[:limit]})


def serializater_testing(request: WSGIRequest):
    words = Task_11.objects.all()
    ser = WordsSerializer(words)
    return JsonResponse({"words": ser.data})

