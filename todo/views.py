from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from todo.models import Todo

class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"