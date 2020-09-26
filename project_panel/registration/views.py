from .forms import RegisterForm, RegisterUserDashboard
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import Role


def register(request):
    if request.user.is_authenticated:
        return logged(request)
    print("Niezalogowany")
    form_user = RegisterForm(request.POST or None)
    form_user_dashboard = RegisterUserDashboard(request.POST or None)
    if request.method == 'POST':
        print("metoda post")
        if form_user.is_valid() and form_user_dashboard.is_valid():
            print("prawidlowe formy")
            user = form_user.save(commit=False)
            user_from_dashboard = form_user_dashboard.save(commit=False)
            user_from_dashboard.user = user
            user_from_dashboard.name = user.first_name
            if request.POST.get("if_executive") == "executive":
                print("czy executive - tak")
                selected_role = Role.objects.get(id=1)
                user_from_dashboard.company_name = ""
                user_from_dashboard.nip = ""
            else:
                print("czy executive - nie")
                selected_role = Role.objects.get(id=2)
            user_from_dashboard.role = selected_role
            print("zapisanie use i user_dashboard")
            user.save()
            user_from_dashboard.save()
            print("kolejny redirect")
            return redirect('dashboard:home')
    return render(request, 'registration/register.html', {'form_user': form_user,
                                                          'form_user_dashboard': form_user_dashboard})




def login(request):
    if request.user.is_authenticated:
        return logged(request)
    return render(request, 'registration/login.html')


def logged(request):
    return render(request, 'registration/logged.html')





