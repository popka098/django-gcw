"""main forms"""
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class LoginForm(forms.Form):
    """форма аунтификации

    :param username: имя пользователя
    :param password: пароль
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input-login"}),
        label=''
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input-password"}),
        label=''
    )


class UserRegistrationForm(forms.ModelForm):
    """форма регистрации

    :param username: имя пользователя
    :param first_name: имя
    :param last_name: фамилия
    :param email: эл. почта
    :param password: пароль
    :param password2: потверждение пароля
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "input-username"}),
        label=''
    )
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "input-name"}),
        label=''
    )
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "input-lastname"}),
        label=''
    )
    email = forms.CharField(widget=forms.TextInput(
        attrs={"class": "input-email"}),
        label=''
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={"class": "input-password"})
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={"class": "input-doblepassword"})
    )

    class Meta:
        """Мета класс для подвязки к пользователю

        """

        model = User
        fields = ('username','first_name','last_name', 'email')
        help_texts = {'username': "", }

    def clean_password2(self):
        """удаление данных из поля подтверждения пароля

        """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class PaymentForm(forms.Form):
    """Форма оплаты

    :param cardNumber: номер карты
    :param cardName: имя владельца
    :param expiryDate: срок действия
    :param cvv: cvv/cvc
    """
    cardNumber = forms.CharField(
        label="",
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
        label="",
        validators=[
            RegexValidator(
                regex='^[A-Za-z ]+$',
                message='Имя должно содержать только буквы'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control card-name-input',
            'placeholder': 'IVAN IVANOV'
        })
    )

    expiryDate = forms.CharField(
        label="",
        validators=[
            RegexValidator(
                regex='^(0[1-9]|1[0-2])\/([0-9]{2})$',
                message='Формат даты: MM/ГГ'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control card-data-input',
            'placeholder': 'MM/ГГ',
            'maxlength': '5'
        })
    )

    cvv = forms.CharField(
        label="",
        validators=[
            RegexValidator(
                regex='^[0-9]{3,4}$',
                message='CVV должен содержать 3 или 4 цифры'
            )
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'form-control card-cvv-input',
            'placeholder': '•••',
            'maxlength': '4'
        })
    )
