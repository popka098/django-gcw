from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponseForbidden
from functools import wraps
from .models import Subscription



def index_page(request: WSGIRequest):
    context = {
        'pagename': "Главная"
    }
    user = authenticate(username="admin", password="admin")
    if user:
        login(request, user)
        context["is_login"] = True
        return render(request, 'pages/index.html', context)

    return render(request, 'pages/index.html', context)


def subscription_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if hasattr(request.user, 'subscription'):
                if request.user.subscription.is_active:
                    return view_func(request, *args, **kwargs)
                else:
                    print("Подписка неактивна")
            else:
                print("Подписка не найдена")
        else:
            print("Пользователь не аутентифицирован")
        return HttpResponseForbidden("У вас нет доступа к этой странице. Пожалуйста, оформите подписку.")

    return _wrapped_view

def login_page(request: WSGIRequest):
    raise NotImplementedError


def registration_page(request: WSGIRequest):
    raise NotImplementedError


@subscription_required
def theory_page(request: WSGIRequest):
    return render(request, 'pages/theory.html')
