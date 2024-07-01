from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import TodoList, TodoItem

# Create your views here.
class ListListView(ListView):
    model = TodoList
    template_name = 'todo_app/index.html'

class ItemListView(ListView):
    model = TodoItem
    tempalte_name = 'todo_app/todo_list.html'

    def get_queryset(self):
        return TodoItem.objects.filter(todo_list_id=self.kwargs['list_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = TodoList.objects.get(id=self.kwargs['list_id'])
        return context
    

    
