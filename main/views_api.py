import random
import json

from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

from rest_framework.exceptions import bad_request

from training.models import Task_9, Task_10, Task_11, Task_12
from training.serializers import TaskSerializer, WordsSerializer

from main.models import Profile


tasks = {
    9: Task_9,
    10: Task_10,
    11: Task_11,
    12: Task_12
}


def get_all_words(request: WSGIRequest, limit=0):
    if request.method == "POST":
        return bad_request(request, "Only GET method")

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


def get_random_words(request: WSGIRequest, task=9, limit=0):
    if request.method == "POST":
        return bad_request(request, "Only GET method")

    if not(9 <= task <= 12):
        return bad_request(request, "No such table")
    

    words = WordsSerializer(tasks[task].objects.all()).data
    if limit == 0:
        limit = len(words)

    words_shuffeled = words.copy()
    random.shuffle(words_shuffeled)
    return JsonResponse({"words": words_shuffeled[:limit]})


def get_random_word(request: WSGIRequest, task=9):
    if request.method == "POST":
        return bad_request(request, "Only GET method")

    if not(9 <= task <= 12):
        return bad_request(request, "No such table")
    
    words = WordsSerializer(tasks[task].objects.all()).data
    word = random.choice(words)

    return JsonResponse(word)


def get_user_sub(request: WSGIRequest):
    """
    docs
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
    if request.method == "GET":
        return bad_request(request, "POST only")
    
    if not request.user.is_authenticated:
        return JsonResponse(
            {
                "auntificated": False,
                "success": False,
            }
        )
    

    data = json.loads(request.body)
    
    time = data["time"]
    successes = data["successes"]
    mistakes = data["mistakes"]
    print(data)

    return JsonResponse(
        {
            "success": True,
            "auntificated": True,
        }
    )
