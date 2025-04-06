import random

from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

words = ["привет", "пока", "база данных", "тестирование", "матвей", "сделай", "эту", "задачу", "пожалуйста"]

def get_all_words(request: WSGIRequest):
    limit = -1
    if limit == -1:
        limit = len(words)
    words_shuffeled = words.copy()
    random.shuffle(words_shuffeled)
    return JsonResponse({"words": words_shuffeled[:limit]})