from django.shortcuts import render, redirect
from .forms import RegisterForm, RegisterUserDashboard
from django.http import HttpResponse
from .models import Role


def register(request):
    form_user = RegisterForm(request.POST or None)
    form_user_dashboard = RegisterUserDashboard(request.POST or None)
    if request.method == 'POST':
        if form_user.is_valid() and form_user_dashboard.is_valid():
            created_user = form_user.save(commit=False)
            user_from_dashboard = form_user_dashboard.save(commit=False)
            user_from_dashboard.user = created_user
            if request.POST.get("if_executive") == "executive":
                selected_role = Role.objects.get(id=1)
                user_from_dashboard.company_name = ""
                user_from_dashboard.nip = ""
            else:
                selected_role = Role.objects.get(id=2)
            user_from_dashboard.role = selected_role
            created_user.save()
            user_from_dashboard.save()
            return redirect('dashboard:home')
    return render(request, 'registration/register.html', {'form_user': form_user,
                                                          'form_user_dashboard': form_user_dashboard})


def login(request):
    return HttpResponse("logowanie")

