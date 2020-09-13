from django.shortcuts import render
from .forms import RegisterForm, RegisterUserDashboard
from django.http import HttpResponse
from .models import Role


def register(request):
    form_user = RegisterForm(request.POST or None)
    form_user_dashboard = RegisterUserDashboard(request.POST or None)
    if request.method == 'POST':
        if form_user.is_valid():
            form_user.save()
            return HttpResponse("Rejestracja pomyślna!")
    return render(request, 'registration/register.html', {'form_user': form_user,
                                                          'form_user_dashboard': form_user_dashboard})


def login(request):
    return HttpResponse("logowanie")

