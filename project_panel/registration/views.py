from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponse


def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse("Rejestracja pomyślna!")
    return render(request, 'registration/register.html', {'form': form})
