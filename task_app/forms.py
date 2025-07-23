from django import forms
from task_app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title", "description", "status","priority", "deadline", 
        ]

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

        self.fields["deadline"].widget.attrs["class"] += " my-custom=datepicker"
            


        
class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("","всі"), 
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Статус")
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, required=False, label="пріорітет")


    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        self.fields["status"].widget.attrs.update({"class": "form-control"})
        self.fields["priority"].widget.attrs.update({"class": "form-control"})
        

    

# class TaskFilterForm1(forms.Form):
#     PRIORITY_CHOICES = [
#         ("low", "Low"),
#         ("medium", "Medium"),
#         ("high", "High"),
#     ]
#     status = forms.CharField(choises = PRIORITY_CHOICES, required=False, label="пріорітет")

#     def __init__(self, *args, **kwargs):
#         super(TaskFilterForm1, self).__init__(*args, **kwargs)
#         self.fields["priority"].widget.attrs.update({"class": "form-control"})
        
