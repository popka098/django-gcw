from django import forms

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

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileExtraForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {'description': 'Описание'}
