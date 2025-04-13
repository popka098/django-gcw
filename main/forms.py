from django import forms

from main.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from PIL import Image

class LoginForm(forms.Form):
    username = forms.CharField(
                               widget=forms.TextInput(
                                   attrs={"class": "input-login"}), label='')
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "input-password"}), label='')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email')
        help_texts = {'username': "", }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


