from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Profile
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


def data_entry_page(request: WSGIRequest):
    """
    Страница ввода данных карты
    :param request: request-object
    :type request: WSGIRequest
    """
    context = {
        "form": PaymentForm(),
    }

    # if request.method == "GET":
    #     return render(request, "pages/payment/data_entry_page.html", context)
    #
    # form = PaymentForm(request.POST)
    # a = form.data["cardName"]

    # data = {
    #     "cardNumber": PaymentForm["cardNumber"],
    #     "cardName": PaymentForm.cardName,
    #     "expiryDate": PaymentForm.expiryDate,
    #     "cvv": PaymentForm.cvv,
    #     "amout": PaymentForm.amount
    # }

    return render(request, "pages/payment/data_entry_page.html", context=context)


def failed_payment(request):
    return render(request, "pages/payment/failed_payment.html")


def success_payment(request):
    return render(request, "pages/payment/success_payment.html")