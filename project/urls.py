from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_app.urls')),  # Підключає маршрути з app/urls.py
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('', include('auth_system.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
