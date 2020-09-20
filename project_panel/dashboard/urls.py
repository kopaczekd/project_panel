from django.urls import path, include
from .views import CustomerPanel, home, ExecutivePanel

app_name = 'dashboard'

urlpatterns = [
    path('', home, name="home"),
    path('customer-panel/',  CustomerPanel.as_view(), name="customer_panel"),
    path('executive-panel', ExecutivePanel.as_view(), name="executive_panel"),
]
