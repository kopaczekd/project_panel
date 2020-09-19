from django.shortcuts import render, redirect
from django.apps import apps
from registration.models import UserDashboard
from django.views.generic import TemplateView
from .models import Project


def home(request):
    if request.user.is_authenticated:
        logged_user = UserDashboard.objects.get(user=request.user.id)
        if logged_user.is_executive():
            return executive_panel(request)
        else:
            return redirect('dashboard:customer_panel')
    return render(request, 'dashboard/home.html')


def executive_panel(request):
    return render(request, 'dashboard/executive_panel.html')


class CustomerPanel(TemplateView):
    template_name = 'dashboard/customer_panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_projects'] = Project.objects.filter(customer=self.request.user)
        return context

    # def get_query_set(self, request):
    #     all_projects = Project.objects.filter(customer=request.user)
    #     return render(request, self.template_name, {'all_projects': all_projects})
