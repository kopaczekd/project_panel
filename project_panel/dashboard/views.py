from django.shortcuts import render, redirect, get_object_or_404
from registration.models import UserDashboard
from django.views.generic import TemplateView, View
from .models import Project, Task, Status
from .forms import ProjectForm
from django.contrib import messages


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_executor = UserDashboard.objects.get(user=self.request.user)
        all_projects = Project.objects.filter(executors=logged_executor)
        status_executing = Status.objects.get(id=2)
        list_of_tasks = []
        for project in all_projects:
            tasks = Task.objects.filter(project=project)
            for task in tasks:
                list_of_tasks.append(task)
                if task.executor == logged_executor and task.status == status_executing:
                    context['busy_executor'] = True

        context['list_of_tasks'] = list_of_tasks
        context['user_dashboard'] = logged_executor
        return context


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


def assign_task(request, task_id):
    logged_executor = UserDashboard.objects.get(user=request.user)

    for task in Task.objects.filter(executor=logged_executor):
        if task.status == 2:
            messages.info(request, "Możesz mieć zarezerwowane maksymalnie jedno zadanie.")
            return redirect('dashboard:home')

        task_to_assign = get_object_or_404(Task, id=task_id)
        task_to_assign.executor = logged_executor
        status_executing = Status.objects.get(id=2)
        task_to_assign.status = status_executing
        task_to_assign.save()
        project = get_object_or_404(Project, id=task_to_assign.project.id)
        project.status = status_executing
        project.save()
        messages.info(request, "Pomyślnie zarezerwowałeś zadanie.")

    return redirect('dashboard:home')


def finish_task(request, task_id):
    task_to_finish = get_object_or_404(Task, id=task_id)
    status_finish = Status.objects.get(id=3)
    task_to_finish.status = status_finish
    task_to_finish.save()
    # Jeżeli wszystkie taski prjekru są Zakończone to projekt jest również zakończony
    messages.info(request, "Pomyślnie zakończyłeś zadanie.")
    return redirect('dashboard:home')
