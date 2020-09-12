from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
