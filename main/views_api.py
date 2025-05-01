"""main vews_api"""

import json
import random

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from rest_framework.exceptions import bad_request

from main.models import Profile
from training.models import (Atts, MistakesAnswers, Stats, Task9, Task10,
                             Task11, Task12)
from training.serializers import WordsSerializer

tasks = {
    9: Task9,
    10: Task10,
    11: Task11,
    12: Task12
}


def get_all_words(request: WSGIRequest, limit=0):
    """Получение всех слов

    :param request: реквест
    :type request: WSGIRequest
    :param limit: количество получемых слов (если 0 то все), defaults to 0
    :type limit: int, optional
    :return: json
    """
    if request.method == "POST":
        return bad_request(request, "Only GET method")

    words = (
        WordsSerializer(Task9.objects.all()).data +
        WordsSerializer(Task10.objects.all()).data +
        WordsSerializer(Task11.objects.all()).data +
        WordsSerializer(Task12.objects.all()).data
    )

    if limit == 0:
        limit = len(words)

    words_shuffled = words.copy()
    random.shuffle(words_shuffled)
    return JsonResponse({"words": words_shuffled[:limit]})


def get_random_words(request: WSGIRequest, task=9, limit=0):
    """получение нескольких случайных слов из определенного задания

    :param request: реквест
    :type request: WSGIRequest
    :param task: задание, defaults to 9
    :type task: int, optional
    :param limit: количество получаемых слов (если 0 то все), defaults to 0
    :type limit: int, optional
    :return: json
    """
    if request.method == "POST":
        return bad_request(request, "Only GET method")

    if not 9 <= task <= 12:
        return bad_request(request, "No such table")


    words = WordsSerializer(tasks[task].objects.all()).data
    if limit == 0:
        limit = len(words)

    words_shuffled = words.copy()
    random.shuffle(words_shuffled)
    return JsonResponse({"words": words_shuffled[:limit]})


def get_random_word(request: WSGIRequest, task=9):
    """Получение одного случанойго слова из задания

    :param request: реквест
    :type request: WSGIRequest
    :param task: задание, defaults to 9
    :type task: int, optional
    :return: json
    """
    if request.method == "POST":
        return bad_request(request, "Only GET method")

    if not 9 <= task <= 12:
        return bad_request(request, "No such table")

    words = WordsSerializer(tasks[task].objects.all()).data
    word = random.choice(words)

    return JsonResponse(word)


def get_user_sub(request: WSGIRequest):
    """Получение подписки пользователя

    :param request: реквест
    :type request: WSGIRequest
    :return: json
    """
    if request.method == "POST":
        return bad_request(request, "Only GET method")

    if not request.user.is_authenticated:
        return JsonResponse({"sub": False})

    return JsonResponse(
        {
            "sub": Profile.objects.get(user=request.user).subscribe
        }
    )


def save_statistics(request: WSGIRequest):
    """сохранение статистики

    :param request: реквест
    :type request: WSGIRequest
    :return: json
    """
    if request.method == "GET":
        return bad_request(request, "POST only")

    if not request.user.is_authenticated:
        return JsonResponse(
            {
                "auntificated": False,
                "success": False,
            }
        )

    stats = Stats.objects.get(user=request.user)
    data = json.loads(request.body)

    time = data["time"]
    successes = data["successes"]
    mistakes = data["mistakes"]

    mistakes_answers = [
        word["Mistake"][:word["Pass"].find(".")] +
        word["Mistake"][word["Pass"].find(".")].upper() +
        word["Mistake"][word["Pass"].find(".") + 1:]
        for word in data["mistake_words"]
    ]
    mistakes_correct = [
        word["Word"][:word["Pass"].find(".")] +
        word["Word"][word["Pass"].find(".")].upper() +
        word["Word"][word["Pass"].find(".") + 1:]
        for word in data["mistake_words"]
    ]

    stats.time += time
    stats.successes += successes
    stats.mistakes += mistakes
    stats.save()

    attempt = Atts(
        time=time,
        successes=successes,
        mistakes=mistakes,
        user=request.user
    )
    attempt.save()

    print(len(mistakes_answers), len(mistakes_correct))
    for i, m in enumerate(mistakes_answers):
        mis = MistakesAnswers(
            input_answer=m,
            correct_answer=mistakes_correct[i],
            att=attempt
        )
        mis.save()


    return JsonResponse(
        {
            "success": True,
            "auntificated": True,
        }
    )
