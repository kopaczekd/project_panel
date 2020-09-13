from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponse
from .models import Role


def register(request):
    form = RegisterForm(request.POST or None)
    roles = Role.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse("Rejestracja pomyślna!")
    return render(request, 'registration/register.html', {'form': form, 'roles': roles})


def login(request):
    return HttpResponse("logowanie")

