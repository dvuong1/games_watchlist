from django.urls import path
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', DetailView.as_view(template_name='homepage/profile.html'), name='profile'),
    path('forgot-password/', 
         views.TemplateView.as_view(template_name='homepage/forgot-password.html'), 
         name='forgot-password')
]
