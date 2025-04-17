import random
import json

from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

from rest_framework.exceptions import bad_request

from training.models import Task_9, Task_10, Task_11, Task_12
from training.serializers import TaskSerializer, WordsSerializer

from main.models import Profile


def get_end(request: WSGIRequest, task=9, limit=0):
    if request.method == "POST":
        return bad_request(request, "Only GET method")

    if not(9 <= task <= 12):
        return bad_request(request, "No such table")
    

    words = WordsSerializer(tasks[task].objects.all()).data
    if limit == 0:
        limit = len(words)
    
    words = filter(lambda word: word['Pass'][-1] == 0, words)

    words_shuffeled = words.copy()
    random.shuffle(words_shuffeled)
    return JsonResponse({"words": words_shuffeled[:limit]})