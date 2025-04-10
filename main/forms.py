from django import forms

from django.core.validators import RegexValidator

from main.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from PIL import Image

class LoginForm(forms.Form):
    """
    Форма для аунтентификации и логина пользователя
    :param username: имя пользователя
    :param password: пароль
    """
    username = forms.CharField(label="Имя пользователя", required=True)
    password = forms.CharField(label="Пароль", required=True, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'sign-in2-textinput1 thq-input thq-body-large'})
        self.fields['password'].widget.attrs.update({'class': 'sign-in2-textinput2 thq-input thq-body-large'})

class RegForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'sign-in2-textinput1 thq-input thq-body-large'})
        self.fields['password1'].widget.attrs.update({'class': 'sign-in2-textinput2 thq-input thq-body-large'})
        self.fields['password2'].widget.attrs.update({'class': 'sign-in2-textinput2 thq-input thq-body-large'})


class PaymentForm(forms.Form):
    cardNumber = forms.CharField(
        label="Номер карты",
        validators=[
            RegexValidator(
                regex='^[0-9]{16,19}$',
                message='Номер карты должен содержать 16-19 цифр'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control card-number-input',
            'placeholder': '1234 5678 9012 3456',
            'maxlength': '19'
        })
    )

    cardName = forms.CharField(
        label="Имя владельца",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'IVAN IVANOV'
        })
    )

    expiryDate = forms.CharField(
        label="Срок действия",
        validators=[
            RegexValidator(
                regex='^(0[1-9]|1[0-2])\/?([0-9]{2})$',
                message='Формат даты: MM/ГГ'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM/ГГ',
            'maxlength': '5'
        })
    )

    cvv = forms.CharField(
        label="CVV/CVC",
        validators=[
            RegexValidator(
                regex='^[0-9]{3,4}$',
                message='CVV должен содержать 3 цифры'
            )
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '•••',
            'maxlength': '3'
        })
    )


