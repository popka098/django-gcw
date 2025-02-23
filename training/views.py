from django.http import Http404

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

from main.views import gen_base_context

from training.models import Task_9, Task_10, Task_11, Task_12, Task_15
# Create your views here.

TASK_MODELS = {
    9: Task_9,
    10: Task_10,
    11: Task_11,
    12: Task_12,
    15: Task_15,
}

def training(request: WSGIRequest, task: int):
    """
    Тренировка
    :param request: Реквест
    :param task: Номер задания
    :type task: int
    """
    context = gen_base_context(request, f"training_{task}")
    
    try:
        task_model = TASK_MODELS[task]
    except:
        raise Http404
    
    if request.method == "GET":
        return render(request, "pages/training/training.html", context)

    return render(request, "pages/training/training.html", context)