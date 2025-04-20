from django.http import Http404

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

from main.views import gen_base_context

from training.models import Stats, Atts
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


def statistics_page(request: WSGIRequest):
    # stat = Stats.objects.get(user=request.user)
    # attemps = Atts.objects.filter(user=request.user)
    # context = {
    #     "time_all" : stat.time,
    #     "success_all" : stat.successes,
    #     "mistakes_all" : stat.mistakes,
    #     "kd" : 0 if (stat.successes == 0 and stat.mistakes == 0) else int(100*(stat.successes / (stat.successes + stat.mistakes))),
    #     "attemps": attemps,
    # }
    context = {}
    return render(request, "pages/general_statistics.html", context)
