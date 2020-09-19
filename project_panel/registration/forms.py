from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserDashboard
from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Imie", required=True)
    password1 = forms.CharField(label=_("Hasło"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Powtórz hasło"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']
        labels = {'username': "Email"}


class RegisterUserDashboard(ModelForm):
    class Meta:
        model = UserDashboard
        exclude = ['user', 'role', 'active', 'name']
