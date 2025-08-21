from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Task, Comment
from task_app.forms import TaskForm, TaskFilterForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from task_app import models
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from task_app.mixins import UserIsOwnerMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class TaskListView(LoginRequiredMixin, ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

    def get_queryset(self):
        
        queryset = Task.objects.filter(author=self.request.user)


        status = self.request.GET.get("status", "")
        if status:
            queryset = queryset.filter(status=status)

        priority = self.request.GET.get("priority", "")
        if priority:
            queryset = queryset.filter(priority=priority)


        return queryset

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #######це як назва##змінна
        context["form"] = TaskFilterForm(self.request.GET)
        return context

class TaskDetailView(LoginRequiredMixin, DetailView):
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


################я розказую ################

class CommentListView(LoginRequiredMixin, ListView):
    model = models.Comment
    context_object_name = "comments"
    template_name = "tasks/task_comment.html"
    form_class = CommentForm
    def get_queryset(self):
        
        task_id = self.kwargs.get("pk")
        task = get_object_or_404(Task, pk=task_id)
        queryset = Comment.objects.filter(task=task)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()  # Додаємо пусту форму до контексту
        return context
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment  = comment_form.save(commit=False)
            comment.author = request.user
            task_id = self.kwargs.get("pk")  # Отримуємо task_id з URL
            comment.task = get_object_or_404(Task, pk=task_id)  # Отримуємо Task
            comment.save()
            return redirect('tasks:task-comment', pk=comment.task.pk)
        else:
            pass

        

class ComentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    template_name = "tasks/task_comment_form.html"
    form_class = CommentForm
    success_url = reverse_lazy("tasks:task-create")

    def form_valid(self, form):
        form.instance.author = self.request.user


        task_id = self.kwargs['pk']
        form.instance.task = get_object_or_404(Task, pk=task_id)
        return super().form_valid(form)
    



class CommentLIkeToggle(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(models.Comment, pk=self.kwargs.get('pk'))
        like_qs = models.Like.objects.filter(comment=comment, user=request.user)
        if like_qs.exists():
            like_qs.delete()
        else:
            models.Like.objects.create(comment=comment, user=request.user)
        return HttpResponseRedirect(comment.get_absolute_url())


##############всьо тоя вже не розказую ###################







class TaskComplateView(LoginRequiredMixin, UserIsOwnerMixin, View):
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = "done"
        task.save()

        return HttpResponseRedirect(reverse_lazy("tasks:task-list")) 
    

    def get_object(self):
        task_id = self.kwargs.get('pk')
        return get_object_or_404(models.Task, pk=task_id)
    

class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = models.Task
    form_class = TaskForm
    template_name = "tasks/task_update_form.html"
    success_url = reverse_lazy("tasks:task-list")



class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = models.Task
    success_url = reverse_lazy("tasks:task-list")
    template_name = "tasks/task_delete_confirmation.html"





# class CustomLoginView(LoginView):
#     template_name = "tasks/custom_register/login.html"
#     redirect_authenticated_user = True
    


# class CustomLogoutView(LogoutView):
#     next_page = "tasks:login"


# class RegisterView(CreateView):
#     template_name = "tasks/custom_register/register.html"
#     form_class = UserCreationForm
#     success_url = reverse_lazy("tasks:login")

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect(self.get_success_url())