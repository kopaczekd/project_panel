from django.shortcuts import render
from django.apps import apps
from registration.models import UserDashboard, Role
# UserDashboard = apps.get_model('registration', 'UserDashboard')
# Role = apps.get_model('registration', 'Role')


def home(request):
    if request.user.is_authenticated:
        logged_user = UserDashboard.objects.get(user=request.user.id)
        print(logged_user)
        if logged_user.is_executive():
            print("Wykonawca")
            render(request, 'dashboard/executive_panel.html')
        else:
            print("Wykonawca")
            render(request, 'dashboard/customer_panel.html')

    return render(request, 'dashboard/home.html')
