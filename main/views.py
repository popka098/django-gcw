import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_page(request: WSGIRequest):
    context = {
        'pagename': "Главная"
    }
    return render(request, 'pages/index.html', context)


def time_page(request: WSGIRequest):
    context = {
        'pagename': 'Текущее время',
        'time': datetime.datetime.now().time(),
    }
    return render(request, 'pages/time.html', context)


def login_page(request: WSGIRequest):
    context = {
        'pagename': 'Логин',
    }
    return render(request, 'pages/login.html', context)
