from django import forms

from django.core.validators import RegexValidator

from main.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from PIL import Image

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input-login"}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input-password"}), label='')

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input-username"}), label='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "input-name"}), label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "input-lastname"}), label='')
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "input-email"}), label='')
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={"class": "input-password"}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={"class": "input-doblepassword"}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email')
        help_texts = {'username': "", }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class PaymentForm(forms.Form):
    cardNumber = forms.CharField(
        label="Номер карты",
        validators=[
            RegexValidator(
                regex='^[0-9 ]{16,22}$',
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
        validators=[
            RegexValidator(
                regex='^[A-Za-z ]+$',
                message='Имя должно содержать только буквы'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'IVAN IVANOV'
        })
    )

    expiryDate = forms.CharField(
        label="Срок действия",
        validators=[
            RegexValidator(
                regex='^(0[1-9]|1[0-2])\/([0-9]{2})$',
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
                message='CVV должен содержать 3 или 4 цифры'
            )
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '•••',
            'maxlength': '4'
        })
    )


