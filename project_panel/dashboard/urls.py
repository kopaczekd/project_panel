from django.urls import path, include
from .views import CustomerPanel, home, ExecutivePanel, AddProject, ProjectDetailsView

app_name = 'dashboard'

urlpatterns = [
    path('', home, name="home"),
    path('customer-panel/',  CustomerPanel.as_view(), name="customer_panel"),
    path('executive-panel/', ExecutivePanel.as_view(), name="executive_panel"),
    path('new-project/', AddProject.as_view(), name="new_project"),
    path('project-details/<int:project_id>/', ProjectDetailsView.as_view(), name="project_details"),
]
