from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from training.models import Stats, Atts



def statistics_page(request: WSGIRequest):
    stat = Stats.objects.get(user=request.user)
    attemps = Atts.objects.filter(user=request.user)
    print(100*(stat.successes // (stat.successes + stat.mistakes)))
    context = {
        "time_all" : stat.time,
        "success_all" : stat.successes,
        "mistakes_all" : stat.mistakes,
        "kd" : 0 if (stat.successes == 0 and stat.mistakes == 0) else int(100*(stat.successes / (stat.successes + stat.mistakes))),
        "attemps": attemps,
    }
    return render(request, "../../training/templates/pages/general_statistics.html", context)
