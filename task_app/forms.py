from django import forms
from task_app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title", "description", "status","priority", "deadline", 
        ]

        
class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("","всі"), 
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Статус")