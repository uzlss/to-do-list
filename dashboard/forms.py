from django import forms
from django.forms import DateInput

from dashboard.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
    )
    deadline = forms.DateField(
        widget=DateInput(
            attrs={
                'class': 'datepicker',
                'placeholder': 'DD/MM/YYYY',
                'data-datepicker-format': 'dd/mm/yyyy',
                'type': 'date',
            }
        ),
    )

    class Meta:
        model = Task
        fields = ("content", "tags", "deadline")


class TaskUpdateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Task
        fields = ("tags", )
