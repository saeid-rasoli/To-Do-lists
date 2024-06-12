from django.contrib import admin
from todo_app.models import TodoItem, TodoList

admin.site.register(TodoItem)
admin.site.register(TodoList)