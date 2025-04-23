from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest

from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Profile
from training.models import Stats
from django.contrib.auth.models import User

from main.forms import LoginForm, UserRegistrationForm
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

from functools import wraps


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


def subscription_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            if hasattr(profile, 'subscribe'):
                if profile.subscribe:
                    return view_func(request, *args, **kwargs)
                else:
                    print("Подписка неактивна")
                    # redirect на покупку подписки
            else:
                print("Подписка не найдена")
                # redirect на покупку подписки
        else:
            print("Пользователь не аутентифицирован")
            # redirect на аунтификацию
        return HttpResponseForbidden("У вас нет доступа к этой странице. Пожалуйста, оформите подписку.")

    return _wrapped_view


@subscription_required
def theory_page(request: WSGIRequest):
    return render(request, 'pages/theory.html')


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
            
            profile = Profile(user=new_user)
            profile.save()
            stats = Stats(user=new_user)
            stats.save()

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
    request.session["number"] = str(number)


    payment = Payments(
        number=number,
        date=datetime.date.today(),
        amount=request.session["amount"],
        user=request.user
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
        context = {
            "number": "TX-" + request.session["number"],
        }
        return render(request, "pages/payment/failed_payment.html", context)
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
        context = {
            "number": "TX-" + request.session["number"],
            "amount": request.session["amount"],
        }
        return render(request, "pages/payment/success_payment.html", context)
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
