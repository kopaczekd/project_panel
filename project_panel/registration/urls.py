from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'registration'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
