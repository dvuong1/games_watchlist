from django.shortcuts import render
from django.views import generic

class TableView(generic.ListView):
    template_name = 'list/table.html'