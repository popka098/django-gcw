import logging

from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from main.views import gen_base_context, subscription_required
from training.models import Atts, Stats, MistakesAnswers, Task9, Task10, Task11, Task12

# Create your views here.

logger = logging.getLogger("__name__")

TASK_MODELS = {
    9: Task9,
    10: Task10,
    11: Task11,
    12: Task12,
}


@login_required
def training(request: WSGIRequest, task: int):
    """страница тренировки

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


@login_required
def statistics_page(request: WSGIRequest):
    """страница статистики

    :param request: реквест
    :type request: WSGIRequest
    """
    context = {}
    stat = Stats.objects.get(user=request.user)
    attempts = Atts.objects.filter(user=request.user)
    attempts = attempts.order_by("id").reverse()
    context = {
        "time_all" : stat.time,
        "success_all" : stat.successes,
        "mistakes_all" : stat.mistakes,
        "kd" : (0 if ((stat.successes == 0 and stat.mistakes == 0))
                else int(100*(stat.successes / (stat.successes + stat.mistakes)))
                ),
        "attempts": attempts,
    }
    return render(request, "pages/statistics/general_statistics.html", context)


@subscription_required
def mistakes_page(request: WSGIRequest, att_id: int):
    """страница просмотра ошибок пользователя

    :param request: реквест
    :type request: WSGIRequest
    :param att_id: id попытки
    :type att_id: int
    """

    attempt = Atts.objects.get(id=att_id)
    if attempt.user != request.user:
        raise Http404

    mistakes = MistakesAnswers.objects.filter(att=attempt)
    context = {
        "att_id": att_id,
        "mistakes": mistakes,
    }

    return render(request, "pages/statistics/mistakes.html", context)
