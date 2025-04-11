import random

from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

from training.models import Task_9, Task_10, Task_11, Task_12
from training.models import TaskSerializer, WordsSerializer



def get_all_words(request: WSGIRequest, limit=0):
    words = ""
    # words = (
    #     list(Task_9.objects.all()) + 
    #     list(Task_10.objects.all()) +
    #     list(Task_11.objects.all()) +
    #     list(Task_12.objects.all())
    # )
    
    # print(words)
    # print(list(Task_9.objects.all()))


    if limit == 0:
        limit = len(words)
    
    words_shuffeled = words.copy()
    random.shuffle(words_shuffeled)
    return JsonResponse({"": ""})
    return JsonResponse(words[:limit], safe=False)



def serializator_testing(request: WSGIRequest):
    words = Task_11.objects.all()
    ser = WordsSerializer(words)

    
    return JsonResponse({"words": ser.data})

