from django.urls import path
from task_app import views

urlpatterns = [
   
    path("", views.TaskListView.as_view(), name = "task-list" ),
    path("<int:pk>/", views.TaskDetailView.as_view(), name = "task-detail" ),
    path("<int:pk>/comment", views.CommentListView.as_view(), name="task-comment"),
    path("<int:pk>/comment-create", views.ComentCreateView.as_view(), name="task-comment-form"),
    path("<int:pk>/update", views.TaskUpdateView.as_view(), name = "task-update" ),
    path("<int:pk>/delete", views.TaskDeleteView.as_view(), name = "task-delete" ),
    path("task-create", views.TaskCreateView.as_view(), name="task-create" ),
    path("<int:pk>/complate/" , views.TaskComplateView.as_view(), name = "task-complate"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),




]

app_name = "tasks"