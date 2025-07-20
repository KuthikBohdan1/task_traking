from django import forms
from task_app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title", "description", "status","priority", "deadline", 
        ]