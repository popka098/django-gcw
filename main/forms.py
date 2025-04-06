from django import forms

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
    cardNumber = forms.CharField(label="Номер карты", required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control card-number-input',
            'id': 'cardNumber',
            'placeholder': '1234 5678 9012 3456',
            'maxlength': '19'
        }
    ))
    cardName = forms.CharField(label="Имя владельца", required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'cardName',
            'placeholder': 'IVAN IVANOV',
        }
    ))
    expiryDate = forms.CharField(label="Срок действия", required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'expiryDate',
            'placeholder': 'MM/ГГ',
            'maxlength': '5'
        }
    ))
    cvv = forms.CharField(label="CVV/CVC", required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'cvv',
            'placeholder': '•••',
            'maxlength': '3'
        }
    ))
    amount = forms.CharField(label="Сумма", disabled=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'amount',
            'placeholder': '1000',
            'maxlength': '3',
            'value': '1000',
        }
    ))


