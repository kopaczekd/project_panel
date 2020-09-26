from .forms import RegisterForm, RegisterUserDashboard, LoginForm
from django.shortcuts import render, redirect
from .models import Role
from django.contrib.auth.views import LoginView


def register(request):
    if request.user.is_authenticated:
        return logged(request)
    form_user = RegisterForm(request.POST or None)
    form_user_dashboard = RegisterUserDashboard(request.POST or None)
    if request.method == 'POST':
        if form_user.is_valid() and form_user_dashboard.is_valid():
            user = form_user.save(commit=False)
            user.email = user.username
            user.save()
            user_from_dashboard = form_user_dashboard.save(commit=False)
            user_from_dashboard.user = user
            user_from_dashboard.name = user.first_name
            if request.POST.get("if_executive") == "executive":
                selected_role = Role.objects.get(id=1)
                user_from_dashboard.company_name = ""
                user_from_dashboard.nip = ""
            else:
                selected_role = Role.objects.get(id=2)
            user_from_dashboard.role = selected_role
            user_from_dashboard.save()
            return redirect('dashboard:home')
    return render(request, 'registration/register.html', {'form_user': form_user,
                                                          'form_user_dashboard': form_user_dashboard})


def login(request):
    if request.user.is_authenticated:
        return logged(request)
    return render(request, 'registration/login.html')


def logged(request):
    return render(request, 'registration/logged.html')


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
