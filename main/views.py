from random import randint
from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import random
import datetime
from dateutil.relativedelta import relativedelta
from main.models import Profile, Payments
from django.contrib.auth.models import User

from main.forms import RegForm, LoginForm, PaymentForm

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
        "user_icon": Profile.objects.get(user=request.user).icon if request.user.is_authenticated else "",
    }
    return context


def index_page(request: WSGIRequest):
    context = gen_base_context(request, "index")
    return render(request, 'pages/index.html', context)


def login_page(request: WSGIRequest):
    """
    Вход в аккаунт
    :param request: Реквест
    :type request: WSGIRequest
    """
    context = gen_base_context(request, "Логин")
    context["form"] = LoginForm()

    if request.method == "GET":
        return render(request, 'pages/accounts/login.html', context)

    form = LoginForm(request.POST)
    if not form.is_valid():
        context["errors"] = form.errors
        context["form"] = form
        return render(request=request, template_name="pages/accounts/login.html", context=context)

    user = authenticate(request=request, username=form.data["username"], password=form.data["password"])

    if user is None:
        messages.error(request, "Login Meh")
        return render(request, 'pages/accounts/login.html', context)

    login(request=request, user=user)
    messages.success(request, "Login success")

    next_url = request.POST.get('next', 'index')
    return redirect(next_url)


def registration_page(request: WSGIRequest):
    """
    Обработка регистрации
    :param request: Реквест
    :type request: WSGIRequest
    """
    context = gen_base_context(request, "Регистрация")
    context["form"] = RegForm()

    if request.method == "GET":
        return render(request=request, template_name="pages/accounts/registration.html", context=context)

    form = RegForm(request.POST)
    if not form.is_valid():
        context["errors"] = form.errors
        context["form"] = form
        return render(request=request, template_name="pages/accounts/registration.html", context=context)

    usr = User.objects.create_user(username=form.data["username"], password=form.data["password1"])

    pr = Profile(user=usr)
    pr.save()

    return redirect("login")
    #return render(request=request, template_name="pages/registration.html", context=context)


def not_found(request: WSGIRequest, exception):
    """
    Страница 404 (не найдено)
    :param request: Реквест
    :type request: WSGIRequest
    """
    return render(request, "pages/ErrorsAndExceptions/404_page.html", status=404)


def not_found_500(request: WSGIRequest):
    """
    СТраница 500 (не найдено)
    :param request: Реквест
    :type request: WSGIRequest
    """
    return render(request, "pages/ErrorsAndExceptions/404_page.html", status=500)

@login_required
def data_entry_page(request: WSGIRequest):
    """
    Страница ввода данных карты
    :param request: request-object
    :type request: WSGIRequest
    """
    if not request.session["amount"] or not request.session["subscribe"]:
        raise Http404

    context = {
        "form": PaymentForm(),
    }

    if request.method == "GET":
        if request.session["amount"]:
            context["amount"] = request.session["amount"]
            return render(request, "pages/payment/data_entry_page.html", context)
        raise Http404

    form = PaymentForm(request.POST)
    number = randint(100000000, 999999999)
    print(form.is_valid())
    print(request.POST)


    payment = Payments(
        number=number,
        date=datetime.date.today(),
        amount=request.session["amount"],
        user=request.user if not request.user.is_anonymous else None
    )

    if form.is_valid():
        payment.status = "Успешно"
        payment.save()
        context = {
            "amount": payment.amount,
            "number": payment.number,
            "date": payment.date,
            "status": "Успешно",
        }
        request.session["is_payment"] = True
        return redirect("/payment/success", context)
    payment.status = "Ошибка"
    payment.save()
    context = {
        "number": payment.number,
        "date": payment.date,
        "status": "Ошибка",
    }
    request.session["is_payment"] = True
    return redirect("/payment/failed", context)


@login_required
def failed_payment_page(request):
    if request.session["is_payment"]:
        request.session["is_payment"] = False
        return render(request, "pages/payment/failed_payment.html")
    raise Http404


@login_required
def success_payment_page(request):
    if request.session["is_payment"]:
        request.session["is_payment"] = False
        counter_month = {
            'month': 1,
            'three_month': 3,
            'year': 12
        }

        c_user = Profile.objects.get(user_id=request.user.id)
        if c_user.period_subscribe:
            datetime_period = c_user.period_subscribe + relativedelta(
                months=counter_month[request.session["subscribe"]])
        else:
            datetime_period = datetime.datetime.now() + relativedelta(months=counter_month[request.session["subscribe"]])
        c_user.period_subscribe = datetime_period
        c_user.subscribe = True
        c_user.save()
        return render(request, "pages/payment/success_payment.html")
    raise Http404


@login_required
def choose_subscriber_page(request: WSGIRequest):
    if request.method == "GET":
        return render(request, "pages/subscribe/choose_subcribe.html")

    prices = {
        "month": 1000,
        "three_month": 2700,
        "year": 9000
    }

    subscribe = request.POST.get("period")
    request.session["subscribe"] = subscribe
    request.session["amount"] = prices[subscribe]

    return redirect("/payment/data_entry")
