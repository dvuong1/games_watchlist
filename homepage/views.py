from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You may now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'homepage/register.html', context)

class HomeView(TemplateView):
    template_name = 'homepage/blank.html'
    
class LoginView(TemplateView):
    template_name = 'homepage/login.html'
