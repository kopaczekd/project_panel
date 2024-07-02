from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from registration.models import UserDashboard
from django.views.generic import TemplateView, View, DetailView
from .models import Project, Task
from .forms import ProjectForm
from django.contrib import messages
from django.http import HttpResponse


def home(request):
    if request.user.is_authenticated:
        logged_user = UserDashboard.objects.get(user=request.user)
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
        logged_customer = UserDashboard.objects.get(user=self.request.user)
        context['all_projects'] = Project.objects.filter(customer=logged_customer)
        context['user_dashboard'] = logged_customer
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
            logged_customer = UserDashboard.objects.get(user=request.user)
            new_project.customer = logged_customer
            new_project.save()

            # Tworzenie i przypisywanie tesków do Projektu
            for key_from_form in request.POST.keys():
                if 'task' in key_from_form:
                    new_task = Task(title=request.POST.get(key_from_form), project=new_project)
                    new_task.save()

                if not Task.objects.filter(project=new_project):
                    startup_task_for_project_without_given_tasks = Task(
                        title='Startowe - stworzone przez system',
                        project=new_project)
                    startup_task_for_project_without_given_tasks.save()

            # Przypisywanie wybranych wykonawców do Projektu
            for selected_executor in project_form.cleaned_data['executors']:
                new_project.executors.add(selected_executor)
            messages.info(request, "Projekt został pomyślnie dodany")
            return redirect('dashboard:home')
        else:
            return redirect('dashboard:new_project')


class ProjectDetailsView(View):
    template_name = 'dashboard/project_details.html'

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['project_id'])
        executors = project.executors.all()
        tasks = Task.objects.filter(project=project)
        context = {'project': project,
                   'executors': executors,
                   'tasks': tasks}
        return render(request, self.template_name, context)

