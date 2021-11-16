from django.shortcuts import render
from django.views import generic

def home(request):
    context = {
        
    }
    
    return render(request, 'homepage/blank.html', context)
