from django.shortcuts import render, redirect, reverse
from django.apps import apps
from registration.models import UserDashboard
from django.views.generic import TemplateView, View
from .models import Project
from .forms import ProjectForm
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        logged_user = UserDashboard.objects.get(user=request.user.id)
        if logged_user.is_executive():
            return redirect('dashboard:executive_panel')
        else:
            return redirect('dashboard:customer_panel')
    return render(request, 'dashboard/home.html')


class ExecutivePanel(TemplateView):
    template_name = 'dashboard/executive_panel.html'


class CustomerPanel(TemplateView):
    template_name = 'dashboard/customer_panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_projects'] = Project.objects.filter(customer=self.request.user)
        context['user_dashboard'] = UserDashboard.objects.get(user=self.request.user)
        return context


class AddProject(View):
    template_name = 'dashboard/project_form.html'
    project_form_class = ProjectForm

    def get(self, request):
        project_form = self.project_form_class(None)
        return render(request, self.template_name, {'project_form': project_form})

    def post(self, request):
        project_form = self.project_form_class(request.POST)
        if project_form.is_valid():
            new_project = project_form.save(commit=False)
            new_project.customer = request.user
            new_project.save()
            messages.info(request, "Projekt został pomyślnie dodany")
            return redirect('dashboard:home')
        else:
            return redirect('dashboard:new_project')
