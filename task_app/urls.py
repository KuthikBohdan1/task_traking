from django.urls import path
from task_app import views

urlpatterns = [
   
    path("", views.TaskListView.as_view(), name = "task-list" ),
    path("<int:pk>/", views.TaskDetailView.as_view(), name = "task-detail" ),
    path("<int:pk>/coment", views.TaskComentView.as_view(), name="task-coment"),
    path("<int:pk>/update", views.TaskUpdateView.as_view(), name = "task-update" ),
    path("<int:pk>/delete", views.TaskDeleteView.as_view(), name = "task-delete" ),
    path("task-create", views.TaskCreateView.as_view(), name="task-create" ),
    path("<int:pk>/complate/" , views.TaskComplateView.as_view(), name = "task-complate")

]

app_name = "tasks"