from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'homepage/blank.html'
    
class LoginView(TemplateView):
    template_name = 'homepage/login.html'
