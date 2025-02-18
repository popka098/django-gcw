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


