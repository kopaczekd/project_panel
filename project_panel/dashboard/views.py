from django.shortcuts import render, redirect
from django.apps import apps
from registration.models import UserDashboard


def home(request):
    if request.user.is_authenticated:
        logged_user = UserDashboard.objects.get(user=request.user.id)
        if logged_user.is_executive():
            return executive_panel(request)
        else:
            return customer_panel(request)
    return render(request, 'dashboard/home.html')


def executive_panel(request):
    return render(request, 'dashboard/executive_panel.html')


def customer_panel(request):
    return render(request, 'dashboard/customer_panel.html')
