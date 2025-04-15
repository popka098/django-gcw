from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from training.models import Stats, Atts


def statistics_page(request: WSGIRequest):
    stat = Stats.objects.get(user=request.user)
    attemps = Atts.objects.filter(user=request.user)
    context = {
        "time_all" : stat.time,
        "success_all" : stat.successes,
        "mistakes_all" : stat.mistakes,
        "kd" : 0 if stat.successes == 0 and stat.mistakes == 0 else 100*(stat.successes // (stat.successes + stat.mistakes)),
        "attemps": attemps,
    }
    return render(request, "pages/statistics/general_statistic.html", context)
