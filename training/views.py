from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from django.shortcuts import render

from main.views import gen_base_context
from training.models import Task9, Task10, Task11, Task12

# Create your views here.

TASK_MODELS = {
    9: Task9,
    10: Task10,
    11: Task11,
    12: Task12,
}

def training(request: WSGIRequest, task: int):
    """страница тренитровки

    :param request: реквест
    :type request: WSGIRequest
    :param task: задание
    :type task: int
    """
    context = gen_base_context(request, f"training_{task}")

    if task not in TASK_MODELS:
        raise Http404

    if request.method == "GET":
        return render(request, "pages/training/training.html", context)

    return render(request, "pages/training/training.html", context)


def statistics_page(request: WSGIRequest):
    """Страница статистики

    :param request: реквест
    :type request: WSGIRequest
    """
    context = {}
    # stat = Stats.objects.get(user=request.user)
    # attemps = Atts.objects.filter(user=request.user)
    # context = {
    #     "time_all" : stat.time,
    #     "success_all" : stat.successes,
    #     "mistakes_all" : stat.mistakes,
    #     "kd" : 0 if (
    #      (stat.successes == 0 and stat.mistakes == 0)
    #       else int(100*(stat.successes / (stat.successes + stat.mistakes)))
    #     ),
    #     "attemps": attemps,
    # }
    return render(request, "pages/general_statistics.html", context)
