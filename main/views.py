from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Profile
from django.contrib.auth.models import User
from training.models import Stats

from main.forms import LoginForm, UserRegistrationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def gen_base_context(request: WSGIRequest, pagename: str):
    """
    генерирует базовый контекст из названия страницы, пользователя и его аватарки
    :param request: Реквест
    :type request: WSGIRequest
    :param pagename: Название страницы
    :type pagename: str
    """
    context = {
        "pagename": pagename,
        "user": request.user if request.user.is_authenticated else "Anon",
        # "user_icon": Profile.objects.get(user=request.user).icon if request.user.is_authenticated else "",
    }
    return context


def index_page(request: WSGIRequest):
    context = gen_base_context(request, "index")
    return render(request, 'pages/index.html', context)


def login_page(request):
    context = {
        "form": LoginForm()
    }
    if request.method == "GET":
        return render(request, "pages/accounts/login.html", context)

    form = LoginForm(request.POST)


    context["form"] = form
    if not form.is_valid():
        return HttpResponse('Некоректные данные')

    data = form.data
    if data['username'].count('@') == 0:
        user = authenticate(username=data['username'], password=data['password'])
    else:
        use = User.objects.filter(email=data['username'])
        if len(use) > 0:
            user = authenticate(username=use[0], password=data['password'])
        else:
            user = None
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('index')

        return HttpResponse('Такого аккаунта нет')
    return render(request, 'pages/accounts/login.html', context)


def registration_page(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()


            return render(request, 'pages/accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'pages/accounts/registration.html', {'user_form': user_form})


@login_required
def profile_page(request):
    context = gen_base_context(request, 'profile')
    return render(request, 'pages/accounts/profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('pages/index.html')


def not_found(request: WSGIRequest, exception):
    """
    Страница 404 (не найдено)
    :param request: Реквест
    :type request: WSGIRequest
    """
    return render(request, "pages/ErrorsAndExceptions/404_page.html", status=404)


def not_found_500(request: WSGIRequest):
    """
    Страница 500 (не найдено)
    :param request: Реквест
    :type request: WSGIRequest
    """
    return render(request, "pages/ErrorsAndExceptions/500_page.html", status=500)
