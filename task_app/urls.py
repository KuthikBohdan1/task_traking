from django.urls import path
from task_app import views

urlpatterns = [
   
    path("", views.TaskListView.as_view(), name = "task-list" ),
    path("<int:pk>/", views.TaskDetailView.as_view(), name = "task-detail" ),
    path("task-create", views.TaskCreateView.as_view(), name="task-create" ),





]

app_name = "tasks"