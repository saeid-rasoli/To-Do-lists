from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import TodoList

# Create your views here.
class ListListView(ListView):
    model = ListView
    template_name = 'todo_app/index.html'