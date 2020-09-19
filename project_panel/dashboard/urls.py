from django.urls import path, include
from .views import CustomerPanel, home

app_name = 'dashboard'

urlpatterns = [
    path('', home, name="home"),
    path('customer-panel/',  CustomerPanel.as_view(), name="customer_panel")
]
