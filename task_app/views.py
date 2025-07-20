from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Task, Comment
from task_app.forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from task_app import models
from django.views.generic import ListView, DetailView, CreateView, View
from task_app.mixins import UserIsOwnerMixin
from django.http import HttpResponseRedirect

class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class TaskComplateView(LoginRequiredMixin, UserIsOwnerMixin, View):
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = "done"
        task.save()

        return HttpResponseRedirect(reverse_lazy("tasks:task-list")) 
    

    def get_object(self):
        task_id = self.kwargs.get('pk')
        return get_object_or_404(models.Task, pk=task_id)