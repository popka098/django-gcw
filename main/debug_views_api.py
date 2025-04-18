import random

from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

from rest_framework.exceptions import bad_request

from training.models import Task_9, Task_10, Task_11, Task_12
from training.serializers import WordsSerializer


tasks = {
    9: Task_9,
    10: Task_10,
    11: Task_11,
    12: Task_12
}

def get_end(request: WSGIRequest, task=9, limit=0):
    if request.method == "POST":
        return bad_request(request, "Only GET method")

    if not(9 <= task <= 12):
        return bad_request(request, "No such table")
    

    words = WordsSerializer(tasks[task].objects.all()).data
    if limit == 0:
        limit = len(words)
    
    words = filter(lambda word: word['Pass'][-1] == 0, words)

    words_shuffled = words.copy()
    random.shuffle(words_shuffled)
    return JsonResponse({"words": words_shuffled[:limit]})