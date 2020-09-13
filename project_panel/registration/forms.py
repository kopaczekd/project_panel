from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserDashboard
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']
        labels = {
            'first_name': "Imie",
            'username': "Email",
            'password1': "Hasło",
            'password2': "Powtórz hasło"
        }


class RegisterUserDashboard(ModelForm):
    class Meta:
        model = UserDashboard
        exclude = ['user', 'role']
