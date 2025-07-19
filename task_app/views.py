from django.shortcuts import render
from .models import Task, Comment
from task_app import models
from django.views.generic import ListView, DetailView, CreateView

class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"