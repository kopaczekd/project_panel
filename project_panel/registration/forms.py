from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import UserDashboard
from django.forms import ModelForm
from django import forms


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Imie i nazwisko", required=True)
    username = forms.EmailField(label="Email", widget=forms.EmailInput)
    password1 = forms.CharField(label="Hasło", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']


class RegisterUserDashboard(ModelForm):
    class Meta:
        model = UserDashboard
        exclude = ['user', 'role', 'active', 'name']


class LoginForm(AuthenticationForm):
    username = UsernameField(label="Email", widget=forms.TextInput(attrs={'autofocus': True}))

    class Meta:
        model = User
        fields = ['username', 'password']
